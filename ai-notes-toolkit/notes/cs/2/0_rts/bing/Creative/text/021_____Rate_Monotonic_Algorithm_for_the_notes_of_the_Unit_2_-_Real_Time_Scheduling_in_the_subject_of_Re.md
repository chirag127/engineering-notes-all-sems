### Rate Monotonic Algorithm for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

- Rate Monotonic Algorithm (RMA) is a static-priority preemptive scheduling algorithm for real-time systems    .
- The static priorities are assigned to tasks based on their periods, so that the shorter the period, the higher the priority   .
- The algorithm is optimal for periodic tasks with fixed deadlines, meaning that no other static-priority algorithm can schedule a task set that RMA cannot   .
- The algorithm is simple and easy to implement, but it has some limitations, such as:
  - It does not consider the actual execution time or the deadline of the tasks, only their periods .
  - It does not handle aperiodic or sporadic tasks well, as they may have unpredictable periods or arrival times .
  - It may not utilize the processor fully, as some tasks may have long idle times between their executions .
- The algorithm has a sufficient and necessary schedulability test, which is based on the utilization factor of the tasks   . The utilization factor of a task is the ratio of its execution time to its period. The schedulability test is:

  - For n tasks, if the sum of their utilization factors is less than or equal to n(2^(1/n) - 1), then the task set is schedulable by RMA   .
  - For n tasks, if the sum of their utilization factors is greater than n(2^(1/n) - 1), then the task set may or may not be schedulable by RMA   .
  - For n tasks, if the sum of their utilization factors is greater than 1, then the task set is not schedulable by RMA or any other algorithm   .

- The algorithm can be extended or modified to handle different types of tasks, such as deadline-monotonic scheduling, which assigns priorities based on deadlines instead of periods  , or sporadic server, which allocates a fixed amount of time for aperiodic or sporadic tasks  .