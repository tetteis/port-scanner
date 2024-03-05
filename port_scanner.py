#!/bin/python

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    # Print error message for incorrect arguments
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()  # Terminate the script if incorrect syntax is provided

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):  ## Scan ports from 50 to 85
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set timeout for connection attempt
        # Check if the port is open
        result = s.connect_ex((target, port))
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))  # Print if port is open
        s.close()

except KeyboardInterrupt:
    # Handle keyboard interrupt gracefully
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    # Handle hostname resolution error
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    # Handle generic socket error
    print("Couldn't connect to server.")
    sys.exit()
