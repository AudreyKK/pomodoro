# # # # # ## # # # # ## # # # # ## # # # # ## # # # # ## # # # # ## # # # # #
# Default time for pomodoro is 25 min
# # # # # ## # # # # ## # # # # ## # # # # ## # # # # ## # # # # ## # # # # #

import time
import datetime as dt
import tkinter
from tkinter import messagebox
import alarm


t_now = dt.datetime.now()
t_pom = 25 * 60
t_delta = dt.timedelta(0, t_pom)
t_fut = t_now + t_delta
delta_sec = 5 * 60
t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)


root = tkinter.Tk()
root.withdraw()

messagebox.showinfo("Pomodoro Started!", "\nIt is now "+t_now.strftime("%H:%M") +
" hrs. \nTimer set for 25 mins.")


total_pomodoros = 0
breaks = 0

# Main Script
while True:
    # Pomodoro time
    if t_now < t_fut:
        print('pomodoro')
    ## It is now past working pomodoro within the break
    elif t_fut <= t_now <= t_fin:
        # check if is firt time here, if so, ring bell
        print('in break')
        if breaks == 0:
            print('if break')
            # Annoy
            for i in range(5):
                alarm.alarm(7)
            print('Break time!')
            breaks += 1
    else:
        print('finished')
        breaks = 0
        for i in range(10):
            alarm.alarm(5)

        usr_ans = messagebox.askyesno("Pomodoro is finished!", "Would you like to start another pomodoro?")
        total_pomodoros += 1
        if usr_ans == True:
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)
            continue
        elif usr_ans == False:
            messagebox.showinfo("""Pomodoro Finished! \nYou completed"""
            +str(total_pomodoros)+ """pomodoros today!""")
            break
    print('sleeping')
    time.sleep(20)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")
