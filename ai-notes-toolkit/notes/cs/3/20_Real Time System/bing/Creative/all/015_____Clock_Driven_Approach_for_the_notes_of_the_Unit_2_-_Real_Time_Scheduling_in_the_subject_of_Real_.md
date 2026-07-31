# Clock Driven Approach

- Clock driven approach is also known as time driven approach or cyclic scheduling .
- In this approach, the system executes tasks according to a predetermined schedule .
- The schedule is computed offline before the system starts running  .
- The schedule is based on the known parameters of the tasks, such as period, deadline, execution time, and precedence constraints  .
- The schedule is usually stored in a table or a cyclic executive  .
- The system follows the schedule at each clock interrupt, which occurs at regular intervals  .
- The system does not depend on the events, such as task arrivals or completions, that occur in the system  .
- The advantages of clock driven approach are  :
  - It is predictable and deterministic, which is desirable for hard real-time systems.
  - It is easy to verify the schedulability of the tasks and the correctness of the system.
  - It avoids the overhead of dynamic scheduling, such as priority assignment, queue management, and context switching.
  - It does not exhibit the anomalous timing behavior of priority driven systems, such as priority inversion or deadline misses.
- The disadvantages of clock driven approach are  :
  - It is inflexible and rigid, which makes it difficult to handle dynamic changes in the system, such as task arrivals, failures, or resource variations.
  - It is inefficient and wasteful, as it may leave some processor idle time or unused resources.
  - It is complex and tedious, as it requires a careful analysis and design of the schedule for all possible scenarios and modes of operation.
  - It is not scalable, as it may not be feasible to compute and store the schedule for a large number of tasks or a long time horizon.