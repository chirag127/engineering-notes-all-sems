#### Elementary Data Link Protocols in Link Layer in Computer Networks

The Data Link Layer in Computer Networks is responsible for transferring data between adjacent network nodes. Elementary Data Link Protocols are a set of simple protocols that are used for this purpose. These protocols are designed to provide reliable transmission of data over a noisy communication channel. In this section, we will discuss the various Elementary Data Link Protocols used in the Link Layer.

##### Stop-and-Wait Protocol

The Stop-and-Wait protocol is a simple protocol that is used to ensure reliable transmission of data. In this protocol, the sender sends a frame and waits for an acknowledgment from the receiver before sending the next frame. The receiver, upon receiving a frame, sends an acknowledgment back to the sender. If the sender does not receive an acknowledgment within a certain time interval, it assumes that the frame has been lost and retransmits it. The Stop-and-Wait protocol is easy to implement but is not very efficient.

##### Go-Back-N Protocol

The Go-Back-N protocol is a sliding window protocol that allows the sender to transmit multiple frames before receiving acknowledgments from the receiver. The sender maintains a window of frames that it has transmitted but has not yet received an acknowledgment for. The receiver sends an acknowledgment for every frame it receives. If the sender does not receive an acknowledgment for a particular frame, it assumes that all the frames after that have been lost and retransmits them. The Go-Back-N protocol is more efficient than the Stop-and-Wait protocol but can lead to unnecessary retransmissions.

##### Selective-Repeat Protocol

The Selective-Repeat protocol is also a sliding window protocol that allows the sender to transmit multiple frames before receiving acknowledgments from the receiver. In this protocol, the sender maintains a window of frames that it has transmitted but has not yet received an acknowledgment for. The receiver sends an acknowledgment for every frame it receives, and also indicates which frames it has received out of order. The sender retransmits only those frames that have been lost or received out of order. The Selective-Repeat protocol is more efficient than the Go-Back-N protocol as it minimizes unnecessary retransmissions.

##### Comparison between Stop-and-Wait, Go-Back-N, and Selective-Repeat Protocols

| Protocol | Advantages | Disadvantages |
| --- | --- | --- |
| Stop-and-Wait | Simple to implement. | Low efficiency. |
| Go-Back-N | More efficient than Stop-and-Wait. | Can lead to unnecessary retransmissions. |
| Selective-Repeat | More efficient than Go-Back-N. | More complex to implement than Stop-and-Wait and Go-Back-N. |

Mnemonics and Learning Tricks:

- Stop-and-Wait: Think of a traffic signal where the sender is the car and the receiver is the traffic signal. The car stops at the signal and waits for the green signal (acknowledgment) before moving forward.
- Go-Back-N: Think of a conveyor belt where the sender sends multiple packages (frames) before receiving the acknowledgment. If a package is lost, all the packages after that go back on the conveyor belt for retransmission.
- Selective-Repeat: Think of a book where the sender sends multiple pages (frames) before receiving the acknowledgment. If a page is lost, the sender only repeats that page instead of repeating all the pages after it.

Conclusion:

Elementary Data Link Protocols are essential for reliable transmission of data in the Link Layer of Computer Networks. The Stop-and-Wait, Go-Back-N, and Selective-Repeat protocols are some of the widely used protocols in this layer. Each protocol has its advantages and disadvantages, and the choice of protocol depends on the specific requirements of the network. The Mnemonics and Learning Tricks mentioned above can be helpful in remembering the key features of these protocols.