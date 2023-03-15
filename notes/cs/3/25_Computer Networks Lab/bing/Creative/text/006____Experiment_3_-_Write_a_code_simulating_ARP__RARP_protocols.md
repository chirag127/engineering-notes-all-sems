## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is used to map a network layer address (such as an IP address) to a data link layer address (such as a MAC address).
- RARP stands for Reverse Address Resolution Protocol. It is used to map a data link layer address to a network layer address.
- Both ARP and RARP use the same packet format, which consists of the following fields:
  - Hardware type: specifies the type of hardware used for the local network, such as Ethernet or Token Ring.
  - Protocol type: specifies the type of protocol used for the network layer, such as IP or IPX.
  - Hardware length: specifies the length of the hardware address in bytes.
  - Protocol length: specifies the length of the protocol address in bytes.
  - Operation: specifies the type of operation, such as ARP request, ARP reply, RARP request, or RARP reply.
  - Sender hardware address: specifies the hardware address of the sender of the packet.
  - Sender protocol address: specifies the protocol address of the sender of the packet.
  - Target hardware address: specifies the hardware address of the target of the packet.
  - Target protocol address: specifies the protocol address of the target of the packet.
- The following is a pseudocode for simulating ARP /RARP protocols:

  ```
  # Define a class for ARP /RARP packets
  class ARPPacket:
    # Initialize the packet with the given fields
    def __init__(self, htype, ptype, hlen, plen, op, sha, spa, tha, tpa):
      self.htype = htype # Hardware type
      self.ptype = ptype # Protocol type
      self.hlen = hlen # Hardware length
      self.plen = plen # Protocol length
      self.op = op # Operation
      self.sha = sha # Sender hardware address
      self.spa = spa # Sender protocol address
      self.tha = tha # Target hardware address
      self.tpa = tpa # Target protocol address

    # Display the packet fields
    def show(self):
      print("Hardware type:", self.htype)
      print("Protocol type:", self.ptype)
      print("Hardware length:", self.hlen)
      print("Protocol length:", self.plen)
      print("Operation:", self.op)
      print("Sender hardware address:", self.sha)
      print("Sender protocol address:", self.spa)
      print("Target hardware address:", self.tha)
      print("Target protocol address:", self.tpa)

  # Define a list of hosts with their hardware and protocol addresses
  hosts = [
    {"ha": "00:0a:95:9d:68:16", "pa": "192.168.0.1"},
    {"ha": "00:0a:95:9d:68:17", "pa": "192.168.0.2"},
    {"ha": "00:0a:95:9d:68:18", "pa": "192.168.0.3"},
    {"ha": "00:0a:95:9d:68:19", "pa": "192.168.0.4"},
    {"ha": "00:0a:95:9d:68:20", "pa": "192.168.0.5"}
  ]

  # Define a function to simulate ARP /RARP
  def arp_rarp(packet):
    # Check the operation field of the packet
    if packet.op == 1: # ARP request
      # Loop through the hosts list
      for host in hosts:
        # Check if the target protocol address matches the host's protocol address
        if packet.tpa == host["pa"]:
          # Create an ARP reply packet with the host's hardware and protocol addresses
          reply = ARPPacket(packet.htype, packet.ptype, packet.hlen, packet.plen, 2, host["ha"], host["pa"], packet.sha, packet.spa)
          # Display the reply packet
          print("ARP reply:")
          reply.show()
          # Return the reply packet
          return reply
      # If no match is found, display an error message
      print("No host with the target protocol address found.")
    elif packet.op == 2: # ARP reply
      # Display the packet
      print("ARP reply:")
      packet.show()
    elif packet.op == 3: # RARP request
      # Loop through the hosts list
      for host in hosts:
        # Check if the target hardware address matches the host's hardware address