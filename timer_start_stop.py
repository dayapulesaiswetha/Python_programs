import time
from datetime import datetime,date



class Timer:

    # def __init__(self, starttime):
    #     self.starttime = starttime
    #     self.endtime = None


    def start(self):
        self.starttime = datetime.now()
        print(f'start time: {self.starttime}')
        
    def end(self):
        self.endtime = datetime.now()
        print(f'end time: {self.endtime}')
    
    def duration(self):
        print(self.endtime - self.starttime)

    # def __del__(self):
    #     self.endtime = datetime.now()
    #     print(self.endtime) 

    


#timer = Timer(datetime.now())
timer = Timer()
timer.start()
time.sleep(5)
timer.end()
timer.duration()

# duration = a.duration()
# print(f'duration: {duration}')
#del a

