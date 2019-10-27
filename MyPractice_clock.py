import time
class Oclock():
    def __init__(self,hour = 0,min = 0,sec = 0):
        self.hour= hour
        self.min = min
        self.sec = sec

    def Run(self):
        self.sec += 1
        if self.sec == 60:
            self.min += 1
            self.sec = 0
        if self.min == 60:
            self.hour += 1
            self.min = 0
        if self.hour == 24:
            self.hour = 0

    def ShowTime(self):
        print("%02d:%02d:%02d" %(self.hour,self.min,self.sec))

times = Oclock(23,59,50)
while True:
    times.ShowTime()
    time.sleep(1)
    times.Run()






