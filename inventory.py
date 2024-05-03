class Inventory:
    """Class to represnet inventory"""

    # Constructor:
    def __init__(self, inventory_id, items, amount):
        self.__inventory_id = inventory_id
        self._items = items
        self._amount = amount


    #Setter Getter functions:
    def set_inventory_id(self, inventory_id):
        self.__inventory_id = inventory_id

    def get_inventory_id(self):
        return self.__inventory_id


    def set_items(self, items):
        self._items = items

    def get_items(self):
        return self._items


    def set_amount(self, amount):
        self._amount = amount

    def get_amount(self):
        return self._amount


    #Functions to add and remove items:
    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item}' added to inventory {self.__inventory_id}.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removed from inventory {self.__inventory_id}.")
        else:
            print(f"Item '{item}' not found in inventory {self.__inventory_id}.")
