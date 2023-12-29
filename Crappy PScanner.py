import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Transalte hostname to IPV4
else:
    print("Invalid amount of arguments. ")
    print("Syntax: python3 scanner.py <ip>") 

#Add a pretty banner
print("-" * 50)
print("Scanning a target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #if a socket or port is not responsing within a sacket we are moving to next
        result = s.connect_ex((target, port))
        if result ==0:
            print(f"Port {port} is open")  
            #Types of string formatting
#             print("My favorite movie is {}.".format(movie))
# print("My favorite movie is %s" % movie)
# print(f"My favorite movie is {movie}")
            s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
