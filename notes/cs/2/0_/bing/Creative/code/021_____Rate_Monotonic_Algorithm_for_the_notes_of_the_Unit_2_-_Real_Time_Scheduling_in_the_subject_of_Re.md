### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- It is a preemptive scheduling algorithm, which means that a higher priority task can preempt a lower priority task at any time .
- It is optimal for periodic tasks, which means that it can schedule any set of periodic tasks that is feasible, i.e., that can be scheduled by any other algorithm  .
- It has a simple schedulability test, which is based on the utilization factor of the task set, i.e., the sum of the ratios of execution time to period for each task  .
- The schedulability test is sufficient and necessary for task sets with harmonic periods, i.e., periods that are integer multiples of each other, and sufficient but not necessary for task sets with arbitrary periods  .
- The schedulability test is given by the following formula, where n is the number of tasks, C_i is the execution time of task i, and T_i is the period of task i  :

![formula](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%5Cfrac%7BC_i%7D%7BT_i%7D%20%5Cleq%20n%20%5Cleft%281%20-%20%5Cfrac%7B1%7D%7B2%5En%7D%5Cright%29)

- The schedulability test can be improved by using the exact response time analysis, which computes the worst-case response time of each task and compares it with its deadline  .
- The advantages of RMA are its simplicity, optimality, and low overhead .
- The disadvantages of RMA are its inability to handle aperiodic or sporadic tasks, its sensitivity to task parameters, and its pessimism for task sets with arbitrary periods .