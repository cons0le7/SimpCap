from scapy.all import sniff, wrpcap
import datetime 

def color_purple(text):
    PURPLE = "\033[35m" 
    RESET = "\033[0m"
    return f"{PURPLE}{text}{RESET}" 

def color_cyan(text):
    CYAN = "\033[36m" 
    RESET = "\033[0m"
    return f"{CYAN}{text}{RESET}"

def log_packet(packet):
    print(color_cyan(packet.summary()))
    wrpcap(log_file, packet, append=True)

print(color_purple(""" 

  _________.__               _________                
 /   _____/|__| _____ ______ \_   ___ \_____  ______  
 \_____  \ |  |/     \\____ \/    \  \/\__  \ \____ \ 
 /        \|  |  Y Y  \  |_> >     \____/ __ \|  |_> >
/_______  /|__|__|_|  /   __/ \______  (____  /   __/ 
        \/          \/|__|           \/     \/|__|    


""")) 

choice = input(color_purple("Logs are stored in /SimpCap/logs.pcap \n\nPress Enter to start.\n\nPress Ctrl + C to stop. \n\n"))

log_file = "logs.pcap"
sniff(prn=log_packet, store=0)


