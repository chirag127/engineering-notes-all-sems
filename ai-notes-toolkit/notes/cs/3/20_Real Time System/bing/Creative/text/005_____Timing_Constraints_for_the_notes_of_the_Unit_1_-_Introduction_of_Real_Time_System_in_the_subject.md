### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also on the result being obtained within the time constraint.
- Every real-time system has a set of timing constraints that it has been designed to meet. If a system does not have timing constraints, it is not real-time.
- Timing constraints can be broken down into two categories :
  - Performance constraints: The constraints enforced on the response of the system are known as performance constraints. They specify the maximum or minimum acceptable delay between an event and the system's reaction to it. For example, a car's airbag system must deploy within a few milliseconds of a collision.
  - Scheduling constraints: The constraints enforced on the execution of tasks are known as scheduling constraints. They specify the order, frequency, duration, and deadlines of tasks that must be completed by the system. For example, a video streaming system must process and transmit frames at a constant rate.
- Timing constraints can be expressed using various constructs in requirements languages, such as deadlines, periods, offsets, jitter, latency, etc.
- Timing constraints can be validated using automatic test systems that can measure and verify the system's behavior under different scenarios and inputs.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.