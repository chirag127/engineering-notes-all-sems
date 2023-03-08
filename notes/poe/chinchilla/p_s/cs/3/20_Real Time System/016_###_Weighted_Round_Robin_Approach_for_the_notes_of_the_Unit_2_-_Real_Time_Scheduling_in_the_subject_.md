### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm that is widely used in Real Time Systems for task scheduling. It is an extension of the Round Robin (RR) scheduling algorithm which assigns equal time slots to all tasks in a cyclic manner. In the WRR scheduling algorithm, each task is assigned a weight which determines the amount of time it will receive in each cycle. 

#### How does it work?

The Weighted Round Robin scheduling algorithm works as follows:

1. Assign a weight to each task, which represents the proportion of time it will receive in each cycle.
2. Sort the tasks in descending order of their weights.
3. Assign time slices to each task based on their weights in a cyclic manner, starting from the highest weight task and moving downwards.
4. If a task finishes before its time slice is over, the remaining time is added to its next time slice.

#### Advantages of Weighted Round Robin Approach

The advantages of using WRR scheduling algorithm are:

1. It provides better response time for high priority tasks as they are assigned a larger proportion of time.
2. It allows for efficient utilization of CPU by assigning appropriate time slices to each task based on their weight.
3. It is easy to implement and does not require complex calculations.

#### Disadvantages of Weighted Round Robin Approach

The disadvantages of using WRR scheduling algorithm are:

1. It may not be suitable for highly dynamic systems where the task priorities change frequently.
2. The performance of WRR heavily depends on the accuracy of the weight assigned to each task.

#### Example of Weighted Round Robin Approach

Consider a Real Time System with three tasks: T1, T2, and T3, with weights 3, 2, and 1 respectively. The time slice is set to 10ms. The scheduling of tasks using WRR algorithm will be as follows:

1. T1 will receive 3 * 10ms = 30ms
2. T2 will receive 2 * 10ms = 20ms
3. T3 will receive 1 * 10ms = 10ms
4. The cycle will repeat with T1 receiving 30ms again, followed by T2 receiving 20ms, and T3 receiving 10ms.

#### Applications of Weighted Round Robin Approach

The Weighted Round Robin scheduling algorithm is used in various Real Time Systems, including:

1. Multimedia systems for video and audio streaming.
2. Network routers for packet scheduling.
3. Web servers for handling requests from multiple clients.

Overall, the Weighted Round Robin approach is an effective scheduling algorithm for Real Time Systems, which provides better response times and efficient utilization of CPU by assigning appropriate time slices to each task based on their weight.