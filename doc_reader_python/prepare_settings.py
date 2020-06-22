#!/usr/bin/env python3

import json
import os

INIT_DATE = 'init'
INIT_LINE = 0
DEFAULT_ITEMS_PER_DAY = 1
NO_SEPARATOR = '__NONE__'
DEFAULT_MODE = "text"

def prepare_settings(doc_dir, items_per_day=DEFAULT_ITEMS_PER_DAY, separator=NO_SEPARATOR):
    settings_file = os.path.join(doc_dir, "settings.txt")

    with open(settings_file, "w") as settings_file_handler:
        # TODO : Put this dict into its own class
        DEFAULT_VALUES = {
            "date" : INIT_DATE,
            "line" : INIT_LINE,
            "items_per_day" : items_per_day,
            "separator" : separator,
            "mode" : DEFAULT_MODE # possible values # [text, html]
        }
        settings_file_handler.write(json.dumps(DEFAULT_VALUES))

base_dir = "files"
doc_dir = os.path.join(base_dir, "pep8")
items_per_day = 1
separator = '<h[0-9]'
prepare_settings(doc_dir, items_per_day, separator)
