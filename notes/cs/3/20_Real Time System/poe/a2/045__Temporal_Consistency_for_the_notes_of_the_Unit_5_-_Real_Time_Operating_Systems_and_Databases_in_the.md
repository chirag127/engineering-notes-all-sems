 Here is the content in markdown format without any emojis or external links and in formal tone:

### Temporal Consistency for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

1. Temporal consistency: It refers to the correctness of the timing of events or transactions. In real-time systems, the timing of outputs in response to inputs is crucial. If outputs are produced too early or too late, the system will not function properly.
2. Hard real-time systems: In hard real-time systems, meeting all deadlines is mandatory. If a deadline is missed, the system may malfunction with catastrophic consequences. Examples are flight control systems, nuclear reactor monitoring systems.
3. Soft real-time systems: In soft real-time systems, deadlines should be usually met, but occasionally a deadline may be missed with degraded performance but no catastrophic consequences. Examples are video and audio processing systems.
4. Scheduling algorithms: Scheduling algorithms are needed to ensure temporal consistency, especially in hard real-time systems. Some commonly used scheduling algorithms for real-time systems are:
- Rate monotonic scheduling: The highest priority is given to the task with the shortest period. It is suitable for scheduling periodic tasks with fixed execution cycles.
- Earliest deadline first scheduling: The highest priority is given to the task with the earliest deadline. It can handle aperiodic tasks and tasks with varying execution times.
- Deadline monotonic scheduling: Similar to rate monotonic scheduling but priorities are assigned according to deadlines instead of periods.

The above points cover the key aspects regarding temporal consistency which needs to be ensured in real-time systems through proper scheduling of tasks as per the requirements. Let me know if you would like me to elaborate on any of the points or add more points to the content.