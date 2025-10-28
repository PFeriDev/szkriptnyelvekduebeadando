import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime
import calendar


class PF_EventManager:
    def __init__(self, filepath="PF_events.json"):
        self.filepath = filepath
        self.events = {}
        self.load_events()

    def load_events(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.events = json.load(f)
        else:
            self.events = {}

    def save_events(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.events, f, indent=4, ensure_ascii=False)

    def get_events_for_date(self, date_str):
        return self.events.get(date_str, [])

    def add_event(self, date_str, event_text):
        if date_str in self.events:
            self.events[date_str].append(event_text)
        else:
            self.events[date_str] = [event_text]
        self.save_events()

    def delete_event(self, date_str, event_index):
        if date_str in self.events and 0 <= event_index < len(self.events[date_str]):
            del self.events[date_str][event_index]
            if not self.events[date_str]:
                del self.events[date_str]
            self.save_events()

class PF_CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Egyszerű Naptár - PF")
        self.root.geometry("450x500")

        self.event_manager = PF_EventManager()
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.create_widgets()
        self.update_calendar()

    def create_widgets(self):
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=5)

        self.prev_button = tk.Button(nav_frame, text="<< Előző hónap", command=self.prev_month)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.month_year_label = tk.Label(nav_frame, text="", font=("Arial", 14))
        self.month_year_label.grid(row=0, column=1, padx=10)

        self.next_button = tk.Button(nav_frame, text="Következő hónap >>", command=self.next_month)
        self.next_button.grid(row=0, column=2, padx=10)


        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()

        days = ["Hé", "Ke", "Sze", "Cs", "P", "Szo", "Va"]
        for i, day in enumerate(days):
            lbl = tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold"), width=5)
            lbl.grid(row=0, column=i)

        self.day_buttons = []

        for i in range(6):
            row_buttons = []
            for j in range(7):
                btn = tk.Button(self.calendar_frame, text="", width=5, command=lambda r=i, c=j: self.on_day_click(r, c))
                btn.grid(row=i+1, column=j)
                row_buttons.append(btn)
            self.day_buttons.append(row_buttons)

        self.events_label = tk.Label(self.root, text="Események", font=("Arial", 12, "bold"))
        self.events_label.pack(pady=(10, 0))

        self.events_listbox = tk.Listbox(self.root, width=50, height=8)
        self.events_listbox.pack(pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        add_event_btn = tk.Button(btn_frame, text="Esemény hozzáadása", command=self.add_event)
        add_event_btn.grid(row=0, column=0, padx=5)

        del_event_btn = tk.Button(btn_frame, text="Esemény törlése", command=self.delete_event)
        del_event_btn.grid(row=0, column=1, padx=5)

    def update_calendar(self):
        self.month_year_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")
        month_calendar = calendar.monthcalendar(self.current_year, self.current_month)

        for row in self.day_buttons:
            for btn in row:
                btn.config(text="", state="disabled", relief="raised")

        for r, week in enumerate(month_calendar):
            for c, day in enumerate(week):
                if day != 0:
                    btn = self.day_buttons[r][c]
                    btn.config(text=str(day), state="normal", relief="raised")
                    date_str = f"{self.current_year:04d}-{self.current_month:02d}-{day:02d}"
                    if self.event_manager.get_events_for_date(date_str):
                        btn.config(relief="sunken")

        self.selected_date_str = None
        self.events_listbox.delete(0, tk.END)

    def on_day_click(self, row, col):
        day_str = self.day_buttons[row][col].cget("text")
        if day_str:
            self.selected_date_str = f"{self.current_year:04d}-{self.current_month:02d}-{int(day_str):02d}"
            self.load_events_for_selected_date()

    def load_events_for_selected_date(self):
        self.events_listbox.delete(0, tk.END)
        if self.selected_date_str:
            events = self.event_manager.get_events_for_date(self.selected_date_str)
            for ev in events:
                self.events_listbox.insert(tk.END, ev)
            self.events_label.config(text=f"Események: {self.selected_date_str}")

    def add_event(self):
        if not self.selected_date_str:
            messagebox.showwarning("Figyelem", "Először válasszon ki egy napot a naptárban!")
            return
        event_text = simpledialog.askstring("Új esemény", "Adja meg az esemény leírását:")
        if event_text:
            self.event_manager.add_event(self.selected_date_str, event_text)
            self.load_events_for_selected_date()
            self.update_calendar()

    def delete_event(self):
        selected_idx = self.events_listbox.curselection()
        if not selected_idx:
            messagebox.showwarning("Figyelem", "Válasszon ki egy törlendő eseményt!")
            return
        idx = selected_idx[0]
        self.event_manager.delete_event(self.selected_date_str, idx)
        self.load_events_for_selected_date()
        self.update_calendar()

    def prev_month(self):
        self.current_month -= 1
        if self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        self.update_calendar()

    def next_month(self):
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        self.update_calendar()

if __name__ == "__main__":
    root = tk.Tk()
    app = PF_CalendarApp(root)
    root.mainloop()
