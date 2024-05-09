import datetime
import tkinter as tk


def display_life_calendar():
    weeks_lived = (datetime.date.today() -
                   datetime.date(year, month, day)).days // 7
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
            canvas.create_rectangle(x, y, x + square_size, y + square_size, fill=(
                "black"if i * 52 + j < weeks_lived else "white"), outline="black")
    root.mainloop()


def make_label(root, text, row, column):
    label = tk.Label(root, text=text)
    label.grid(row=row, column=column, padx=pad, pady=pad)
    return label


# def make_entry(root, default_text, row, column):
#     entry = tk.Entry(root)
#     entry.insert(0, default_text)
#     entry.grid(row=row, column=column, padx=pad, pady=pad)
#     return int(entry.get())

def make_entry(root, default_text, row, column, max_lenght=4):
    def validate_input(text):
        return (text.isdigit() and len(text) <= max_lenght) or text == ""

    entry = tk.Entry(root, validate="key", validatecommand=(
        root.register(validate_input), '%P'))
    entry.insert(0, default_text)
    entry.grid(row=row, column=column, padx=pad, pady=pad)
    return int(entry.get())


def make_button(root, text, row, column, command):
    button = tk.Button(root, text=text, command=command)
    button.grid(row=row, columnspan=column, padx=pad, pady=pad)
    return button


# GUI setup
root = tk.Tk()
root.title("Life Calendar Setup")
root.geometry("260x190")
pad = 7
make_label(root, "Birth Year:", 0, 0)
year = make_entry(root, "2000", 0, 1, 4)
make_label(root, "Birth Month:", 1, 0)
month = make_entry(root, "1", 1, 1, 2)
make_label(root, "Birth Day:", 2, 0)
day = make_entry(root, "1", 2, 1, 2)
make_label(root, "Lifespan (years):", 3, 0)
lifespan = make_entry(root, "80", 3, 1, 3)
make_button(root, "Draw Calendar", 4, 2, display_life_calendar)
root.mainloop()
