from datetime import datetime 

class PoolTable: 
    def __init__(self, table_number): 
        self.table_number = table_number
        self.is_occupied = False 
        self.start_time = None
        self.end_time = None 

    def checkout(self): 
        self.is_occupied = True 
        self.start_time = datetime.now()
    def checkin(self): 
        self.is_occupied = False 
        self.end_time = datetime.now()

    def get_time_played(self):
        if self.start_time == None:
            return
        elif self.end_time == None:
            return
        else:
            return self.end_time - self.start_time