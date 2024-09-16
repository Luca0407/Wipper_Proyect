import time

while True:
    print(time.strftime('%H:%M'), end="\r")
    time.sleep(1)