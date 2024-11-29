import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Calendar with Reminders")

        # Calendar widget
        self.calendar = Calendar(root, selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        self.calendar.pack(pady=20)

        # Reminder text entry
        self.reminder_entry = tk.Entry(root, width=50)
        self.reminder_entry.pack(pady=10)

        # Add reminder button
        self.add_reminder_button = tk.Button(root, text="Add Reminder", command=self.add_reminder)
        self.add_reminder_button.pack(pady=5)

        # Reminder list
        self.reminder_listbox = tk.Listbox(root, width=50)
        self.reminder_listbox.pack(pady=10)

        # Delete reminder button
        self.delete_reminder_button = tk.Button(root, text="Delete Reminder", command=self.delete_reminder)
        self.delete_reminder_button.pack(pady=5)

        # Dictionary to hold reminders
        self.reminders = {}

    def add_reminder(self):
        date = self.calendar.get_date()
        reminder_text = self.reminder_entry.get()

        if reminder_text:
            if date not in self.reminders:
                self.reminders[date] = []
            self.reminders[date].append(reminder_text)
            self.update_reminder_listbox(date)
            self.reminder_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a reminder.")

    def delete_reminder(self):
        selected_reminder_index = self.reminder_listbox.curselection()
        if selected_reminder_index:
            date = self.calendar.get_date()
            reminder_text = self.reminder_listbox.get(selected_reminder_index)
            self.reminders[date].remove(reminder_text)
            if not self.reminders[date]:  # If no reminders left for that date, remove the date entry
                del self.reminders[date]
            self.update_reminder_listbox(date)
        else:
            messagebox.showwarning("Selection Error", "Please select a reminder to delete.")

    def update_reminder_listbox(self, date):
        self.reminder_listbox.delete(0, tk.END)
        if date in self.reminders:
            for reminder in self.reminders[date]:
                self.reminder_listbox.insert(tk.END, reminder)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
