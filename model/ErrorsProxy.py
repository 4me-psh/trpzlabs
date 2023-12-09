class ErrorsProxy:
    addressline = ''

    def error_404(self):
        ErrorsProxy.description_404(self)
        pass

    def error_502(self):
        ErrorsProxy.description_502(self)
        pass

    def error_503(self):
        ErrorsProxy.description_503(self)
        pass

    def description_404(self):
        print("Виникла помилка на пристрої, спробуйте...")

    def description_502(self):
        print("Виникла проблема на сервері...")
        pass

    def description_503(self):
        print("Сервер зараз не може прийняти запит, зачекайте...")
        pass
# методи для обробки помилок(проксі)
