#!/usr/bin/python3
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    json_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    with open("add_item.json", "w") as f:
        f.write("[]")
    exit(0)

for argv_data in sys.argv[1:]:
    json_data.append(argv_data)
save_to_json_file(json_data, "add_item.json")
