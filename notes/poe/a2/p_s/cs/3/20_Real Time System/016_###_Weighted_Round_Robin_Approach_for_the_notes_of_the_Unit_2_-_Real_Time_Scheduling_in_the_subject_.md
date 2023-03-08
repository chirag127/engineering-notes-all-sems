 Here is the content in markdown format for the topic -

### Weighted Round Robin Approach

Weighted Round Robin (WRR) is an extension of basic Round Robin scheduling approach. In WRR, each task is assigned a weight that determines the number of times the task will be served in one round. The key steps in WRR are:

1. Assign weights to each task. Higher weightage is given to higher priority tasks.
2. Serve each task for one time slice and decrement its weight.
3. If weight of a task becomes zero, it is moved to the end of the queue.
4. Repeat step#2 until all tasks have zero weight. This completes one round.

Few advantages of WRR are:

- Prioritizes important tasks by giving higher weights to them.
- Prevents starvation as each task gets a minimum guarantee of CPU access in one round.
- Simple to implement.

However, determining appropriate weights for tasks can be challenging. Improper weights can lead to priority inversion and resource starvation. WRR is useful for soft real-time systems where most tasks need to meet their deadlines but few missing deadlines is acceptable.

WRR can be extended to concepts like Priority Based Weighted Round Robin which incorporates both task priorities and weights to provide better performance. WRR finds applications in CPU scheduling, network packet scheduling, etc.

Here is a simple ascii diagram to show working of WRR with 3 tasks -

Round 1:
Task 1 (weight 4): ####
Task 2 (weight 2): ##
Task 3 (weight 3): ###

Round 2:
Task 1: ###
Task 2: #
Task 3: ##

[Include other diagrams/images/codes/points as needed]