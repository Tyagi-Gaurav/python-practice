import urllib.request
from html.parser import HTMLParser


class MyFootballParser(HTMLParser):
    def __init__(self, base, output=None):
        HTMLParser.__init__(self)
        if output is None:
            output = []
        self.output = output
        self.base = base

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            contains_beta_callout = any(
                attr[0] == 'class' and 'beta-callout full-height-link whole-row-link' in attr[1] for attr in attrs)
            if contains_beta_callout:
                href = [attr for attr in attrs if attr[0] == 'href']
                # print("Tag Attributes:", attrs)
                if href:
                    # print(href[0][1])
                    self.output += [self.base + href[0][1]]

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


def get_all_matches(path):
    base = "http://www.oddschecker.com"
    uri = base + path
    req = urllib.request.Request(uri, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    parser = MyFootballParser(base)
    parser.feed(content)
    return parser.output
