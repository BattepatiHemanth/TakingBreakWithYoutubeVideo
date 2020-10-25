import time
import webbrowser

#number of breaks
total_breaks = 4
break_count = 0

print("This program started on" +time.ctime())
while(break_count < total_breaks):
    time.sleep(2)#2hours (you can define this in many ways but associated with seconds)
    webbrowser.open("https://www.youtube.com/watch?v=5yBSJ2Z6pjY")
    break_count = break_count+1
