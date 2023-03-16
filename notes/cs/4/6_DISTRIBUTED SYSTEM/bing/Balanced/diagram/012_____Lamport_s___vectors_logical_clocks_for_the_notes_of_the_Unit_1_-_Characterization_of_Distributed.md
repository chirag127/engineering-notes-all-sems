### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on the causal relationships between them.
- Lamport's logical clocks are based on the idea that if event a causes event b, then a should happen before b in any consistent ordering of events.
- Lamport's logical clocks use numerical software counter values maintained in each process to assign timestamps to events.
- The rules for Lamport's logical clocks are:

  - Each process increments its counter value by one before each event in that process.
  - Each process attaches its counter value to every message it sends.
  - Each process updates its counter value to the maximum of its own value and the received value, before processing the message.

- Lamport's logical clocks ensure that if a -> b, then C(a) < C(b), where C(a) and C(b) are the timestamps of events a and b, respectively.
- Lamport's logical clocks do not ensure that if C(a) < C(b), then a -> b, because events in different processes may be concurrent and have no causal relationship.
- Lamport's logical clocks are also known as scalar clocks or Lamport timestamps.