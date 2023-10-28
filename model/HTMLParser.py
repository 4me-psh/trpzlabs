from bs4 import BeautifulSoup


class HTMLParser:
    addressline = ''

    #метод для парсингу HTML вмісту
    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        pass
