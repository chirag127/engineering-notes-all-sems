## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both protocols use broadcast messages to request and reply the address mappings.
- The code below is a Python program that simulates the ARP and RARP protocols using sockets and threads.

```python
# Import the required modules
import socket
import threading
import time

# Define the broadcast address and port
BROADCAST_ADDR = "255.255.255.255"
BROADCAST_PORT = 5000

# Define the IP and MAC address mappings
IP_MAC_TABLE = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
    "192.168.1.4": "00:0a:95:9d:68:19",
}

MAC_IP_TABLE = {
    "00:0a:95:9d:68:16": "192.168.1.1",
    "00:0a:95:9d:68:17": "192.168.1.2",
    "00:0a:95:9d:68:18": "192.168.1.3",
    "00:0a:95:9d:68:19": "192.168.1.4",
}

# Define a function to create a UDP socket
def create_socket():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Enable broadcasting
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Bind the socket to the broadcast address and port
    sock.bind((BROADCAST_ADDR, BROADCAST_PORT))
    # Return the socket
    return sock

# Define a function to handle ARP requests
def handle_arp_request(sock, addr, data):
    # Extract the source and destination IP addresses from the data
    src_ip, dst_ip = data.split()
    # Print the ARP request message
    print(f"Received ARP request from {src_ip} to {dst_ip}")
    # Check if the destination IP address is in the IP-MAC table
    if dst_ip in IP_MAC_TABLE:
        # Get the corresponding MAC address
        dst_mac = IP_MAC_TABLE[dst_ip]
        # Create the ARP reply message
        reply = f"{dst_ip} {dst_mac}"
        # Send the ARP reply message to the source address
        sock.sendto(reply.encode(), addr)
        # Print the ARP reply message
        print(f"Sent ARP reply to {src_ip} with {dst_ip} {dst_mac}")

# Define a function to handle RARP requests
def handle_rarp_request(sock, addr, data):
    # Extract the source and destination MAC addresses from the data
    src_mac, dst_mac = data.split()
    # Print the RARP request message
    print(f"Received RARP request from {src_mac} to {dst_mac}")
    # Check if the destination MAC address is in the MAC-IP table
    if dst_mac in MAC_IP_TABLE:
        # Get the corresponding IP address
        dst_ip = MAC_IP_TABLE[dst_mac]
        # Create the RARP reply message
        reply = f"{dst_mac} {dst_ip}"
        # Send the RARP reply message to the source address
        sock.sendto(reply.encode(), addr)
        # Print the RARP reply message
        print(f"Sent RARP reply to {src_mac} with {dst_mac} {dst_ip}")

# Define a function to listen for incoming messages
def listen(sock):
    # Loop forever
    while True:
        # Receive a message from the socket
        data, addr = sock.recvfrom(1024)
        # Decode the message
        data = data.decode()
        # Check if the message is an ARP request
        if data.startswith("ARP"):
            # Handle the ARP request
            handle_arp_request(sock, addr, data[4:])
        # Check if the message is a RARP request
        elif data.startswith("RARP"):
            # Handle the RARP request
            handle_rarp_request(sock, addr, data[5