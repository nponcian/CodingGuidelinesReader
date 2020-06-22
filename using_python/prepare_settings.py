#!/usr/bin/env python3

import json
import os

INIT_DATE = 'init'
DEFAULT_ITEMS_PER_DAY = 1
NO_SEPARATOR = '__NONE__'

def prepare_settings(doc_dir, items_per_day=DEFAULT_ITEMS_PER_DAY, separator=NO_SEPARATOR):
    settings_file = os.path.join(doc_dir, "settings.txt")

    with open(settings_file, "w") as settings_file_handler:
        DEFAULT_VALUES = {
            "date" : INIT_DATE,
            "line" : 0,
            "items_per_day" : items_per_day,
            "separator" : separator
        }
        settings_file_handler.write(json.dumps(DEFAULT_VALUES))

base_dir = "files"
doc_dir = os.path.join(base_dir, "pep8")
items_per_day = 1
separator = '<h[0-9]'
prepare_settings(doc_dir, items_per_day, separator)
