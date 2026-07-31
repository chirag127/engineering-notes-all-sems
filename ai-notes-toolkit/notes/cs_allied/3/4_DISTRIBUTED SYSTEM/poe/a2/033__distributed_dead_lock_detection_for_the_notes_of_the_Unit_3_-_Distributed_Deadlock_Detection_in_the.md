 Here is the content in Markdown format without any emojis or external links:

### Distributed Deadlock Detection

1. Centralized Approach: In centralized approach, there is a central coordinator which maintains the global state of all the transactions in the system. It tracks the resource allocation of each transaction and detects the deadlock. This approach has following disadvantages:
- It creates a performance bottleneck.
- It represents a single point of failure. If the central coordinator fails, the system cannot proceed with any transaction processing.

2. Distributed Approach: In distributed approach, each site (in distributed system) independently detects the local deadlocks and then they coordinate among themselves to resolve the global deadlocks. This approach removes the single point of failure of centralized approach. However, following issues are there:
- The distributed deadlock detection is more complex than centralized detection.
- Additional message exchanges are required between sites to resolve global deadlocks which can create overhead.

3. Hybrid Approach: The hybrid approach tries to achieve the best of both centralized and distributed approach. In this approach, most of the transactions are monitored in a distributed manner. Only in certain conditions, the system switches to a central coordinator for deadlock resolution. This reduces the number of messages required as compared to pure distributed approach and removes the single point of failure of pure centralized approach.

The content is written in points and in a formal tone without any feelings or friendliness. The formatting is done in Markdown and no emojis or external links are included. Please let me know if you would like me to modify or add anything.