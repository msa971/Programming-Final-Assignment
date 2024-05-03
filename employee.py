from enum import Enum
class Title(Enum):
    manager = 1
    employee = 2

class Department(Enum):
    Sales = 1
    HR = 2
    organizing = 3
    inventory = 4
    billing = 5
    customerservice = 6

class Employee:
    """Class to represent an employee"""

    # Constructor:
    def __init__(self, employee_id, name, department, title, salary, manager_id):
        self.__employee_id = employee_id #employee ID is private.
        self._name = name #employee name is protected.
        self._department = department #employee department is protected.
        self._title = title #employee title is protected.
        self.__salary = salary #employee salary is private.
        self.__manager_id = manager_id #employee's manager's ID is private.

    #Setter Getter functions:
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id


    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


    def set_department(self, department):
        self._department = department

    def get_department(self):
        return self._department


    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title


    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


    def set_manager_id(self, manager_id):
        self.__manager_id = manager_id

    def get_manager_id(self):
        return self.__manager_id


    def promotion(self):
        if self._title == Title.EMPLOYEE:
            self._title = Title.MANAGER
            print(f"{self._name} has been promoted to Manager.")
        else:
            print(f"{self._name} is already a Manager.")

    def calculate_bonus(self, percentage):
        bonus_amount = self.__salary * bonus_percentage / 100
        print(f"Bonus for {self._name}: {bonus_amount}")

