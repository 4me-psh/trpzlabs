# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

from controller import HTTPResponseHandler
from model import ErrorsProxy, HTMLVisitor
from repository import Repository
import model
from model import CSSRenderer, HTMLParser, ImageLoader, JSInterpreter

# клас для виводу головного вікна
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def mainWindow(self):

        repository = Repository
        repository.Repository.fetch(repository.Repository(), dbname='WebBrowser', user='postgres', password='1234',
                                    host='127.0.0.1', port='5432')

        http_handler = HTTPResponseHandler
        response = http_handler.HTTPResponseHandler.send_get_response('http://example.com')


        # html_parser = HTMLParser
        # parsed_data = html_parser.HTMLParser.parse(response)
        # print(parsed_data)
        #

        # css_renderer = CSSRenderer
        # css_content = "body { background-color: lightblue; }"
        # css_renderer.CSSRenderer.render_css(css_content)
        #

        # js_interpreter = JSInterpreter
        # js_code = "console.log('Hello, World!');"
        # js_interpreter.JSInterpreter.execute_js(js_code)
        #

        # image_loader = ImageLoader
        # image_url = 'http://example.com/image.jpg'
        # image_loader.ImageLoader.load_image(image_url)
        print(response)

    # головний метод для виводу вікна
    def showHistoryuser(self, user):
        repository = Repository
        for names in Repository.Repository.exec(repository.Repository(), dbname='WebBrowser', user='postgres',
                                                password='1234',
                                                host='127.0.0.1', port='5432', query='SELECT name from users'):
            if user.name == names:
                if user.administrator == False:
                    Repository.Repository.exec(repository.Repository(), dbname='WebBrowser', user='postgres',
                                               password='1234',
                                               host='127.0.0.1', port='5432',
                                               query='SELECT name from pages, users, histories WHERE '
                                                     'histories.user_id = users.id AND '
                                                     'users.page_id = pages.id AND'
                                                     'users.name = ${user}')

                else:
                    MainWindow.showhistoryadmin(user=user)
            else:
                print("Ви не зареєстровані")

    # Метод для перевірки, чи юзер зареєстрований
    def showHistoryadmin(self, user):
        repository = Repository
        for names in Repository.Repository.exec(repository.Repository(), dbname='WebBrowser', user='postgres',
                                                password='1234',
                                                host='127.0.0.1', port='5432', query='SELECT name from users'):
            if user.name == names and user.administrator == True:
                Repository.Repository.exec(repository.Repository(), dbname='WebBrowser', user='postgres',
                                           password='1234',
                                           host='127.0.0.1', port='5432',
                                           query='SELECT *, name, name from histories, users, pages WHERE '
                                                 'histories.id_user = users.id AND histories.page_id ='
                                                 'pages.id')

    # Метод для перевірки, чи юзер - адміністратор

    def is_user_registered(self, user):
        repository = Repository
        for names in Repository.Repository.exec(repository.Repository(), dbname='WebBrowser', user='postgres',
                                                password='1234',
                                                host='127.0.0.1', port='5432', query='SELECT name from users'):
            if user.User.name == names:
                registered_user = model.Factory_Recommendations.Factory_Recommendations.create_recommendation(
                    "registered")
                return registered_user.Recommendations_Registered.recommend()
            else:
                not_registered_user = model.Factory_Recommendations.Factory_Recommendations.create_recommendation(
                    "not_registered")

                return not_registered_user.Recommendations_Not_Registered.recommend()
    # Метод для перевірки, чи користувач зареєстрований та повертає рекомендації в залежності від перевірки

    def css_content(self, content):
        return CSSRenderer.CSSRenderer.content_compile(content)
    def html_content(self, content):
        return HTMLParser.HTMLParser.content_compile(content)
    def image_content(self, content):
        return ImageLoader.ImageLoader.content_compile(content)
    def js_content(self, content):
        return JSInterpreter.JSInterpreter.content_compile(content)

    #приклад методів для обробки відповідного контенту та його повернення

    def visit_html(self, html_content):
        search_tag = self.html_content(html_content)
        search_image = self.image_content(html_content)
        search_script = self.js_content(html_content)

        HTMLVisitor.HTMLVisitor.visit_tag(search_tag)
        HTMLVisitor.HTMLVisitor.visit_image(search_image)
        HTMLVisitor.HTMLVisitor.visit_script(search_script)
