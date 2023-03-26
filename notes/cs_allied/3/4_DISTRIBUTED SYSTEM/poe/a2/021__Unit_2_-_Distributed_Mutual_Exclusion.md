 Here is the content in markdown format with formal tone and without emojis:

## Unit 2 - Distributed Mutual Exclusion

1. Introduction
- Mutual exclusion: Ensuring that only one process can access a critical section at a time.
- Critical section: A piece of code that accesses shared resources.
- Need for distributed mutual exclusion: When multiple processes are running on different machines and need to access shared resources.

2. Centralized approach
- A central server grants permissions to processes to enter their critical sections.
- Issues: Single point of failure and bottleneck.

3. Token-based approach
- A token is passed between processes. A process can enter its critical section only if it possesses the token.
- Types of tokens:
-- Physical token: Passed explicitly from one process to the next.
-- Logical token: Represented by a message transmitted from one process to the next.
- Pros: No central server; fault-tolerant.
- Cons: Livelock possible if token is lost.

[No external links are included. Content is written in points and in a formal tone with no emojis.]