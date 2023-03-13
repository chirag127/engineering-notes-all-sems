A total order is a way of ordering the events in a distributed system such that every process agrees on the same order. A total order can be achieved by using logical clocks, such as Lamport timestamps, to assign a unique identifier to each event, and then comparing the identifiers to determine the order. A total order is useful for ensuring consistency and coordination among the processes in a distributed system.

The following diagram illustrates the basic architecture of a total order system using Lamport timestamps:

```
+--------+     +--------+     +--------+
|        |     |        |     |        |
|  P1    |     |  P2    |     |  P3    |
|        |     |        |     |        |
+--------+     +--------+     +--------+
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |
   |             |             |  a(1)
   |             |             |  |
   |             |             |  |
   |             |             |  |
   |             |             |  |
   |             |             |  |
   |             |             |  |
   |             |             |  |
   |             |             |  |
   |             |             |  v
   |             |             +----+
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             +----+
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             +----+
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |
   |             |             |    |  b(2)
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  |
   |             |             |    |  v
   |             |             +----+----+
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             +----+----+
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             +----+----+
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |
   |             |             |    |    |  c(3)
   |             |             |    |    |  |
   |             |