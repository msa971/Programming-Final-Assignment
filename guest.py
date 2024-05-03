from Client import Client
from enum import Enum

class Rsvp(Enum):
    yes = 1
    no = 2

class Guest(Client):
    """Class to represnet a guest"""

    # Constructor:
    def __init__(self, guest_id, name, contact, budget, rsvp):
        super().__init__(guest_id, name, contact, budget)
        self.__rsvp = rsvp


    #Setter Getter functions:
    def set_rsvp(self, rsvp):
        self.__rsvp = rsvp

    def get_rsvp(self):
        return self.__rsvp
