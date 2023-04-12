## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both ARP and RARP use broadcast messages to request and reply the address mappings.
- The following is a pseudocode for simulating ARP /RARP protocols:

```
# Define a class for a device on the network
class Device:
  # Initialize the device with its IP and MAC addresses
  def __init__(self, ip, mac):
    self.ip = ip
    self.mac = mac
    self.arp_table = {} # A dictionary to store the ARP cache
    self.rarp_table = {} # A dictionary to store the RARP cache

  # A method to send an ARP request to the network
  def arp_request(self, target_ip):
    # Broadcast a message to the network with the target IP and the sender's IP and MAC addresses
    broadcast_message = f"ARP request: Who has {target_ip}? Tell {self.ip}, {self.mac}"
    print(f"{self.ip} sends {broadcast_message}")
    # Return the broadcast message
    return broadcast_message

  # A method to receive an ARP request from the network
  def arp_receive(self, message):
    # Parse the message and extract the target IP, the sender IP and the sender MAC addresses
    message_parts = message.split()
    target_ip = message_parts[2]
    sender_ip = message_parts[4][:-1]
    sender_mac = message_parts[5]
    # Check if the target IP matches the device's IP
    if target_ip == self.ip:
      # Send an ARP reply to the sender with the device's IP and MAC addresses
      self.arp_reply(sender_ip, sender_mac)
    # Update the ARP cache with the sender's IP and MAC addresses
    self.arp_table[sender_ip] = sender_mac

  # A method to send an ARP reply to the sender
  def arp_reply(self, sender_ip, sender_mac):
    # Send a message to the sender with the device's IP and MAC addresses and the sender's IP and MAC addresses
    reply_message = f"ARP reply: {self.ip}, {self.mac} is at {target_ip}, {target_mac}"
    print(f"{self.ip} sends {reply_message} to {sender_ip}")
    # Return the reply message
    return reply_message

  # A method to receive an ARP reply from the sender
  def arp_receive_reply(self, message):
    # Parse the message and extract the sender IP, the sender MAC, the target IP and the target MAC addresses
    message_parts = message.split()
    sender_ip = message_parts[1][:-1]
    sender_mac = message_parts[2]
    target_ip = message_parts[4][:-1]
    target_mac = message_parts[5]
    # Check if the target IP matches the device's IP
    if target_ip == self.ip:
      # Update the ARP cache with the sender's IP and MAC addresses
      self.arp_table[sender_ip] = sender_mac

  # A method to send a RARP request to the network
  def rarp_request(self, target_mac):
    # Broadcast a message to the network with the target MAC and the sender's IP and MAC addresses
    broadcast_message = f"RARP request: Who has {target_mac}? Tell {self.ip}, {self.mac}"
    print(f"{self.ip} sends {broadcast_message}")
    # Return the broadcast message
    return broadcast_message

  # A method to receive a RARP request from the network
  def rarp_receive(self, message):
    # Parse the message and extract the target MAC, the sender IP and the sender MAC addresses
    message_parts = message.split()
    target_mac = message_parts[2]
    sender_ip = message_parts[4][:-1]
    sender_mac = message_parts[5]
    # Check if the target MAC matches the device's MAC
    if target_mac == self.mac:
      # Send a RARP reply to the sender with the device's IP and MAC addresses
      self.rarp_reply(sender_ip, sender_mac)
    # Update the RARP cache with the sender's IP and MAC addresses
    self.rarp_table[sender_mac] = sender_ip

  # A method to send a RARP reply to the sender
  def rarp_reply(self, sender_ip, sender_mac):
    # Send a

```
