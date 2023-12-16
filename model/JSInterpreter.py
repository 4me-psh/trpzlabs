from model.PageCompiler import PageCompiler


class JSInterpreter(PageCompiler):
    def content_compile(self, js_code):
        self.execute_js(js_code)

    addressline = ''

    # Метод для відображення(запуску) JS коду
    def execute_js(self, js_code):
        pass
