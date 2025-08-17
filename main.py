import time
import notificationDisplay  #The notification displayer file

def countdown(minutes):
    for remaining in range(minutes*60, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"Time left: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)

#Calculation: 1200 seconds = 20 minutes

def start():
    notificationDisplay.displayNotification("Learning Session","This is the time to learn something new about current coding language from youtube")
    countdown(20)
    
    notificationDisplay.displayNotification("Practicing Time","Practice what you learnt from the youtube")
    countdown(15)
    
    notificationDisplay.displayNotification("Research Time","Research about some new thing in tech/coding from platforms like reddit etc.")
    countdown(12)
    
    notificationDisplay.displayNotification("Share what you learnt","Make notes and share the code in the github,reddit and discord")
    countdown(15)
    
    notificationDisplay.displayNotification("Free!","Now you are free!")

start()