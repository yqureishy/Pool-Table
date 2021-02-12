from datetime import datetime 
from class_file import PoolTable
import json
time_now = datetime.now().strftime("%H:%M:%S")
date_now = datetime.now().strftime("%m/%d/%Y")


pool_tables = []
j_son = []

for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)
def display():
    for index in range(0,12):
        pool_table = pool_tables[index]
        print(f"Table #{pool_table.table_number} -- Is it occupied: {pool_table.is_occupied} -- Start Time: {pool_table.start_time} -- End Time: {pool_table.end_time} -- Time Played: {pool_table.get_time_played()}")
    
def menu():
    print('''Choose from one of the following options:

    1. Display Tables
    2. Check out Table
    3. Check in Table
    4. Quit
    ''')

while True:

    menu()
    choice = input("Input one of the numbers from the menu above: ")

    if choice == "1":
        display()
    elif choice == "2":
        display()
        selection = int(input("Select the table number you want to checkout: "))
        pool_table = pool_tables[selection-1]
        pool_table.checkout()
    elif choice == "3":
        display()
        selection = int(input("Select the table number you want to checkin: "))
        pool_table = pool_tables[selection - 1]
        pool_table.checkin()
        with open(f"{datetime.now().strftime('%m-%d-%Y')}.json", "w") as file:
            p_table = {"table number": pool_table.table_number, "check out time": pool_table.start_time.strftime('%H:%M:%S'), "check in time": pool_table.end_time.strftime('%H:%M:%S')}
            j_son.append(p_table)
            json.dump(j_son, file)
    elif choice == "4":
        break
    else:
        print("Please select from one of the options below.")

