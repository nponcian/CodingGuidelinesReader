from datetime import date
import json
import os
import re

# TODO : Fix imports
# from prepare_settings import INIT_LINE, NO_SEPARATOR
from .html_to_text import html_content_to_text
INIT_LINE = 0
NO_SEPARATOR = '__NONE__'

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

            line = line.strip()
            if not line:
                continue

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

    return None

def _view_lines(doc_file, start_line, end_line, mode):
    print(f"[info] Lines to display: {start_line} - {end_line}")
    print()

    with open(doc_file) as doc_file_handler:
        doc_lines = doc_file_handler.readlines()

        if start_line: start_line -= 1
        if end_line: end_line -= 1

        lines_to_display = doc_lines[start_line:end_line]

        if mode == "text":
            lines_to_display = html_content_to_text("\n".join(lines_to_display))

        print(lines_to_display)

def view_document(doc_file, settings_file):
    with open(settings_file) as settings_file_handler:
        settings_content = settings_file_handler.read()
        settings_dict = json.loads(settings_content)

    with open(doc_file) as doc_file_handler:
        doc_line_count = len(doc_file_handler.readlines())

    date_today = str(date.today())
    if date_today != settings_dict['date']:
        settings_dict['date'] = date_today
        if settings_dict['separator'] == NO_SEPARATOR:
            if settings_dict['line'] == INIT_LINE:
                settings_dict['line'] = 1
            else:
                settings_dict['line'] += settings_dict['items_per_day']
                if settings_dict['line'] > doc_line_count:
                    settings_dict['line'] = 1
        else:
            INIT_ITEMS_PER_DAY = 1
            target_items_per_day = INIT_ITEMS_PER_DAY if settings_dict['line'] == INIT_LINE \
                                    else settings_dict['items_per_day']
            start_line = _find_next_separator_tag(doc_file,
                                                  settings_dict['line'],
                                                  target_items_per_day,
                                                  settings_dict['separator'])
            if start_line is None:
                start_line = _find_next_separator_tag(doc_file,
                                                      INIT_LINE,
                                                      INIT_ITEMS_PER_DAY,
                                                      settings_dict['separator'])
                if start_line is None:
                    start_line = INIT_LINE

            settings_dict['line'] = start_line

        with open(settings_file, "w") as settings_file_handler:
            settings_file_handler.write(json.dumps(settings_dict))

    if settings_dict['separator'] == NO_SEPARATOR:
        end_line = settings_dict['line'] + settings_dict['items_per_day']
    else:
        end_line = _find_next_separator_tag(doc_file,
                                            settings_dict['line'],
                                            settings_dict['items_per_day'],
                                            settings_dict['separator'])
    _view_lines(doc_file, settings_dict['line'], end_line, settings_dict['mode'])
