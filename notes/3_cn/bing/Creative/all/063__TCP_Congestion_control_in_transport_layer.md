### TCP Congestion Control in Transport Layer

- TCP congestion control is a mechanism that prevents the network from being overloaded by the TCP traffic.
- TCP congestion control adapts the sending rate of the TCP sender to the network conditions, such as the available bandwidth and the level of congestion.
- TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection.
- TCP congestion control uses two variables to control the sending rate: congestion window (cwnd) and slow start threshold (ssthresh).
- Congestion window (cwnd) is the amount of data that the sender can send without waiting for an acknowledgment. It is initially set to one segment size (MSS).
- Slow start threshold (ssthresh) is the threshold that determines the transition from slow start to congestion avoidance. It is initially set to a large value, such as the receiver's advertised window size.

#### Slow Start Phase

- In the slow start phase, the sender increases the cwnd exponentially by one MSS for every acknowledgment received.
- The sender can send up to cwnd segments in one round trip time (RTT).
- The slow start phase ends when cwnd reaches or exceeds ssthresh.

#### Congestion Avoidance Phase

- In the congestion avoidance phase, the sender increases the cwnd additively by one MSS per RTT.
- The sender can send up to cwnd segments in one RTT.
- The congestion avoidance phase continues until a congestion event occurs, such as a timeout or a triple duplicate acknowledgment.

#### Congestion Detection Phase

- In the congestion detection phase, the sender detects a congestion event and reduces the cwnd and ssthresh accordingly.
- There are two types of congestion events: timeout and triple duplicate acknowledgment.
- Timeout occurs when the sender does not receive any acknowledgment for a long time, indicating a severe congestion or a packet loss.
- Triple duplicate acknowledgment occurs when the sender receives three consecutive duplicate acknowledgments for the same segment, indicating a mild congestion or a packet reordering.
- When a timeout occurs, the sender sets ssthresh to half of the current cwnd, sets cwnd to one MSS, and restarts the slow start phase.
- When a triple duplicate acknowledgment occurs, the sender sets ssthresh to half of the current cwnd, sets cwnd to ssthresh, and enters the congestion avoidance phase.

#### Example

- Assume a TCP sender with a segment size of 1 KB and a RTT of 100 ms.
- The sender starts with cwnd = 1 KB and ssthresh = 64 KB.
- The sender enters the slow start phase and sends one segment in the first RTT.
- The sender receives an acknowledgment and increases cwnd to 2 KB.
- The sender sends two segments in the second RTT.
- The sender receives two acknowledgments and increases cwnd to 4 KB.
- The sender sends four segments in the third RTT.
- The sender receives four acknowledgments and increases cwnd to 8 KB.
- The sender sends eight segments in the fourth RTT.
- The sender receives eight acknowledgments and increases cwnd to 16 KB.
- The sender sends 16 segments in the fifth RTT.
- The sender receives 16 acknowledgments and increases cwnd to 32 KB.
- The sender sends 32 segments in the sixth RTT.
- The sender receives 32 acknowledgments and increases cwnd to 64 KB.
- The sender sends 64 segments in the seventh RTT.
- The sender receives 64 acknowledgments and reaches the ssthresh of 64 KB.
- The sender enters the congestion avoidance phase and increases cwnd to 65 KB.
- The sender sends 65 segments in the eighth RTT.
- The sender receives 65 acknowledgments and increases cwnd to 66 KB.
- The sender sends 66 segments in the ninth RTT.
- The sender receives 66 acknowledgments and increases cwnd to 67 KB.
- The sender sends 67 segments in the tenth RTT.
- The sender receives 67 acknowledgments and increases cwnd to 68 KB.
- The sender sends 68 segments in the eleventh RTT.
- The sender receives a triple duplicate acknowledgment for the first segment, indicating a congestion event.
- The sender sets ssthresh to half of the current cwnd, which is 34 KB, and sets cwnd to ssthresh, which is also 34 KB.
- The sender enters the congestion avoidance phase and retransmits the lost segment.
- The sender sends 34 segments in the twelfth RTT.
- The sender receives