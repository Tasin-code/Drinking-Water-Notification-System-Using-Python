import time
from plyer import notification

def drink_water(title, message):
    while True:
        notification.notify(
            title = title,
            message = message,
            app_icon = ".\\water_1.ico",
            timeout = 7
        )
        time.sleep(60*60)

if __name__ == '__main__':
    drink_water("Please Drink Water Now!!", "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men About 11.5 cups (2.7 liters) of fluids a day for women")