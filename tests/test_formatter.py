from unittest import TestCase
from nose.tools import ok_, eq_
from OrderedFormat.formatter import *
from io import StringIO

class TestOrderedFormat(TestCase):

    def test_iterdepth_for_simple(self):
        eq_(iterdepth([]), 0)
        eq_(iterdepth(()), 0)
        eq_(iterdepth([1]), 1)
        eq_(iterdepth((1, )), 1)

    def test_iterdepth_for_list(self):
        list_array = [0, "1", ["2", [3, 4]], [5, "6"], [7, 8], [9, 10, [11, [12, 13]]]]
        eq_(iterdepth(list_array), 4)

    def test_iterdepth_for_dic(self):
        dict_value = {"a": 1, "b": {"c": 2, "d": {"f": 3, "g": {"h": 4}}}}
        eq_(iterdepth(dict_value), 4)

    def test_kflatten_simple(self):
        yml_data = """
        human:
          name: John
          age: 22
        """

        key_data = """
        human:
        - name
        - name
        """

        ordered_key = getorderedkeys(key_data=key_data, ext="yml")

        data = kflatten(yml_data, ordered_keys=ordered_key)
        eq_(data[0], "John")
        eq_(data[1], "John")