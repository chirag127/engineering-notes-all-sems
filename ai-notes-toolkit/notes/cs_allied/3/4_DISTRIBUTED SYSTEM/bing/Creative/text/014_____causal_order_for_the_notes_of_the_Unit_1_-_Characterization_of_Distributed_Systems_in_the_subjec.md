### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the notion of "happened before" or "influenced by" among events, regardless of when or where they occurred.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially when dealing with concurrent or asynchronous events.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events based on their causal dependencies.
- Causal order can be implemented using various algorithms, such as vector clocks, causal broadcast, or causal delivery, which ensure that messages are delivered or processed in a way that respects their causal order.
- Causal order can be relaxed or strengthened depending on the application requirements and trade-offs. For example, total-causal order is a stricter version of causal order that imposes a single linearization of all events, while fuzzy causal order is a weaker version that allows some degree of uncertainty or ambiguity in the ordering of events.