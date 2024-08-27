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
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps+=1

    if reps % 8 ==0:
        count_down(long_break_sec)
        timer.config(text="Break",fg="red")
    elif reps % 2 == 0:
        timer.config(text="Break",fg="pink")
        count_down(short_break_sec)
    else:
        label.config(text="Work",fg="Green")
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        emp = ""
        work_sessions = math.floor(reps/2)
        for x in range(work_sessions):
            emp+="✔"
        check.config(text=emp)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg="yellow")


#added an image using canvas and added background color and text
canvas = Canvas(width=200,height=224,bg="yellow", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
fg = GREEN

canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer",fg=fg,bg="yellow",font=(FONT_NAME,50))
label.grid(column=1,row=0)

start = Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=3)

reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=3,row=3)

check = Label(text="✔",fg="green",bg="yellow")
check.grid(column=1,row=4)


window.mainloop()