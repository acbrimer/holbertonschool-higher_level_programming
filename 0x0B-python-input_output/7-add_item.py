#!/usr/bin/python3
"""
    Module for add_item
"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    """ Function to add item to list and save to file """
    l = []
    if os.path.exists("add_item.json"):
        l += load_from_json_file("add_item.json")
    l += sys.argv[1:]
    save_to_json_file(l, "add_item.json")

if __name__ == "__main__":
    add_item()
