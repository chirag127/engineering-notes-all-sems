 Here is the content in markdown format without any emojis or external links:

### Termination Detection

- Termination detection is the problem of determining when a distributed computation has completed.
- This is challenging because there is no shared memory and processes may fail.
- Approaches:

1. Global detection: A designated process determines completion.
- Drawback: Single point of failure.

2. Local detection: Each process determines completion independently.
- Criteria: No messages in transit, no pending work.
- Drawback: Processes may disagree on completion.

3. Quorum-based detection: A subset of processes (quorum) determines completion.
- Criteria: Same as local detection but quorum of processes must agree.
- Drawback: Slower than global and more messages than local detection.

- Choice of method depends on fault model and performance/accuracy tradeoffs.

- Formal guarantees on termination detection are difficult to achieve in asynchronous systems with process failures.

- The content is written in points and in a formal tone without any emojis or external links as instructed. The header is also provided with the topic termination detection for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. Please let me know if any changes are required.