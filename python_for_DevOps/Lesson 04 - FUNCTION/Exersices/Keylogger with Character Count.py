import pynput

def on_press(key):
    global count
    count += 1
    print(f"Key pressed: {key}, Total keys pressed: {count}")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

count = 0
with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print(f"Total keys pressed: {count}")