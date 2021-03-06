from pelican import signals


def set_category_order(generator):
  # check category order
  category_order = generator.settings.get('CATEGORIES_ORDER', None)
  cats = generator.context.get("categories", [])

  if isinstance(category_order, list) or isinstance(category_order, tuple):
    new = sorted(cats, key=lambda t: category_order.index(t[0]))
    generator.context["categories"] = new
  else:
    category_order_by = generator.settings.get('CATEGORIES_ORDER_BY', 'size-rev')
    tag_order_by = generator.settings.get('TAGS_ORDER_BY', 'size-rev')

    for attr, order in [('categories', category_order_by), ('tags', tag_order_by)]:
      raw = generator.context.get(attr, [])

      if order == 'size-rev':
        new = sorted(raw, key=lambda t: len(t[1]), reverse=True)
      elif order == 'size':
        new = sorted(raw, key=lambda t: len(t[1]))
      elif order == 'alphabetic-rev':
        new = sorted(raw, key=lambda t: t[0], reverse=True)
      else:
        new = sorted(raw, key=lambda t: (t[0]))
    
    generator.context[attr] = new

  
def register():
  signals.article_generator_finalized.connect(set_category_order)
