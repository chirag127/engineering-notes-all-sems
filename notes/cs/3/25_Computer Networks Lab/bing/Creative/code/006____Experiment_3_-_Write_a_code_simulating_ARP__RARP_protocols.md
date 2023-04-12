Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a physical address (MAC address) of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a physical address (MAC address) to an IP address of a device on the same network.
- Both ARP and RARP are used to resolve the addresses of devices that communicate on the same network layer (layer 2) of the OSI model.
- The basic steps of ARP and RARP are as follows:

  - ARP:
    - A device (sender) that wants to communicate with another device (target) on the same network sends an ARP request packet to the broadcast address (FF:FF:FF:FF:FF:FF) with the target's IP address and its own MAC and IP addresses.
    - All devices on the network receive the ARP request packet and check if the target's IP address matches their own IP address.
    - If a device (target) finds a match, it sends an ARP reply packet to the sender's MAC address with its own MAC and IP addresses.
    - The sender receives the ARP reply packet and updates its ARP cache with the target's MAC and IP address.
    - The sender can now communicate with the target using its MAC address.

  - RARP:
    - A device (sender) that does not have an IP address but has a MAC address sends a RARP request packet to the broadcast address (FF:FF:FF:FF:FF:FF) with its own MAC address.
    - All devices on the network receive the RARP request packet and check if they have an IP address assigned to the sender's MAC address.
    - If a device (target) has an IP address assigned to the sender's MAC address, it sends a RARP reply packet to the sender's MAC address with its own MAC and IP addresses.
    - The sender receives the RARP reply packet and updates its IP configuration with the target's IP address.
    - The sender can now communicate with other devices using its IP address.

- Here is a sample code in Python that simulates the ARP and RARP protocols:

```python
# Importing the socket module
import socket

# Creating a raw socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

# Defining the MAC and IP addresses of the devices
mac_a = "00:0a:95:9d:68:16"
ip_a = "192.168.1.1"
mac_b = "00:0a:95:9d:68:17"
ip_b = "192.168.1.2"
mac_c = "00:0a:95:9d:68:18"
ip_c = "192.168.1.3"
mac_d = "00:0a:95:9d:68:19"
ip_d = ""

# Defining the broadcast address
broadcast = "FF:FF:FF:FF:FF:FF"

# Defining the ARP and RARP packet formats
arp_request = mac_a + broadcast + "0806" + "0001" + "0800" + "06" + "04" + "0001" + mac_a + ip_a + "000000000000" + ip_b
arp_reply = mac_b + mac_a + "0806" + "0001" + "0800" + "06" + "04" + "0002" + mac_b + ip_b + mac_a + ip_a
rarp_request = mac_d + broadcast + "8035" + "0001" + "0800" + "06" + "04" + "0003" + mac_d + "00000000" + "000000000000" + "00000000"
rarp_reply = mac_c + mac_d + "8035" + "0001" + "0800" + "06" + "04" + "0004" + mac_c + ip_c + mac_d + ip_d

# Converting the packets to bytes
arp_request = bytes.fromhex(arp_request.replace(":", ""))
arp_reply = bytes.fromhex(arp_reply.replace(":", ""))
rarp_request = bytes.fromhex(rarp_request.replace(":", ""))
rarp_reply = bytes.fromhex(rarp_reply.replace(":", ""))

# Sending and receiving the packets
s

```
