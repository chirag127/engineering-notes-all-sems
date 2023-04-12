## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both ARP and RARP use broadcast messages to request and reply the address mappings.
- The following is a pseudocode that simulates the basic functions of ARP and RARP protocols.

```
# Define a class for a device on the network
class Device:
  # Initialize the device with an IP address and a MAC address
  def __init__(self, ip, mac):
    self.ip = ip
    self.mac = mac
    self.arp_table = {} # A dictionary to store the ARP cache
    self.rarp_table = {} # A dictionary to store the RARP cache

  # Define a method to send an ARP request to the network
  def arp_request(self, target_ip):
    # Broadcast a message to the network with the target IP address and the sender's IP and MAC addresses
    broadcast_message = "ARP request: Who has " + target_ip + "? Tell " + self.ip + " (" + self.mac + ")"
    print(self.ip + " (" + self.mac + ") sends " + broadcast_message)

    # Return the broadcast message
    return broadcast_message

  # Define a method to receive an ARP request from another device
  def arp_receive(self, message):
    # Parse the message to get the target IP address and the sender's IP and MAC addresses
    message_parts = message.split()
    target_ip = message_parts[2]
    sender_ip = message_parts[5]
    sender_mac = message_parts[6]

    # Check if the target IP address matches the device's IP address
    if target_ip == self.ip:
      # Send an ARP reply to the sender with the device's IP and MAC addresses
      self.arp_reply(sender_ip, sender_mac)
    else:
      # Update the ARP cache with the sender's IP and MAC addresses
      self.arp_table[sender_ip] = sender_mac
      print(self.ip + " (" + self.mac + ") updates its ARP cache with " + sender_ip + " (" + sender_mac + ")")

  # Define a method to send an ARP reply to another device
  def arp_reply(self, target_ip, target_mac):
    # Send a message to the target device with the device's IP and MAC addresses and the target's IP and MAC addresses
    message = "ARP reply: " + self.ip + " is at " + self.mac + " for " + target_ip + " (" + target_mac + ")"
    print(self.ip + " (" + self.mac + ") sends " + message)

    # Return the message
    return message

  # Define a method to receive an ARP reply from another device
  def arp_receive_reply(self, message):
    # Parse the message to get the sender's IP and MAC addresses and the target's IP and MAC addresses
    message_parts = message.split()
    sender_ip = message_parts[1]
    sender_mac = message_parts[4]
    target_ip = message_parts[6]
    target_mac = message_parts[7]

    # Check if the target IP address matches the device's IP address
    if target_ip == self.ip:
      # Update the ARP cache with the sender's IP and MAC addresses
      self.arp_table[sender_ip] = sender_mac
      print(self.ip + " (" + self.mac + ") updates its ARP cache with " + sender_ip + " (" + sender_mac + ")")
    else:
      # Ignore the message
      print(self.ip + " (" + self.mac + ") ignores the message")

  # Define a method to send a RARP request to the network
  def rarp_request(self, target_mac):
    # Broadcast a message to the network with the target MAC address and the sender's IP and MAC addresses
    broadcast_message = "RARP request: Who has " + target_mac + "? Tell " + self.ip + " (" + self.mac + ")"
    print(self.ip + " (" + self.mac + ") sends " + broadcast_message)

    # Return the broadcast message
    return broadcast_message

  # Define a method to receive a RARP request from another device
  def rarp_receive(self, message):
    # Parse the message to get the target MAC address and the sender's IP and MAC addresses
    message_parts = message.split()
    target_mac = message_parts[2]
    sender_ip = message_parts[5

```
