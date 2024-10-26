import time
from plyer import notification # pip install plyer

def send_notification(message):
    """Display a desktop notification."""
    notification.notify(
        title="Pomodoro Timer",
        message=message,
        timeout=10 #Notification timeout
    )

def pomodoro_timer(work_minutes=25, short_break_minutes=5, long_break_minutes=15, cycles=4):
    """Run a Pomodoro timer with work/break cycles."""
    for cycle in range(1, cycles + 1):
        # Work period
        send_notification("Time to focus! Work for 25 minutes.")
        time.sleep(work_minutes * 60)  # Work interval

        # Check if it's time for a long break
        if cycle % cycles == 0:
            send_notification("Great job! Take a 15-minute break.")
            time.sleep(long_break_minutes * 60)  # Long break interval
        else:
            send_notification("Take a 5-minute break.")
            time.sleep(short_break_minutes * 60)  # Short break interval

# Start the Pomodoro timer
pomodoro_timer()
