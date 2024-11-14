import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    if not name:
        return
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
        return
    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    email = simpledialog.askstring("Add Contact", "Enter email address:")
    address = simpledialog.askstring("Add Contact", "Enter address:")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    update_contact_list()
    messagebox.showinfo("Success", "Contact added successfully!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']}")

def view_contact():
    try:
        selected = contact_list.get(contact_list.curselection())
        name = selected.split(" - ")[0]
        info = contacts[name]
        messagebox.showinfo("Contact Details",
                            f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to view.")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    if not query:
        return
    for name, info in contacts.items():
        if query.lower() in name.lower() or query == info["phone"]:
            messagebox.showinfo("Search Result",
                                f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            return
    messagebox.showinfo("Not Found", "Contact not found.")

def update_contact():
    try:
        selected = contact_list.get(contact_list.curselection())
        name = selected.split(" - ")[0]
        new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=name)
        if not new_name:
            return
        phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contacts[name]["phone"])
        email = simpledialog.askstring("Update Contact", "Enter new email address:", initialvalue=contacts[name]["email"])
        address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contacts[name]["address"])
        
        del contacts[name] 
        contacts[new_name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to update.")

def delete_contact():
    try:
        selected = contact_list.get(contact_list.curselection())
        name = selected.split(" - ")[0]
        if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {name}?"):
            del contacts[name]
            update_contact_list()
            messagebox.showinfo("Success", "Contact deleted successfully!")
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to delete.")

# Main GUI
root = tk.Tk()
root.title("Contact Manager")

contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(button_frame, text="View Contact", command=view_contact)
view_button.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact)
search_button.grid(row=0, column=2, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.grid(row=0, column=3, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=0, column=4, padx=5, pady=5)

update_contact_list() 

root.mainloop()
