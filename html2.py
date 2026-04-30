from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # Check if the comment spans multiple lines
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        # Only print data if it is not just a newline character
        if data != '\n':
            print(">>> Data")
            print(data)
n = int(input())
html_string = ""
for _ in range(n):
    html_string += input().rstrip() + '\n'
parser = MyHTMLParser()
parser.feed(html_string)
parser.close()
