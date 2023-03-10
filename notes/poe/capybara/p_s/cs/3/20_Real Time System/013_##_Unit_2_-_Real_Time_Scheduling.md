## Unit 2 - Real Time Scheduling

Real Time Scheduling is a critical aspect of operating systems design that ensures timely execution of tasks. In this unit, we will learn about the various scheduling algorithms used in real-time systems and how they are implemented.

### Types of Real Time Scheduling

There are two types of real-time scheduling: hard real-time scheduling and soft real-time scheduling.

#### Hard Real-Time Scheduling

In hard real-time scheduling, tasks have strict deadlines that must be met. If a task misses its deadline, it can result in a system failure. Some commonly used hard real-time scheduling algorithms include:

- Rate Monotonic Scheduling (RMS)
- Earliest Deadline First Scheduling (EDF)

#### Soft Real-Time Scheduling

In soft real-time scheduling, tasks have deadlines, but missing them does not result in a system failure. Some commonly used soft real-time scheduling algorithms include:

- Weighted Round Robin (WRR)
- Proportional Share Scheduling (PSS)

### Scheduling Algorithms

Scheduling algorithms are used to decide which task to execute next. The choice of algorithm depends on the type of real-time scheduling being used.

#### Rate Monotonic Scheduling (RMS)

RMS is a priority-based scheduling algorithm used in hard real-time systems. In RMS, each task is assigned a priority based on its period. A task with a shorter period has a higher priority than a task with a longer period. Tasks are scheduled in order of priority, with the highest priority task being executed first.

#### Earliest Deadline First Scheduling (EDF)

EDF is another priority-based scheduling algorithm used in hard real-time systems. In EDF, each task is assigned a priority based on its deadline. A task with an earlier deadline has a higher priority than a task with a later deadline. Tasks are scheduled in order of priority, with the task with the earliest deadline being executed first.

#### Weighted Round Robin (WRR)

WRR is a scheduling algorithm used in soft real-time systems. In WRR, tasks are assigned weights based on their importance. A task with a higher weight is executed more frequently than a task with a lower weight.

#### Proportional Share Scheduling (PSS)

PSS is another scheduling algorithm used in soft real-time systems. In PSS, tasks are assigned shares of the processor's time based on their importance. A task with a higher share gets more processor time than a task with a lower share.

### Advantages and Disadvantages

The choice of scheduling algorithm depends on the specific requirements of the real-time system. Some advantages and disadvantages of different scheduling algorithms include:

#### Rate Monotonic Scheduling (RMS)

Advantages:
- Simple and efficient algorithm
- Guaranteed to meet all task deadlines if the system is schedulable

Disadvantages:
- Limited flexibility in terms of scheduling priorities

#### Earliest Deadline First Scheduling (EDF)

Advantages:
- Flexible scheduling algorithm that can handle both periodic and aperiodic tasks
- Guaranteed to meet all task deadlines if the system is schedulable

Disadvantages:
- More complex than RMS and requires more processing power

#### Weighted Round Robin (WRR)

Advantages:
- Allows for more flexibility in scheduling priorities
- Simple and efficient algorithm

Disadvantages:
- Does not guarantee that all tasks will meet their deadlines

#### Proportional Share Scheduling (PSS)

Advantages:
- Provides fair allocation of resources among tasks
- Allows for more flexibility in scheduling priorities

Disadvantages:
- Does not guarantee that all tasks will meet their deadlines

### Applications

Real-time scheduling is used in a variety of applications, including:

- Industrial control systems
- Medical equipment
- Aerospace systems
- Multimedia systems

### Conclusion

Real-time scheduling is a critical aspect of operating systems design. The choice of scheduling algorithm depends on the specific requirements of the real-time system. By understanding the different types of real-time scheduling and the advantages and disadvantages of different scheduling algorithms, we can design more efficient and reliable real-time systems.