### Hard Real Time Systems

Hard real-time systems are those computer systems where the correctness of the system's output depends not only on the correctness of results but also on the timing of the results. There are several characteristics of hard real-time systems, some of which are mentioned below:

- **Timing Constraints** - In hard real-time systems, there are strict timing constraints that must be met. The system must produce a correct output within a specific time limit; otherwise, the system may fail.

- **Determinism** - The system's behavior must be predictable and deterministic, i.e., the system must always produce the same output for the same input within the specified time limit.

- **Safety-Critical Systems** - Hard real-time systems are often safety-critical systems, i.e., any failure in the system may result in severe consequences such as loss of life, property, or environmental damage.

- **Priority-Based Scheduling** - In hard real-time systems, priority-based scheduling is used to ensure that the system meets all timing constraints. The highest priority task is executed first, and lower priority tasks are executed only if there is enough time left.

- **Hardware Support** - Hard real-time systems often require specialized hardware support to meet timing constraints. For example, real-time operating systems often use hardware timers to ensure that tasks are executed within the specified time limit.

- **Concurrency** - Hard real-time systems often have multiple tasks running concurrently. The system must ensure that all tasks meet their timing constraints and that there are no conflicts between tasks.

- **Fault Tolerance** - Hard real-time systems must be fault-tolerant, i.e., the system must continue to operate correctly even in the presence of hardware or software failures.

In conclusion, hard real-time systems are critical computer systems that must meet strict timing constraints and produce deterministic results. These systems often require specialized hardware and software support to meet their requirements and must be fault-tolerant to ensure the system's safety and reliability.