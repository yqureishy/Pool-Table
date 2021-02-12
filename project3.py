import datetime 
time = datetime.datetime.now()

class PoolTable: 
    def __init__(self, table_number): 
        self.table_number = table_number
        self.is_occupied = False 
        self.start_time = None
        self.end_time = None 

    def checkout(self): 
        self.is_occupied = True 
        self.start_time = datetime.datetime.now()
    def checkin(self): 
        self.is_occupied = False 
        self.end_time = datetime.datetime.now()

    def get_time_played(self):
        if self.start_time == None:
            return (time - time)
        elif self.end_time == None:
            return (time - self.start_time)
        else:
            return(self.end_time - self.start_time)

time = datetime.datetime.now()
# Creates 12 objects of class Pool_Table 
# and enters them into pool_tables array
pool_tables = []
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