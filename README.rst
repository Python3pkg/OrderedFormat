=============
OrderedFormat
=============

|buildstatus|_ |coverage|_

Ordered value getter from Dictionary type value.

Requirements
============

Python 2.7 upper and 3.x

From a dictionary type, this can acquire a value in order of a methodical keys.

Install
=======

::

    pip install OrderedFormat

Usage
=====

QuickStart ::

    import OrderedFormat.formatter as odf

    yml_txt_data = """
    human:
      name: John
      age: 22
    """

    yml_key_txt = """
    human:
    - name
    - age
    - name
    """

    ordered_keys = odf.load_ordered_keys(None, raw_txt=yml_key_txt, load_type="yaml")
    ordered_data = odf.kflatten(yml_txt_data, ordered_keys, load_type="yaml")

    # ordered_data = ("John", "John", 22, "John")


Currentry, ``kflatten`` method return flat tuple value.

When you load keys value or dict value (json/yaml file type), you can use two method.

Using Load File Data ::

  ordered_keys = odf.load_ordered_keys("<keys_file.json | keys_file.yaml>")
  dict_data = odf.load_dict_val("<dict_file.json | dict_file.yaml>")

  odf.kflatten(dict_data, ordered_keys)

Available extension is ".yaml" , ".yml" and "json".

.. |buildstatus| image:: https://travis-ci.org/Himenon/OrderedFormat.svg?branch=master
.. _buildstatus: https://travis-ci.org/Himenon/OrderedFormat

.. |coverage| image:: https://coveralls.io/repos/github/Himenon/OrderedFormat/badge.svg?branch=master
.. _coverage: https://coveralls.io/github/Himenon/OrderedFormat
