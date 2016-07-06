=============
OrderedFormat
=============

|buildstatus|_

Ordered value getter from Dictionary type value.

Requirements
============

Python 2.6 upper and 3.x

From a dictionary type, this can acquire a value in order of a methodical keys.

Example
=======

QuickStart ::

  import OrderedFormat as odf

  yml_data = """
  human:
  name: John
  age: 22
  """

  key_data = """
  human:
  - name
  - age
  - name
  """

  ordered_keys = odf.get_ordered_keys(key_data=key_data, ext="yml")

  ordered_data = odf.kflatten(yml_data, ordered_keys, type="yaml")
  # ordered_data = ("John", "John", 22, "John")

Currentry, ``kflatten`` method return flat tuple value.

When you load keys value or dict value (json/yaml file type), you can use two method.

Using Load File Data ::

  ordered_keys = odf.load_ordered_keys(key_data=None, filename="<keys_file.json | keys_file.yaml>")
  dict_data = odf.load_dict_val("<dict_file.json | dict_file.yaml>")

  odf.kflatten(dict_data, ordered_keys)

Available extension is ".yaml" , ".yml" and "json".

.. |buildstatus| image:: https://travis-ci.org/Himenon/OrderedFormat.svg?branch=master
.. _buildstatus: https://travis-ci.org/Himenon/OrderedFormat
