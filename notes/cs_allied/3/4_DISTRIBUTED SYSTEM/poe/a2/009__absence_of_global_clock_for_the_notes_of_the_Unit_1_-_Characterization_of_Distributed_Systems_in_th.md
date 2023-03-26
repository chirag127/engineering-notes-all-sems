 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### Absence of Global Clock

- In a distributed system, there is no single global clock. Each machine may have its own local clock which can be slightly different from others.
- This makes it difficult to assign timestamps and determine the ordering of events.
- For example, if there are two events E1 and E2 happening in a distributed system, we cannot conclusively say that E1 happened before E2 or vice-versa just based on their local timestamps. The local clocks can be out of sync.
- To partially solve this, many systems use synchronization algorithms to closely align local clocks. However, perfect synchronization is not feasible due to network delays and clock drifts.
- Some systems use logical clocks or Lamport timestamps to assign timestamps and partially order events. But there cannot be a true global timeline of events in a distributed system without a single global clock.

The above points cover the key highlights of the absence of a global clock in distributed systems. The content is written in a formal tone with points and without any emojis or external links as specified. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.