#### Elementary Data Link Protocols in link layer in Computer Networks

Elementary Data Link Protocols are the protocols used in the link layer of computer networks to provide reliable communication between two adjacent nodes. These protocols are responsible for framing, flow control, and error control.

Here is an example of a simple Stop-and-Wait protocol implemented in Python:

```python
def stop_and_wait(sender, receiver, data):
    # sender sends data to receiver using stop-and-wait protocol
    for packet in data:
        # sender sends packet
        sender.send(packet)
        # wait for acknowledgment from receiver
        ack = receiver.receive()
        # if acknowledgment is not received, resend packet
        while ack != packet:
            sender.send(packet)
            ack = receiver.receive()
```

This protocol works by having the sender send a packet of data and then wait for an acknowledgment from the receiver before sending the next packet. If the acknowledgment is not received, the sender resends the packet until it is successfully received by the receiver.

This is just one example of an elementary data link protocol. There are many other protocols that can be used in the link layer of computer networks to provide reliable communication between adjacent nodes.