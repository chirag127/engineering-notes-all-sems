 Here is the content in Markdown format:

### Types of connections in Computer Networks

1. Point-to-Point Connection: A direct connection between two devices. It is a dedicated link between the two devices. Examples are leased lines and dial-up connections.
Advantage: High speed, high security.
Disadvantage: Expensive.

2. Broadcast Connection: A network where packets are delivered to all devices. Examples are wireless networks and Ethernet networks.
Advantage: Inexpensive, easy to set up.
Disadvantage: Delivering packets to all devices reduces efficiency.

3. Multicast Connection: A network where packets are delivered to a group of devices. It is more efficient than broadcast as packets are only sent to devices that are part of the multicast group. Examples are video and audio streaming.
Advantage: Efficient use of network bandwidth.
Disadvantage: Complex to implement compared to broadcast.

[Detailed diagrams and examples can be added here for better understanding]

Applications:
- Point-to-point: Leased lines, DSL
- Broadcast: Wireless networks, Ethernet
- Multicast: Streaming media, online videos

### Depth buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

The depth buffer method is used to solve the hidden surface problem in 3D computer graphics. It stores the depth value (z-coordinate) of the visible surface at each pixel location in a matrix called the depth buffer or z-buffer.

Working:

1. Clear the depth buffer and frame buffer to initialize them.
2. For each polygon in the scene:
- Calculate the depth value (z-coordinate) of each pixel covered by the polygon.
- Compare the depth value of each pixel with the corresponding value in the depth buffer.
- If the depth value of the polygon is smaller than the depth buffer value, the polygon is visible. Update the depth buffer and frame buffer with the depth value and color of the polygon respectively.
- Else, discard the polygon as it is hidden.
3. Display the contents of the frame buffer.

Advantages:
- Simple and efficient algorithm.
- Can handle complicated scenes with hidden surfaces.

Disadvantages:
- Requires large amounts of memory to store depth and frame buffers.
- Fails if two surfaces share the same depth value (depth complexity).

[Detailed diagrams can be added here for better understanding]

Applications: 3D computer graphics, video games, CAD software, etc.