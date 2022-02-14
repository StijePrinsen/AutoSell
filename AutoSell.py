import time, pynput, threading
keyboard = pynput.keyboard.Controller()

isActive = False

def on_press(key):
    global isActive

    if 'char' in dir(key):
        if key.char == "o":
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
        keyboard.tap('/')
        time.sleep(0.02)
        keyboard.tap(pynput.keyboard.Key.up)
        time.sleep(0.02)
        keyboard.tap(pynput.keyboard.Key.enter)
        time.sleep (10)


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()