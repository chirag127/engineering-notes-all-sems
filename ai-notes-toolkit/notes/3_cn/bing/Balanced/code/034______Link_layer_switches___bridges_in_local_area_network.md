#### Link layer switches & bridges in local area network

A link layer switch or a bridge is a network device that connects multiple LANs (local area networks) together to form a larger LAN. It operates at the data link layer of the OSI model and uses MAC addresses to forward Ethernet frames from one device to another device in the same LAN or across different LANs. A switch or a bridge can also filter frames based on their MAC addresses and prevent unnecessary traffic from reaching other devices. A switch or a bridge can also handle different data link layer technologies, such as Ethernet and FDDI, by converting the frame format and adjusting the maximum frame size. 

Here is a pseudocode example of how a switch or a bridge works:

```
# Define a table that maps MAC addresses to ports
table = {}

# Define a function that forwards a frame to a port
def forward(frame, port):
  # Send the frame to the port
  port.send(frame)

# Define a function that floods a frame to all ports except the source port
def flood(frame, source_port):
  # Loop through all the ports
  for port in ports:
    # If the port is not the source port
    if port != source_port:
      # Send the frame to the port
      port.send(frame)

# Define a function that handles a frame received from a port
def handle(frame, port):
  # Get the source and destination MAC addresses from the frame
  source_mac = frame.source_mac
  destination_mac = frame.destination_mac

  # Update the table with the source MAC address and port
  table[source_mac] = port

  # If the destination MAC address is in the table
  if destination_mac in table:
    # Get the port associated with the destination MAC address
    destination_port = table[destination_mac]
    # Forward the frame to the destination port
    forward(frame, destination_port)
  # Else, the destination MAC address is unknown
  else:
    # Flood the frame to all ports except the source port
    flood(frame, port)
```