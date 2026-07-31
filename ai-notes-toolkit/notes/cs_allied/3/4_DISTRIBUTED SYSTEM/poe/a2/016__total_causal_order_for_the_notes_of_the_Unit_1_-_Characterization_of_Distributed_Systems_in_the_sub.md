 Here is the content in markdown format without any emojis or external links:

### Total Causal Order

1. In distributed systems, events can occur concurrently. This can lead to causality violations if not handled properly.
2. Total causal order ensures that the events are delivered to processes in the same order as they occurred in the system. This preserves causality.
3. Lamport's logical clocks are used to assign timestamps to events. The timestamp of an event is the maximum of the timestamp of the received messages plus 1. This ensures that the timestamp of the child event is always greater than the parent event.
4. The events are then delivered to the processes in the increasing timestamp order. This ensures total causal order and avoids causality violations.
5. Total causal order is a strong guarantee and can impact the performance of the system. It is suitable for applications where strict event ordering is required.

The content is written in a formal tone with points and without any emojis or links as requested. Please let me know if you would like me to modify or expand the content in any way.