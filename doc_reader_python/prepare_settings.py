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
        default_values = {
            "date" : INIT_DATE,
            "line" : INIT_LINE,
            "items_per_day" : items_per_day,

            # The divider between the items in the guidelines. So if each item in the guidelines
            # are separated by the html tag <h1> Guideline 1... <h1> Guideline 2... and so on, then
            # you can put here a regex value of "<h[0-9]"
            "separator" : separator,  # The divider between items in the guidelines. Such as if aaaa

            # Possible values are ["text", "html"]
            "mode" : DEFAULT_MODE
        }
        settings_file_handler.write(json.dumps(default_values))

