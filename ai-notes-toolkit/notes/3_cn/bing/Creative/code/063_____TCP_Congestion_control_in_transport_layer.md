### TCP Congestion control in transport layer

TCP congestion control is a mechanism that aims to prevent network congestion by regulating the amount of data that a TCP sender can inject into the network. TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection.

- Slow start: In this phase, the TCP sender starts with a small congestion window (CWND) that limits the number of unacknowledged packets that can be in transit. The CWND is increased by one segment for every acknowledgment received, resulting in an exponential growth of the CWND until a threshold is reached .
- Congestion avoidance: In this phase, the TCP sender increases the CWND by one segment per round-trip time (RTT), resulting in a linear growth of the CWND. This phase aims to probe the network capacity without causing congestion .
- Congestion detection: In this phase, the TCP sender detects congestion by observing packet loss or delay. Packet loss is indicated by a timeout or a duplicate acknowledgment. Delay is indicated by an increase in the RTT. When congestion is detected, the TCP sender reduces the CWND by a multiplicative factor, typically by half. This phase aims to react to congestion and avoid further packet loss  .

The following pseudocode illustrates the TCP congestion control algorithm:

```
# Initialize CWND and threshold
CWND = 1
threshold = 64

# Loop until all data is sent
while data is not sent:

  # Send CWND segments and wait for ACKs
  send(CWND)
  wait_for_ACKs()

  # If ACKs are received without loss or delay
  if no_loss_or_delay():

    # If CWND is below threshold, use slow start
    if CWND < threshold:
      CWND = CWND * 2

    # If CWND is above threshold, use congestion avoidance
    else:
      CWND = CWND + 1

  # If loss or delay is detected
  else:

    # Reduce threshold and CWND by half
    threshold = CWND / 2
    CWND = CWND / 2
```