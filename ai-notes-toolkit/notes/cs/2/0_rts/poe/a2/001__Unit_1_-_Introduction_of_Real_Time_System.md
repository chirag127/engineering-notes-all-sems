 Here is the content in formal tone without emojis or external links in Markdown format:

## Unit 1 - Introduction of Real Time System

1. Real Time Systems: A real time system is a system where correctness depends not only on the logical correctness of the outputs but also on the time at which the outputs are produced. Such systems must react to inputs within certain time constraints.

2. Examples: Some examples of real time systems are:
- Control systems for machines/robots in a manufacturing plant
- Monitoring systems for patients in intensive care units of hospitals
- Anti-lock braking systems in vehicles
- Flight control and guidance systems
- Process control systems in power plants

3. Characteristics: The key characteristics of a real time system are:
- Well-defined timing constraints: They must produce correct results within specified time bounds.
- Event-driven: They continuously monitor their environment/inputs and react to events.
- Concurrency: They often contain concurrently executing processes/threads.
- Time-critical: The correctness of the system depends on strictly meeting the timing constraints. Even a small delay can lead to system failure.

4. Challenges: Some of the major challenges in real time system design are:
- Guaranteeing determinism: Ensuring that tasks are completed on time as per schedule.
- Dealing with concurrency: Coordinating the execution of concurrent processes and avoiding race conditions and deadlocks.
- Resource constraints: Having limited resources and allocating them efficiently to tasks while meeting timing requirements.
- Fault tolerance: Continuing to operate correctly even in the presence of hardware/software faults. Providing graceful degradation if time constraints cannot be met.