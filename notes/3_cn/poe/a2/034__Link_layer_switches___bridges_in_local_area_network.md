 Here is the formal content on the given topic in Markdown format:

#### Link layer switches & bridges in local area network

1. Link layer switches:
- Operate at OSI Layer 2 (Data Link Layer)
- Forward frames based on MAC address
- Store MAC addresses in a table to make forwarding decisions
- Filters frames and forwards only to necessary ports to improve performance
- Broadcasts are forwarded to all ports except the source port
- Examples: Ethernet switch, MAC bridge

2. Bridges:
- Connect two network segments (LANs) at the link layer
- Forward frames between segments based on MAC addresses
- Store address table to forward frames only to necessary segments
- Prevent loops by disabling ports if frames are received from connected segments
- Can be used to divide a large network into smaller, more efficient networks

3. Differences between switches and bridges:
- Switches support many ports while bridges usually support 2 ports
- Switches use ASICs for faster frame forwarding while bridges use software
- Switches filter broadcasts while bridges forward all broadcasts
- Switches provide additional features like VLANs, STP, QoS, monitoring, etc.

The above content summarizes the key points about link layer switches and bridges used in local area networks. The points are written in a formal tone with Markdown formatting and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer.