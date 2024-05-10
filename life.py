import datetime
import tkinter as tk
from tkcalendar import Calendar


def display_life_calendar(year, month, day, lifespan):
    years_lived = int((datetime.date.today() -
                       datetime.date(year, month, day)).days / 365.0)
    weeks_lived = int(((datetime.date.today() -
                        datetime.date(year, month, day)).days % 365.0) // 7)
    square_size = 10
    space_size = 1.2
    root = tk.Tk()
    root.title("Life Calendar")
    canvas = tk.Canvas(root, width=52 * square_size * space_size + 4,
                       height=lifespan * square_size * space_size + 4)
    canvas.pack()
    for i in range(lifespan):
        for j in range(52):
            x = j * square_size * space_size + 2
            y = i * square_size * space_size + 2
            t = (i < years_lived - 1) or (i == years_lived and j < weeks_lived)
            canvas.create_rectangle(x, y, x + square_size, y + square_size, fill=(
                "black" if t else "white"), outline="black")
    root.mainloop()


def make_button(root, text, row, column, command):
    button = tk.Button(root, text=text, command=command)
    button.grid(row=row, columnspan=column, padx=pad, pady=pad)
    return button


def on_date_selected():
    selected_date = date_picker.get_date().split('/')
    year, month, day = int(
        selected_date[2]), int(selected_date[0]), int(selected_date[1])
    if year > datetime.date.today().year or (year == datetime.date.today().year and month > datetime.date.today().month) or (year == datetime.date.today().year and month == datetime.date.today().month and day > datetime.date.today().day):
        print("Please select a date in the past")
        return
    display_life_calendar(year, month, day, 80)


root = tk.Tk()
root.title("Life Calendar")
root.geometry("265x280")
pad = 7

label = tk.Label(root, text="Select Your Birthdate")
label.grid(row=0, column=0, padx=pad, pady=pad)
date_picker = Calendar(root, selectmode="day", year=1996,
                       month=11, day=10, date_pattern="mm/dd/yyyy")
date_picker.grid(row=1, column=0, padx=pad, pady=pad)
draw_button = make_button(
    root, "Show My Life Calender", 2, 2, on_date_selected)
root.mainloop()
