class Page:
    id = ''
    name = ''
    address = ''

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address
