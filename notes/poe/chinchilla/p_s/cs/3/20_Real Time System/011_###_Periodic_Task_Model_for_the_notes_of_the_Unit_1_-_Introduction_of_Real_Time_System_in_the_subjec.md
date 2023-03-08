### Periodic Task Model for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

The Periodic Task Model is a widely used scheduling model in Real Time Systems. It is used to schedule tasks that repeat after a certain period of time. In this model, tasks are executed at regular intervals, and the period between two consecutive tasks is fixed. 

Here are some important points to understand the Periodic Task Model in detail:

- **Task**: A task is a unit of work that is executed by the system. Each task has a fixed execution time and period. 

- **Arrival Time**: The time at which a task arrives in the system is called its arrival time. 

- **Deadline**: The deadline is the time by which a task must complete its execution. If a task fails to complete its execution by its deadline, it is considered a missed deadline.

- **Period**: The period is the time between two consecutive instances of a periodic task. 

- **Utilization**: The utilization of a task set is the ratio of the total execution time of all tasks to the time interval between two consecutive instances of the highest priority task. 

- **Schedulability**: A task set is said to be schedulable if all tasks can complete their execution before their deadlines. 

- **Preemption**: Preemption is the ability of the system to stop executing a task before its completion and switch to another task. 

- **Priority**: Priority is used to determine the order in which tasks are executed. A higher priority task will be executed before a lower priority task. 

Advantages of the Periodic Task Model are:

- It is easy to implement and understand. 

- It allows for efficient use of system resources. 

- It is well-suited for periodic tasks that have strict timing requirements. 

Disadvantages of the Periodic Task Model are:

- It is not suitable for aperiodic tasks since it requires a fixed period between task executions. 

- It assumes that tasks have fixed execution times and periods, which may not be true in practice. 

- It does not provide a mechanism for handling tasks with varying priorities. 

Examples of applications that use the Periodic Task Model are:

- Industrial control systems 

- Aerospace systems 

- Medical devices 

- Telecommunications systems 

Overall, the Periodic Task Model is an important scheduling model in Real Time Systems, and understanding its key concepts is essential for designing and implementing real-time applications.