#!/usr/bin/env python3

from datetime import date
import json
import os
import re

from prepare_settings import NO_SEPARATOR

def _find_next_separator_tag(doc_file, current_line, items_per_day, separator):
    with open(doc_file) as doc_file_handler:
        doc_lines = doc_file_handler.readlines()

        is_previous_line_a_separator = True
        items_covered = 0
        separator_re = re.compile(separator)

        # Take note that while the 'current_line' is the actual line number in the file, the
        # doc_lines which holds the content of the file is a list with base 0
        line_iterator = current_line - 1
        for line in doc_lines[current_line:]:
            line_iterator += 1

            found_pattern = separator_re.search(line)
            if not found_pattern:
                is_previous_line_a_separator = False
                continue
            if is_previous_line_a_separator:
                continue

            is_previous_line_a_separator = True
            items_covered += 1

            if items_covered == items_per_day:
                return line_iterator + 1

    return 1

def view_document(doc_file, settings_file):
    with open(settings_file) as settings_file_handler:
        settings_content = settings_file_handler.read()
        settings_dict = json.loads(settings_content)

    date_today = str(date.today())
    if date_today != settings_dict['date']:
        settings_dict['date'] = date_today
        if settings_dict['separator'] == NO_SEPARATOR:
            settings_dict['line'] += settings_dict['items_per_day']
        else:
            next_batch = _find_next_separator_tag(doc_file,
                                                  settings_dict['line'],
                                                  settings_dict['items_per_day'],
                                                  settings_dict['separator'])
            settings_dict['line'] = next_batch

        with open(settings_file, "w") as settings_file_handler:
            settings_file_handler.write(json.dumps(settings_dict))


base_dir = "files"
doc_dir = os.path.join(base_dir, "pep8")
doc_file = os.path.join(doc_dir, "doc.txt")
config_file = os.path.join(doc_dir, "settings.txt")
view_document(doc_file, config_file)
