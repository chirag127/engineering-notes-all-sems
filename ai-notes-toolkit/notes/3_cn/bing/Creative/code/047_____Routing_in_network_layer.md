### Routing in network layer

Routing is the process of finding the best path for a packet to reach its destination in a network. Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model. A router is a networking device that forwards the packet based on the information available in the packet header and forwarding table. The routing algorithms are used for routing the packets .

There are two types of routing: static routing and dynamic routing. Static routing is based on fixed tables that are rarely changed and manually configured by the network administrator. Dynamic routing is based on automatic updates that depend on network conditions and use routing protocols to exchange information between routers. Some examples of routing protocols are RIP, OSPF, EIGRP, BGP, etc .

The network layer is responsible for routing packets from the source host to the destination host. The routes can be based on various factors such as distance, cost, congestion, reliability, etc. The network layer can also partition a network into sub-networks or subnets, which are logical divisions of an IP network that allow efficient use of address space and improve network performance .

The network layer also provides packetizing, which is the process of dividing a message into smaller units called packets, and forwarding, which is the process of sending a packet from one router to another until it reaches its destination.

Here is an example of routing in network layer using Python code:

```python
# Define a class for a packet
class Packet:
  def __init__(self, source, destination, data):
    self.source = source # The IP address of the source host
    self.destination = destination # The IP address of the destination host
    self.data = data # The payload of the packet

# Define a class for a router
class Router:
  def __init__(self, name, interfaces, routing_table):
    self.name = name # The name of the router
    self.interfaces = interfaces # A dictionary of interface names and IP addresses
    self.routing_table = routing_table # A dictionary of destination networks and next hops

  # Define a method for forwarding a packet
  def forward(self, packet):
    # Check if the destination of the packet is in the routing table
    if packet.destination in self.routing_table:
      # Get the next hop for the destination
      next_hop = self.routing_table[packet.destination]
      # Print the forwarding information
      print(f"{self.name} forwards packet from {packet.source} to {packet.destination} via {next_hop}")
      # Return the next hop
      return next_hop
    else:
      # Print an error message
      print(f"{self.name} cannot forward packet from {packet.source} to {packet.destination}")
      # Return None
      return None

# Define a function for simulating routing in a network
def routing(packet, routers):
  # Initialize the current router as the source of the packet
  current_router = packet.source
  # Loop until the packet reaches its destination or cannot be forwarded
  while current_router != packet.destination and current_router != None:
    # Find the router object that matches the current router
    for router in routers:
      if router.name == current_router:
        # Forward the packet using the router object
        current_router = router.forward(packet)
        # Break the loop
        break

# Define some packets
packet1 = Packet("R1", "R4", "Hello")
packet2 = Packet("R2", "R3", "World")
packet3 = Packet("R1", "R5", "Invalid")

# Define some routers
R1 = Router("R1", {"Fa0/0": "10.0.0.1", "Fa0/1": "10.0.1.1"}, {"10.0.0.0": "Fa0/0", "10.0.1.0": "Fa0/1", "10.0.2.0": "R2", "10.0.3.0": "R2"})
R2 = Router("R2", {"Fa0/0": "10.0.1.2", "Fa0/1": "10.0.2.1", "Fa0/2": "10.0.3.1"}, {"10.0.0.0": "R1", "10.0.1.0": "R1", "

```
