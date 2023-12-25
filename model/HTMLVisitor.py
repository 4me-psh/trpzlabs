from model.Visitor import Visitor


class HTMLVisitor(Visitor):
    def visit_tag(self, tag):
        # Логіка обробки тегів
        pass

    def visit_script(self, script):
        # Логіка обробки скриптів
        pass

    def visit_image(self, image):
        # Логіка обробки зображень
        pass