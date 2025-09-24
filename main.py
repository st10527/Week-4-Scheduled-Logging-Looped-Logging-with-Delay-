import psutil
from datetime import datetime
import csv
import os

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # TODO: Use psutil to get CPU, memory, and disk usage
    cpu = 
    memory = 
    disk = 
    
    return [now, cpu, memory, disk]

def write_log(data):
    # TODO: Check if log.csv exists
    # If not, create it and write a header row
    # Then append the current data row
    pass

if __name__ == "__main__":
    row = get_system_info()
    write_log(row)
    print("Logged:", row)
