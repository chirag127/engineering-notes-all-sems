
### Optimality of EffectiveDeadlineFirst (EDF) and Least-Slack-Time-First (LST) Algorithms for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Real-time scheduling algorithms are used to determine the order in which tasks are executed in a real-time system. The two main algorithms used in this context are the Effective Deadline First (EDF) and the Least-Slack-Time-First (LST) algorithms. 

EDF is an algorithm that schedules tasks by assigning the highest priority to the task with the earliest deadline. This algorithm is optimal in terms of minimizing the number of missed deadlines. However, it can lead to high processor utilization and low throughput. 

LST is an algorithm that schedules tasks by assigning the highest priority to the task with the least slack time. This algorithm is optimal in terms of minimizing the amount of time that tasks are waiting to be executed. However, it can lead to low processor utilization and high throughput.

Ascii diagram:

```
Task 1  |  Task 2  |  Task 3  |  Task 4
  EDF   |   LST   |   EDF   |   LST
```

Advantages of EDF:

- Optimal in terms of minimizing the number of missed deadlines
- Easy to implement

Disadvantages of EDF:

- High processor utilization
- Low throughput

Advantages of LST:

- Optimal in terms of minimizing the amount of time that tasks are waiting to be executed
- Low processor utilization

Disadvantages of LST:

- High throughput
- Difficult to implement

Examples of applications that use EDF and LST algorithms include embedded systems, robotics, and real-time systems.

The main difference between EDF and LST is that EDF is optimal in terms of minimizing the number of missed deadlines, while LST is optimal in terms of minimizing the amount of time that tasks are waiting to be executed.