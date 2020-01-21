#!/usr/bin/python3
import sys
import json

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
with open(filename, 'a+') as f:
    pass

try:
    my_list = load_from_json_file(filename)
except ValueError:
    my_list = []
list1 = sys.argv[1:]
my_list += list1
save_to_json_file(my_list, filename)
