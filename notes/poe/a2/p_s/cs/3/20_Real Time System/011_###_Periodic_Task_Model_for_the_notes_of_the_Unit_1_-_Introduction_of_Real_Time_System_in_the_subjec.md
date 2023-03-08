 Here is the content in markdown format for the topic ### Periodic Task Model for the notes of the Unit 1 - Introduction of Real Time System:

### Periodic Task Model

- In periodic task model, tasks are executed repeatedly after fixed time intervals known as periods.
- The tasks have well-defined execution requirements in terms of computation time and deadline.
- The tasks are required to complete their execution before their deadlines to meet the timing constraints.
- If a task misses its deadline, it leads to failure of the real-time system.
- The periodic task model is widely used in real-time systems as many real-time applications have tasks that need to be performed repeatedly after fixed time intervals like sensing environment, monitoring processes, etc.
- The characteristics of a periodic task are:

**Period (T)** - Time interval between two consecutive task invocations
**Deadline (D)** - Latest time instant by which the task must complete
**Computation Time (C)** - Time required by the task to complete one instance of its job

- The requirements of a periodic real-time task can be represented using the notation (T, C, D) where T is the period, C is the computation time and D is the deadline.
- For a periodic task to meet its deadlines, the following condition must be satisfied:

**D ??? C**

- The periodic task model is useful for analyzing the timing behavior of real-time systems. The key metrics for analyzing a set of periodic tasks are:

**Utilization (U)** - Ratio of total computation time of all tasks to the hyperperiod (LCM of all periods)
**Overload** - Condition when utilization exceeds 100% leading to miss of deadlines
** schedulability** - Ability of a scheduling algorithm to meet all deadlines of a task set

- Examples of periodic tasks:

Sensing environment periodically
Controlling processes with fixed sampling rate
Streaming data periodically

- Advantages: Simple model, well suited for repetitive tasks
- Disadvantages: Inflexible, cannot handle sporadic tasks with aperiodic execution patterns