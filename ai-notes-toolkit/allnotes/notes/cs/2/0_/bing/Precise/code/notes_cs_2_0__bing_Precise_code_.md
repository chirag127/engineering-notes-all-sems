

# Real Time System

A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.

The term “real-time system” refers to any information processing system with hardware and software components that perform real-time application functions and can respond to events within predictable and specific time constraints.

## Applications of Real-Time Systems

- **Process Control Systems**: Process control systems are used in industrial applications where production is continuous.
- **Machine Vision**: Machine vision is used to help machines rapidly interpret data so they can see their surroundings.
- **Robotics**: Robotics is another application of real-time systems.

Real-time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare.

## Types of Real-Time Systems

Real-time systems can be classified based on their timing constraints.



## Unit 1 - Introduction of Real Time System

A real-time system is a computer system that is designed to process data and provide outputs within a specific time frame. This time frame is known as the system's deadline, and it is determined by the requirements of the application for which the system is being used.

Some key points to consider when discussing real-time systems include:

1. Real-time systems are used in a wide range of applications, including industrial control, aviation, and telecommunications.
2. These systems are designed to provide timely and accurate responses to external events.
3. Real-time systems can be classified as either hard or soft, depending on the consequences of missing a deadline.
4. Hard real-time systems have strict deadlines, and missing a deadline can result in catastrophic consequences.
5. Soft real-time systems have more flexible deadlines, and missing a deadline may result in degraded system performance but not catastrophic consequences.
6. The design of real-time systems requires careful consideration of factors such as scheduling, resource allocation, and fault tolerance.




### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A **real-time system** is a computer system that is designed to process data and provide outputs within a specific time frame.
- The time frame is determined by the requirements of the system and can range from milliseconds to seconds.
- Real-time systems are used in applications where timely responses are critical, such as in control systems, communication systems, and financial systems.
- These systems are designed to provide predictable and deterministic responses to events, ensuring that the system can meet its timing requirements.
- Real-time systems can be classified into two types: **hard real-time systems** and **soft real-time systems**.
- **Hard real-time systems** have strict timing requirements and failure to meet these requirements can result in catastrophic consequences.
- **Soft real-time systems** have more relaxed timing requirements and failure to meet these requirements may result in degraded system performance but not catastrophic consequences.
- Real-time systems are typically implemented using specialized hardware and software to ensure that the system can meet its timing requirements.
- The design of real-time systems requires careful consideration of the system's requirements, including its timing requirements, to ensure that the system can provide timely and predictable responses to events.



### Typical Real Time Applications

Real-time systems are computer systems that monitor, respond to, or control an external environment. These systems are subject to a real-time constraint, which means they must respond to an input or event within a specific time frame. Here are some typical real-time applications:

1. **Industrial control systems:** These systems are used to control industrial processes such as manufacturing, chemical processing, and power generation. They must respond quickly to changes in the environment to maintain safe and efficient operation.

2. **Avionics systems:** These systems are used in aircraft to control flight, navigation, and communication. They must respond quickly to changes in the environment, such as weather conditions or air traffic, to ensure safe flight.

3. **Medical systems:** These systems are used in healthcare to monitor and treat patients. They must respond quickly to changes in a patient's condition to provide appropriate care.

4. **Telecommunications systems:** These systems are used to transmit and receive data over communication networks. They must respond quickly to changes in network conditions to maintain reliable communication.

5. **Multimedia systems:** These systems are used to process and display multimedia content, such as video and audio. They must respond quickly to user input to provide a smooth and responsive user experience.

6. **Defense systems:** These systems are used in military applications to monitor and respond to threats. They must respond quickly to changes in the environment to provide effective defense.

7. **Financial systems:** These systems are used in finance to process transactions and manage financial data. They must respond quickly to changes in market conditions to provide accurate and timely information.

These are just a few examples of the many real-time applications that exist. Real-time systems are essential for the safe and efficient operation of many critical systems and processes.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Release times refer to the specific times at which the notes for Unit 1 - Introduction of Real Time System in the subject of Real Time System are made available to students.
- These release times may vary depending on the institution, course, and instructor.
- It is important for students to be aware of the release times for the notes in order to effectively plan their study schedule.
- Students can typically find information about the release times for the notes on their course syllabus or by contacting their instructor.
- It is recommended that students regularly check for updates on the release times for the notes to ensure that they have the most up-to-date information.




### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Deadlines refer to the specific time by which a task or set of tasks must be completed.
- In the context of Real Time Systems, deadlines are critical as they ensure that the system can respond to events in a timely manner.
- Missing a deadline in a Real Time System can have severe consequences, such as system failure or loss of data.
- It is important to set realistic deadlines for tasks in a Real Time System to ensure that they can be completed on time.
- Deadlines can be hard or soft. A hard deadline is one that must be met, while a soft deadline is one that can be missed without severe consequences.
- In the subject of Real Time System, Unit 1 - Introduction of Real Time System, it is important to understand the concept of deadlines and their importance in the functioning of Real Time Systems.



### Timing Constraints

- Timing constraints are a fundamental aspect of real-time systems.
- Real-time systems are designed to respond to events within a specific time frame, known as the deadline.
- The deadline is the maximum allowable time for the system to respond to an event.
- Missing a deadline can result in system failure or degraded performance.
- There are two types of timing constraints: hard and soft.
- Hard timing constraints must be met, otherwise the system will fail.
- Soft timing constraints, on the other hand, can be missed occasionally without causing system failure.
- The design of a real-time system must take into account the timing constraints to ensure that the system can meet its deadlines.
- This can involve the use of scheduling algorithms, priority assignment, and resource management techniques.
- Meeting timing constraints is critical to the correct operation of a real-time system.



### Hard Real Time Systems

- Hard real-time systems are systems in which the correctness of the system depends not only on the logical result of the computation, but also on the time at which the results are produced.
- In a hard real-time system, a missed deadline is considered a system failure.
- Hard real-time systems are often used in safety-critical applications, such as aviation, nuclear power plants, and medical equipment.
- These systems require a high degree of reliability and predictability, and often use specialized hardware and software to achieve these goals.
- Examples of hard real-time systems include flight control systems, engine control systems, and pacemakers.
- The design of hard real-time systems involves careful consideration of timing constraints and the use of techniques such as worst-case execution time analysis and real-time scheduling algorithms.
- Hard real-time systems must be thoroughly tested and verified to ensure that they meet their timing constraints under all possible conditions.




### Soft Real Time Systems

- A soft real-time operating system is one where there is a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system.
- Soft real-time systems, though less precise, can be run on multiple cores and impose fewer restrictions on applications.
- Soft real-time is when a system continues to function even if it’s unable to execute within an allotted time.
- If the system has missed its deadline, it will not result in critical consequences.
- The system can continue to function, though with undesirable lower quality of output.
- Soft real-time systems are typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems include software that maintains and updates the flight plans for commercial airliners.




### Reference Models for Real Time Systems

Real-time systems are computer systems that must meet timing constraints while performing their tasks. These systems are used in a variety of applications, including control systems, multimedia systems, and communication systems. To design and analyze real-time systems, several reference models have been proposed. These models provide a framework for understanding the behavior of real-time systems and for developing techniques to ensure that timing constraints are met.

Some of the reference models for real-time systems are:

1. **Rate Monotonic Scheduling (RMS)**: This model is used for scheduling periodic tasks in a uniprocessor system. In this model, tasks are assigned priorities based on their periods, with shorter period tasks having higher priorities.

2. **Earliest Deadline First (EDF)**: This model is used for scheduling tasks with deadlines in a uniprocessor system. In this model, tasks are assigned priorities based on their deadlines, with tasks having earlier deadlines having higher priorities.

3. **Sporadic Server**: This model is used for scheduling aperiodic tasks in a uniprocessor system. In this model, a server task is used to execute aperiodic tasks. The server is assigned a budget of execution time, which it can use to execute aperiodic tasks.

4. **Priority Inheritance Protocol (PIP)**: This model is used to prevent priority inversion in a uniprocessor system. In this model, when a high-priority task is blocked by a lower-priority task, the lower-priority task inherits the priority of the high-priority task.

5. **Priority Ceiling Protocol (PCP)**: This model is used to prevent priority inversion and deadlock in a uniprocessor system. In this model, each resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource. When a task accesses a resource, its priority is raised to the priority ceiling of the resource.

These are some of the reference models used in the design and analysis of real-time systems. These models provide a framework for understanding the behavior of real-time systems and for developing techniques to ensure that timing constraints are met.



### Processors and Resources

- A processor is a hardware component that performs computations and executes instructions.
- In a real-time system, the processor must be able to execute tasks within their specified deadlines.
- The processor's speed and performance are critical factors in ensuring that the system can meet its real-time requirements.
- Resources refer to any hardware or software component that is required for the execution of a task.
- In a real-time system, resources must be managed carefully to ensure that tasks have access to the resources they need when they need them.
- Resource management involves allocating and deallocating resources, as well as resolving conflicts when multiple tasks require access to the same resource.
- Effective resource management is essential for ensuring that the system can meet its real-time requirements.




### Temporal Parameters of Real Time Workload

Real-time systems are designed to process data and produce results within a specific time frame. The temporal parameters of a real-time workload refer to the timing constraints that must be met by the system in order to function correctly. These parameters include:

1. **Release time**: The time at which a task becomes ready for execution.
2. **Deadline**: The time by which a task must complete its execution.
3. **Period**: The time interval between consecutive releases of a periodic task.
4. **Execution time**: The time required for a task to complete its execution once it starts.
5. **Response time**: The time interval between the release of a task and the completion of its execution.

These temporal parameters are critical in the design and analysis of real-time systems, as they determine the feasibility of the system and its ability to meet the timing constraints of the workload. Failure to meet these constraints can result in incorrect or undesirable behavior of the system. Therefore, it is important to carefully consider and analyze these parameters when designing and implementing real-time systems.



### Periodic Task Model

- A periodic task is a task that is executed repeatedly at regular intervals.
- The interval between executions is called the period of the task.
- The period is usually specified as a fixed number of time units, such as milliseconds.
- Periodic tasks are commonly used in real-time systems to perform regular activities, such as data acquisition, control, and monitoring.
- A periodic task is characterized by its period, execution time, and deadline.
- The execution time is the time required to complete one execution of the task.
- The deadline is the time by which the task must complete its execution.
- In a real-time system, it is important that periodic tasks meet their deadlines, otherwise, the system may fail to perform its intended function.
- To ensure that periodic tasks meet their deadlines, the system must be designed to provide sufficient resources, such as processing time and memory, to the tasks.
- The utilization of a periodic task is defined as the ratio of its execution time to its period.
- The utilization of a set of periodic tasks is the sum of the utilizations of the individual tasks.
- A set of periodic tasks is schedulable if there exists a scheduling algorithm that can schedule the tasks to meet their deadlines.
- Common scheduling algorithms for periodic tasks include Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF) scheduling.
- In RMS, tasks are assigned priorities based on their periods, with shorter period tasks having higher priorities.
- In EDF, tasks are assigned priorities based on their deadlines, with earlier deadline tasks having higher priorities.
- The schedulability of a set of periodic tasks can be analyzed using techniques such as utilization bound analysis and response time analysis.



### Precedence Constraints and Data Dependency

Precedence constraints and data dependencies are important concepts in real-time systems. Here are some key points to consider:

1. **Precedence constraints** refer to the order in which tasks must be executed. For example, in a real-time system, a task that processes sensor data may need to be executed before a task that uses the processed data to make a decision.

2. **Data dependencies** occur when the output of one task is used as the input of another task. This means that the second task cannot be executed until the first task has completed.

3. Precedence constraints and data dependencies can affect the schedulability of a real-time system. If tasks are not scheduled in the correct order, the system may not be able to meet its deadlines.

4. To ensure that a real-time system meets its deadlines, it is important to carefully analyze the precedence constraints and data dependencies between tasks.

5. There are several techniques that can be used to manage precedence constraints and data dependencies in real-time systems, including priority-based scheduling and resource reservation.

6. By carefully managing precedence constraints and data dependencies, it is possible to improve the performance and reliability of a real-time system. 




## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning system resources to tasks in a timely and predictable manner. This is important in real-time systems, where tasks have strict timing constraints and must be completed within a certain time frame.

There are several types of real-time scheduling algorithms, including:

1. **Rate Monotonic Scheduling (RMS)**: This is a static priority scheduling algorithm where tasks are assigned priorities based on their periods. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their deadlines. The earlier the deadline, the higher the priority.

3. **Least Laxity First (LLF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity, the higher the priority.

Real-time scheduling algorithms must ensure that all tasks meet their deadlines while also maximizing system utilization. This can be a challenging problem, and there are many factors to consider when choosing a real-time scheduling algorithm for a particular system.



### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of allocating system resources to tasks in a way that ensures that all tasks meet their timing constraints. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period of a task, the higher its priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline of a task, the higher its priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity of a task, the higher its priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of each task is assigned by the system designer and does not change during runtime.

These are some of the common approaches to real-time scheduling. Each approach has its advantages and disadvantages, and the choice of approach depends on the specific requirements of the system being designed.



### Clock Driven Approach

The clock-driven approach is a real-time scheduling method used in real-time systems. This approach is also known as time-driven or table-driven scheduling. In this approach, the scheduler uses a pre-computed schedule or a table to determine when tasks should be executed. The schedule is computed offline, before the system starts executing, and is based on the worst-case execution times of the tasks, their deadlines, and their periods.

Some key points to note about the clock-driven approach are:

1. The schedule is computed offline, before the system starts executing.
2. The schedule is based on the worst-case execution times of the tasks, their deadlines, and their periods.
3. The scheduler uses a pre-computed schedule or a table to determine when tasks should be executed.
4. This approach is also known as time-driven or table-driven scheduling.

This approach is suitable for systems with periodic tasks and fixed deadlines, where the worst-case execution times of the tasks are known in advance. It is not suitable for systems with aperiodic or sporadic tasks, or where the worst-case execution times of the tasks are not known in advance.



### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the relative importance of the task. The scheduler allocates CPU time to each task based on its weight, with higher-weighted tasks receiving more CPU time than lower-weighted tasks.

The steps involved in the WRR algorithm are as follows:
1. The scheduler assigns a time quantum to each task, which is proportional to the task's weight.
2. The tasks are placed in a queue in the order of their arrival.
3. The scheduler selects the first task in the queue and allocates it the CPU for its time quantum.
4. If the task completes before its time quantum expires, it is removed from the queue. Otherwise, the remaining time quantum is recalculated, and the task is placed at the end of the queue.
5. The scheduler selects the next task in the queue and repeats the process until all tasks are completed.

The WRR algorithm is suitable for real-time systems where tasks have different priorities and importance. It ensures that higher priority tasks receive more CPU time, while still allowing lower priority tasks to make progress. However, the algorithm may suffer from the problem of priority inversion, where a lower priority task holds a resource needed by a higher priority task, causing the higher priority task to be blocked. This can be mitigated by using techniques such as priority inheritance or priority ceiling.



### Priority Driven Approach

Priority-driven scheduling is a method used in real-time systems to schedule tasks based on their priority levels. In this approach, tasks with higher priority are executed before tasks with lower priority. This approach is commonly used in real-time systems to ensure that critical tasks are completed on time.

Some key points to consider when using a priority-driven approach for real-time scheduling include:

1. Tasks are assigned priority levels based on their importance and urgency.
2. The scheduler selects the highest priority task that is ready to execute and assigns it to the processor.
3. If two or more tasks have the same priority level, the scheduler may use other criteria, such as earliest deadline first, to determine which task to execute.
4. Preemption may be used to interrupt a lower priority task and allow a higher priority task to execute.
5. Priority inversion can occur when a lower priority task holds a resource needed by a higher priority task. This can be addressed using techniques such as priority inheritance or priority ceiling.

Overall, the priority-driven approach is a widely used and effective method for scheduling tasks in real-time systems. It ensures that critical tasks are completed on time and helps to maximize system performance. However, careful consideration must be given to the assignment of priority levels and the handling of priority inversion to ensure that the system operates as intended.



### Dynamic Versus Static Systems

- **Dynamic systems** are systems that change over time, while **static systems** remain constant.
- In the context of real-time scheduling, dynamic systems refer to systems where the scheduling decisions are made at runtime, based on the current state of the system.
- In contrast, static systems refer to systems where the scheduling decisions are made offline, before the system starts executing.
- Dynamic scheduling algorithms are more flexible and can adapt to changes in the system, such as varying workload or resource availability.
- Static scheduling algorithms, on the other hand, are more predictable and easier to analyze, as the scheduling decisions are made in advance.
- Examples of dynamic scheduling algorithms include Earliest Deadline First (EDF) and Least Laxity First (LLF).
- Examples of static scheduling algorithms include Rate Monotonic (RM) and Deadline Monotonic (DM).
- The choice between dynamic and static scheduling depends on the specific requirements of the system, such as the need for flexibility or predictability.




### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two algorithms used in real-time scheduling. These algorithms are used to schedule tasks in a way that ensures that all tasks meet their deadlines.

1. **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest absolute deadline is scheduled first. EDF is an optimal algorithm for scheduling tasks on a single processor, meaning that if a feasible schedule exists, EDF will always find it.

2. **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time, which is the amount of time left until the task's deadline minus the task's remaining execution time. The task with the least slack time is scheduled first. LST is also an optimal algorithm for scheduling tasks on a single processor.

In summary, both EDF and LST are optimal algorithms for scheduling tasks on a single processor in a real-time system. They ensure that all tasks meet their deadlines if a feasible schedule exists. These algorithms are commonly used in real-time scheduling and are important concepts in the study of real-time systems.



### Rate Monotonic Algorithm

The Rate Monotonic Algorithm (RMA) is a scheduling algorithm used in real-time systems. It is a priority-driven, pre-emptive scheduling algorithm that assigns priorities to tasks based on their periods. The shorter the period of a task, the higher its priority.

Here are some key points to remember about the Rate Monotonic Algorithm:

1. RMA is a static priority scheduling algorithm, meaning that priorities are assigned to tasks before the system starts running and do not change during execution.
2. The algorithm is optimal for a set of independent, periodic tasks with fixed deadlines equal to their periods.
3. The schedulability of a task set can be determined using the Liu and Layland utilization bound, which states that a set of n periodic tasks is schedulable if the total utilization of the task set is less than or equal to n(2^(1/n) - 1).
4. RMA can also be used for tasks with deadlines shorter than their periods, but the schedulability test becomes more complex.
5. The algorithm can handle sporadic tasks, which are tasks that have a minimum inter-arrival time between successive releases, by treating them as periodic tasks with a period equal to their minimum inter-arrival time.
6. RMA is not suitable for tasks with deadlines longer than their periods or for tasks with shared resources, as it can lead to priority inversion.




### Offline Versus Online Scheduling

Offline scheduling and online scheduling are two approaches to scheduling tasks in real-time systems.

1. **Offline scheduling** involves determining a schedule for tasks before the system starts executing. This schedule is fixed and does not change during the execution of the system. Offline scheduling is suitable for systems with predictable workloads, where the tasks and their execution times are known in advance.

2. **Online scheduling**, on the other hand, involves making scheduling decisions during the execution of the system. The scheduler must make decisions based on the current state of the system, including the current workload and the state of the tasks. Online scheduling is suitable for systems with unpredictable workloads, where the tasks and their execution times are not known in advance.

In summary, the choice between offline and online scheduling depends on the predictability of the workload in the system. If the workload is predictable, offline scheduling can be used to determine a fixed schedule in advance. If the workload is unpredictable, online scheduling can be used to make scheduling decisions during the execution of the system.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- **Aperiodic jobs** are tasks that do not have a regular arrival pattern and can arrive at any time.
- **Sporadic jobs** are tasks that have a minimum inter-arrival time between two consecutive jobs.
- **Priority-driven systems** assign priorities to tasks and schedule them based on their priorities.
- **Clock-driven systems** schedule tasks based on a pre-determined timetable.

#### Scheduling Aperiodic Jobs in Priority Driven Systems
- In priority-driven systems, aperiodic jobs can be scheduled using one of the following methods:
  - **Background**: Aperiodic jobs are assigned the lowest priority and are executed only when no other higher priority jobs are ready to execute.
  - **Polling Server**: A periodic task, called a polling server, is introduced with a fixed capacity. The server is used to execute aperiodic jobs whenever it has available capacity.
  - **Deferrable Server**: Similar to the polling server, but the server can defer its capacity to the next period if no aperiodic jobs are ready to execute.
  - **Sporadic Server**: Similar to the deferrable server, but the server can also reclaim unused capacity from the previous period.

#### Scheduling Sporadic Jobs in Priority Driven Systems
- In priority-driven systems, sporadic jobs can be scheduled using the sporadic server method mentioned above.

#### Scheduling Aperiodic and Sporadic Jobs in Clock Driven Systems
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using the **Time-Triggered** approach, where a fixed time slot is reserved for the execution of aperiodic and sporadic jobs.
- Another approach is the **Slack Stealing** method, where the system dynamically adjusts the schedule to accommodate aperiodic and sporadic jobs by utilizing the slack time available in the schedule.




## Unit 3 - Resources Sharing

Resource sharing refers to the sharing of resources among multiple users or systems. This can include sharing of physical resources, such as hardware, or logical resources, such as data or software.

Some benefits of resource sharing include:

1. Cost savings: Sharing resources can reduce the cost of acquiring and maintaining resources for each individual user or system.
2. Increased efficiency: Sharing resources can increase efficiency by allowing multiple users or systems to access the same resources simultaneously.
3. Improved collaboration: Sharing resources can facilitate collaboration among users or systems by allowing them to access and work on the same data or software.

There are several methods for sharing resources, including:

1. Network-based sharing: This involves sharing resources over a network, such as the Internet or a local area network (LAN).
2. Cloud-based sharing: This involves sharing resources through a cloud service provider, such as Google Drive or Dropbox.
3. Virtualization: This involves creating virtual versions of physical resources, such as servers or storage devices, which can be shared among multiple users or systems.

Resource sharing can also involve the use of protocols and standards to facilitate the sharing of resources. Some common protocols and standards for resource sharing include:

1. File Transfer Protocol (FTP): This is a standard network protocol used to transfer files from one host to another over a TCP-based network.
2. Network File System (NFS): This is a distributed file system protocol that allows a user on a client computer to access files over a network as if they were on the local hard disk.
3. Common Internet File System (CIFS): This is a protocol that provides shared access to files, printers, and other resources on a network.

In conclusion, resource sharing is an important concept that can provide many benefits, including cost savings, increased efficiency, and improved collaboration. There are several methods for sharing resources, and the use of protocols and standards can facilitate the sharing of resources among multiple users or systems.



### Effect of Resource Contention and Resource Access Control (RAC)

- A resource access-control protocol, or simply an access-control protocol, is a set of rules that govern when and under what conditions each request for resource is granted and how jobs requiring resources are scheduled.
- Resource contention often leads to performance degradation in the applications contending for the shared resource. This can cause unexpected project delays, because processes contending for resources will be stalled until they can access the resource.
- Resource Access Control Protocols work to reduce the undesirable effect of resource contention. Resource contention affects the execution behavior and schedulability of jobs.
- One of the major objectives of resource access control is to minimize the undesirable effects of resource allocation.
- Access to resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterward; the time the resource is locked is the critical section. If a lock request fails, the requesting job is blocked; a job holding a lock cannot be preempted by a higher priority job needing that lock.



### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, regardless of the priority of other tasks.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- This is achieved by ensuring that only one task can enter the critical section at a time.
- If another task attempts to enter the critical section while it is already occupied, it will be blocked until the occupying task exits the critical section.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms, such as semaphores or mutexes.
- It is important to use non-preemptive critical sections carefully, as they can introduce the potential for priority inversion and deadlock if not used correctly.
- Priority inversion occurs when a lower priority task holds a resource needed by a higher priority task, causing the higher priority task to be blocked.
- Deadlock occurs when two or more tasks are blocked, waiting for resources held by each other, resulting in a circular wait.
- To avoid these issues, it is important to follow best practices for using non-preemptive critical sections, such as avoiding nested critical sections and ensuring that tasks do not hold resources for longer than necessary.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage the sharing of resources among tasks. These protocols are designed to prevent priority inversion, which occurs when a high-priority task is blocked by a lower-priority task that is holding a shared resource.

1. **Priority-Inheritance Protocol**: This protocol allows a lower-priority task that is holding a shared resource to temporarily inherit the priority of the highest-priority task that is blocked and waiting for the resource. This allows the lower-priority task to complete its use of the resource and release it, allowing the higher-priority task to proceed.

2. **Priority-Ceiling Protocol**: This protocol assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only access a shared resource if its priority is higher than the current priority ceiling of all resources it currently holds or will hold during its execution. This prevents lower-priority tasks from blocking higher-priority tasks and ensures that a task can only be blocked by tasks with a higher priority.

These protocols are used to ensure that high-priority tasks can access shared resources in a timely manner, preventing priority inversion and improving the predictability and performance of real-time systems. They are commonly used in systems with fixed-priority scheduling, where tasks are assigned priorities based on their importance and deadlines.



### Stack Based Priority-Ceiling Protocol

- Stack-Based Priority Ceiling Protocol is based on original work to allow jobs to share a run-time stack, extended to control access to other resources.
- Defining rules: Ceiling: When all resources are free, Π(t) = Ω; Π(t) updated each time a resource is allocated or freed.
- Π(t) is the current priority ceiling of all resources.
- Priority Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways.
- Real-Time Systems are multitasking systems that involve the use of semaphore variables, signals, and events for job synchronization.
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource.
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is updated each time task priorities change .
- The protocol specifies a dynamic priority ceiling for each critical section which is the earliest deadline of jobs which are currently in or will enter the critical section .
- Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section which is in use .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP) .




### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by low priority tasks holding shared resources.

Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the current preemption ceiling of the system, which is the maximum of the preemption ceilings of all resources currently locked by other tasks.
3. When a task locks a resource, the system's preemption ceiling is raised to the preemption ceiling of the resource.
4. When a task releases a resource, the system's preemption ceiling is lowered to the maximum of the preemption ceilings of all resources still locked by other tasks.
5. A task can be preempted only by tasks with priorities higher than the current preemption ceiling of the system.

This protocol ensures that high priority tasks are not blocked by low priority tasks holding shared resources, and also prevents unbounded priority inversion. It is commonly used in real-time systems to ensure timely execution of high priority tasks.



### Access Control in Multiple-Unit Resources

Access control in multiple-unit resources refers to the management of access to resources that have multiple units or instances. In a real-time system, these resources may include processors, memory, and I/O devices, among others. The goal of access control is to ensure that the system can effectively share these resources among multiple tasks while meeting their timing constraints.

Some key points to consider when implementing access control in multiple-unit resources include:

1. **Resource allocation**: The system must have a mechanism for allocating resources to tasks based on their requirements and priorities. This may involve reserving resources for high-priority tasks or using a scheduling algorithm to determine which tasks should be given access to resources at any given time.

2. **Resource contention**: When multiple tasks require access to the same resource, the system must have a mechanism for managing contention. This may involve using a priority-based scheme, where higher-priority tasks are given precedence, or using a fair-sharing scheme, where resources are allocated based on the proportion of the total resource requirement of each task.

3. **Deadlock prevention**: The system must have a mechanism for preventing deadlock, which can occur when multiple tasks are waiting for resources held by other tasks. This may involve using a resource allocation policy that avoids circular dependencies or using a timeout mechanism to detect and resolve deadlock situations.

4. **Resource monitoring**: The system must have a mechanism for monitoring the usage of resources to ensure that tasks are meeting their timing constraints. This may involve tracking the utilization of resources and generating alerts or taking corrective action when resource usage exceeds a certain threshold.

In summary, access control in multiple-unit resources is an important aspect of resource sharing in real-time systems. It involves the use of various mechanisms to allocate resources, manage contention, prevent deadlock, and monitor resource usage to ensure that the system can meet the timing constraints of its tasks.



### Controlling Concurrent Accesses to Data Objects

1. **Introduction**: In a real-time system, multiple tasks may need to access shared data objects concurrently. This can lead to conflicts and inconsistencies in the data if not managed properly.

2. **Critical Section**: A critical section is a section of code that accesses shared data and must be executed atomically. Only one task can execute its critical section at a time.

3. **Mutual Exclusion**: Mutual exclusion is a mechanism to ensure that only one task can enter its critical section at a time. This can be achieved through various techniques such as locks, semaphores, and monitors.

4. **Priority Inversion**: Priority inversion occurs when a high-priority task is blocked by a lower-priority task that holds a lock on a shared resource. This can be resolved through techniques such as priority inheritance and priority ceiling.

5. **Deadlock**: Deadlock occurs when two or more tasks are blocked, each waiting for the other to release a resource. This can be prevented through techniques such as resource ordering and the banker's algorithm.

6. **Conclusion**: Controlling concurrent accesses to data objects is crucial in real-time systems to ensure data consistency and avoid conflicts. Various techniques such as mutual exclusion, priority inversion resolution, and deadlock prevention can be used to achieve this.



## Unit 4 - Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. This type of communication is essential for applications where immediate feedback is necessary, such as in video conferencing, online gaming, and remote control systems.

Some key points to consider when discussing real-time communication include:

1. **Latency**: This refers to the time it takes for a signal to travel from the sender to the receiver. Low latency is essential for real-time communication, as it ensures that the information is delivered with minimal delay.

2. **Bandwidth**: This refers to the amount of data that can be transmitted over a communication channel in a given period of time. High bandwidth is necessary for applications that require the transmission of large amounts of data, such as video streaming.

3. **Reliability**: This refers to the ability of a communication system to deliver information accurately and consistently. In real-time communication, it is important that the information is delivered without errors or interruptions.

4. **Security**: This refers to the measures taken to protect the information being transmitted from unauthorized access or tampering. In real-time communication, it is important to ensure that the information is transmitted securely to prevent interception or manipulation.

Real-time communication can be achieved through various technologies, including Voice over IP (VoIP), instant messaging, and video conferencing. These technologies allow users to communicate in real-time, regardless of their location, and have revolutionized the way we communicate and collaborate.



### Basic Concepts in Real time Communication

Real-time communication (RTC) refers to any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real-time communication include voice over landlines and mobile phones. Real-time communication is any online communication that happens in real-time. Data is sent directly and instantly from the sender to the receiver and is not stored en route to the destination.

Real-time communication has evolved and matters more than ever in the enterprise. There are many RTC vendors and products available. Effective communication is about more than just exchanging information. It's about understanding the emotion and intentions behind the information.



### Soft and Hard RT Communication systems

Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT). The difference between a hard and soft real-time communication system is the consequences of incorrect operation.

- **Hard Real-Time (HRT)**: Hard real time systems have a strict time limit, or we can say deadlines. It is important to meet those deadlines, otherwise, the system is considered a system failure.

- **Soft Real-Time (SRT)**: In a soft real time system, there is no mandatory requirement of completing the deadline for every task. Unlike hard real-time communication systems, soft real-time communication systems generally do not have the capacity to cause catastrophic harm upon a fault, which allows for non-deterministic, less rigorous network infrastructure.

Soft Real-time Communication is a communication system that is used to support soft real-time applications in a LAN. Soft real-time communication networks do not provide absolute Quality of Service (QoS) guarantee to applications. These networks always ensure prioritized treatment for real-time messages.



### Model of Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. In the context of real-time systems, this communication must occur within strict time constraints to ensure the correct functioning of the system. Here are some key points to consider when discussing the model of real-time communication:

1. **Timing Constraints:** Real-time communication must occur within strict timing constraints to ensure the correct functioning of the system. This means that messages must be delivered and processed within a certain time frame to meet the system's requirements.

2. **Reliability:** The communication must be reliable to ensure that messages are delivered correctly and without errors. This can be achieved through the use of error detection and correction techniques, as well as through the use of redundant communication channels.

3. **Synchronization:** In many real-time systems, it is important for the different components of the system to be synchronized in order to function correctly. This can be achieved through the use of synchronization protocols, which ensure that all components of the system are operating on the same time scale.

4. **Protocols:** Real-time communication often makes use of specialized protocols that are designed to meet the timing, reliability, and synchronization requirements of the system. These protocols may include features such as priority-based message scheduling and real-time error detection and correction.

5. **Network Topology:** The topology of the communication network can also play a role in the performance of real-time communication. For example, a star topology may be more suitable for systems with strict timing requirements, as it allows for more direct communication between components.

Overall, the model of real-time communication must take into account the specific requirements of the system in terms of timing, reliability, synchronization, and network topology. By carefully designing the communication model, it is possible to ensure that the system can function correctly and meet its real-time requirements.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-Based Service and Weighted Round-Robin Service Disciplines are two types of scheduling algorithms used in switched networks.
- Priority-Based Service assigns different priorities to different packets based on their importance. Packets with higher priority are transmitted before packets with lower priority.
- Weighted Round-Robin Service assigns different weights to different packets based on their importance. Packets with higher weights are transmitted more frequently than packets with lower weights.
- Both algorithms aim to improve the quality of service in switched networks by ensuring that important packets are transmitted in a timely manner.
- These algorithms are commonly used in real-time communication systems, where timely transmission of packets is critical.
- In Unit 4 of the Real Time System course, these algorithms are studied in the context of real-time communication in switched networks.




### Medium Access Control Protocols for Broadcast Networks

Medium Access Control (MAC) protocols are used to coordinate the access of multiple devices to a shared communication medium. In broadcast networks, where all devices can transmit and receive data simultaneously, MAC protocols play a crucial role in ensuring efficient and fair use of the shared medium.

Some common MAC protocols for broadcast networks include:

1. **Aloha**: A simple protocol where devices transmit data whenever they have data to send. If two or more devices transmit at the same time, a collision occurs and the data is lost. Devices then wait for a random amount of time before retransmitting the data.

2. **Carrier Sense Multiple Access (CSMA)**: A protocol where devices listen to the medium before transmitting. If the medium is busy, the device waits for a random amount of time before attempting to transmit again.

3. **Collision Avoidance (CA)**: A protocol where devices use a handshake mechanism to reserve the medium before transmitting. This helps to avoid collisions and improve the efficiency of the network.

4. **Time Division Multiple Access (TDMA)**: A protocol where time is divided into slots and each device is assigned a specific time slot to transmit. This ensures that only one device transmits at a time, avoiding collisions.

These are just a few examples of the many MAC protocols available for broadcast networks. Each protocol has its own advantages and disadvantages, and the choice of protocol depends on the specific requirements of the network.



### Internet and Resource Reservation Protocols

Real-time communication is an important aspect of real-time systems. In order to facilitate real-time communication, various internet and resource reservation protocols have been developed. These protocols are designed to provide guaranteed Quality of Service (QoS) for real-time applications.

Some of the key internet and resource reservation protocols include:

1. **RSVP (Resource Reservation Protocol):** RSVP is a signaling protocol used to reserve resources across a network for an integrated services internet. It is used by hosts and routers to request and reserve resources for a particular data flow.

2. **DiffServ (Differentiated Services):** DiffServ is a protocol for specifying and controlling network traffic by classifying it into different levels of service. It provides a way to prioritize traffic and allocate network resources based on the level of service required by the traffic.

3. **MPLS (Multiprotocol Label Switching):** MPLS is a protocol for speeding up and shaping network traffic flows. It is used to provide QoS guarantees for real-time traffic by assigning labels to packets and forwarding them based on the labels.

4. **IntServ (Integrated Services):** IntServ is a protocol for providing QoS guarantees for individual data flows. It uses RSVP to reserve resources for specific flows and provides end-to-end QoS guarantees.

These protocols play a crucial role in ensuring that real-time communication is reliable and efficient. They provide the necessary mechanisms for reserving resources and prioritizing traffic, which is essential for real-time applications.



## Unit 5 - Real Time Operating Systems and Databases

Real-time operating systems (RTOS) and databases are essential components of many modern systems, including embedded systems, control systems, and data acquisition systems.

1. **Real-time operating systems (RTOS)** are operating systems designed to meet the needs of real-time applications. These applications have strict timing constraints and require predictable and deterministic behavior from the operating system.

2. **Databases** are organized collections of data that can be accessed and manipulated by computer programs. Databases are used to store, retrieve, and manage large amounts of data.

3. **Real-time databases** are databases designed to meet the needs of real-time applications. These databases must be able to handle transactions with strict timing constraints and provide predictable and deterministic behavior.

4. **Key features of RTOS** include pre-emptive multitasking, priority-based scheduling, and fast context switching. These features allow the operating system to quickly switch between tasks and ensure that high-priority tasks are given precedence over lower-priority tasks.

5. **Key features of real-time databases** include support for real-time transactions, predictable and deterministic behavior, and the ability to handle large amounts of data with low latency.

6. **Examples of RTOS** include VxWorks, QNX, and FreeRTOS. These operating systems are commonly used in embedded systems, control systems, and data acquisition systems.

7. **Examples of real-time databases** include RTDBMS, eXtremeDB, and TimesTen. These databases are commonly used in applications that require fast and predictable access to large amounts of data.



### Features of RTOS

Real-Time Operating Systems (RTOS) are designed to provide predictable and deterministic execution of tasks in real-time applications. Some of the key features of RTOS include:

1. **Deterministic behavior**: RTOS provides deterministic behavior, meaning that the time taken to execute a task is predictable and consistent.

2. **Preemptive scheduling**: RTOS uses preemptive scheduling, which allows high-priority tasks to interrupt lower-priority tasks, ensuring that critical tasks are executed in a timely manner.

3. **Fast context switching**: RTOS is designed to have fast context switching, which allows the system to quickly switch between tasks, reducing the overhead of task switching.

4. **Small memory footprint**: RTOS is designed to have a small memory footprint, which allows it to be used in resource-constrained systems.

5. **Real-time clock**: RTOS provides a real-time clock, which allows the system to keep track of time and execute tasks at specific times.

6. **Inter-task communication**: RTOS provides mechanisms for inter-task communication, such as message queues and semaphores, which allow tasks to communicate and synchronize with each other.

7. **Interrupt handling**: RTOS provides efficient interrupt handling, which allows the system to quickly respond to external events.

These are some of the key features of RTOS that make it suitable for use in real-time applications.



### Time Services

Time services are an essential component of real-time operating systems and databases. They provide the necessary functionality for managing and synchronizing time within the system. Here are some key points to consider when studying time services in the context of real-time systems:

1. Time services provide a mechanism for measuring the passage of time and for synchronizing activities within the system.
2. Time services can be implemented using hardware clocks, software clocks, or a combination of both.
3. Hardware clocks are typically more accurate and reliable than software clocks, but they can be more expensive and complex to implement.
4. Software clocks can be implemented using timers or counters, and they can be synchronized with external time sources such as GPS or NTP servers.
5. Time services can provide various time-related functions, such as time-stamping, time synchronization, and time-based scheduling.
6. Time services are critical for ensuring the correct operation of real-time systems, as they enable the system to meet its timing constraints and deadlines.
7. Time services can also be used to support the implementation of real-time databases, by providing mechanisms for managing temporal data and for ensuring the consistency and correctness of time-based queries.




### UNIX as RTOS

- UNIX is a multi-user, multi-tasking operating system that was originally developed in the late 1960s.
- It is widely used in both academic and commercial environments.
- UNIX is known for its stability, security, and flexibility.
- It is capable of handling multiple users and processes simultaneously, making it a popular choice for use as a real-time operating system (RTOS).
- An RTOS is an operating system that is designed to meet the demands of real-time applications, where timing constraints are critical.
- UNIX can be used as an RTOS because it has features such as preemptive scheduling, inter-process communication, and real-time signals that allow it to meet the timing requirements of real-time applications.
- Preemptive scheduling allows the operating system to interrupt a running process and switch to another process that has a higher priority.
- Inter-process communication allows processes to communicate with each other and share data in a timely manner.
- Real-time signals provide a mechanism for processes to receive notifications of events in a timely manner.
- These features, combined with the stability and security of UNIX, make it a popular choice for use as an RTOS in applications such as industrial control systems, telecommunications, and aerospace.



### POSIX Issues

POSIX (Portable Operating System Interface) is an operating system interface standard based on the popular UNIX operating system. Its main goal is to support application portability at the source-code level. POSIX defines a standard way for an application to interface with the operating system. The original POSIX standard defines interfaces to core functions such as file operations, process management, signals, and devices. Subsequent releases of POSIX have also been defined to cover real-time extensions and multi-threading.

The POSIX standard promotes portability of applications across different operating system platforms. This is especially important for applications designed for longevity, where the hardware and software infrastructure may change during the application's life cycle. The international standard POSIX standard has been adopted by virtually all operating systems in use and most real-time operating systems including ThreadX, QNX, VxWorks, Integrity, LynxOS, and Unison OS.

However, UNIX is not a real-time operating system, and there is no de-facto standard for these applications. Because of the need to achieve application portability for real-time systems, a real-time working group was established in POSIX. This group is developing standards to add POSIX (or UNIX) the OS services that are needed by real-time applications.



### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

Temporal data refers to data that represents the state of an entity at a particular point in time. It is used to track changes in data over time and is commonly used in fields such as finance, healthcare, and social sciences. Some of the key characteristics of temporal data include:

1. **Time-stamped**: Temporal data is associated with a specific point in time, usually represented as a timestamp. This allows for the tracking of changes in data over time.

2. **Historical**: Temporal data allows for the storage and retrieval of historical data. This is useful for analyzing trends and patterns over time.

3. **Versioned**: Temporal data is often versioned, meaning that multiple versions of the same data can exist at different points in time. This allows for the tracking of changes and the ability to revert to previous versions if necessary.

4. **Consistent**: Temporal data must be consistent, meaning that the data must accurately represent the state of the entity at the specified point in time.

5. **Valid**: Temporal data must be valid, meaning that the data must conform to the rules and constraints of the system in which it is used.

6. **Accurate**: Temporal data must be accurate, meaning that the data must accurately represent the state of the entity at the specified point in time.

7. **Complete**: Temporal data must be complete, meaning that all relevant data for the specified point in time must be present.

These are some of the key characteristics of temporal data that are important for the effective use of temporal data in real-time operating systems and databases.



### Temporal Consistency

Temporal consistency refers to the maintenance of the correct temporal relationships between data items in a real-time database. In a real-time system, data is often time-sensitive, meaning that its value and relevance can change over time. Temporal consistency ensures that the data used in real-time decision-making is up-to-date and accurate.

Some key points to consider when discussing temporal consistency in the context of real-time operating systems and databases include:

1. Temporal consistency is important in real-time systems because it ensures that the data used in decision-making is accurate and up-to-date.
2. Temporal consistency can be achieved through various mechanisms, such as timestamping data items and using real-time concurrency control protocols.
3. Temporal consistency is closely related to other concepts in real-time systems, such as temporal validity and temporal constraints.
4. Maintaining temporal consistency can be challenging in distributed real-time systems, where data may be replicated across multiple nodes.
5. Temporal consistency is an important consideration in the design of real-time databases and real-time operating systems.



### Concurrency Control

Concurrency control is a technique used in real-time operating systems and databases to ensure that multiple transactions can be executed simultaneously without interfering with each other. This is important in real-time systems where multiple processes may need to access shared resources at the same time.

Some of the key points to remember about concurrency control are:

1. Concurrency control is necessary to ensure the consistency and integrity of data in a real-time system.
2. There are several techniques used for concurrency control, including locking, timestamp ordering, and optimistic concurrency control.
3. Locking involves placing locks on shared resources to prevent multiple transactions from accessing them simultaneously.
4. Timestamp ordering assigns a unique timestamp to each transaction and ensures that transactions are executed in the order of their timestamps.
5. Optimistic concurrency control assumes that conflicts between transactions are rare and allows transactions to proceed without locking. Conflicts are detected and resolved when they occur.
6. Choosing the right concurrency control technique depends on the specific requirements of the real-time system and the nature of the transactions being executed.




### Overview of Commercial Real Time databases

A real-time database is a data store designed to collect, process, and/or enrich an incoming series of data points (i.e., a data stream) in real time, typically immediately after the data is created. This term does not refer to a discrete class of database management systems, but rather, applies to several types of databases.

A commercial real-time database is one created for commercial purposes only and it’s available at a price. With a commercial real estate database, you’re in a stronger position to detect market patterns, pinpoint trends and work efficiently. In short, commercial real estate databases allow you to screen deals faster and more strategically, ultimately propelling your business forward.

At the most basic level, a commercial real estate database needs to be able to source critical industry information firms use to guide investment decisions. Data must not only be accurate, but also reflect real-time changes. Your team can’t spend their limited time manually inputting or updating information.

