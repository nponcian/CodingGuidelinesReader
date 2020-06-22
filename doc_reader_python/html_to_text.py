from html.parser import HTMLParser
import requests

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, d):
        self.result.append(d)

    def get_text(self):
        return ''.join(self.result)

def html_content_to_text(html_content):
    s = HTMLTextExtractor()
    s.feed(html_content)
    return s.get_text()

def get_text_contents_of_urls(*urls):
    merged_content = str()
    for url in urls:
        url = url.strip()
        if len(url) == 0: continue

        response = requests.get(url)
        html_content = response.text
        # if isinstance(html_content, (bytes, bytearray)): # necessary if using # response.content
        #     html_content = html_content.decode()
        merged_content += html_content_to_text(html_content) + "\n"

    return merged_content
