Total causal order is a way of ordering events in a distributed system such that every event is causally related to every other event, and all processes agree on the same linearization of events. It is the strictest form of ordering, and it implies that the system is synchronous.

One way to implement total causal order is to use a sequencer, which is a special process that assigns a unique sequence number to every message that is multicast in the system. The sequencer receives every message from the sender, and then multicasts it to all the other processes with a sequence number. The processes deliver the messages in the order of the sequence numbers, and discard any duplicate messages. This way, all the processes see the same order of messages, and the order is consistent with the causal order.

Another way to implement total causal order is to use a vector clock, which is a data structure that records the logical time of every process in the system. Every process maintains a vector clock, and updates it whenever it sends or receives a message. The vector clock of a message contains the logical time of the sender at the time of sending. The processes compare the vector clocks of the messages to determine the causal order, and deliver the messages according to a total order relation defined on the vector clocks.

The following diagram illustrates the basic architecture of a distributed system with total causal order using a sequencer:

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
    +------------>|             |
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             +------------>|
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             |             |
    |             +------------>|             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    +---------------------------------------->|
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    +------------>|             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             +------------>|             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    +---------------------------------------->|
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    +------------>|             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             +------------>|             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    +---------------------------------------->|
    |             |             |