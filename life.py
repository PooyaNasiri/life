import datetime
import tkinter as tk
from tkcalendar import Calendar


def center_window(window, width, height):
    x = int((window.winfo_screenwidth() / 2) - (width / 2))
    y = int((window.winfo_screenheight() / 2) - (height / 2) - 100)
    s = f"{width}x{height}" + f"+{int(x)}+{int(0 if y < 0 else y)}"
    window.geometry(s)
    window.resizable(False, False)


def display_life_calendar(year, month, day, lifespan):
    years_lived = int((datetime.date.today() -
                       datetime.date(year, month, day)).days / 365.2425)
    weeks_lived = int(((datetime.date.today() -
                        datetime.date(year, month, day)).days % 365.2425) // 7)
    square_size = 10
    space_size = 1.2
    root = tk.Tk()
    w = int(52 * square_size * space_size + 48)
    h = int(lifespan * square_size * space_size + 20)
    root.title("Life Calendar")
    canvas = tk.Canvas(root, width=w, height=h)
    canvas.pack()
    center_window(root, w, h)
    root.resizable(False, False)
    for i in range(lifespan):
        canvas.create_text(2, (i * square_size * space_size +
                           17 + square_size / 2), text=f"Year {i+1}", anchor="w")
        for j in range(52):
            if i == 0:
                canvas.create_text(
                    (j * square_size * space_size + square_size / 2 + 38), 10, text=f"{j+1}", anchor="w", fill='gray' if j % 2 == 1 else 'black')
            x = j * square_size * space_size + 44
            y = i * square_size * space_size + 17
            t = (i < years_lived) or (i == years_lived and j < weeks_lived)
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
center_window(root, 265, 280)
pad = 7
label = tk.Label(root, text="Select Your Birthdate")
label.grid(row=0, column=0, padx=pad, pady=pad)
date_picker = Calendar(root, selectmode="day", year=1996,
                       month=11, day=10, date_pattern="mm/dd/yyyy")
date_picker.grid(row=1, column=0, padx=pad, pady=pad)
draw_button = make_button(
    root, "Show My Life Calender", 2, 2, on_date_selected)
root.mainloop()
