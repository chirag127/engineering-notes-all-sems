According to the search results, total causal order is a strict ordering of events in a distributed system that is consistent with the causal order, which means that if an event a happens before an event b, then every process in the system must observe a before b. Total causal order can be implemented using various protocols, such as vector clocks, Chandy/Lamport snapshot algorithm, or ISIS system. A possible ASCII diagram for total causal order is shown below:

### Total causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

```
    P1      P2      P3
    |       |       |
    a       |       |
    |       |       |
    |------>b       |
    |       |       |
    |       |------>c
    |       |       |
    |       |<------d
    |       |       |
    |<------e       |
    |       |       |
    |       |------>f
    |       |       |
    |------>g       |
    |       |       |
    |       |<------h
    |       |       |
    |       |------>i
    |       |       |
    |<------j       |
    |       |       |
    |------>k       |
    |       |       |
    |       |------>l
    |       |       |
    |       |<------m
    |       |       |
    |<------n       |
    |       |       |
    |------>o       |
    |       |       |
    |       |------>p
    |       |       |
    |       |<------q
    |       |       |
    |<------r       |
    |       |       |
    |------>s       |
    |       |       |
    |       |------>t
    |       |       |
    |       |<------u
    |       |       |
    |<------v       |
    |       |       |
    |------>w       |
    |       |       |
    |       |------>x
    |       |       |
    |       |<------y
    |       |       |
    |<------z       |
    |       |       |
```

In this diagram, each letter represents an event that occurs in one of the three processes P1, P2, or P3. The vertical lines represent the local order of events in each process, and the horizontal arrows represent the messages sent and received between the processes. The total causal order of the events is given by the alphabetical order of the letters, which is consistent with the causal order defined by the happens-before relation. For example, event a happens before event b, because P1 sends a message to P2 before P2 receives it. Similarly, event b happens before event c, because P2 sends a message to P3 before P3 receives it. Therefore, a happens before c transitively. However, event c is concurrent with event d, because P3 receives a message from P2 and sends a message to P2 at the same time, and there is no causal relation between them. The total causal order protocol ensures that every process observes the same order of events, regardless of the transmission delays, network congestion, or system failures.