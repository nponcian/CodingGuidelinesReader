import os
import sys

from .prepare_document import prepare_document
from .prepare_settings import prepare_settings
from .view_document import set_next, view_document

PROJECT_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(PROJECT_DIR, "files")

def _view_help():
    print("Usage")
    print("    export PYTHONPATH=/path/to/CodingGuidelinesReader:${PYTHONPATH}")
    print("    python3 -m doc_reader_python [OPTION]")
    print()
    print("Options")
    print("    --help")
    print("        Display help")
    print()
    print("    --init")
    print("        Initialize app")
    print()
    print("    --view")
    print("        View document")

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if not args or args[0] == "--help":
        _view_help()

    elif args[0] == "--init":
        prepare_document(PROJECT_DIR)

        doc_dir = os.path.join(FILES_DIR, "pep8")
        items_per_day = 1
        separator = '<h[0-9]'
        prepare_settings(doc_dir, items_per_day, separator)

    elif args[0] == "--view":
        doc_dir = os.path.join(FILES_DIR, "pep8")
        doc_file = os.path.join(doc_dir, "doc.txt")
        settings_file = os.path.join(doc_dir, "settings.txt")
        view_document(doc_file, settings_file)

    elif args[0] == "--next":
        doc_dir = os.path.join(FILES_DIR, "pep8")
        settings_file = os.path.join(doc_dir, "settings.txt")
        set_next(settings_file)

    else:
        _view_help()

if __name__ == "__main__":
    main()
