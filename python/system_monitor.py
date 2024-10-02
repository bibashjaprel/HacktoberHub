#!/usr/bin/env python3

import psutil
import time

def monitor_system():
    while True:
        # CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")

        # Memory usage
        memory = psutil.virtual_memory()
        print(f"Memory Usage: {memory.percent}%")

        # Disk usage
        disk_usage = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_usage.percent}%")

        print("-" * 30)
        time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    monitor_system()
