# Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Some common types of performance constraints are:
  - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events.
  - Duration Constraint: A duration constraint describes the maximum or minimum time interval for the execution of a task.
- Some common types of reliability constraints are:
  - Synchronization Constraint: A synchronization constraint describes the order or precedence of events or tasks.
  - Consistency Constraint: A consistency constraint describes the validity or accuracy of data or information.
  - Availability Constraint: An availability constraint describes the minimum or maximum time interval for the availability of a resource or service.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval logic, or event calculus.
- Timing constraints can be validated using automatic test systems that can measure the actual response time, execution time, or synchronization time of the system.