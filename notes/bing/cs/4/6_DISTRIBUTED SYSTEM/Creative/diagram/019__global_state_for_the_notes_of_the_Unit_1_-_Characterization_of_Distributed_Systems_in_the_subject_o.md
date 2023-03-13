The global state of a distributed system is the union of the states of the individual processes and the channels that communicate between them. A global state is consistent if it satisfies some logical or causal relationship among the local states and the messages. A global state can be computed by taking a snapshot of the local states and the messages in transit along a consistent cut. A consistent cut is a set of events that partitions the distributed system into two parts: the past and the future. A consistent cut is also called a global snapshot.

The following diagram illustrates the basic architecture of a distributed system with four processes and four channels, and a possible consistent cut that determines a global state:

```
    +-----+     m1     +-----+     m2     +-----+
    | P1  |----------->| P2  |----------->| P3  |
    +-----+            +-----+            +-----+
      |                  |                  |
      |                  |                  |
      |                  |                  |
     m3                 m4                 m5
      |                  |                  |
      |                  |                  |
      |                  |                  |
    +-----+            +-----+            +-----+
    | P4  |<-----------| P5  |<-----------| P6  |
    +-----+     m6     +-----+     m7     +-----+

    Consistent cut: {m1, m2, m4, m5, m7}
    Global state: {P1, P2, P3, P4, P5, P6, m3, m6}
```