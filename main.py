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
    global reps
    window.after_cancel(timer)
    cavas.itemconfig(timer_text, text=f"00:00")
    timer_lable.config(text="Timer", fg=GREEN)
    tik_lable.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    reps += 1
    if reps in [1,3,5,7]:
        timer_lable.config(text="Work", fg=GREEN)

        count_down(work_sec)
        print("work 25 sec ")



    elif reps == 8:
        timer_lable.config(text="Break", fg=RED)
        count_down(long_break_sec)
        print("long break 20 sec")


    elif reps in [2,4,6]:
        timer_lable.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        print("short break 5 ")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    cavas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        tik="✔"
        if reps%2==0:
            tik_lable.config(text=f"{tik*math.floor(reps/2)}")

        # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomidoro")
window.config(padx=100, pady=50, bg=YELLOW)




cavas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
cavas.create_image(100, 112, image=tomato_img)
timer_text = cavas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
cavas.grid(row=1,column=1)
# cavas.pack( )


timer_lable = Label(text="Timer", fg=GREEN,  bg=YELLOW, font=(FONT_NAME,40))
timer_lable.grid(row=0,column=1)

stat_button = Button(text="Start",background=YELLOW, highlightthickness=0, command=start_timer)
stat_button.grid(row=2,column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

tik_lable = Label(bg=YELLOW, fg=GREEN,font=(FONT_NAME,35,"bold"))
tik_lable.grid(row=3,column=1)

window.mainloop()