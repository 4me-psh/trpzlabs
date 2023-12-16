from abc import ABC, abstractmethod
class PageCompiler(ABC):
    def header_compile(self):
        pass
    def footer_compile(self):
        pass
    @abstractmethod
    def content_compile(self, content):
        pass
    def build_compile(self):
        self.header_compile()
        self.content_compile(any)
        self.footer_compile()
#клас та методи для реалізації template method