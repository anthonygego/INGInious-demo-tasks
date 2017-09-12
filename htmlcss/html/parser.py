from html.parser import HTMLParser

class HTMLExpander(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = []
    
    def handle_starttag(self, tag, attrs):
        self.result.append({"type": 0, "tag": tag, "attrs": attrs})

    def handle_endtag(self, tag):
        self.result.append({"type": 1, "tag": tag})

    def handle_data(self, data):
        data = data.strip()
        if data:
            self.result.append({"type": 2, "data": data})
    
    def get_result(self):
        return self.result
    
    def reset(self):
        HTMLParser.reset(self)
        self.result = []