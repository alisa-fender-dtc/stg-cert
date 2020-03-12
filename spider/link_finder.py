from html.parser import HTMLParser
from urllib import parse

#Written as part of doing a web crawler tutorial but not used in final project. Opted to use
#requests and beautiful soup for gathering links

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_startendtag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    print(url)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


