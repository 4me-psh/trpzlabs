from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_tag(self, tag):
        pass

    @abstractmethod
    def visit_script(self, script):
        pass

    @abstractmethod
    def visit_image(self, image):
        pass
