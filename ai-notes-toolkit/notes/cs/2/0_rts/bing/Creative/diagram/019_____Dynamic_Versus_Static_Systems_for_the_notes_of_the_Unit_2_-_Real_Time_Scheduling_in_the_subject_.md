### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival times, execution times, deadlines, priorities, etc.) are known and fixed before the system runs.
- A **dynamic system** is one where the tasks and their attributes may change or be unknown until the system runs.
- Static systems are easier to validate and analyze than dynamic systems, since they have less uncertainty and variability .
- Dynamic systems may provide better performance and adaptability than static systems, since they can respond to changing workloads and events .
- Static systems are more suitable for hard real-time systems, where missing deadlines can have catastrophic consequences .
- Dynamic systems are more suitable for soft real-time systems, where missing deadlines can have acceptable or negligible consequences.
- Static systems use **static scheduling** algorithms, where the task priorities and order of execution are determined before the system runs.
- Dynamic systems use **dynamic scheduling** algorithms, where the task priorities and order of execution are determined as the system runs.
- Static scheduling algorithms are simpler and faster than dynamic scheduling algorithms, since they do not require runtime information or decision making.
- Dynamic scheduling algorithms are more complex and slower than static scheduling algorithms, since they require runtime information and decision making.
- Static scheduling algorithms are optimal for periodic tasks with fixed deadlines, such as rate-monotonic scheduling (RMS) and earliest deadline first (EDF) scheduling.
- Dynamic scheduling algorithms are optimal for aperiodic or sporadic tasks with variable deadlines, such as least slack time (LST) scheduling and least laxity first (LLF) scheduling.
- Static systems can be centralized or distributed, where the scheduling decisions are made at one central site or at multiple sites respectively.
- Dynamic systems are usually distributed, where the scheduling decisions are made cooperatively by the sites involved.