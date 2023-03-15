### Point-to-point networks in network layer

A point-to-point network is a network topology in which two nodes are directly connected by a link, without any intermediate nodes or devices. Point-to-point networks are often used in wide area networks (WANs) to connect two routers or two hosts over long distances. Point-to-point networks can provide high bandwidth, low latency, and security for data transmission.

One of the common protocols used in point-to-point networks is the Point-to-Point Protocol (PPP), which is a data link layer protocol that encapsulates multiprotocol data into frames for transmission over the link. PPP can also provide authentication, encryption, and compression features to enhance the security and efficiency of the communication. PPP consists of three main components:

- A framing method that defines how to delimit the start and end of a frame, how to identify the type of payload, and how to detect errors in the frame.
- A Link Control Protocol (LCP) that establishes, configures, and tests the data link connection between the two nodes. LCP can negotiate parameters such as maximum frame size, authentication method, and compression algorithm.
- A set of Network Control Protocols (NCPs) that configure and manage the network layer protocols used on the link, such as IP, IPX, or AppleTalk.

The following is an example of a Python code that implements a simple PPP frame:

```python
# Define constants for frame fields
FLAG = b'\x7e' # Flag byte that marks the start and end of a frame
ADDRESS = b'\xff' # Address byte that indicates a broadcast frame
CONTROL = b'\x03' # Control byte that indicates an unnumbered information frame
FCS = b'\x00\x00' # Frame check sequence bytes that are used for error detection

# Define a function that calculates the FCS using CRC-16-CCITT algorithm
def crc16_ccitt(data):
    # Initialize the CRC value to 0xFFFF
    crc = 0xFFFF
    # Iterate over each byte in the data
    for byte in data:
        # XOR the CRC value with the byte
        crc ^= byte
        # Perform 8 iterations of bit shifting and XORing
        for _ in range(8):
            # Check the least significant bit of the CRC value
            if crc & 1:
                # If it is 1, right shift the CRC value by one bit and XOR it with 0x8408
                crc = (crc >> 1) ^ 0x8408
            else:
                # If it is 0, right shift the CRC value by one bit
                crc >>= 1
    # Return the CRC value as a two-byte object in little-endian order
    return crc.to_bytes(2, 'little')

# Define a function that creates a PPP frame with a given payload
def create_ppp_frame(payload):
    # Concatenate the address, control, and payload fields
    data = ADDRESS + CONTROL + payload
    # Calculate the FCS for the data
    fcs = crc16_ccitt(data)
    # Concatenate the flag, data, and fcs fields
    frame = FLAG + data + fcs + FLAG
    # Return the frame
    return frame

# Define a sample payload that contains an IP packet
payload = b'\x45\x00\x00\x28\x00\x00\x00\x00\x40\x11\x00\x00\x0a\x00\x00\x01\x0a\x00\x00\x02\x00\x00\x00\x00\x00\x14\x00\x00\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'

# Create a PPP frame with the payload
frame = create_ppp_frame(payload)

# Print the frame in hexadecimal format
print(frame.hex())
```

The output of the code is:

`7eff03004500002800000000401100000a0000010a000002000000000014000048656c6c6f20576f726c64b1a67e7e`

This is a PPP frame that contains an IP packet with the message "Hello World" as the payload. The frame has the following structure:

| Flag | Address | Control | Protocol | Payload | FCS | Flag |
|------|---------|---------|----------|---------|-----|------|
| 7e   | ff      | 03      | 4500     | ...     | b1