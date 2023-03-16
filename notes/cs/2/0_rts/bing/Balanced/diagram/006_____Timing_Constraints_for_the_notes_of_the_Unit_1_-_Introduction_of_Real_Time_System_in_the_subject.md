### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Performance Constraints are further divided into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events.
  - Duration Constraint: A duration constraint describes the maximum or minimum time interval for the execution of a task.
- Reliability Constraints are further divided into two types:
  - Synchronization Constraint: A synchronization constraint describes the order or precedence of events or tasks in a system.
  - Consistency Constraint: A consistency constraint describes the logical or temporal relationship between the states or values of variables in a system.
- A real-time system must satisfy both performance and reliability constraints to ensure the correct functioning of the system.
- A real-time system must also have the ability to produce the expected result by a specific deadline (timeliness) and the capability of agents to coordinate independent clocks and operate together in unison (time synchronization).
- An example of a real-time system with timing constraints is an air traffic control system, which must monitor and control the movements of aircrafts in a timely and reliable manner.