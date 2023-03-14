TCP over wireless is a technique to adapt the Transmission Control Protocol (TCP) to wireless networks, such as cellular networks or wireless LANs. TCP is a reliable and connection-oriented protocol that ensures the correct delivery of data packets over the Internet. However, TCP was designed for wired networks and assumes that packet losses are mainly due to congestion. Therefore, TCP responds to packet losses by reducing the transmission rate, which can degrade the performance of wireless networks that have high error rates due to noise, interference, or mobility.

To overcome this problem, TCP over wireless uses various mechanisms to improve the performance of TCP over wireless links, such as:

- Splitting the TCP connection into two sub-connections: one between the sender and a base station, and another between the base station and the receiver. This way, the base station can handle the wireless errors locally and avoid triggering the congestion control of the sender.
- Using a selective acknowledgement (SACK) option in the TCP header to inform the sender about which packets have been received and which have been lost. This way, the sender can retransmit only the lost packets and avoid unnecessary retransmissions.
- Using a fast retransmit and fast recovery algorithm to quickly detect and recover from packet losses without waiting for a timeout. This way, the sender can maintain a high transmission rate and avoid slow start.
- Using a delayed acknowledgement (DACK) option in the TCP header to reduce the number of acknowledgements sent by the receiver. This way, the receiver can save bandwidth and power consumption in wireless networks.

The following diagram illustrates the basic architecture of a TCP over wireless system:

```
+--------+        +-----------+        +--------+
| Sender | <----> | Base      | <----> |        |
|        |  TCP   | Station   |  TCP   |        |
|        |        |           |        |        |
+--------+        +-----------+        +--------+
                  /           \        /        \
                 /             \      /          \
                /               \    /            \
               /                 \  /              \
              /                   \/                \
             /                    /\                 \
            /                    /  \                 \
           /                    /    \                 \
          /                    /      \                 \
         /                    /        \                 \
        /                    /          \                 \
       /                    /            \                 \
      /                    /              \                 \
     /                    /                \                 \
    /                    /                  \                 \
   /                    /                    \                 \
  /                    /                      \                 \
 /                    /                        \                 \
+--------+        +-----------+        +--------+        +--------+
| Sender | <----> | Base      | <----> | Base   | <----> |        |
|        |  TCP   | Station   |  TCP   | Station|  TCP   |        |
|        |        |           |        |        |        |        |
+--------+        +-----------+        +--------+        +--------+
```

The sender and the receiver communicate using TCP over a wired network. The base stations act as intermediaries between the wired and wireless networks. They split the TCP connection into two sub-connections and use different mechanisms to handle the wireless errors. The base stations can also communicate with each other using TCP over a wired network.