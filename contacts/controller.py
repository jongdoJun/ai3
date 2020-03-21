from contacts.service import Service
from contacts.model import Model
class Controller:
    def __init__(self):
        self.service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name
        model.phone = phone
        model.email = email
        model.addr = addr
        self.service.add_contact(model)

    def list(self):
        return self.service.get_contacts()

    def remove(self, name):
        self.service.del_contact(name)

