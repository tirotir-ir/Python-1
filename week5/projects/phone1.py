import tkinter as tk
from tkinter import messagebox
import json
import os

# نام فایل ذخیره مخاطبین
CONTACTS_FILE = "contacts.json"

# تابع بارگذاری مخاطبین از فایل
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# تابع ذخیره مخاطبین در فایل
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

# تابع افزودن مخاطب
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts[name] = phone
        update_contact_list()
        save_contacts()
    else:
        messagebox.showwarning("خطا", "لطفا نام و شماره تلفن را وارد کنید")

# تابع حذف مخاطب
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        del contacts[selected_contact]
        update_contact_list()
        save_contacts()

# تابع جستجوی مخاطبین
def search_contacts():
    search_query = search_entry.get().lower()
    filtered_contacts = {}
    for name, phone in contacts.items():
        if search_query in name.lower() or search_query in phone:
            filtered_contacts[name] = phone
    update_contact_list(filtered_contacts)

# تابع به‌روزرسانی لیست مخاطبین
def update_contact_list(filtered_contacts=None):
    contact_listbox.delete(0, tk.END)
    contact_display = filtered_contacts if filtered_contacts else contacts
    for name in contact_display:
        contact_listbox.insert(tk.END, f"{name}: {contact_display[name]}")

# پنجره اصلی
root = tk.Tk()
root.title("دفترچه تلفن")
root.geometry("400x500")

# لیست مخاطبین
contacts = load_contacts()

# فرم افزودن مخاطب
name_label = tk.Label(root, text="نام:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="شماره تلفن:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

add_button = tk.Button(root, text="افزودن", command=add_contact)
add_button.pack()

# فرم جستجوی مخاطب
search_label = tk.Label(root, text="جستجو:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="جستجو", command=search_contacts)
search_button.pack()

# لیست مخاطبین
contact_listbox = tk.Listbox(root)
contact_listbox.pack(fill=tk.BOTH, expand=1)

# دکمه حذف مخاطب
delete_button = tk.Button(root, text="حذف", command=delete_contact)
delete_button.pack()

# به‌روزرسانی لیست مخاطبین در شروع برنامه
update_contact_list()

# شروع حلقه اصلی Tkinter
root.mainloop()
