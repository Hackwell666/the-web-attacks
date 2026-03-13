# now we are going to use python typosquatting .

import os 
import time 
import platform
import subprocess
from pynput.keyboard._base import Key, Controller

working = ["Kayson"]

def ducky():
    kb = Controller()
    
    for line in working:
        kb.type("adm.Siphe")
        kb.press(Key.enter)
        kb.release(Key.enter)
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.enter)
        kb.release(Key.enter)
    
    for ch in line:
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.enter)
        kb.release(Key.enter)
        kb.type("admin")
        kb.press(Key.tab)
        kb.type("spare")
        kb.press(Key.enter)
        kb.release(Key.enter)
admin = True   
def main():
    if platform.system == "Windows":
        msg = input("Do you want to test your system")
        if msg.capitalize == "yes" or "YES" or "YEAH":
            time(0.6)
            subprocess.run("WSL --install kali linux" , shell=True)
            subprocess.run(working)
        else:
            exit("I got rejected")
    elif platform.system == "Linux" or "macOS":
        subprocess.run("WSL --install kali linux {line}")
    else:
        exit("wrong codes inside in")
        

main()

try:
    def evelaution():
        os.system == "NT"
        evelaution = input("do you want to try it ?\n ")
        if evelaution.capitalize() == "Yes":
            subprocess.run("")
        elif evelaution.capitalize == "no":
            subprocess.run("shutdown /r")
        else:
            print("don't recognise the answer {evelaution}")
except Exception as e:
    print(f"an error was founded{e}")

# now let's lookup what's inside the system of this person

def system_check():
    if platform.system == "Windows":
        subprocess.run("dir/s")
    elif platform.system == "Linux":
        subprocess.run("sudo,apt,install nmap")
    else:
        print("not founded")

system_check()
    