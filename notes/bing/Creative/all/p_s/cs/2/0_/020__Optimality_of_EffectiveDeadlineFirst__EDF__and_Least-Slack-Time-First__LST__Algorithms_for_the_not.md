### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms for Real Time Scheduling

- Effective-Deadline-First (EDF) is a dynamic priority scheduling algorithm that assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is scheduled first. EDF is optimal for scheduling preemptive tasks on one processor, meaning that it can produce a feasible schedule if and only if a feasible schedule exists for the given task set. EDF can handle both periodic and aperiodic tasks, as well as tasks with arbitrary release times and deadlines. EDF can also achieve 100% CPU utilization, meaning that it does not waste any processor time when there are tasks to execute.

- Least-Slack-Time-First (LST) is another dynamic priority scheduling algorithm that assigns priorities to tasks according to their slack (or laxity), which is the difference between the deadline and the remaining execution time of the task. The task with the least slack has the highest priority and is scheduled first. LST is also optimal for scheduling preemptive tasks on one processor, and it can handle both periodic and aperiodic tasks, as well as tasks with arbitrary release times and deadlines. However, LST requires the knowledge of the execution times of the tasks, which may be difficult to predict in real-time systems. LST may also under-utilize the CPU, meaning that it may leave some processor time idle when there are tasks to execute.

- Both EDF and LST are optimal for scheduling preemptive tasks on one processor, but they may have different performance in terms of response time, jitter, and power consumption. EDF tends to favor tasks with shorter deadlines, while LST tends to favor tasks with shorter execution times. EDF may cause more preemptions and context switches than LST, which may increase the overhead and reduce the power efficiency. LST may cause more deadline misses than EDF, especially when the task set is overloaded or the execution times are uncertain. Therefore, the choice of the algorithm depends on the characteristics and requirements of the task set and the system.

- Here is an example of how EDF and LST schedule a set of four tasks with different release times, execution times, and deadlines:

| Task | Release Time | Execution Time | Deadline |
|------|--------------|----------------|----------|
| A    | 0            | 2              | 4        |
| B    | 1            | 3              | 6        |
| C    | 2            | 2              | 8        |
| D    | 3            | 4              | 10       |

- The following figure shows the schedule produced by EDF and LST for the task set:

```
EDF: | A | B | A | C | D | B | C | D |
     0    1    2    3    4    5    6    7    8    9   10

LST: | A | B | A | D | C | B | C | D |
     0    1    2    3    4    5    6    7    8    9   10
```

- As we can see, EDF and LST produce different schedules, but both of them meet all the deadlines. EDF has more preemptions and context switches than LST, but LST has more idle time than EDF. EDF has lower response time and jitter for task A, while LST has lower response time and jitter for task D. The power consumption of both algorithms depends on the power model of the processor and the overhead of the scheduling algorithm.

Some possible mnemonics and learning tricks for the topic are:

- EDF: Earliest Deadline First, Easy to Do First, Every Day First
- LST: Least Slack Time, Last Second Task, Lazy Schedule Task
- EDF favors tasks with shorter deadlines, LST favors tasks with shorter execution times
- EDF has more preemptions, LST has more idle time
- EDF has lower response time and jitter for tasks with shorter deadlines, LST has lower response time and jitter for tasks with shorter execution times
- EDF and LST are optimal for preemptive tasks on one processor, but may have different performance in terms of response time, jitter, power consumption, and deadline misses
- To remember the difference between slack and deadline, think of slack as the amount of time you can slack off before the deadline, and deadline as the time when you have to finish the task. The less slack you have, the more urgent the task is.