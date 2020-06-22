import os
import requests

REQUESTS_TIMEOUT = 10

def prepare_document(project_dir):
    # TODO : Remove static values. These should be entered by the user.

    document_url = "https://pep8.org/"

    base_dir = os.path.join(project_dir, "files")
    doc_dir = os.path.join(base_dir, "pep8")
    doc_file = os.path.join(doc_dir, "doc.txt")

    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    with open(doc_file, "w") as doc_file_handler:
        print("Sending request to", document_url)
        response = requests.get(document_url, timeout=REQUESTS_TIMEOUT)
        print("Received response from", document_url)
        doc_file_handler.write(response.text)
