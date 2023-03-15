# Clock Driven Approach

- Clock driven approach is a scheduling method for hard real-time systems that require predictable and deterministic behaviour.
- In clock driven approach, the system executes tasks according to a predetermined schedule, which is computed offline based on the task parameters and system constraints .
- The schedule is usually periodic and cyclic, meaning that it repeats itself after a fixed interval of time, called the major cycle .
- The schedule specifies the exact time instants when each task should start and finish execution, independent of events such as job releases and completions .
- The schedule is stored in a table or a program, and is invoked by a clock interrupt at regular intervals .
- Clock driven approach has several advantages, such as:
  - It guarantees that all tasks will meet their deadlines, as long as the schedule is feasible and the system is stable .
  - It avoids the overhead of dynamic scheduling decisions and priority assignments at runtime .
  - It simplifies the analysis and verification of the system's timing behaviour .
- Clock driven approach also has some limitations, such as:
  - It requires that all task parameters and system constraints are known and fixed in advance .
  - It cannot handle aperiodic or sporadic tasks, or tasks with variable execution times or deadlines .
  - It may waste processor time if some tasks finish earlier than expected or do not arrive at all .
  - It may not be able to adapt to changes in the system's workload or environment .
- Clock driven approach is suitable for applications that have periodic and deterministic tasks, such as industrial control, avionics, and multimedia.
- Clock driven approach is not suitable for applications that have aperiodic or sporadic tasks, or tasks with variable execution times or deadlines, such as interactive systems, network servers, and mobile computing.