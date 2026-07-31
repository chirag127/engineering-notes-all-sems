## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address in a local area network (LAN).
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address in a LAN.
- Both ARP and RARP use the same packet format, which consists of the following fields:
  - Hardware type: specifies the type of network hardware, such as Ethernet or Token Ring.
  - Protocol type: specifies the type of network protocol, such as IPv4 or IPv6.
  - Hardware length: specifies the length of the hardware address in bytes, such as 6 for Ethernet MAC address.
  - Protocol length: specifies the length of the protocol address in bytes, such as 4 for IPv4 address.
  - Operation: specifies the type of operation, such as 1 for ARP request, 2 for ARP reply, 3 for RARP request, or 4 for RARP reply.
  - Sender hardware address: specifies the MAC address of the sender of the packet.
  - Sender protocol address: specifies the IP address of the sender of the packet.
  - Target hardware address: specifies the MAC address of the target of the packet.
  - Target protocol address: specifies the IP address of the target of the packet.
- The following is a pseudocode for simulating ARP /RARP protocols:

```python
# Define a class for ARP /RARP packet
class ARPPacket:
  def __init__(self, hw_type, pr_type, hw_len, pr_len, op, sha, spa, tha, tpa):
    self.hw_type = hw_type # Hardware type
    self.pr_type = pr_type # Protocol type
    self.hw_len = hw_len # Hardware length
    self.pr_len = pr_len # Protocol length
    self.op = op # Operation
    self.sha = sha # Sender hardware address
    self.spa = spa # Sender protocol address
    self.tha = tha # Target hardware address
    self.tpa = tpa # Target protocol address

# Define a function for sending an ARP /RARP packet
def send_packet(packet):
  # Check the operation field of the packet
  if packet.op == 1: # ARP request
    # Broadcast the packet to all nodes in the LAN
    broadcast(packet)
    # Wait for an ARP reply from the target node
    reply = receive_packet()
    # Check if the reply matches the request
    if reply.op == 2 and reply.spa == packet.tpa and reply.tpa == packet.spa:
      # Print the MAC address of the target node
      print("The MAC address of " + packet.tpa + " is " + reply.sha)
    else:
      # Print an error message
      print("No ARP reply received")
  elif packet.op == 2: # ARP reply
    # Send the packet to the node that sent the ARP request
    send(packet, packet.tha)
  elif packet.op == 3: # RARP request
    # Broadcast the packet to all nodes in the LAN
    broadcast(packet)
    # Wait for a RARP reply from the gateway router
    reply = receive_packet()
    # Check if the reply matches the request
    if reply.op == 4 and reply.sha == packet.tha and reply.tha == packet.sha:
      # Print the IP address of the sender node
      print("The IP address of " + packet.sha + " is " + reply.spa)
    else:
      # Print an error message
      print("No RARP reply received")
  elif packet.op == 4: # RARP reply
    # Send the packet to the node that sent the RARP request
    send(packet, packet.tha)
  else:
    # Print an error message
    print("Invalid operation")
```