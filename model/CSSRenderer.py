from model.PageCompiler import PageCompiler


class CSSRenderer(PageCompiler):
    def content_compile(self, css_content):
        self.render_css(css_content)

    addressline = ''

    # метод для обробки CSS
    def render_css(self, css_content):
        pass
