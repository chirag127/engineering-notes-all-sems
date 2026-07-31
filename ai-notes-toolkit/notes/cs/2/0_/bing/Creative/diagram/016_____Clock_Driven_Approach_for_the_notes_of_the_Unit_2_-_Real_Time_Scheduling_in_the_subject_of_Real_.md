Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Clock Driven Approach for the Unit 2 - Real Time Scheduling in the subject of Real Time System.

### Clock Driven Approach

- Clock driven scheduling is also called as time-driven scheduling.
- When scheduling is clock driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock driven scheduler computes a schedule offline, before the system starts to execute, and stores it in a table.
- The scheduler consults the table at each scheduling point and dispatches the jobs accordingly.
- A scheduling point is determined by the interrupts received from a clock.
- A clock driven scheduler does not depend on events, such as job releases and completions, in the system.
- A clock driven scheduler never exhibits the anomalous timing behavior of priority-driven systems.
- A clock driven scheduler can handle periodic, sporadic and aperiodic jobs, as long as they are known in advance.
- A clock driven scheduler can also handle precedence constraints and resource sharing among jobs.
- A clock driven scheduler requires a periodic static schedule, which is a sequence of frames, each containing a set of jobs.
- A periodic static schedule is also called a cyclic schedule.
- A cyclic schedule can be generated using various algorithms, such as cyclic executive, table-driven scheduling, and bus-cycle scheduling.
- A clock driven scheduler has some advantages, such as predictability, simplicity, and low overhead.
- A clock driven scheduler also has some disadvantages, such as inflexibility, inefficiency, and difficulty in handling dynamic situations.