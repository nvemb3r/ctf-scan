##########################################
# ctf-scan.py by Zack Nelson (@nvemb3r)  #
##########################################

import socket
import os
from typing import List

targetHost = "192.168.1.1"


def portscan(host):
    curport = 0
    openports: List[int] = []

    # Scan every port on the target host
    while curport < 65535:
        try:
            # Attempt to connect to the host on a particular machine, and add it if it succeeds
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, curport))

            # If we can connect to the host on that port, add it to the list, and increment
            openports.append(curport)
            curport = curport + 1
        except ConnectionRefusedError:
            # Port is closed, increment
            curport = curport + 1

        # Close the connection, if one is still open
        connection.close()
    return openports


# Initiate portscan, and store open ports
openTcpPorts = portscan(targetHost)

# Run nmap, and store output in multiple file formats
os.system("nmap -A -T4 -oA " + str(targetHost) + "-scan -p " + ','.join(str(p) for p in openTcpPorts) + " "
          + str(targetHost))
