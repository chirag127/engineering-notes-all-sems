### Optimality of EffectiveDeadlineFirst (EDF) and Least-Slack-Time-First (LST) Algorithms for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System
EDF (Effective Deadline First) and LST (Least Slack Time First) are two algorithms used in real-time scheduling for prioritizing tasks in real-time systems.

EDF: Tasks are prioritized based on their deadlines, with the task with the earliest deadline given the highest priority. This algorithm is optimal if all deadlines are strict and tasks are independent.

LST: Tasks are prioritized based on the amount of time left until their deadlines, with tasks having the least amount of time left given the highest priority. This algorithm is optimal for tasks with soft deadlines and can handle dependencies between tasks.

Both algorithms have their own advantages and disadvantages, and the choice between them depends on the specific requirements of the real-time system.
