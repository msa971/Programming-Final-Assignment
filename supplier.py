from enum import Enum
class Type(Enum):
    caterer = 1
    games = 2
    furniture = 3
    flowers = 4
    decoration = 5
    venue = 6


class Supplier:
    """Class to represent a supplier"""

    # Constructor:
    def __init__(self, supplier_id, name, contact, type):
        self._supplier_id = supplier_id #supplier ID is protected.
        self.name = name #supplier name is public.
        self.contact = contact #supplier contact information is public.
        self.type = type #supplier type is public.


    #Setter Getter functions:
    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

    def get_supplier_id(self):
        return self._supplier_id


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact


    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type


    #Function to update contact:
    def update_contact(self, new_contact):
        self.contact = new_contact
        print(f"Contact information for {self.name} updated to {new_contact}.")
