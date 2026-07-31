# Dynamic Versus Static Systems

- A **dynamic system** is one that changes its behavior or configuration in response to external events or inputs, such as workload, user requests, or environmental conditions.
- A **static system** is one that has a fixed and predetermined behavior or configuration that does not change during the system execution.
- Dynamic and static systems have different advantages and disadvantages for real-time scheduling, which is the process of assigning priorities and resources to tasks that have timing constraints.
- Some of the factors that affect the choice of dynamic or static scheduling are:

  - The **predictability** of the system workload and environment. Static scheduling is more suitable for systems that have a known and fixed set of tasks and deadlines, while dynamic scheduling is more flexible for systems that have variable and unpredictable workloads and events .
  - The **complexity** of the system and the scheduling algorithm. Static scheduling is simpler and faster to implement and execute, while dynamic scheduling requires more computation and overhead to determine the optimal priorities and resources for each task at run time .
  - The **validation** of the system and the scheduling algorithm. Static scheduling is easier to verify and guarantee the correctness and feasibility of the schedule, while dynamic scheduling is harder to analyze and prove the schedulability and optimality of the schedule .
  - The **performance** of the system and the scheduling algorithm. Dynamic scheduling can achieve better performance in terms of response time, resource utilization, and adaptability, while static scheduling can suffer from poor performance due to over-provisioning, under-utilization, and rigidity .

- Some of the examples of dynamic and static scheduling algorithms are:

  - **Earliest Deadline First (EDF)**: A dynamic scheduling algorithm that assigns the highest priority to the task with the earliest absolute deadline .
  - **Least Slack Time (LST)**: A dynamic scheduling algorithm that assigns the highest priority to the task with the least amount of slack time, which is the difference between the deadline and the remaining execution time .
  - **Rate Monotonic (RM)**: A static scheduling algorithm that assigns the highest priority to the task with the shortest period or inter-arrival time .
  - **Deadline Monotonic (DM)**: A static scheduling algorithm that assigns the highest priority to the task with the shortest relative deadline .

- Depending on the requirements and characteristics of the real-time system, one may choose a dynamic or a static scheduling algorithm, or a combination of both, to achieve the desired performance and reliability.