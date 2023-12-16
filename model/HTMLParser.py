from bs4 import BeautifulSoup
from model.PageCompiler import PageCompiler


class HTMLParser(PageCompiler):
    def content_compile(self, html_content):
        self.parse(html_content)

    addressline = ''

    # метод для парсингу HTML вмісту
    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        pass
