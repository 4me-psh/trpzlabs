# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

from controller import HTTPResponseHandler
from model import ErrorsProxy
from repository import Repository


#клас для виводу головного вікна
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

    #головний метод для виводу вікна



