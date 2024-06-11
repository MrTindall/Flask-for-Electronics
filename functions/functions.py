import time

class Functions:

    def __init__(self):
       self.is_running = False
    
    def count_to_100(self):
        for i in range(0, 100):
            print(i)
            time.sleep(.001)
            
            if not self.is_running:
                break

    def print_hello_100_times(self):
        for i in range(0, 100):
            print("hello")
            time.sleep(.001)
            
            if not self.is_running:
                break
    
    def set_is_running(self, bool):
        self.is_running = bool
