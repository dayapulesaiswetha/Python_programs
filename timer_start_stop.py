#import time
#from datetime import datetime,date

#class Timer:

#    def start(self):
        # self.starttime = datetime.now()
        # print(f'start time: {self.starttime}')
        
    # def end(self):
    #     self.endtime = datetime.now()
    #     print(f'end time: {self.endtime}')
    
    # def duration(self):
    #     print(self.endtime - self.starttime)

    # def __del__(self):
    #     self.endtime = datetime.now()
    #     print(self.endtime) 

    


#timer = Timer(datetime.now())
# timer = Timer()
# timer.start()
# time.sleep(5)
# timer.end()
# timer.duration()


import time
import datetime

def timer_example(total_seconds):
    
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer,end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("End of countdown")

seconds = input('Enter number of second')
timer_example(int(seconds))
