Control Category Display Order
==============================

By default, you can only set the order categories (and tags) alphabetically.
This plugin offers to sort them by the number of articles in that category (or
tag). See a live demo `here`_.

Settings
========

- ``CATEGORIES_ORDER``: type: `tuple` or `list` of `str`s; should contain all categories, demonstrating the order of categories.

- ``CATEGORIES_ORDER_BY``: can be ``size``, ``size-rev``, ``alphabetic-rev``
  or ``alphabetic``.
- ``TAGS_ORDER_BY``: can be ``size``, ``size-rev``, ``alphabetic-rev``
  or ``alphabetic``.

The default value of these two settings is ``size-rev``.

.. _here: http://jhshi.me/blog/categories/index.html
