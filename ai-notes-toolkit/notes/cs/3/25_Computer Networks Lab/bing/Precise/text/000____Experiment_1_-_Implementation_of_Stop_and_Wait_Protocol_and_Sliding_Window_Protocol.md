## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

1. **Stop and Wait Protocol** is a flow control protocol in which the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
2. The receiver sends an acknowledgment after receiving a frame and checking it for errors.
3. If the sender does not receive an acknowledgment within a certain time period, it assumes that the frame was lost or corrupted and retransmits it.
4. This protocol is simple to implement but has low efficiency due to the time spent waiting for acknowledgments.
5. **Sliding Window Protocol** is a more efficient flow control protocol in which the sender can send multiple frames before waiting for acknowledgments.
6. The sender maintains a window of frames that can be sent without waiting for acknowledgments.
7. The receiver sends acknowledgments for received frames and the sender slides the window to send new frames.
8. This protocol has higher efficiency than the Stop and Wait Protocol due to the reduced waiting time for acknowledgments.
9. Both protocols can be implemented using programming languages such as C or Java.
10. The implementation involves creating sender and receiver programs that communicate using sockets and implement the flow control logic.
11. The programs can be tested by running them on separate machines and observing the flow of frames and acknowledgments.