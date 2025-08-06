import sqlite3
import tkinter as tk
from tkinter import messagebox
import time
import threading

def init_db():
    conn = sqlite3.connect('medication_reminder.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY,
            medication_name TEXT NOT NULL,
            dosage TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class MedicationReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medication Reminder")

        # Medication Name
        self.medication_name_label = tk.Label(root, text="Medication Name")
        self.medication_name_label.grid(row=0, column=0)
        self.medication_name_entry = tk.Entry(root)
        self.medication_name_entry.grid(row=0, column=1)

        # Dosage
        self.dosage_label = tk.Label(root, text="Dosage")
        self.dosage_label.grid(row=1, column=0)
        self.dosage_entry = tk.Entry(root)
        self.dosage_entry.grid(row=1, column=1)

        # Time
        self.time_label = tk.Label(root, text="Time (HH:MM)")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=2, column=1)

        # Add Reminder Button
        self.add_button = tk.Button(root, text="Add Reminder", command=self.add_reminder)
        self.add_button.grid(row=3, column=0, columnspan=2)

        # Edit and Delete Buttons
        self.edit_button = tk.Button(root, text="Edit Reminder", command=self.edit_reminder)
        self.edit_button.grid(row=4, column=0)
        self.delete_button = tk.Button(root, text="Delete Reminder", command=self.delete_reminder)
        self.delete_button.grid(row=4, column=1)

        # Listbox for displaying reminders
        self.reminders_listbox = tk.Listbox(root)
        self.reminders_listbox.grid(row=5, column=0, columnspan=2)

        # Load existing reminders
        self.load_reminders()

        # Start checking for reminders
        self.check_reminders()

    def add_reminder(self):
        medication_name = self.medication_name_entry.get()
        dosage = self.dosage_entry.get()
        time = self.time_entry.get()

        if medication_name and dosage and time:
            conn = sqlite3.connect('medication_reminder.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO reminders (medication_name, dosage, time)
                VALUES (?, ?, ?)
            ''', (medication_name, dosage, time))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Reminder added successfully!")
            self.medication_name_entry.delete(0, tk.END)
            self.dosage_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)

            self.load_reminders()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")

    def load_reminders(self):
        self.reminders_listbox.delete(0, tk.END)
        conn = sqlite3.connect('medication_reminder.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, medication_name, dosage, time FROM reminders')
        reminders = cursor.fetchall()
        conn.close()

        for reminder in reminders:
            self.reminders_listbox.insert(tk.END, f"{reminder[0]}: {reminder[1]} - {reminder[2]} at {reminder[3]}")

    def edit_reminder(self):
        selected = self.reminders_listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Reminder", "Please select a reminder to edit")
            return

        reminder_id = int(self.reminders_listbox.get(selected[0]).split(':')[0])

        medication_name = self.medication_name_entry.get()
        dosage = self.dosage_entry.get()
        time = self.time_entry.get()

        if medication_name and dosage and time:
            conn = sqlite3.connect('medication_reminder.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE reminders
                SET medication_name = ?, dosage = ?, time = ?
                WHERE id = ?
            ''', (medication_name, dosage, time, reminder_id))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Reminder updated successfully!")
            self.medication_name_entry.delete(0, tk.END)
            self.dosage_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)

            self.load_reminders()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")

    def delete_reminder(self):
        selected = self.reminders_listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Reminder", "Please select a reminder to delete")
            return

        reminder_id = int(self.reminders_listbox.get(selected[0]).split(':')[0])

        conn = sqlite3.connect('medication_reminder.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reminders WHERE id = ?', (reminder_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reminder deleted successfully!")
        self.load_reminders()

    def check_reminders(self):
        def check():
            while True:
                current_time = time.strftime("%H:%M")
                conn = sqlite3.connect('medication_reminder.db')
                cursor = conn.cursor()
                cursor.execute('SELECT medication_name, dosage FROM reminders WHERE time = ?', (current_time,))
                reminders = cursor.fetchall()
                conn.close()

                for reminder in reminders:
                    messagebox.showinfo("Reminder", f"It's time to take your medication: {reminder[0]} - {reminder[1]}")

                time.sleep(60)

        threading.Thread(target=check, daemon=True).start()

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = MedicationReminderApp(root)
    root.mainloop()
