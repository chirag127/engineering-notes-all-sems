 Here is the content in markdown format:

### Detection & Resolution for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Distributed deadlock detection involvescoordinating multiple sites to detect and resolve deadlocks that span multiple sites.Some approaches for distributed deadlock detection are:

1. Centralized approach: Elect a single site as the coordinator that collects resource allocation information from all sites and detects global deadlocks.

Advantages: Simple to implement.
Disadvantages: Single point of failure and potential bottleneck.

2. Decentralized approach: Each site detects local deadlocks and potential global deadlocks (based on messages from other sites). Global deadlock is detected if a set of sites detect local deadlocks that form a deadlock cycle.

Advantages: No single point of failure.
Disadvantages: More complex to implement. Excessive messaging overhead if many sites and resources.

3. Distributed algorithm: Use a distributed algorithm (e.g., a token ring algorithm) to have each site detect local deadlocks and potential global deadlocks in a coordinated fashion.

Advantages: No single point of failure and more scalable than decentralized approach.
Disadvantages: More complex to implement than centralized or decentralized approaches.

Once a global deadlock is detected, it can be resolved by:

1. Aborting and rolling back one or more transactions to break the deadlock cycle.
2. Preemptively releasing and reallocating resources to break the deadlock cycle.
3. Rescheduling one or more transactions to avoid the deadlock in the future.

The specific deadlock resolution approach taken will depend on application requirements and implementation details. The goal is to resolve the deadlock while minimizing impact on performance and preserving data consistency.