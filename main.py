import tkinter  as tk #GUI for the interface
from actualTime import Time #a class that gets mi the current time, it easily be put in the main
from actualDate import CurrentDate # a class that gets me the current date, useful to convert month number to name and get day of the weak

interface = tk.Tk() #instance tk
interface.geometry("800x300")  #proportions of the window whit the clock
font_date=('times',20,'italic') # display size and style for the date
font_clock=('times',60,'bold') # display size and style for the clock
l1=tk.Label(interface,font=font_date,bg='green') #design  of first line
l1.grid(row=1,column=1,padx=5,pady=5)
l2=tk.Label(interface,font=font_clock,bg='red')#design  of second line
l2.grid(row=2,column=1,padx=5,pady=1)

def get_date():
    dateTime=CurrentDate()  #implementation of current date
    date_string= 'Today is '+(str(dateTime.getDayNumber()))+' of '+(str(dateTime.getMonthName()))+' of the year is '+(str(dateTime.getYear()))+ '. is a '+(str(dateTime.getDayName()))
    time_string = Time.getHour()+':'+Time.getMinute()+':'+Time.getSecond()  
    l1.config(text=date_string)
    l2.config(text=time_string)
    l2.after(1000,get_date)


get_date()
interface.mainloop()



