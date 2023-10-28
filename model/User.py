class User:
    id = ''
    name = ''
    password = ''
    page_id = ''

    def __init__(self, id, name, password, page_id):
        self.id = id
        self.name = name
        self.password = password
        self.page_id = page_id

    #також будуть гетери та сетери