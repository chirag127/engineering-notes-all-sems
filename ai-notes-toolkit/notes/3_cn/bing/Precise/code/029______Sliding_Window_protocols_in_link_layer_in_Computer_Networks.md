#### Sliding Window protocols in link layer in Computer Networks
Sliding Window protocols are used in the link layer of computer networks to provide reliable data transfer. These protocols use a window of sequence numbers to keep track of the frames that have been sent and acknowledged. Here is an example of a sliding window protocol implemented in Python:

```python
# Sender
window_size = 4
next_seq_num = 0
base = 0

def send_data(data):
    global next_seq_num
    global base
    while base < len(data):
        while next_seq_num < base + window_size and next_seq_num < len(data):
            send_frame(data[next_seq_num], next_seq_num)
            next_seq_num += 1
        receive_ack()

def send_frame(frame, seq_num):
    # send the frame with the sequence number
    pass

def receive_ack():
    global base
    # receive the acknowledgement and update the base
    pass

# Receiver
expected_seq_num = 0

def receive_data():
    global expected_seq_num
    while True:
        frame, seq_num = receive_frame()
        if seq_num == expected_seq_num:
            deliver_data(frame)
            expected_seq_num += 1
        send_ack(expected_seq_num)

def receive_frame():
    # receive the frame and the sequence number
    pass

def deliver_data(frame):
    # deliver the data to the upper layer
    pass

def send_ack(ack_num):
    # send the acknowledgement
    pass
```
This is a basic implementation of a sliding window protocol. The sender keeps track of the next sequence number to be sent and the base of the window. The receiver keeps track of the expected sequence number. When the receiver receives a frame with the expected sequence number, it delivers the data to the upper layer and sends an acknowledgement. The sender updates the base of the window when it receives an acknowledgement. The window size can be adjusted to control the flow of data.