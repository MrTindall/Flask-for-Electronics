import time

class Functions:
    
    is_running = False
    
    def __init__(self) -> None:
        pass
    
    def count_to_100(self):
        for i in range(0, 100):
            print(i)
            time.sleep(.05)
            print(self.is_running)
            
            if not self.is_running:
                break

    def print_hello_100_times(self):
        for i in range(0, 100):
            print("hello")
            time.sleep(0.05)
            
            if not self.is_running:
                break
    
    def set_is_running(self, bool):
        self.is_running = bool
