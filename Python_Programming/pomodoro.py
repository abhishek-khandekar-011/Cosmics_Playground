from tkinter import *
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    if TIMER is not None:
        window.after_cancel(TIMER)
    reps = 0
    canvas.itemconfig(title_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60

    if sec_count < 10:
        sec_count = f"0{sec_count}"
    if min_count < 10:
        min_count = f"0{min_count}"

    canvas.itemconfig(title_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
button1 = Button()
button2 = Button()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=100, height=50)

canvas = Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0)

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "tomato.png")
photo_img = PhotoImage(file=IMAGE_PATH)

canvas.create_image(100, 112, image=photo_img)
title_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

button1.config(width=10, height=1, highlightthickness=0, command=start)
button1.config(text="Start")
button1.grid(column=0, row=5)

button2.config(width=10, height=1, highlightthickness=0, command=reset)
button2.config(text="Reset")
button2.grid(column=3, row=5)

mark = Label(text="", fg=GREEN, bg=YELLOW)
mark.grid(column=1, row=5)

canvas.grid(column=1, row=1)
window.mainloop()
