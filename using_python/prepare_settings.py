#!/usr/bin/env python3

import json
import os

def prepare_settings(doc_dir, items_per_day=1, separator='__NONE__'):
    config_file = os.path.join(doc_dir, "config.txt")

    with open(config_file, "w") as config_file_handler:
        DEFAULT_VALUES = {
            "date" : "init",
            "line" : 0,
            "items_per_day" : items_per_day,
            "separator" : separator
        }
        config_file_handler.write(json.dumps(DEFAULT_VALUES))

base_dir = "files"
doc_dir = os.path.join(base_dir, "pep8")
items_per_day = 1
separator = '<h[0-9]>'
prepare_settings(doc_dir, items_per_day, separator)
