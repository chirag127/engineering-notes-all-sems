## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

The link layer is the lowest layer in the OSI model of computer networking. It is responsible for the transmission of data between two directly connected nodes. The link layer is responsible for providing services such as framing, error detection and correction, and flow control.

Medium Access Control (MAC) is a sublayer of the link layer that controls how devices in a network access the shared communication medium. MAC protocols are used to ensure that only one device transmits on the medium at a time, to avoid collisions.

Local Area Networks (LANs) are computer networks that are designed to operate over a small geographical area, such as a home, office, or campus. LANs typically use a shared communication medium, such as Ethernet or Wi-Fi, and are characterized by high data transfer rates and low latency.

Here is an example of a simple MAC protocol, called the Aloha protocol:

```python
def aloha(time, frame):
    if time % 2 == 0:
        transmit(frame)
    else:
        wait()
```

This protocol allows devices to transmit frames at even time slots, and waits at odd time slots. This reduces the chance of collisions, but can result in low channel utilization if there are many devices in the network.
