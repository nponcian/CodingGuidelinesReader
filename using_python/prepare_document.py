#!/usr/bin/env python3

import os
import requests

document_url = "https://pep8.org/"

base_dir = "files"
target_dir = os.path.join(base_dir, "pep8")
doc_file = os.path.join(target_dir, "doc.txt")
config_file = os.path.join(target_dir, "config.txt")
os.makedirs(target_dir)

with open(doc_file, "w") as doc_file_handler:
    response = requests.get(document_url)
    doc_file_handler.write(response.text)
