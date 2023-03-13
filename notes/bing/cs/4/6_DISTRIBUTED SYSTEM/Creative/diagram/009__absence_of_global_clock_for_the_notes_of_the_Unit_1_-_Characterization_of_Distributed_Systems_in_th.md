The absence of global clock in distributed systems means that there is no common notion of time among the processes that communicate over a network. The message delays are unpredictable and vary depending on the network conditions and the load on the processes. Therefore, the processes cannot rely on having an accurate view of the global state of the system, as they may have different and inconsistent local clocks.

One way to illustrate the absence of global clock in distributed systems is to use a diagram that shows two processes, P1 and P2, that send and receive messages over a network. The diagram can use vertical lines to represent the local clocks of the processes, and horizontal arrows to represent the messages. The diagram can also show the logical timestamps of the messages, which are assigned by the processes based on their local clocks. The diagram can show how the logical timestamps may not reflect the actual order of events in the system, due to the message delays and the lack of synchronization among the local clocks.

The following diagram is an example of such a diagram, using ASCII characters:

```
    P1                  P2
    |                   |
    |                   |
    |---m1(1)---------> |  m1 arrives at P2 at time 3
    |                   |  P2 updates its clock to 4
    |                   |
    |                   |---m2(4)--------->  m2 arrives at P1 at time 5
    |                   |                   P1 updates its clock to 6
    |                   |
    |---m3(6)---------> |  m3 arrives at P2 at time 7
    |                   |  P2 updates its clock to 8
    |                   |
    |                   |---m4(8)--------->  m4 arrives at P1 at time 9
    |                   |                   P1 updates its clock to 10
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
```

The diagram shows that the logical timestamps of the messages do not match the actual order of events in the system. For example, m1 is sent before m2, but m2 has a higher timestamp than m1. Similarly, m3 is sent before m4, but m4 has a higher timestamp than m3. This is because the local clocks of P1 and P2 are not synchronized, and the message delays are not constant. Therefore, the processes cannot use the logical timestamps to determine the global state of the system, as they may have different and inconsistent views of the events. This is the essence of the absence of global clock in distributed systems.