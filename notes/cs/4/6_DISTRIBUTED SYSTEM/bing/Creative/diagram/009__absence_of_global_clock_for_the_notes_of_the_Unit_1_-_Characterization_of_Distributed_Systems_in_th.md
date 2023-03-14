The absence of global clock in distributed systems means that there is no common notion of time among the processes that are spatially separated and running independently. This makes it difficult to determine the order of events and the state of the system. A possible way to illustrate this limitation is to use a space-time diagram, where each process is represented by a vertical line and each event is represented by a point on the line. A message is represented by a horizontal line connecting two events on different processes. The diagram shows the logical order of events, but not the actual time when they occurred. For example, the following diagram shows a distributed computation involving three processes P1, P2 and P3, and nine events e1, e2, ..., e9. The diagram does not show the actual time when each event happened, only the causal dependencies among them.

```
P1 | e1
   |  \
   |   \
   |    \
   |     e3
   |     |
   |     e4
   |    /
   |   /
   |  /
   | e6
   |
P2 | e2
   |  \
   |   \
   |    \
   |     e5
   |     |
   |     e7
   |    /
   |   /
   |  /
   | e9
   |
P3 | e8
   |
```

From the diagram, we can infer that e1 happened before e3, e3 happened before e4, e4 happened before e6, and so on. However, we cannot tell if e1 happened before e2, or e2 happened before e3, or e5 happened before e6, and so on. These events are concurrent, meaning that there is no causal relation between them. Without a global clock, we cannot determine the exact order of concurrent events.