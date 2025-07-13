from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- EDIT TIMER ------------------------------- #

def trial():
    # trial
    new_window = Tk()
    # trial
    new_window.title("Pomodoro")
    new_window.config(padx=50, pady=25, bg=YELLOW)
    # trial
    work_title = Label(new_window, text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    work_title.grid(column=0, row=0)
    short_break_title = Label(new_window, text="Short break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    short_break_title.grid(column=0, row=1)
    long_break_title = Label(new_window, text="Long break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    long_break_title.grid(column=0, row=2)
    minutes_text_1 = Label(new_window,text="Mins",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
    minutes_text_1.grid(column=2, row=0)
    minutes_text_2 = Label(new_window, text="Mins", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
    minutes_text_2.grid(column=2, row=1)
    minutes_text_3 = Label(new_window, text="Mins", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
    minutes_text_3.grid(column=2, row=2)
    # work input
    def work_spinbox_used():
        global WORK_MIN
        WORK_MIN = int(work_spinbox.get())
    work_spinbox = Spinbox(new_window, from_=0, to=50, width=5, command=work_spinbox_used)
    work_spinbox.grid(column=1, row=0)

    # short break input
    def short_spinbox_used():
        global SHORT_BREAK_MIN
        SHORT_BREAK_MIN = int(short_spinbox.get())
    short_spinbox = Spinbox(new_window, from_=0, to=10, width=5, command=short_spinbox_used)
    short_spinbox.grid(column=1, row=1)

    # long break input
    def long_spinbox_used():
        global LONG_BREAK_MIN
        LONG_BREAK_MIN = int(long_spinbox.get())
    long_spinbox = Spinbox(new_window, from_=0, to=40, width=5, command=long_spinbox_used)
    long_spinbox.grid(column=1, row=2)

    # new_window closing button
    new_button = Button(new_window, text="Apply and close",command=new_window.destroy)
    new_button.grid(column=2, row=4)

    # creating a button to set to default values.
    def default_values():
        global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
        WORK_MIN = 25
        SHORT_BREAK_MIN = 5
        LONG_BREAK_MIN = 20

    default_button = Button(new_window, text="Set Default", command=default_values)
    default_button.grid(column=0, row=4)

    new_window.mainloop()

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    rep=0
    timer_title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if rep%8==0:
        count_down(long_break_secs)
        timer_title.config(text="Break", fg=RED)
    elif rep%2==0:
        count_down(short_break_secs)
        timer_title.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        timer_title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    # making of use of python's dynamic typing feature.
    if count_sec<=9:
        count_sec=f"0{count_sec}"
    if count_min<=9:
        count_min = f"0{count_min}"
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(rep/2)
        for _ in range(work_session):
            mark += "✓"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1, row=1)

# title
timer_title = Label(text="Timer",font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)
#Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=5)
#Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
#Check mark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,20,"bold"))
check_mark.grid(column=1, row=3)
# creating an edit button for editing minutes for pomodoro application.
edit_button = Button(window, text="Edit", command=trial)
edit_button.grid(column=0, row=2)
window.mainloop()
