# Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must respond to events within a specified time interval.
- A real-time system can be classified as either hard or soft, depending on the consequences of missing a deadline.
- A hard real-time system is one where missing a deadline can cause a catastrophic failure or unacceptable loss. For example, a nuclear reactor control system or an air traffic control system.
- A soft real-time system is one where missing a deadline can degrade the performance or quality of service, but not cause a failure. For example, a video streaming system or a multimedia application.
- A real-time system consists of a set of tasks that must be executed periodically or sporadically, depending on the arrival of events or requests.
- A task is a unit of computation that has a well-defined functionality and a set of timing constraints, such as a release time, a deadline, and an execution time.
- A release time is the earliest time at which a task can start its execution. A release time can be fixed or variable, depending on the nature of the task.
- A fixed release time is one that is known in advance and does not depend on the occurrence of any event or condition. For example, a periodic task that is executed every 10 milliseconds has a fixed release time of 0, 10, 20, ... milliseconds.
- A variable release time is one that is determined by the occurrence of an event or condition that is not known in advance. For example, a sporadic task that is triggered by a sensor reading or a user input has a variable release time that depends on when the sensor or the user generates the event.
- A release time is an important parameter for scheduling real-time tasks, as it determines the order and priority of the tasks that are ready to execute at any given time.
- A release time can also affect the feasibility and optimality of a real-time system, as it can impose constraints on the allocation and utilization of the system resources.