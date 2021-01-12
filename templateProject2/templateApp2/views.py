from django.shortcuts import render
import datetime
def Datetime(request):
    dt=datetime.datetime.now()
    h1=dt.strftime('%H')
    h=int(h1)
    if(h<12):
        msg="Good morning"
    elif(h<15):
        msg="Good afternoon"
    elif(h<20):
        msg="Good evening"
    else:
        msg="Good night"
    d={'datetime':dt,'wishes':msg}
    return render(request,'templateApp2/1.html',d)
