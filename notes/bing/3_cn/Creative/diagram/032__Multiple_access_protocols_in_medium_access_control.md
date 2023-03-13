Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model. These protocols allow a number of nodes or users to access a shared network channel  .

There are different types of multiple access protocols, such as random access, controlled access, and channelization protocols. Each type has its own advantages and disadvantages, depending on the network scenario and requirements .

#### Multiple access protocols in medium access control

The following diagram illustrates the basic architecture of a multiple access protocol in medium access control:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Node 1     |      |     Node 2     |      |     Node 3     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+------------------+
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Node 4     |      |     Node 5     |      |     Node 6     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The diagram shows six nodes that want to access a shared network channel. The network channel is represented by the vertical line in the middle. The multiple access protocol is responsible for coordinating the access of the nodes to the channel, avoiding collisions and maximizing the channel utilization .

Some examples of multiple access protocols are:

- ALOHA: A random access protocol that allows nodes to transmit data whenever they have data to send, without checking the channel state. If a collision occurs, the nodes wait for a random time and retransmit the data .
- CSMA: A random access protocol that allows nodes to sense the channel state before transmitting data. If the channel is busy, the nodes wait until it becomes idle. There are different variants of CSMA, such as CSMA/CD and CSMA/CA, that use different methods to handle collisions .
- TDMA: A controlled access protocol that divides the channel into fixed time slots and assigns each slot to a node. The nodes can only transmit data in their assigned slots, avoiding collisions and ensuring fair access .
- FDMA: A channelization protocol that divides the channel into fixed frequency bands and assigns each band to a node. The nodes can only transmit data in their assigned bands, avoiding interference and ensuring orthogonal access .