OrderedFormat
=============

.. image:: https://travis-ci.org/Himenon/OrderedFormat.svg?branch=master
    :target: https://travis-ci.org/Himenon/OrderedFormat


Requirements
------------

Python 2.7 and 3.

From a dictionary type, this can acquire a value in order of a methodical keys.

Example
-------

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

        ordered_keys = get_ordered_keys(key_data=key_data, ext="yml")

        ordered_data = kflatten(yml_data, ordered_keys, type="yaml")

        # ordered_data = ("John", "John", 22, "John")
