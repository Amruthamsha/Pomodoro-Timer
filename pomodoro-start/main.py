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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
# noinspection PyTypeChecker
def reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lab.config(text="TIMER", fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_time)
        timer_lab.config(text="Looong Break!!", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_time)
        timer_lab.config(text="Break!", fg=RED)
    else:
        count_down(work_time)
        timer_lab.config(text="TIMER", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min =math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sesh = math.floor(reps/2)
        for _ in range(work_sesh):
            marks+="✔"
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=75, pady=75, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#start-button
start_lab = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_lab.grid(column=0, row=2)

#reset-button
start_lab = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset)
start_lab.grid(column=2, row=2)

#timer-header
timer_lab = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_lab.grid(column=1, row=0)

#TICK_MARK
tick_label = Label(text="", fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

window.mainloop()