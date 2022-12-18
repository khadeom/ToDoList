from django.shortcuts import render
import time
# Create your views here.

def pal(request):
    for i in range(100,100000):
        if str(i)==str(i)[::-1]:
            # 10000
            print(i)

    return render(request,"pal.html")
# pal()
        
# create a stopwatch that having three functionality hr, mins, sec and three buttons like start, stop, resume



class Stopwatch():

    def __init__(self):
        self.on = False
        self.start_time = time.time()
        print(time.time())

    def show(self,test=0):
        
        if self.on:
            interval = time.time()- self.start_time
            if test:
                interval =test

            if interval <60:
                sec = int(interval)
                if interval<10:
                    sec="0"+str(sec)

                print(f"00:00:{sec}")
            elif interval//60 <60:
                sec = int(interval%60)
                min = int(interval//60)
                if interval%60 < 10:
                    sec = "0"+str(sec)
                if interval//60<10:
                    min = "0" +str(min)
                print("00:{min}:{sec}") 

            else:
                sec=interval%60

                interval -=sec
                interval /= 60
                min = int(interval%60)
                hr = int(interval//60)
                if sec<10:
                    sec = "0"+str(sec)
                if min<10:
                    min = "0" +str(min)
                if hr<10:
                    hr  = "0"+str(hr)


                print(f"{hr}:{min}:{sec}")


            










        else:
            print("00:00")


    def start(self):
        if self.on:
            print("stop watch is running")
            self.show()
        
        else:
            self.on=True
            print("stop watch started")
            self.start_time = time.time()

    def reset(self):
        self.start_time = time.time()
        print("00:00")

watch =  Stopwatch()

watch.show()
watch.start()

# time.sleep(3)
watch.show(50)

watch.show(500)
watch.show(50000)



    
        






