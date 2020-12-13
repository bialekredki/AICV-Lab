import tkinter
import datetime

START_DAY = 28
START_MONTH = 11
START_YEAR = 2020
START_HOUR = 17
START_MINUTE = 19
START = datetime.datetime(START_YEAR,START_MONTH,START_DAY,START_HOUR,START_MINUTE,0,0)
string = "xd"

def stripTime(time:str):
    arr = time.split("h")
    return int(arr[0]), int(arr[1])

def stripDate(date:str):
    arr = date.split(".")
    return int(arr[0]), int(arr[1]), int(arr[2])

def getDate(time:str):
    arr = time.split(' ')
    hour, minute = stripTime(arr[1])
    day,month,year = stripDate(arr[0])
    return datetime.datetime(year,month,day,hour,minute,0)

def calculateDifference(time=None):
    if time is None:
        now = datetime.datetime.now()
        delta = (now - START)
        return round(delta.total_seconds()/60)
    return round((time - START).total_seconds()/60)

def szuszu(datestr):
    date = getDate(datestr)
    string = "{}".format(calculateDifference(date))
    result.delete(0, tkinter.END)
    result.insert(0, string)

def szuszu_now():
    string = "{}".format(calculateDifference())
    result.delete(0,tkinter.END)
    result.insert(0,string)
    set2Now()

def set2Now():
    now = datetime.datetime.now()
    txtime.delete(0,tkinter.END)
    txtime.insert(0, "{}.{}.{} {}h{}".format(now.day, now.month, now.year, now.hour, now.minute))


window = tkinter.Tk()
window.title("All aboard dziekanka train!")
button = tkinter.Button(text="szuuszu", bg="black", fg="white", command=lambda:szuszu(txtime.get()))
now_button = tkinter.Button(text="szuuszu now", bg="black", fg="white", command=szuszu_now)
txtime = tkinter.Entry()
result = tkinter.Entry()
set2Now()
button.pack()
now_button.pack()
txtime.pack()
result.pack()
result.insert(0,string)
window.mainloop()
exit()

