Causal order is a partial ordering of messages in a distributed system that reflects the causal relationship between events. It means that if a message send event causally precedes another message send event, then the corresponding message receive events must also be ordered accordingly. Causal order is useful for maintaining consistency and avoiding anomalies in distributed systems.

One way to draw a diagram for causal order is to use a space-time diagram, where each process is represented by a vertical line and each message is represented by a horizontal arrow. The diagram shows the logical time of each event, which is a number assigned by a logical clock that increases monotonically and preserves the causal order. The diagram also shows the happened-before relation, which is a partial order that indicates which events are causally related. The happened-before relation is denoted by a dashed line connecting two events.

The following diagram illustrates the causal order of messages in a distributed system with three processes, P1, P2, and P3. The messages are labeled as M1, M2, M3, and M4. The logical time of each event is shown in parentheses. The happened-before relation is shown by dashed lines.

```
P1 | P2 | P3
|    |    |
|    |    | (1) send M1
|    |    |----------> (2) receive M1
|    |    |    |    /
|    |    |    |   /
|    |    |    |  /
|    |    |    | /
|    |    |    |/
|    |    | (3) send M2
|    |    |----------> (4) receive M2
|    |    |    |    |
|    |    |    |    | (5) send M3
|    |    |    |    |----------> (6) receive M3
|    |    |    |    |    |    /
|    |    |    |    |    |   /
|    |    |    |    |    |  /
|    |    |    |    |    | /
|    |    |    |    |    |/
| (7) send M4 |    |    |
|----------> (8) receive M4 |    |
|    |    |    |    |    |
|    |    |    |    |    |
```

The diagram shows that M1 causally precedes M2, M2 causally precedes M3, and M3 causally precedes M4. The logical time of each event reflects this causal order. For example, the logical time of the send event of M2 is 3, which is greater than the logical time of the receive event of M1, which is 2. The diagram also shows that M1 and M4 are concurrent, as they are not causally related. The logical time of the send event of M4 is 7, which is not greater than the logical time of the receive event of M1, which is 2. The diagram also shows that the happened-before relation is transitive, as M1 happened before M2, M2 happened before M3, and M3 happened before M4. The dashed lines connect the events that are causally related by the happened-before relation.