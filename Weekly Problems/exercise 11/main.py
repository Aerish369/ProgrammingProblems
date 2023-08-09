
#! Exercise 11 - Drink Water Reminder

#* Write a python program which reminds you of drinking water 
#* every hour or two. Your program can either beep or send desktop 
#* notifications for a specific operating system

#?Alternative method
# from win10toast import ToastNotifier

# notification = ToastNotifier()

# notification.show_toast("Drink Water", "Hello Aerish!\nThis is a reminder for you to drink water.\nStay Hydrated!!! I wuv you.", duration=3)


from winotify import Notification, audio
import time




while True:
    notify = Notification(app_id="Aerish Script",
                    title="Drink Water Reminder",
                    msg="Hello Aerish!\nThis is a reminder for you to drink water.\nStay Hydrated!!! I wuv you.",
                    duration="short",
                    icon=r"C:\Users\aryal\OneDrive\Desktop\Programming Problems\Weekly Problems\week1\zoro.jpeg")

    notify.set_audio(audio.Default, loop=False)
    notify.add_actions(label="Importance of water", launch="https://www.healthline.com/health/food-nutrition/why-is-water-important#saliva")
    
    notify.show()
    time.sleep(5)
    
