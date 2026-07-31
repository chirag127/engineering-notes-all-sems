### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must produce the expected result by a specific deadline .
- The deadline is the maximum acceptable delay between the occurrence of an event and the completion of the system's response to that event.
- The correctness of the result in a real-time system depends not only on the logical correctness but also on the timeliness of the result.
- A timing constraint is a restriction or requirement on the timing behavior of a real-time system.
- Timing constraints can be classified into two categories :
  - Performance constraints: The constraints enforced on the response of the system, such as the minimum and maximum response time, the average response time, the throughput, etc.
  - Scheduling constraints: The constraints enforced on the execution of the tasks in the system, such as the deadlines, the priorities, the periods, the execution time, etc.
- Timing constraints can be further classified into three types based on the severity of the consequences of missing the deadline:
  - Hard constraints: The constraints that must be met for the system to function correctly. Missing a hard constraint can cause catastrophic failure or unacceptable loss.
  - Soft constraints: The constraints that should be met for the system to perform optimally. Missing a soft constraint can cause degraded performance or reduced quality of service.
  - Firm constraints: The constraints that have a benefit only if met, but no benefit if missed. Missing a firm constraint can cause wasted resources or missed opportunities.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval algebra, event calculus, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual timing behavior of the system and compare it with the expected timing behavior.