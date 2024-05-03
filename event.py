from Task import Task

class Event:
    """Class to represent an event"""

    # Constructor:
    def __init__(self, event_id, type, date, location, client):
        self.__event_id = event_id #event ID is private.
        self._type = type #event type is protected.
        self.__date = date #event date is private.
        self.__location = location #event location is private.
        self.__client = client #client that is organizing the event is private.
        self.tasks = [] #empty list to add tasks that need to be done for the event.


    #Setter Getter functions:
    def set_event_id(self, event_id):
        self.__event_id = event_id

    def get_event_id(self):
        return self.__event_id


    def set_type(self, type):
        self._type = type

    def get_type(self):
        return self._type


    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date


    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location


    def set_client(self, client):
        self.__client = client

    def get_client(self):
        return self.__client

    # Adding tasks that need to be done for the event to the empty list of tasks:
    def add_task(self, task):
        self.tasks.append(task)

    def cancel_event(self):
        # Cancel all tasks associated with the event
        for task in self.tasks:
            task.cancel_task()
