import tkinter as tk
from tkinter import ttk
from filehandling import FileHandler
from enum import Enum
from employee import Employee
from client import Client
from guest import Guest
from supplier import Supplier
from event import Event
from task import Task
from invoice import Invoice
from inventory import Inventory
from employee import Department
from employee import Title
from tkinter import messagebox


class Application(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("Entity Management GUI")


       self.tab_control = ttk.Notebook(self)
       self.employee_tab = ttk.Frame(self.tab_control)
       self.client_tab = ttk.Frame(self.tab_control)
       self.guest_tab = ttk.Frame(self.tab_control)
       self.supplier_tab = ttk.Frame(self.tab_control)
       self.event_tab = ttk.Frame(self.tab_control)


       self.tab_control.add(self.employee_tab, text="Employee")
       self.tab_control.add(self.client_tab, text="Client")
       self.tab_control.add(self.guest_tab, text="Guest")
       self.tab_control.add(self.supplier_tab, text="Supplier")
       self.tab_control.add(self.event_tab, text="Event")


       self.tab_control.pack(expand=1, fill="both")


       self.create_employee_widgets()
       self.create_client_widgets()
       self.create_guest_widgets()
       self.create_supplier_widgets()
       self.create_event_widgets()




   def create_employee_widgets(self):
       # Employee ID
       tk.Label(self.employee_tab, text="Employee ID:").grid(row=0, column=0)
       self.employee_id_entry = tk.Entry(self.employee_tab)
       self.employee_id_entry.grid(row=0, column=1)


       # Name
       tk.Label(self.employee_tab, text="Name:").grid(row=1, column=0)
       self.name_entry = tk.Entry(self.employee_tab)
       self.name_entry.grid(row=1, column=1)


       # Department
       tk.Label(self.employee_tab, text="Department:").grid(row=2, column=0)
       self.department_entry = ttk.Combobox(self.employee_tab, values=[d.name for d in Department])
       self.department_entry.grid(row=2, column=1)


       # Title
       tk.Label(self.employee_tab, text="Title:").grid(row=3, column=0)
       self.title_entry = ttk.Combobox(self.employee_tab, values=[t.name for t in Title])
       self.title_entry.grid(row=3, column=1)


       # Salary
       tk.Label(self.employee_tab, text="Salary:").grid(row=4, column=0)
       self.salary_entry = tk.Entry(self.employee_tab)
       self.salary_entry.grid(row=4, column=1)


       # Manager ID
       tk.Label(self.employee_tab, text="Manager ID:").grid(row=5, column=0)
       self.manager_id_entry = tk.Entry(self.employee_tab)
       self.manager_id_entry.grid(row=5, column=1)


       # Button to add employee
       self.add_employee_button = tk.Button(self.employee_tab, text="Add Employee", command=self.add_employee)
       self.add_employee_button.grid(row=6, column=0, columnspan=2)


       # Button to delete employee
       tk.Label(self.employee_tab, text="Employee ID to Delete:").grid(row=7, column=0)
       self.employee_id_to_delete_entry = tk.Entry(self.employee_tab)
       self.employee_id_to_delete_entry.grid(row=7, column=1)
       self.delete_employee_button = tk.Button(self.employee_tab, text="Delete Employee", command=self.delete_employee)
       self.delete_employee_button.grid(row=8, column=0, columnspan=2)


       # Button to modify employee
       tk.Label(self.employee_tab, text="Employee ID to Modify:").grid(row=9, column=0)
       self.employee_id_to_modify_entry = tk.Entry(self.employee_tab)
       self.employee_id_to_modify_entry.grid(row=9, column=1)
       self.modify_employee_button = tk.Button(self.employee_tab, text="Modify Employee", command=self.modify_employee)
       self.modify_employee_button.grid(row=10, column=0, columnspan=2)


       # Button to display employee
       tk.Label(self.employee_tab, text="Employee ID to Display:").grid(row=11, column=0)
       self.employee_id_to_display_entry = tk.Entry(self.employee_tab)
       self.employee_id_to_display_entry.grid(row=11, column=1)
       self.display_employee_button = tk.Button(self.employee_tab, text="Display Employee", command=self.display_employee)
       self.display_employee_button.grid(row=12, column=0, columnspan=2)




   def add_employee(self):
       # Get values from entry fields
       employee_id = self.employee_id_entry.get()
       name = self.name_entry.get()
       department = Department[self.department_entry.get()]
       title = Title[self.title_entry.get()]
       salary = float(self.salary_entry.get())
       manager_id = self.manager_id_entry.get()


       # Create Employee object
       new_employee = Employee(employee_id, name, department, title, salary, manager_id)


       # Load existing data if file exists
       file_handler = FileHandler('employees.pickle')
       existing_data = file_handler.load_data()


       # If file doesn't exist or is empty, initialize with an empty list
       if existing_data is None:
           existing_data = []


       # Append the new employee to existing data
       existing_data.append(new_employee)


       # Save the updated data
       file_handler.save_data(existing_data)


       print("Employee Successfully Added!")




   def delete_employee(self):
       # Get employee ID to delete
       employee_id_to_delete = self.employee_id_to_delete_entry.get()


       # Load existing data
       file_handler = FileHandler('employees.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No employees to delete.")
           return


       # Find and remove the employee with the given employee_id
       updated_data = [employee for employee in existing_data if employee.get_employee_id() != employee_id_to_delete]


       if len(existing_data) == len(updated_data):
           print("Employee not found.")
           return


       # Save the updated data
       file_handler.save_data(updated_data)


       print(f"Employee with ID {employee_id_to_delete} deleted successfully.")




   def modify_employee(self):
       # Get employee ID to modify
       employee_id_to_modify = self.employee_id_to_modify_entry.get()


       # Load existing data
       file_handler = FileHandler('employees.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No employees to modify.")
           return


       # Search for the employee with the provided ID
       employee_to_modify = None
       for employee in existing_data:
           if employee.get_employee_id() == employee_id_to_modify:
               employee_to_modify = employee
               break


       if employee_to_modify is None:
           print("Employee not found.")
           return


       # Update employee details
       employee_to_modify.set_name(self.name_entry.get())
       employee_to_modify.set_department(Department[self.department_entry.get()])
       employee_to_modify.set_title(Title[self.title_entry.get()])
       employee_to_modify.set_salary(float(self.salary_entry.get()))
       employee_to_modify.set_manager_id(self.manager_id_entry.get())


       # Save the updated data
       file_handler.save_data(existing_data)


       print(f"Employee with ID {employee_id_to_modify} modified successfully.")




   def display_employee(self):
       # Get the employee ID to display
       employee_id_to_display = self.employee_id_to_display_entry.get()


       # Load existing data
       file_handler = FileHandler('employees.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No employees to display.")
           return


       # Search for the employee with the provided ID
       for employee in existing_data:
           if employee.get_employee_id() == employee_id_to_display:
               # Display employee details using a message box
               messagebox.showinfo("Employee Details", str(employee))
               return


       print("Employee not found.")




   def create_client_widgets(self):
       # Client ID
       tk.Label(self.client_tab, text="Client ID:").grid(row=0, column=0)
       self.client_id_entry = tk.Entry(self.client_tab)
       self.client_id_entry.grid(row=0, column=1)


       # Name
       tk.Label(self.client_tab, text="Name:").grid(row=1, column=0)
       self.name_entry = tk.Entry(self.client_tab)
       self.name_entry.grid(row=1, column=1)


       # Contact
       tk.Label(self.client_tab, text="Contact:").grid(row=2, column=0)
       self.contact_entry = tk.Entry(self.client_tab)
       self.contact_entry.grid(row=2, column=1)


       # Email
       tk.Label(self.client_tab, text="Email:").grid(row=3, column=0)
       self.email_entry = tk.Entry(self.client_tab)
       self.email_entry.grid(row=3, column=1)


       # Button to add client
       self.add_client_button = tk.Button(self.client_tab, text="Add Client", command=self.add_client)
       self.add_client_button.grid(row=4, column=0, columnspan=2)


       # Button to delete client
       tk.Label(self.client_tab, text="Client ID to Delete:").grid(row=5, column=0)
       self.client_id_to_delete_entry = tk.Entry(self.client_tab)
       self.client_id_to_delete_entry.grid(row=5, column=1)
       self.delete_client_button = tk.Button(self.client_tab, text="Delete Client", command=self.delete_client)
       self.delete_client_button.grid(row=6, column=0, columnspan=2)


       # Button to modify client
       tk.Label(self.client_tab, text="Client ID to Modify:").grid(row=7, column=0)
       self.client_id_to_modify_entry = tk.Entry(self.client_tab)
       self.client_id_to_modify_entry.grid(row=7, column=1)
       self.modify_client_button = tk.Button(self.client_tab, text="Modify Client", command=self.modify_client)
       self.modify_client_button.grid(row=8, column=0, columnspan=2)


       # Button to display client
       tk.Label(self.client_tab, text="Client ID to Display:").grid(row=9, column=0)
       self.client_id_to_display_entry = tk.Entry(self.client_tab)
       self.client_id_to_display_entry.grid(row=9, column=1)
       self.display_client_button = tk.Button(self.client_tab, text="Display Client", command=self.display_client)
       self.display_client_button.grid(row=10, column=0, columnspan=2)




   def add_client(self):
       # Get values from entry fields
       client_id = self.client_id_entry.get()
       name = self.name_entry.get()
       contact = self.contact_entry.get()
       email = self.email_entry.get()


       # Create Client object
       new_client = Client(client_id, name, contact, email)


       # Load existing data if file exists
       file_handler = FileHandler('clients.pickle')
       existing_data = file_handler.load_data()


       # If file doesn't exist or is empty, initialize with an empty list
       if existing_data is None:
           existing_data = []


       # Append the new client to existing data
       existing_data.append(new_client)


       # Save the updated data
       file_handler.save_data(existing_data)


       print("Client Successfully Added!")




   def delete_client(self):
       # Get client ID to delete
       client_id_to_delete = self.client_id_to_delete_entry.get()


       # Load existing data
       file_handler = FileHandler('clients.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No clients to delete.")
           return


       # Find and remove the client with the given client_id
       updated_data = [client for client in existing_data if client.get_client_id() != client_id_to_delete]


       if len(existing_data) == len(updated_data):
           print("Client not found.")
           return


       # Save the updated data
       file_handler.save_data(updated_data)


       print(f"Client with ID {client_id_to_delete} deleted successfully.")


   def modify_client(self):
       # Get client ID to modify
       client_id_to_modify = self.client_id_to_modify_entry.get()


       # Load existing data
       file_handler = FileHandler('clients.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No clients to modify.")
           return


       # Search for the client with the provided ID
       client_to_modify = None
       for client in existing_data:
           if client.get_client_id() == client_id_to_modify:
               client_to_modify = client
               break


       if client_to_modify is None:
           print("Client not found.")
           return


       # Update client details
       client_to_modify.email = self.email_entry.get()  # Modify the email attribute directly


       # Save the updated data
       file_handler.save_data(existing_data)


       print(f"Client with ID {client_id_to_modify} modified successfully.")




   def display_client(self):
       # Get the client ID to display
       client_id_to_display = self.client_id_to_display_entry.get()


       # Load existing data
       file_handler = FileHandler('clients.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No clients to display.")
           return


       # Search for the client with the provided ID
       for client in existing_data:
           if client.get_client_id() == client_id_to_display:
               # Display client details using a message box
               messagebox.showinfo("Client Details", str(client))
               return


       print("Client not found.")




   def create_guest_widgets(self):
       # Guest ID
       tk.Label(self.guest_tab, text="Guest ID:").grid(row=23, column=0)
       self.guest_id_entry = tk.Entry(self.guest_tab)
       self.guest_id_entry.grid(row=23, column=1)


       # Name
       tk.Label(self.guest_tab, text="Name:").grid(row=24, column=0)
       self.name_entry = tk.Entry(self.guest_tab)
       self.name_entry.grid(row=24, column=1)


       # Contact
       tk.Label(self.guest_tab, text="Contact:").grid(row=25, column=0)
       self.contact_entry = tk.Entry(self.guest_tab)
       self.contact_entry.grid(row=25, column=1)


       # Budget
       tk.Label(self.guest_tab, text="Budget:").grid(row=26, column=0)
       self.budget_entry = tk.Entry(self.guest_tab)
       self.budget_entry.grid(row=26, column=1)


       # RSVP
       tk.Label(self.guest_tab, text="RSVP:").grid(row=27, column=0)
       self.rsvp_entry = tk.Entry(self.guest_tab)
       self.rsvp_entry.grid(row=27, column=1)


       # Button to add guest
       self.add_guest_button = tk.Button(self.guest_tab, text="Add Guest", command=self.add_guest)
       self.add_guest_button.grid(row=28, column=0, columnspan=2)


       # Button to delete guest
       tk.Label(self.guest_tab, text="Guest ID to Delete:").grid(row=29, column=0)
       self.guest_id_to_delete_entry = tk.Entry(self.guest_tab)
       self.guest_id_to_delete_entry.grid(row=29, column=1)
       self.delete_guest_button = tk.Button(self.guest_tab, text="Delete Guest", command=self.delete_guest)
       self.delete_guest_button.grid(row=30, column=0, columnspan=2)


       # Button to modify guest
       tk.Label(self.guest_tab, text="Guest ID to Modify:").grid(row=31, column=0)
       self.guest_id_to_modify_entry = tk.Entry(self.guest_tab)
       self.guest_id_to_modify_entry.grid(row=31, column=1)
       self.modify_guest_button = tk.Button(self.guest_tab, text="Modify Guest", command=self.modify_guest)
       self.modify_guest_button.grid(row=32, column=0, columnspan=2)


       # Button to display guest
       tk.Label(self.guest_tab, text="Guest ID to Display:").grid(row=33, column=0)
       self.guest_id_to_display_entry = tk.Entry(self.guest_tab)
       self.guest_id_to_display_entry.grid(row=33, column=1)
       self.display_guest_button = tk.Button(self.guest_tab, text="Display Guest", command=self.display_guest)
       self.display_guest_button.grid(row=34, column=0, columnspan=2)




   def add_guest(self):
       # Get values from entry fields
       guest_id = self.guest_id_entry.get()
       name = self.name_entry.get()
       contact = self.contact_entry.get()
       budget = (self.budget_entry.get())
       rsvp = self.rsvp_entry.get()


       # Create Guest object
       new_guest = Guest(guest_id, name, contact, budget, rsvp)


       # Load existing data if file exists
       file_handler = FileHandler('guests.pickle')
       existing_data = file_handler.load_data()


       # If file doesn't exist or is empty, initialize with an empty list
       if existing_data is None:
           existing_data = []


       # Append the new guest to existing data
       existing_data.append(new_guest)


       # Save the updated data
       file_handler.save_data(existing_data)


       print("Guest Successfully Added!")


   def delete_guest(self):
       # Get guest ID to delete
       guest_id_to_delete = self.guest_id_to_delete_entry.get()


       # Load existing data
       file_handler = FileHandler('guests.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No guests to delete.")
           return


       # Find and remove the guest with the given guest_id
       updated_data = [guest for guest in existing_data if guest.get_client_id() != guest_id_to_delete]


       if len(existing_data) == len(updated_data):
           print("Guest not found.")
           return


       # Save the updated data
       file_handler.save_data(updated_data)


       print(f"Guest with ID {guest_id_to_delete} deleted successfully.")


   def modify_guest(self):
       # Get guest ID to modify
       guest_id_to_modify = self.guest_id_to_modify_entry.get()


       # Load existing data
       file_handler = FileHandler('guests.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No guests to modify.")
           return


       # Search for the guest with the provided ID
       guest_to_modify = None
       for guest in existing_data:
           if guest.get_client_id() == guest_id_to_modify:
               guest_to_modify = guest
               break


       if guest_to_modify is None:
           print("Guest not found.")
           return


       # Update guest details
       guest_to_modify.set_name(self.name_entry.get())
       guest_to_modify.set_contact(self.contact_entry.get())
       guest_to_modify.set_budget(self.budget_entry.get())
       guest_to_modify.set_rsvp(self.rsvp_entry.get())


       # Save the updated data
       file_handler.save_data(existing_data)


       print(f"Guest with ID {guest_id_to_modify} modified successfully.")


   def display_guest(self):
       # Get the guest ID to display
       guest_id_to_display = self.guest_id_to_display_entry.get()


       # Load existing data
       file_handler = FileHandler('guests.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No guests to display.")
           return


       # Search for the guest with the provided ID
       guest_found = False
       for guest in existing_data:
           if guest.get_client_id() == guest_id_to_display:
               guest_found = True
               # Display guest details using a message box
               messagebox.showinfo("Guest Details", str(guest))
               break


       if not guest_found:
           print("Guest not found.")


   def create_supplier_widgets(self):
       # Supplier ID
       tk.Label(self.supplier_tab, text="Supplier ID:").grid(row=35, column=0)
       self.supplier_id_entry = tk.Entry(self.supplier_tab)
       self.supplier_id_entry.grid(row=35, column=1)


       # Name
       tk.Label(self.supplier_tab, text="Name:").grid(row=36, column=0)
       self.name_entry = tk.Entry(self.supplier_tab)
       self.name_entry.grid(row=36, column=1)


       # Contact
       tk.Label(self.supplier_tab, text="Contact:").grid(row=37, column=0)
       self.contact_entry = tk.Entry(self.supplier_tab)
       self.contact_entry.grid(row=37, column=1)


       # Email
       tk.Label(self.supplier_tab, text="Email:").grid(row=38, column=0)
       self.email_entry = tk.Entry(self.supplier_tab)
       self.email_entry.grid(row=38, column=1)


       # Type
       tk.Label(self.supplier_tab, text="Type:").grid(row=39, column=0)
       self.type_entry = tk.Entry(self.supplier_tab)  # Adding type_entry
       self.type_entry.grid(row=39, column=1)


       # Button to add supplier
       self.add_supplier_button = tk.Button(self.supplier_tab, text="Add Supplier", command=self.add_supplier)
       self.add_supplier_button.grid(row=40, column=0, columnspan=2)


       # Button to delete supplier
       tk.Label(self.supplier_tab, text="Supplier ID to Delete:").grid(row=41, column=0)
       self.supplier_id_to_delete_entry = tk.Entry(self.supplier_tab)
       self.supplier_id_to_delete_entry.grid(row=41, column=1)
       self.delete_supplier_button = tk.Button(self.supplier_tab, text="Delete Supplier", command=self.delete_supplier)
       self.delete_supplier_button.grid(row=42, column=0, columnspan=2)


       # Button to modify supplier
       tk.Label(self.supplier_tab, text="Supplier ID to Modify:").grid(row=43, column=0)
       self.supplier_id_to_modify_entry = tk.Entry(self.supplier_tab)
       self.supplier_id_to_modify_entry.grid(row=43, column=1)
       self.modify_supplier_button = tk.Button(self.supplier_tab, text="Modify Supplier", command=self.modify_supplier)
       self.modify_supplier_button.grid(row=44, column=0, columnspan=2)


       # Button to display supplier
       tk.Label(self.supplier_tab, text="Supplier ID to Display:").grid(row=45, column=0)
       self.supplier_id_to_display_entry = tk.Entry(self.supplier_tab)
       self.supplier_id_to_display_entry.grid(row=45, column=1)
       self.display_supplier_button = tk.Button(self.supplier_tab, text="Display Supplier",
                                                command=self.display_supplier)
       self.display_supplier_button.grid(row=46, column=0, columnspan=2)


   def add_supplier(self):
       # Get values from entry fields
       supplier_id = self.supplier_id_entry.get()
       name = self.name_entry.get()
       contact = self.contact_entry.get()
       email = self.email_entry.get()


       # Create Supplier object
       new_supplier = Supplier(supplier_id, name, contact, email)


       # Load existing data if file exists
       file_handler = FileHandler('suppliers.pickle')
       existing_data = file_handler.load_data()


       # If file doesn't exist or is empty, initialize with an empty list
       if existing_data is None:
           existing_data = []


       # Append the new supplier to existing data
       existing_data.append(new_supplier)


       # Save the updated data
       file_handler.save_data(existing_data)


       print("Supplier Successfully Added!")




   def delete_supplier(self):
       # Get supplier ID to delete
       supplier_id_to_delete = self.supplier_id_to_delete_entry.get()


       # Load existing data
       file_handler = FileHandler('suppliers.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No suppliers to delete.")
           return


       # Find and remove the supplier with the given supplier_id
       updated_data = [supplier for supplier in existing_data if supplier.get_supplier_id() != supplier_id_to_delete]


       if len(existing_data) == len(updated_data):
           print("Supplier not found.")
           return


       # Save the updated data
       file_handler.save_data(updated_data)


       print(f"Supplier with ID {supplier_id_to_delete} deleted successfully.")


   def modify_supplier(self):
       # Get supplier ID to modify
       supplier_id_to_modify = self.supplier_id_to_modify_entry.get()


       # Load existing data
       file_handler = FileHandler('suppliers.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No suppliers to modify.")
           return


       # Search for the supplier with the provided ID
       supplier_to_modify = None
       for supplier in existing_data:
           if supplier.get_supplier_id() == supplier_id_to_modify:
               supplier_to_modify = supplier
               break


       if supplier_to_modify is None:
           print("Supplier not found.")
           return


       # Update supplier details
       supplier_to_modify.set_name(self.name_entry.get())
       supplier_to_modify.set_contact(self.contact_entry.get())
       supplier_to_modify.set_type(self.type_entry.get())


       # Save the updated data
       file_handler.save_data(existing_data)


       print(f"Supplier with ID {supplier_id_to_modify} modified successfully.")


   def display_supplier(self):
       # Get the supplier ID to display
       supplier_id_to_display = self.supplier_id_to_display_entry.get()


       # Load existing data
       file_handler = FileHandler('suppliers.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No suppliers to display.")
           return


       # Search for the supplier with the provided ID
       for supplier in existing_data:
           if supplier.get_supplier_id() == supplier_id_to_display:
               # Display supplier details using a message box
               messagebox.showinfo("Supplier Details", str(supplier))
               return


       print("Supplier not found.")


   def create_event_widgets(self):
       # Event ID
       tk.Label(self.event_tab, text="Event ID:").grid(row=46, column=0)
       self.event_id_entry = tk.Entry(self.event_tab)
       self.event_id_entry.grid(row=46, column=1)


       # Name
       tk.Label(self.event_tab, text="Name:").grid(row=47, column=0)
       self.name_entry = tk.Entry(self.event_tab)
       self.name_entry.grid(row=47, column=1)


       # Date
       tk.Label(self.event_tab, text="Date:").grid(row=48, column=0)
       self.date_entry = tk.Entry(self.event_tab)
       self.date_entry.grid(row=48, column=1)


       # Location
       tk.Label(self.event_tab, text="Location:").grid(row=49, column=0)
       self.location_entry = tk.Entry(self.event_tab)
       self.location_entry.grid(row=49, column=1)


       # Budget
       tk.Label(self.event_tab, text="Budget:").grid(row=50, column=0)
       self.budget_entry = tk.Entry(self.event_tab)
       self.budget_entry.grid(row=50, column=1)


       # Type
       tk.Label(self.event_tab, text="Type:").grid(row=51, column=0)
       self.type_entry = tk.Entry(self.event_tab)
       self.type_entry.grid(row=51, column=1)


       # Client
       tk.Label(self.event_tab, text="Client:").grid(row=52, column=0)
       self.client_entry = tk.Entry(self.event_tab)
       self.client_entry.grid(row=52, column=1)


       # Button to add event
       self.add_event_button = tk.Button(self.event_tab, text="Add Event", command=self.add_event)
       self.add_event_button.grid(row=53, column=0, columnspan=2)


       # Button to delete event
       tk.Label(self.event_tab, text="Event ID to Delete:").grid(row=54, column=0)
       self.event_id_to_delete_entry = tk.Entry(self.event_tab)
       self.event_id_to_delete_entry.grid(row=54, column=1)
       self.delete_event_button = tk.Button(self.event_tab, text="Delete Event", command=self.delete_event)
       self.delete_event_button.grid(row=55, column=0, columnspan=2)


       # Button to modify event
       tk.Label(self.event_tab, text="Event ID to Modify:").grid(row=56, column=0)
       self.event_id_to_modify_entry = tk.Entry(self.event_tab)
       self.event_id_to_modify_entry.grid(row=56, column=1)
       self.modify_event_button = tk.Button(self.event_tab, text="Modify Event", command=self.modify_event)
       self.modify_event_button.grid(row=57, column=0, columnspan=2)


       # Button to display event
       tk.Label(self.event_tab, text="Event ID to Display:").grid(row=58, column=0)
       self.event_id_to_display_entry = tk.Entry(self.event_tab)
       self.event_id_to_display_entry.grid(row=58, column=1)
       self.display_event_button = tk.Button(self.event_tab, text="Display Event", command=self.display_event)
       self.display_event_button.grid(row=59, column=0, columnspan=2)




   def add_event(self):
       # Get values from entry fields
       event_id = self.event_id_entry.get()
       name = self.name_entry.get()
       date = self.date_entry.get()
       location = self.location_entry.get()
       budget = float(self.budget_entry.get())


       # Create Event object
       new_event = Event(event_id, name, date, location, budget)


       # Load existing data if file exists
       file_handler = FileHandler('events.pickle')
       existing_data = file_handler.load_data()


       # If file doesn't exist or is empty, initialize with an empty list
       if existing_data is None:
           existing_data = []


       # Append the new event to existing data
       existing_data.append(new_event)


       # Save the updated data
       file_handler.save_data(existing_data)


       print("Event Successfully Added!")




   def delete_event(self):
       # Get event ID to delete
       event_id_to_delete = self.event_id_to_delete_entry.get()


       # Load existing data
       file_handler = FileHandler('events.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No events to delete.")
           return


       # Find and remove the event with the given event_id
       updated_data = [event for event in existing_data if event.get_event_id() != event_id_to_delete]


       if len(existing_data) == len(updated_data):
           print("Event not found.")
           return


       # Save the updated data
       file_handler.save_data(updated_data)


       print(f"Event with ID {event_id_to_delete} deleted successfully.")


   def modify_event(self):
       # Get event ID to modify
       event_id_to_modify = self.event_id_to_modify_entry.get()


       # Load existing data
       file_handler = FileHandler('events.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No events to modify.")
           return


       # Search for the event with the provided ID
       event_to_modify = None
       for event in existing_data:
           if event.get_event_id() == event_id_to_modify:
               event_to_modify = event
               break


       if event_to_modify is None:
           print("Event not found.")
           return


       # Update event details
       event_to_modify.set_type(self.type_entry.get())
       event_to_modify.set_date(self.date_entry.get())
       event_to_modify.set_location(self.location_entry.get())
       event_to_modify.set_client(self.client_entry.get())


       # Save the updated data
       file_handler.save_data(existing_data)


       print(f"Event with ID {event_id_to_modify} modified successfully.")




   def display_event(self):
       # Get the event ID to display
       event_id_to_display = self.event_id_to_display_entry.get()


       # Load existing data
       file_handler = FileHandler('events.pickle')
       existing_data = file_handler.load_data()


       if existing_data is None:
           print("No events to display.")
           return

       # Search for the event with the provided ID
       for event in existing_data:
           if event.get_event_id() == event_id_to_display:
               # Display event details using a message box
               messagebox.showinfo("Event Details", str(event))
               return


       print("Event not found.")

if __name__ == "__main__":
   app = Application()
   app.mainloop()