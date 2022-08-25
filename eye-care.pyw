from win10toast import ToastNotifier
import time

while (True):
    toast = ToastNotifier()
    toast.show_toast("Eye Care", "Take 20 second break", duration=5)
    time.sleep(1200)
    
