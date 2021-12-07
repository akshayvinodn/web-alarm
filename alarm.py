import time
import webbrowser
Actual_Time=time.strftime("%I:%M:%S")
print(Actual_Time)
Set_Alarm =input("set the website alarm as H:M:S(all in the digits):")
url= input("enter the website you want to open:")
Actual_Time=time.strftime("%I:%M:%S")

while (Actual_Time != Set_Alarm):
    print("the time is"+Actual_Time)
    Actual_Time=time.strftime("%I:%M:%S")
    time.sleep(1)
if (Actual_Time == Set_Alarm):
    print("opening now:" +url)
    webbrowser.open(url)