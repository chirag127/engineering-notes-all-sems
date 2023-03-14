The global state of a distributed system is the collection of the local states of the processes and the channels. A global state is consistent if it satisfies the condition that no message is received before it is sent. A consistent global state can be determined by taking a snapshot of the system along a consistent cut, which is a subset of events that divides the system into past and future. A consistent cut can be obtained by using an algorithm such as the Chandy-Lamport algorithm, which involves sending marker messages along the channels to record the state of the processes and the messages in transit.

The following diagram illustrates the basic architecture of a distributed system with four processes and four channels, and a consistent cut that determines a consistent global state:

```
    +-----+            +-----+
    | P1  |            | P2  |
    |     |            |     |
    |  e1 |----------->|  e2 |
    +-----+            +-----+
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      |                  |
      v                  v
    +-----+            +-----+
    | P3  |            | P4  |
    |     |            |     |
    |  e3 |<-----------|  e4 |
    +-----+            +-----+
```

The consistent cut is shown by the dashed line that cuts through the events e1, e2, e3, and e4. The global state consists of the local states of P1, P2, P3, and P4 at these events, and the messages that are sent but not yet received along the channels. For example, the message from P1 to P2 is not part of the global state, because it is received before the cut. The message from P4 to P3 is part of the global state, because it is sent before the cut and received after the cut. The messages from P1 to P3 and from P2 to P4 are also part of the global state, because they are in transit at the time of the cut. The global state is consistent, because no message is received before it is sent.