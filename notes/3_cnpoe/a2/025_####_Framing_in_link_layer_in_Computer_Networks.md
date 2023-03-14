 Here is the content in markdown format for the topic #### Framing in link layer in Computer Networks:

#### Framing in link layer in Computer Networks

The link layer is responsible for transferring data between adjacent network nodes. For effective and error-free data transfer, the link layer uses framing techniques. Some key points about framing in the link layer are:

- Data coming from the upper layers is divided into frames of fixed or variable length. These frames contain the actual data along with some control information added by the link layer.
- The control information added is known as the frame header. It contains fields like frame synchronization bytes, address fields, frame check sequences, etc.
- Frame synchronization bytes are used for synchronization between the transmitter and receiver. They indicate the start and end of a frame.
- Address fields contain source and destination addresses to identify the sender and receiver of the frame.
- Frame check sequences contain error-detecting codes to check for errors in the frame. They help in detecting and discarding corrupted frames.
- After framing, the frames are transmitted on the physical medium using certain modulation techniques. The receiver extracts the frames, checks for errors, and reassembles the data from the correct frames.
- Some advantages of framing are that they provide synchronization, add addressing for delivery, and enable error detection. However, framing does introduce some overhead, which can reduce the effective throughput.

I have included the key points about framing in the link layer. I have not included any complex mnemonics or learning tricks as the points themselves are easy to understand and remember. Let me know if you would like me to elaborate on any of the points or include additional details.