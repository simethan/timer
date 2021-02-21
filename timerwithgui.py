import time, datetime
from playsound import playsound
from tkinter import *
from tkinter import messagebox        
x = [input("One by one, hour, min, sec. ") for i in range(3)]
root = Tk()
root.geometry("960x540")

root.title("Time Counter")
root.configure(bg='black')

tim = StringVar()
hour = StringVar()
minute  = StringVar()
second = StringVar()
text = StringVar()

hour.set(int(x[0]))
minute.set(int(x[1]))
second.set(int(x[2]))
tim.set("")
text.set("H/M/S")
display = Label(root,font=("Arial",80,"bold"), fg = "white", bg = "black", textvariable=text)
display.pack(anchor = "w", side = TOP)

hours= Label(root, font=("Arial ",100,"bold"), fg = "white", bg = "black", textvariable=hour)
hours.pack(side=LEFT)
  
minutes= Label(root, font=("Arial ",100,"bold"), fg = "white", bg = "black", textvariable=minute)
minutes.pack(side=LEFT)
  
seconds= Label(root, font=("Arial ",100,"bold"), fg = "white", bg = "black", textvariable=second)
seconds.pack(side=LEFT)

timern = Label(root, font=("Arial ", 12, "bold"), fg = "white", bg = "black", textvariable=tim)
timern.pack( anchor = "e", side = BOTTOM)

temp = 0
def poop():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        timee = datetime.datetime.now().strftime('%H:%M:%S %p')
        mins,secs = divmod(temp,60) 

        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
            
        text.set("Time Left:")
        hour.set("{0:2d}H".format(hours))
        minute.set("{0:2d}M".format(mins))
        second.set("{0:2d}S".format(secs))
        tim.set(f"Current time: {timee}")
        root.update()
        time.sleep(1)
    
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            root.quit()
        temp -= 1

btn = Button(root, text='Start Countdown',bd = 2, fg = "white", bg="black" ,command= poop)
btn.place(x = 850,y = 450)
root.bind("x", quit)
root.mainloop()

