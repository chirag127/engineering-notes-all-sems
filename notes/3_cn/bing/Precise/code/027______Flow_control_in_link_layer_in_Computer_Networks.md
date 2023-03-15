#### Flow control in link layer in Computer Networks

Flow control is a mechanism used in the link layer of computer networks to prevent the sender from overwhelming the receiver with data. This is achieved by regulating the rate at which data is transmitted from the sender to the receiver.

Here is an example of flow control using the sliding window protocol in the link layer:

```python
# Sender
window_size = 4
next_frame_to_send = 0
max_seq = 2 * window_size

def send_data(data):
    global next_frame_to_send
    while data:
        while next_frame_to_send < window_size:
            send_frame(data.pop(0), next_frame_to_send)
            next_frame_to_send = (next_frame_to_send + 1) % max_seq

def send_frame(frame, seq_num):
    # send frame with sequence number seq_num
    pass

def receive_ack(ack_num):
    global next_frame_to_send
    next_frame_to_send = max(next_frame_to_send, ack_num + 1)

# Receiver
expected_frame = 0

def receive_frame(frame, seq_num):
    global expected_frame
    if seq_num == expected_frame:
        deliver_data(frame)
        expected_frame = (expected_frame + 1) % max_seq
        send_ack(expected_frame)

def send_ack(ack_num):
    # send acknowledgement with ack_num
    pass

def deliver_data(data):
    # deliver data to the upper layer
    pass
```

This code demonstrates how the sender and receiver use the sliding window protocol to regulate the flow of data between them. The sender maintains a window of frames that it is allowed to send, and the receiver sends acknowledgements to the sender to indicate which frames have been received. The sender adjusts its window based on the acknowledgements received from the receiver, ensuring that the receiver is not overwhelmed with data.