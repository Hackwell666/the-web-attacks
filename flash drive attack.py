
import time
from pynput.keyboard import Controller # pyright: ignore[reportMissingModuleSource]
from pynput.keyboard import Key
import subprocess
import platform

def ducky_demo():
    kb = Controller()

    # Wait 3 seconds so you can click into a text editor (e.g., Notepad)
    print("The SIPHE 6 GOD WILL START >>>>>>. Typing starts in 6 seconds...")
    time.sleep(6)

    # The payload (safe and harmless)
    payload = []
    if platform.system() == "Windows":
            subprocess.run(
                "WSL --install kali linux", shell=True
            )
    else:
        raise SystemError("Error")
    for line in payload:
        for ch in line:
            kb.press(Key.enter)
            kb.press(ch)
            kb.release(ch)
            time.sleep(0.05)  # slow down so you can see it type
        kb.press("\n")
        kb.release("\n")
        time.sleep(1)

if __name__ == "__main__":
    ducky_demo()
