# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]


# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry


import win32com.client as wincl


l = ["Rahul", "Nishant", "Harry"]

speak = wincl.Dispatch("SAPI.SpVoice")

for i in l:
    speak.Speak(f"Shout out to {i}")


#Output: IN VOICE
#Shoutout to Rahul
#Shoutout to Nishant
#Shoutout to Harry


