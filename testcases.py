from tkinter import messagebox

#Exception Handling:

try:
   # Code that may raise exceptions
   employee = Employee(
       employee_id=entry_id.get(),
       name=entry_name.get(),
       department=Department(entry_department.get()),
       title=Title(entry_title.get()),
       salary=float(entry_salary.get()),
       manager_id=entry_manager_id.get()
   )
   save_object(employee, 'employees.pkl')
   messagebox.showinfo("Success", "Employee added successfully!")


except ValueError:
   # Handle ValueError, raised when converting strings to float or enums
   messagebox.showerror("Error", "Invalid input. Please enter valid data.")


except Exception as e:
   # Handle other exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")




try:
   client = Client(
       client_id=entry_client_id.get(),
       name=entry_client_name.get(),
       contact=entry_client_contact.get(),
       budget=float(entry_client_budget.get())
   )
   save_object(client, 'clients.pkl')
   messagebox.showinfo("Success", "Client added successfully!")


except ValueError:
   # Handle ValueError, raised when converting strings to float
   messagebox.showerror("Error", "Invalid input. Please enter valid data.")


except Exception as e:
   # Handle other exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")




try:
   guest = Guest(
       guest_id=entry_guest_id.get(),
       name=entry_guest_name.get(),
       contact=entry_guest_contact.get(),
       budget=float(entry_guest_budget.get()),
       rsvp=Rsvp(entry_guest_rsvp.get())
   )
   save_object(guest, 'guests.pkl')
   messagebox.showinfo("Success", "Guest added successfully!")


except ValueError:
   # Handle ValueError, raised when converting strings to float or enums
   messagebox.showerror("Error", "Invalid input. Please enter valid data.")


except Exception as e:
   # Handle other exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")




try:
   supplier = Supplier(
       supplier_id=entry_supplier_id.get(),
       name=entry_supplier_name.get(),
       contact=entry_supplier_contact.get(),
       type=Type(entry_supplier_type.get())
   )
   save_object(supplier, 'suppliers.pkl')
   messagebox.showinfo("Success", "Supplier added successfully!")


except ValueError:
   # Handle ValueError, raised when converting strings to enums
   messagebox.showerror("Error", "Invalid input. Please enter valid data.")


except Exception as e:
   # Handle other exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")






try:
   event = Event(
       event_id=entry_event_id.get(),
       type=entry_event_type.get(),
       date=entry_event_date.get(),
       location=entry_event_location.get(),
       client=entry_event_client.get()
   )
   save_object(event, 'events.pkl')
   messagebox.showinfo("Success", "Event added successfully!")


except Exception as e:
   # Handle any exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")




try:
   task = Task(
       task_employee=entry_task_employee.get(),
       type=entry_task_type.get(),
       description=entry_task_description.get()
   )
   # Do something with the task object, such as saving it to a file
   messagebox.showinfo("Success", "Task added successfully!")


except Exception as e:
   # Handle any exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")




try:
   invoice = Invoice(
       date=entry_invoice_date.get(),
       amount=float(entry_invoice_amount.get()),
       client=entry_invoice_client.get(),
       payment_method=entry_invoice_payment_method.get()
   )
   save_object(invoice, 'invoices.pkl')
   messagebox.showinfo("Success", "Invoice added successfully!")


except ValueError:
   # Handle ValueError, raised when converting strings to float
   messagebox.showerror("Error", "Invalid input. Please enter valid data.")


except Exception as e:
   # Handle other exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")




try:
   inventory = Inventory(
       inventory_id=entry_inventory_id.get(),
       items=entry_inventory_items.get(),
       amount=float(entry_inventory_amount.get())
   )
   save_object(inventory, 'inventory.pkl')
   messagebox.showinfo("Success", "Inventory added successfully!")


except ValueError:
   # Handle ValueError, raised when converting strings to float
   messagebox.showerror("Error", "Invalid input. Please enter valid data.")


except Exception as e:
   # Handle other exceptions
   messagebox.showerror("Error", str(e))


finally:
   # Code that will always execute, regardless of whether an exception occurred or not
   print("Finally block will always execute.")