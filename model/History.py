class History:
    id = ''
    id_user = ''
    id_page = ''

    def __init__(self, id, id_user, id_page):
        self.id = id
        self.id_user = id_user
        self.id_page = id_page

    def get_id(self):
        return self.id

    def set_id_user(self, id_user):
        self.id_user = id_user

    def get_id_user(self):
        return self.id_user

    #гетери та сетери, будуть дописані