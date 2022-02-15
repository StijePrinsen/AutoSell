import time, pynput, threading, playsound

keyboard = pynput.keyboard.Controller()

isActive = False

def on_press(key):
    global isActive

    if 'char' in dir(key):
        if key.char == "o":
            if isActive != True:
                t = threading.Thread(target=AutoMine)
                t.start()

    if 'char' in dir(key):
        if key.char == "i":
            isActive = False

def AutoMine():
    global isActive
    isActive = True
    while True:
        if not isActive:
            break
        playsound.playsound(r'C:\Users\Doe040\Desktop\Ping.mp3')
        keyboard.tap('/')
        time.sleep(0.02)
        keyboard.tap(pynput.keyboard.Key.up)
        time.sleep(0.02)
        keyboard.tap(pynput.keyboard.Key.enter)
        time.sleep (10)


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()