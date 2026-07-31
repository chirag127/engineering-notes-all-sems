### TCP Congestion control in transport layer

TCP congestion control is a mechanism that regulates the amount of data that a sender can transmit over a network, based on the network's capacity and the feedback from the receiver. TCP congestion control aims to avoid network congestion, which occurs when the network is overloaded with packets and causes packet loss, delay, and reduced throughput.

TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion recovery. In each phase, TCP uses a variable called congestion window (cwnd) to determine how many packets can be sent at a time. The cwnd is initially set to a small value, and is increased or decreased depending on the network conditions and the acknowledgments (ACKs) received from the receiver.

- Slow start: In this phase, TCP starts with a small cwnd and increases it exponentially for every ACK received, until it reaches a threshold value (ssthresh) or a packet loss occurs. This phase allows TCP to probe the network capacity and find the optimal cwnd value.
- Congestion avoidance: In this phase, TCP increases the cwnd linearly for every ACK received, until a packet loss occurs. This phase allows TCP to maintain a high throughput and avoid network congestion.
- Congestion recovery: In this phase, TCP reduces the cwnd and the ssthresh by half, and enters either slow start or congestion avoidance phase, depending on the value of cwnd. This phase allows TCP to recover from packet loss and adapt to the changing network conditions.

The following pseudocode illustrates the TCP congestion control algorithm:

```
# Initialize cwnd and ssthresh
cwnd = 1
ssthresh = 64

# Loop until all data is sent
while data is not sent:

  # Send cwnd packets and wait for ACKs
  send cwnd packets
  wait for ACKs

  # If all packets are acknowledged
  if all packets are ACKed:

    # If cwnd is less than ssthresh, enter slow start phase
    if cwnd < ssthresh:
      cwnd = cwnd * 2

    # Else, enter congestion avoidance phase
    else:
      cwnd = cwnd + 1

  # Else, if some packets are lost
  else:

    # Enter congestion recovery phase
    ssthresh = cwnd / 2
    cwnd = ssthresh

    # If cwnd is less than 1, set it to 1
    if cwnd < 1:
      cwnd = 1
```