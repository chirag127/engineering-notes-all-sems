Causal ordering of messages is a partial ordering of messages in a distributed computing environment. It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .

The following diagram illustrates the basic architecture of a distributed system with causal ordering of messages using vector timestamps. The vector timestamps are shown in parentheses next to each message. Each process maintains a vector of size equal to the number of processes in the system, and updates it according to the following rules:

- When a process sends a message, it increments its own entry in the vector by one.
- When a process receives a message, it updates each entry in its vector to the maximum of its own value and the value received in the message, and then increments its own entry by one.
- A process can deliver a message only if its vector timestamp is less than or equal to the process's vector timestamp in all entries except for the sender's entry, where it must be equal.

```
    P1            P2            P3
    |             |             |
    |---(1,0,0)-->|             |  P1 sends m1 to P2
    |             |             |
    |             |---(1,1,0)-->|  P2 sends m2 to P3
    |             |             |
    |<--(2,1,0)---|             |  P2 sends m3 to P1
    |             |             |
    |             |<--(0,1,1)---|  P3 sends m4 to P2
    |             |             |
    |---(3,1,0)-->|             |  P1 sends m5 to P2
    |             |             |
    |             |---(3,2,1)-->|  P2 sends m6 to P3
    |             |             |
```

The delivery order of the messages is as follows:

- P1 delivers m1, m3, m5
- P2 delivers m1, m2, m3, m4, m5, m6
- P3 delivers m2, m4, m6

Note that the delivery order respects the causal order of the messages, but it is not the same as the total order or the FIFO order. For example, P3 delivers m4 before m6, even though m6 was sent later by P2, because m4 causally precedes m6. Similarly, P1 delivers m3 before m5, even though m5 was sent later by P1, because m3 causally precedes m5.