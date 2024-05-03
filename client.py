class Client:
    """Class to represent a client"""

    # Constructor:
    def __init__(self, id, name, contact, budget):
        self.__id = id #client ID is private.
        self._name = name #client name is protected.
        self.__contact = contact #client contact information is private.
        self._budget = budget #client budget is protected


    #Setter Getter functions:
    def set_client_id(self, id):
        self.__id = id

    def get_client_id(self):
        return self.__id


    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


    def set_contact(self, contact):
        self.__contact = contact

    def get_contact(self):
        return self.__contact


    def set_budget(self, budget):
        self._budget = budget

    def get_budget(self):
        return self._budget

    def increase_budget(self, amount):
        self._budget += amount
        print(f"Budget for {self._name} increased by {amount}.")

    def decrease_budget(self, amount):
        self._budget -= amount
        print(f"Budget for {self._name} decreased by {amount}.")
