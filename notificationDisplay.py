from plyer import notification

def displayNotification(titleImp,messageImp):
    notification.notify(
        title= titleImp,
        message= messageImp,
    )

if __name__=="__main__":
    print("Import Successfull from the notification.py")