 Here is the content in markdown format for the given topic:

### Processors and Resources for the notes of the Unit 1 - Introduction of Real Time System

1. Processors:
- Real time systems require processors with fast execution speeds and deterministic response times.
- Examples: Microcontrollers, DSPs, ASICs, FPGAs, etc.
- These provide fast interrupt response, less latency, and ability to guarantee worst case execution times.
- They have features like low interrupt latency, priority based interrupt handling, memory protection, etc suited for real time processing.

2. Resources:
- Real time systems require resources with deterministic and consistent response times.
- Examples: Deterministic buses like CAN bus, LIN bus, etc; Non-preemptive scheduler; Priority based resource allocation; Memory with fast, consistent access; etc.
- These ensure predictable behaviour and timings which is crucial for real time systems to function properly.
- Even small deviations or delays can lead to system failures or hazards. Hence, all components must have stringent requirements for latency, throughput, consistency, etc.

3. Importance of meeting deadlines:
- In real time systems, meeting task deadlines is critical. Even small delays can lead to hazards or failures.
- Hence, it is important to allocate appropriate processors and resources to tasks based on their criticality and deadline requirements.
- The scheduling must be done carefully to ensure all deadlines are met and no task is delayed beyond its allowed limit. This requires studying worst case scenarios and reserving resources accordingly.
- Examples of consequences of missing deadlines: Self-driving car cannot brake on time leading to accident; Industrial robot arm misses coordination leading to damage; etc.

[Additional points, diagrams, codes, examples, etc can be added here for further explanation.]