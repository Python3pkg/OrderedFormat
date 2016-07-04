import os
import re
import json
import yaml
import yamlordereddictloader
from itertools import chain
from collections import OrderedDict

def iterdepth(arr):
    if isinstance(arr, dict) and arr:
        return 1 + max(iterdepth(arr[a]) for a in arr)
    if isinstance(arr, list) and arr:
        return 1 + max(iterdepth(a) for a in arr)
    if isinstance(arr, tuple) and arr:
        return iterdepth(list(arr))
    return 0

def getorderedkeys(key_data, file_path=None, ext=None):

    if file_path:
        if not os.path.exists(file_path):
            raise IOError("Not found '{file_path}'".format(file_path=file_path))
        if not ext:
            ext = os.path.splitext(file_path)[1]

    if not ext:
        raise ValueError("You must set value for 'ext' field!")

    json_flag = re.match("\.json|json", ext)
    yaml_flag = re.match("yml|\.yml|yaml|\.yaml", ext)
    print(json_flag, yaml_flag)

    if isinstance(key_data, str):
        if json_flag:
            return json.JSONDecoder(object_pairs_hook=OrderedDict).decode(key_data)
        if  yaml_flag:
            return yaml.load(key_data, Loader=yamlordereddictloader.Loader)

    if json_flag:
        with open(file_path) as stream:
            return json.JSONDecoder(object_pairs_hook=OrderedDict).decode(stream.read())
    if yaml_flag:
        return yaml.load(open(file_path), Loader=yamlordereddictloader.Loader)

def kflatten(dict_value, ordered_keys):
    ordered_and_flatten_list = []

    def _kflatten(_dict_value, _ordered_keys):
        if isinstance(_ordered_keys, OrderedDict):
            map(lambda sub_key: _kflatten(_dict_value[sub_key], _ordered_keys[sub_key]), _ordered_keys)
        if isinstance(_ordered_keys, list):
            for key in _ordered_keys:
                if isinstance(key, OrderedDict):
                    map(lambda sub_key: _kflatten(_dict_value[sub_key], key[sub_key]), key)
                if isinstance(key, str):
                    ordered_and_flatten_list.append(_dict_value[key])

    _kflatten(dict_value, ordered_keys)

    if iterdepth(ordered_and_flatten_list) > 1:
        return tuple(chain.from_iterable(ordered_and_flatten_list))
    else:
        return tuple(ordered_and_flatten_list)


if __name__ == '__main__':

    yml_data = yaml.load("""
    human:
      name: John
      age: 22
    """)

    print(yml_data)

    data = """
    human:
    - name
    - name
    """

    key_data = getorderedkeys(key_data=data, ext=".yml")

    print(key_data)

    print(kflatten(yml_data, key_data))
