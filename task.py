class Task:
    """Class to represent a task"""

    # Constructor:
    def __init__(self, task_employee, type, description):
        #all attributes are protected:
        self._task_employee = task_employee
        self._type = type
        self._description = description

    def set_task_employee(self, task_employee):
        self._task_employee = task_employee

    def get_task_employee(self):
        return self._task_employee


    def set_type(self, type):
        self._type = type

    def get_type(self):
        return self._type


    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description


    #Function to cancel tasks:
    def cancel_task(self):
        print(f"Task '{self._description}' canceled.")
