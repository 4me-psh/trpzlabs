class User:
    id = ''
    name = ''
    password = ''
    page_id = ''
    administrator = False

    def __init__(self, id, name, password, page_id, administrator):
        self.id = id
        self.name = name
        self.password = password
        self.page_id = page_id
        self.administrator = administrator

    def get_id(self):
        return self.id

    def set_name_user(self, name):
        self.name = name

    def get_name_user(self):
        return self.name

    def get_password_user(self):
        return self.password

    def set_password_user(self, password):
        self.password = password

    def get_user_page_id(self):
        return self.page_id

    def set_user_page_id(self, page_id):
        self.page_id = page_id

    def get_administrator_user(self):
        return self.administrator

    def set_administrator_user(self, administrator):
        self.administrator = administrator
