 Here is the content in markdown format for the topic ### Hard Real Time Systems for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System:

### Hard Real Time Systems

- Hard real-time systems are systems where missing a deadline is unacceptable. Missing a deadline in these systems can lead to catastrophic consequences.
- Examples of hard real-time systems include aircraft control systems, nuclear reactor control systems, etc. where even a slight delay in response can lead to loss of control or accidents.
- In hard real-time systems, all deadlines must be met under all conditions. So, hard real-time systems must have a high degree of predictability and determinism.
- Some characteristics of hard real-time systems are:
    - Low latency - They must respond to events within strict time constraints. Even milliseconds of delay can be unacceptable.
    - High reliability - They must be highly reliable and fault-tolerant to avoid failures.
    - Simple & deterministic processing - They should avoid complex processing and non-deterministic operations like dynamic memory allocation to ensure predictability.
    - Static requirement analysis - The worst-case execution requirements must be determined before system operation for guaranteeing deadlines.
    - Hardware support - They often require specialized hardware for timely response and reliability.

- Examples of applications of hard real-time systems:
    - Flight control systems
    - Automobile engine control systems
    - Industrial control systems
    - Mars rover control system
    - Robot motion control systems
    - Medical life-support systems, etc.

- Some key challenges in designing hard real-time systems are:
    - Guaranteeing worst-case execution times
    - Handling concurrency & unpredictable delays
    - Implementing fault tolerance
    - Verifying & validating systems to ensure correctness
    - Managing hardware failures & errors

[Detailed diagrams, examples, etc. can be included here if required to explain the concepts better.]