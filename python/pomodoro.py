# Simple Pomodoro timer 

import time
import threading
from plyer import notification # pip install plyer

def send_notification(title, message):
    notification.notify(title=title, message=message, timeout=10)

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

## notify when the countdown finishes
    print("Time's up!")

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def pomodoro_timer():
    work_minutes = get_positive_integer("Enter work minutes (default 25): ") or 25
    short_break_minutes = get_positive_integer("Enter short break minutes (default 5): ") or 5
    long_break_minutes = get_positive_integer("Enter long break minutes (default 15): ") or 15
    cycles = get_positive_integer("Enter number of cycles (default 4): ") or 4

    for cycle in range(1, cycles + 1):

 # start countdown for work period
        send_notification("Pomodoro Timer", "Time to focus!")
        countdown(work_minutes * 60)

        if cycle % cycles == 0:
            send_notification("Pomodoro Timer", "Great job! Take a 15-minute break.")
            countdown(long_break_minutes * 60)
        else:
            send_notification("Pomodoro Timer", "Take a 5-minute break.")
            countdown(short_break_minutes * 60)

        print(f"Completed cycle {cycle}/{cycles}.")

# Start the Pomodoro timer
pomodoro_timer()
