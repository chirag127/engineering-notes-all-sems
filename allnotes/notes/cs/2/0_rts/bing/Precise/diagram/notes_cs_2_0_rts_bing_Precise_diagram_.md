

# Real Time System

A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). The term “real-time system” refers to any information processing system with hardware and software components that perform real-time application functions and can respond to events within predictable and specific time constraints.

## Types of Real-Time Systems

Real-time systems can be classified based on their timing constraints:

- **Hard real-time system**: This type of system can never miss its deadline. Missing the deadline may have disastrous consequences.
- **Soft real-time system**: This type of system can miss its deadline occasionally with some acceptably low probability.

## Applications of Real-Time Systems

Real-time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare. Some examples of real-time systems include:

- **Process Control Systems**: Process control systems are used in industrial applications where production is continuous.
- **Machine Vision**: Machine vision is used to help machines rapidly interpret data so they can see their surroundings.
- **Robotics**: Robotics is another field where real-time systems are used.



## Unit 1 - Introduction of Real Time System

A real-time system is a computer system that is designed to process data and provide output within a specific time frame. This time frame is known as the system's deadline, and it is determined by the requirements of the system's application.

1. Real-time systems are used in a variety of applications, including process control, robotics, and avionics.
2. These systems are characterized by their ability to provide timely and accurate responses to external events.
3. Real-time systems can be classified into two categories: hard real-time systems and soft real-time systems.
4. Hard real-time systems have strict deadlines, and failure to meet these deadlines can result in catastrophic consequences.
5. Soft real-time systems, on the other hand, have more flexible deadlines, and failure to meet these deadlines may result in degraded system performance, but not catastrophic consequences.
6. The design of real-time systems requires careful consideration of the system's timing requirements, as well as the use of specialized hardware and software to ensure that these requirements are met.
7. Real-time operating systems (RTOS) are commonly used in the development of real-time systems, as they provide features such as preemptive scheduling and inter-process communication that are essential for meeting the system's timing requirements.



### Unit 1 - Introduction of Real Time System

#### Definition

A real-time system is a computer system that is designed to process data and provide output within a specific time frame. This time frame is determined by the requirements of the system and is often referred to as the system's deadline. Real-time systems are used in a variety of applications, including process control, aviation, and telecommunications.

Some key characteristics of real-time systems include:
- The system must provide a guaranteed response time to events or inputs.
- The system must be able to handle multiple tasks or processes concurrently.
- The system must be able to prioritize tasks based on their importance and deadlines.
- The system must be able to recover from failures quickly and continue to operate.

Real-time systems can be classified into two types: hard real-time systems and soft real-time systems. Hard real-time systems have strict deadlines and missing a deadline can result in catastrophic consequences. Soft real-time systems, on the other hand, have more flexible deadlines and missing a deadline may result in degraded performance but not catastrophic consequences.



### Typical Real Time Applications

Real-time systems are computer systems that monitor, respond to, or control an external environment. These systems are subject to a real-time constraint, which means that they must respond to events within a certain time frame. Here are some typical real-time applications:

1. **Industrial control systems:** These systems are used to control industrial processes such as manufacturing, chemical processing, and power generation. They must respond quickly to changes in the environment to maintain safe and efficient operation.

2. **Avionics systems:** These systems are used in aircraft to control flight, navigation, and communication. They must respond quickly to changes in the environment to ensure the safety of the aircraft and its passengers.

3. **Medical systems:** These systems are used in hospitals and clinics to monitor and treat patients. They must respond quickly to changes in the patient's condition to provide effective treatment.

4. **Telecommunications systems:** These systems are used to transmit and receive data over communication networks. They must respond quickly to changes in the network to maintain reliable communication.

5. **Multimedia systems:** These systems are used to process and display multimedia content such as video and audio. They must respond quickly to user input to provide a smooth and responsive user experience.

6. **Defense systems:** These systems are used by the military to monitor and respond to threats. They must respond quickly to changes in the environment to protect national security.

7. **Financial systems:** These systems are used by banks and financial institutions to process transactions and manage accounts. They must respond quickly to changes in the market to provide accurate and timely financial services.

These are just a few examples of the many real-time applications that exist. Real-time systems are essential for the safe and efficient operation of many critical systems in our society.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Release times refer to the specific times at which the notes for Unit 1 - Introduction of Real Time System in the subject of Real Time System will be made available to students.
- These release times may vary depending on the institution, course, and instructor.
- It is important for students to be aware of the release times for the notes in order to plan their study schedule accordingly.
- Students can typically find information about the release times for the notes on their course syllabus or by contacting their instructor.
- It is recommended that students regularly check for updates on the release times for the notes to ensure that they have the most up-to-date information.




### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A deadline is a specific time or date by which a task must be completed.
- In the context of Real Time Systems, deadlines are critical as they determine the usefulness of the system's output.
- Missing a deadline in a Real Time System can result in a failure of the system, and in some cases, can have catastrophic consequences.
- There are two types of deadlines in Real Time Systems: hard and soft.
- A hard deadline is one that must be met, otherwise the system will fail.
- A soft deadline is one that can be missed, but the usefulness of the system's output decreases as the deadline is missed by a greater amount.
- It is important to properly manage and schedule tasks in a Real Time System to ensure that all deadlines are met.
- This can be achieved through the use of scheduling algorithms and priority assignment.
- The study of Real Time Systems and their deadlines is an important topic in the field of computer science and engineering.



### Timing Constraints

Timing constraints are a crucial aspect of real-time systems. These constraints specify the time limits within which a task must be completed. There are two types of timing constraints: hard and soft.

1. **Hard timing constraints**: These constraints must be met for the system to function correctly. Failure to meet a hard timing constraint can result in catastrophic consequences, such as loss of life or damage to equipment. For example, in a nuclear power plant, the control system must respond to changes in reactor conditions within a certain time frame to prevent a meltdown.

2. **Soft timing constraints**: These constraints are less critical, and failure to meet them may result in degraded system performance, but not catastrophic consequences. For example, in a multimedia system, a delay in the delivery of audio or video data may result in a temporary loss of synchronization between the audio and video streams, but the system will continue to function.

In summary, timing constraints are an essential part of real-time systems, and the system must be designed to meet these constraints to ensure correct operation. Hard timing constraints are critical and must be met, while soft timing constraints are less critical and may result in degraded performance if not met.



### Hard Real Time Systems

- Hard real-time systems are systems in which the correctness of the system depends not only on the logical result of the computation, but also on the time at which the results are produced.
- In hard real-time systems, missing a deadline is considered a system failure.
- These systems are often used in safety-critical applications, where the failure to meet a deadline can result in serious consequences, such as loss of life or damage to equipment.
- Examples of hard real-time systems include air traffic control systems, nuclear power plant control systems, and medical equipment.
- Hard real-time systems require rigorous testing and verification to ensure that they meet their deadlines under all possible conditions.
- The design of hard real-time systems often involves the use of specialized scheduling algorithms and hardware to ensure that tasks are completed on time.



### Soft Real Time Systems

Soft real-time systems are systems where the completion of tasks after their deadlines is still useful, but may result in degraded system performance. In these systems, the consequences of missing a deadline are not catastrophic, but can still impact the overall performance of the system.

Some key points to note about soft real-time systems are:

1. Soft real-time systems have a more flexible approach to task scheduling compared to hard real-time systems.
2. The consequences of missing a deadline in a soft real-time system are not catastrophic, but can still impact the overall performance of the system.
3. Soft real-time systems are often used in applications where the timely delivery of data is important, but not critical.
4. Examples of soft real-time systems include multimedia streaming, online gaming, and virtual reality applications.

In summary, soft real-time systems are systems where the timely completion of tasks is important, but not critical. These systems have a more flexible approach to task scheduling and can still function effectively even if some deadlines are missed. However, missing deadlines can still impact the overall performance of the system.



### Reference Models for Real Time Systems

Real-time systems are computer systems that are designed to interact with the external environment in a timely manner. These systems are used in a variety of applications, including control systems, multimedia systems, and communication systems. To ensure that real-time systems meet their timing requirements, several reference models have been developed. These models provide a framework for the design and analysis of real-time systems.

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-based scheduling algorithm for periodic tasks. In this model, tasks are assigned priorities based on their periods, with shorter periods being assigned higher priorities. RMS is an optimal scheduling algorithm for periodic tasks with fixed priorities.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm for periodic and aperiodic tasks. In this model, tasks are assigned priorities based on their deadlines, with earlier deadlines being assigned higher priorities. EDF is an optimal scheduling algorithm for periodic and aperiodic tasks with dynamic priorities.

3. **Sporadic Server**: This model is used to schedule aperiodic tasks in a system with periodic tasks. In this model, a server task is created to handle the execution of aperiodic tasks. The server task is assigned a fixed priority and a fixed budget of execution time. When an aperiodic task arrives, it is executed by the server task until its budget is exhausted.

4. **Constant Bandwidth Server (CBS)**: This is an extension of the sporadic server model. In this model, the server task is assigned a variable priority and a variable budget of execution time. The priority and budget of the server task are adjusted dynamically based on the workload of the system.

These are some of the reference models used in the design and analysis of real-time systems. These models provide a framework for ensuring that real-time systems meet their timing requirements. It is important to choose the appropriate reference model for the specific application and workload of the system.



### Processors and Resources

In the context of Real Time Systems, processors and resources are essential components that enable the system to function and meet its real-time constraints.

1. **Processors**: A processor is the hardware component that executes instructions and performs computations. In a real-time system, the processor must be able to execute tasks within their specified deadlines to ensure the system meets its real-time constraints.

2. **Resources**: Resources refer to any hardware or software component that is required for the execution of a task. This can include memory, storage, input/output devices, and network connections. In a real-time system, resources must be managed effectively to ensure that tasks have access to the resources they need to execute within their specified deadlines.

Effective management of processors and resources is critical to the successful operation of a real-time system. This involves scheduling tasks and allocating resources in a way that ensures all tasks can be executed within their specified deadlines. Failure to do so can result in missed deadlines and degraded system performance.



### Temporal Parameters of Real Time Workload

Real-time systems are computer systems that are required to respond to events within a specific time frame. The temporal parameters of a real-time workload refer to the timing constraints that must be met by the system in order to function correctly. These parameters include:

1. **Release time**: The time at which a task becomes ready for execution.
2. **Deadline**: The time by which a task must complete its execution.
3. **Period**: The time interval between consecutive releases of a periodic task.
4. **Execution time**: The time required for a task to complete its execution once it starts.
5. **Response time**: The time interval between the release of a task and the completion of its execution.

These temporal parameters are critical in the design and analysis of real-time systems, as they determine the system's ability to meet its timing constraints and provide the desired level of performance. Failure to meet these constraints can result in system failure or degraded performance. Therefore, it is important to carefully consider these parameters when designing and implementing real-time systems.



### Periodic Task Model

The periodic task model is a commonly used model in real-time systems. In this model, tasks are executed periodically at regular intervals. Each task has a fixed period, which is the time between two consecutive executions of the task. The following are some key points to note about the periodic task model:

1. **Period**: The period of a task is the time between two consecutive executions of the task. It is a fixed value for each task.

2. **Deadline**: The deadline of a task is the time by which the task must complete its execution. In the periodic task model, the deadline is usually equal to the period of the task.

3. **Utilization**: The utilization of a task is the ratio of its execution time to its period. The total utilization of the system is the sum of the utilizations of all tasks.

4. **Schedulability**: A set of periodic tasks is schedulable if there exists a schedule that ensures that all tasks meet their deadlines. There are several schedulability tests that can be used to determine if a set of tasks is schedulable.

5. **Priority**: In many real-time systems, tasks are assigned priorities based on their periods or deadlines. Tasks with shorter periods or earlier deadlines are usually assigned higher priorities.

The periodic task model is widely used in real-time systems because it provides a simple and predictable way to schedule tasks. However, it may not be suitable for all types of real-time systems, especially those with highly dynamic workloads. In such cases, other task models, such as the sporadic task model or the aperiodic task model, may be more appropriate.



### Precedence Constraints and Data Dependency

Precedence constraints and data dependency are important concepts in the study of real-time systems. These concepts are related to the order in which tasks are executed and the flow of data between them.

1. **Precedence Constraints:** Precedence constraints define the order in which tasks must be executed. For example, in a real-time system, a task that processes sensor data may need to be executed before a task that uses the processed data to control an actuator. Precedence constraints can be represented using a directed acyclic graph (DAG), where the nodes represent tasks and the edges represent the precedence constraints between them.

2. **Data Dependency:** Data dependency refers to the flow of data between tasks. A task may require data from another task to be able to execute correctly. For example, in a real-time system, a task that controls an actuator may require data from a task that processes sensor data. Data dependency can be represented using a data flow graph, where the nodes represent tasks and the edges represent the flow of data between them.

Understanding precedence constraints and data dependency is important for the design and analysis of real-time systems. These concepts can help to ensure that tasks are executed in the correct order and that data is available when it is needed.



## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning system resources to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines while optimizing system performance.

1. **Hard Real-Time Systems**: In hard real-time systems, missing a deadline can result in catastrophic consequences. Therefore, the scheduling algorithm must guarantee that all tasks meet their deadlines.

2. **Soft Real-Time Systems**: In soft real-time systems, missing a deadline is undesirable but not catastrophic. The scheduling algorithm tries to ensure that all tasks meet their deadlines, but it is not guaranteed.

3. **Rate Monotonic Scheduling (RMS)**: RMS is a priority-based scheduling algorithm for periodic tasks in hard real-time systems. The priority of a task is inversely proportional to its period, i.e., the shorter the period, the higher the priority.

4. **Earliest Deadline First (EDF)**: EDF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is determined by its absolute deadline, i.e., the earlier the deadline, the higher the priority.

5. **Least Laxity First (LLF)**: LLF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is determined by its laxity, i.e., the difference between its deadline and its remaining computation time. The smaller the laxity, the higher the priority.

6. **Scheduling in Multiprocessor Systems**: Real-time scheduling in multiprocessor systems is more complex than in single-processor systems. Some common approaches include partitioned scheduling, global scheduling, and hybrid scheduling.



### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of assigning priorities to tasks in a real-time system to ensure that they meet their deadlines. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline, the higher the priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the difference between its deadline and its remaining computation time. The smaller the laxity, the higher the priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priorities of tasks are assigned based on their importance or criticality. The more important or critical the task, the higher the priority.

These are some of the common approaches to real-time scheduling. Each approach has its advantages and disadvantages, and the choice of approach depends on the specific requirements of the real-time system.



### Clock Driven Approach

The clock-driven approach is a scheduling method used in real-time systems. It is also known as time-driven or table-driven scheduling. In this approach, the scheduler uses a pre-computed schedule or a table to determine when tasks should be executed. The schedule is computed offline, before the system starts executing, and is based on the worst-case execution times of the tasks, their deadlines, and their periods.

The main characteristics of the clock-driven approach are:

1. The schedule is computed offline, before the system starts executing.
2. The schedule is based on the worst-case execution times of the tasks, their deadlines, and their periods.
3. The scheduler uses a pre-computed schedule or a table to determine when tasks should be executed.
4. The clock-driven approach is suitable for systems with periodic tasks and fixed task sets.

The clock-driven approach has several advantages, including:

1. The schedule is computed offline, which reduces the runtime overhead.
2. The schedule is guaranteed to meet the deadlines of all tasks, as long as the worst-case execution times are accurate.
3. The clock-driven approach is suitable for systems with periodic tasks and fixed task sets.

However, the clock-driven approach also has some disadvantages, including:

1. The schedule is computed offline, which means that it cannot adapt to changes in the system at runtime.
2. The schedule is based on the worst-case execution times of the tasks, which can result in low CPU utilization if the actual execution times are shorter than the worst-case execution times.
3. The clock-driven approach is not suitable for systems with aperiodic or sporadic tasks, or for systems with dynamic task sets.

Overall, the clock-driven approach is a useful scheduling method for real-time systems with periodic tasks and fixed task sets. However, it may not be suitable for all real-time systems, and its effectiveness depends on the accuracy of the worst-case execution times of the tasks.



### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight that determines the length of its time slice.

Here are the key points to note about the Weighted Round Robin approach:

1. In WRR, tasks are assigned a weight, which determines the length of their time slice. The higher the weight, the longer the time slice.
2. The scheduler assigns time slices to tasks in a round-robin fashion, but the length of each time slice is determined by the task's weight.
3. WRR can be used to provide differentiated service levels to tasks, by assigning higher weights to higher priority tasks.
4. WRR is simple to implement and can provide fair scheduling for tasks with different processing requirements.
5. However, WRR may not be suitable for all real-time systems, as it does not take into account the deadlines of tasks.

In summary, the Weighted Round Robin approach is a simple and fair scheduling algorithm that can provide differentiated service levels to tasks in a real-time system. However, it may not be suitable for all real-time systems, as it does not take into account the deadlines of tasks.



### Priority Driven Approach

Priority driven approach is a scheduling method used in real-time systems. In this approach, tasks are assigned priorities based on their importance and urgency. The scheduler then selects the highest priority task to execute at any given time.

Some key points to note about priority driven approach are:

1. Priorities can be assigned statically or dynamically. Static priorities are assigned at design time and do not change during the execution of the system. Dynamic priorities, on the other hand, can change during the execution of the system based on various factors such as deadlines, resource availability, etc.

2. Priority driven approach can be preemptive or non-preemptive. In preemptive scheduling, a higher priority task can interrupt the execution of a lower priority task. In non-preemptive scheduling, a task once started, must run to completion before another task can be scheduled.

3. Priority inversion is a problem that can occur in priority driven approach. It happens when a low priority task holds a resource that is required by a higher priority task. This can cause the higher priority task to be blocked and miss its deadline.

4. Priority inheritance and priority ceiling protocols are two methods used to solve the priority inversion problem.

5. Priority driven approach is widely used in real-time systems due to its simplicity and effectiveness in meeting deadlines.




### Dynamic Versus Static Systems

- **Dynamic systems** are systems that change over time, while **static systems** remain constant.
- In the context of real-time scheduling, dynamic systems refer to systems where the scheduling decisions are made at runtime, based on the current state of the system.
- In contrast, static systems refer to systems where the scheduling decisions are made offline, before the system starts executing.
- Dynamic scheduling algorithms are more flexible and can adapt to changes in the system, such as varying workload or resource availability.
- Static scheduling algorithms, on the other hand, are more predictable and easier to analyze, since the scheduling decisions are made in advance.
- The choice between dynamic and static scheduling depends on the specific requirements of the system, such as the need for flexibility, predictability, and ease of analysis.
- Some common dynamic scheduling algorithms used in real-time systems include Earliest Deadline First (EDF) and Least Laxity First (LLF).
- Some common static scheduling algorithms used in real-time systems include Rate Monotonic (RM) and Deadline Monotonic (DM).



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two algorithms used in real-time scheduling. These algorithms are used to schedule tasks in a way that ensures that all tasks meet their deadlines.

1. **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest deadline is scheduled first. EDF is an optimal algorithm for scheduling tasks on a single processor, meaning that if a feasible schedule exists, EDF will find it.

2. **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time, which is the amount of time remaining until the task's deadline minus the task's remaining execution time. The task with the least slack time is scheduled first. LST is also an optimal algorithm for scheduling tasks on a single processor.

In summary, both EDF and LST are optimal algorithms for scheduling tasks on a single processor in a real-time system. They ensure that all tasks meet their deadlines if a feasible schedule exists. These algorithms are commonly used in real-time scheduling and are important concepts in the study of real-time systems.



### Rate Monotonic Algorithm

Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time scheduling. It is a part of Unit 2 - Real Time Scheduling in the subject of Real Time System. Here are some key points to note about RMA:

1. RMA is an optimal static priority scheduling algorithm for periodic tasks.
2. In RMA, the task with the shortest period is assigned the highest priority.
3. RMA is suitable for hard real-time systems where missing a deadline can have severe consequences.
4. The schedulability of a task set under RMA can be determined using Liu and Layland's utilization bound or by performing a response time analysis.
5. RMA has been shown to be effective in practice and is widely used in real-time systems.




### Offline Versus Online Scheduling

- **Offline scheduling** refers to the process of determining a schedule for a set of tasks before the system starts executing them. This type of scheduling is also known as **static scheduling**.
- In contrast, **online scheduling** refers to the process of making scheduling decisions during the execution of the system. This type of scheduling is also known as **dynamic scheduling**.
- Offline scheduling is typically used in systems where the set of tasks and their characteristics are known in advance. The schedule can be computed beforehand and is then followed during the execution of the system.
- Online scheduling is used in systems where the set of tasks or their characteristics are not known in advance, or where the system needs to respond to changing conditions. The scheduler makes decisions on-the-fly based on the current state of the system.
- Offline scheduling can result in more efficient schedules, as the scheduler has complete information about the tasks and can take the time to compute an optimal schedule. However, it is not suitable for systems where the set of tasks or their characteristics are not known in advance, or where the system needs to respond to changing conditions.
- Online scheduling is more flexible, as the scheduler can respond to changing conditions and make decisions based on the current state of the system. However, it may result in less efficient schedules, as the scheduler has less information and less time to make decisions.
- In the context of real-time systems, offline scheduling is typically used for **hard real-time systems**, where the set of tasks and their characteristics are known in advance and the system must meet strict timing constraints. Online scheduling is typically used for **soft real-time systems**, where the system must respond to changing conditions and the timing constraints are more relaxed.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are tasks that do not have a regular arrival pattern and can arrive at any time.
- Sporadic jobs are tasks that have a minimum inter-arrival time between consecutive jobs.
- In priority-driven systems, tasks are assigned priorities and the scheduler selects the highest priority task to execute.
- In clock-driven systems, the scheduler uses a pre-computed schedule to determine which task to execute at a given time.
- Aperiodic and sporadic jobs can be scheduled in priority-driven systems using techniques such as slack stealing, where the scheduler uses the slack time of lower priority tasks to schedule aperiodic or sporadic jobs.
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using techniques such as sporadic servers, where a server task is assigned to handle aperiodic or sporadic jobs and is scheduled according to the pre-computed schedule.
- These techniques allow for the efficient scheduling of aperiodic and sporadic jobs in real-time systems while ensuring that the timing constraints of all tasks are met.



## Unit 3 - Resources Sharing

1. Resource sharing refers to the sharing of resources among multiple users or systems.
2. This can include sharing of hardware, software, data, and information.
3. Resource sharing can improve efficiency and reduce costs by allowing multiple users to access the same resources.
4. Examples of resource sharing include file sharing, printer sharing, and internet sharing.
5. Resource sharing can be implemented through various methods, such as networking, virtualization, and cloud computing.
6. Security and access control are important considerations when implementing resource sharing.
7. Resource sharing can also facilitate collaboration and cooperation among users or systems.
8. Proper management and allocation of shared resources is crucial to ensure fair and efficient use.




### Effect of Resource Contention and Resource Access Control (RAC)

- A resource access-control protocol, or simply an access-control protocol, is a set of rules that govern (1) when and under what conditions each request for resource is granted and (2) how jobs requiring resources are scheduled.
- Resource contention often leads to performance degradation in the applications contending for the shared resource. This can cause unexpected project delays, because processes contending for resources will be stalled until they can access the resource.
- Resource Access Control Protocols work to reduce the undesirable effect of resource contention. Resource contention affects the execution behavior and schedulability of jobs.
- One of the major objectives of resources access control is to minimize the undesirable effects of resource allocation.
- Access to resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section. If a lock request fails, the requesting job is blocked; a job holding a lock cannot be preempted by a higher priority job needing that lock.



### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, regardless of the priority of other tasks.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- To implement non-preemptive critical sections, a task must first acquire a lock before entering the critical section. This lock ensures that no other task can enter the critical section until the current task releases the lock.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms such as semaphores, mutexes, and spinlocks.
- It is important to use non-preemptive critical sections carefully, as they can lead to priority inversion and deadlock if not used correctly.
- Priority inversion occurs when a high-priority task is blocked by a lower-priority task that is executing in a non-preemptive critical section.
- Deadlock occurs when two or more tasks are blocked, waiting for each other to release a lock.
- To avoid these issues, it is important to follow best practices when using non-preemptive critical sections, such as avoiding nested critical sections and ensuring that locks are always released in the same order they were acquired.



### Basic Priority-Inheritance and Priority-Ceiling Protocols for Resources Sharing in Real Time System

- **Priority inheritance protocol** and **priority ceiling protocol** are two protocols belonging to the priority inheritance protocols class.
- Both protocols solve the uncontrolled priority inversion problem.
- The priority ceiling protocol solves this uncontrolled priority inversion problem particularly well; it reduces the worst-case task-blocking time to at most the duration of execution of a single critical section of a lower-priority task.
- This protocol also prevents the formation of deadlocks.
- Sufficient conditions under which a set of periodic tasks using this protocol may be scheduled is derived.
- Priority Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways.
- Real-Time Systems are multitasking systems that involve the use of semaphore variables, signals, and events for job synchronization.
- In real-time computing, the priority ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority Inheritance protocols are greedy while Priority Ceiling protocols are not.
- The allocation rule of priority inheritance protocol lets the requesting job have a resource whenever the resource is free but in case of priority ceiling protocol, a job may be denied its requested resource even when the resource is free at the time.



### Stack Based Priority-Ceiling Protocol

Stack Based Priority-Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion, which occurs when a high priority task is blocked by a lower priority task that is holding a shared resource.

Here are some key points to note about the Stack Based Priority-Ceiling Protocol:

1. Each shared resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the priority ceilings of all resources currently locked by other tasks.
3. When a task locks a resource, its priority is temporarily raised to the priority ceiling of the resource.
4. When a task releases a resource, its priority is restored to its original value.

This protocol ensures that a high priority task will not be blocked by a lower priority task holding a shared resource for an extended period of time. It also prevents deadlocks by ensuring that tasks can only lock resources in a specific order.




### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that may lock the resource.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The protocol specifies a dynamic priority ceiling for each critical section which is the earliest deadline of jobs which are currently in or will enter the critical section. Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section which is in use .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP) .




### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by lower priority tasks.

Here are some key points to note about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling.
3. When a task locks a resource, the preemption ceiling is raised to the ceiling of the locked resource.
4. When a task releases a resource, the preemption ceiling is lowered to the highest ceiling of all resources still locked by the task.
5. A task can be preempted only by tasks with priority higher than the current preemption ceiling.

This protocol ensures that high priority tasks are not blocked by lower priority tasks and prevents priority inversion. It also ensures that tasks do not experience unbounded blocking, as the maximum blocking time is limited by the highest preemption ceiling of all resources that the task may lock.



### Access Control in Multiple-Unit Resources

1. Access control is a mechanism that ensures that only authorized users have access to shared resources.
2. In the context of multiple-unit resources, access control is used to manage the allocation of multiple units of a resource to different users or processes.
3. One approach to access control in multiple-unit resources is to use a resource allocation algorithm that takes into account the priorities of the users or processes requesting the resource.
4. Another approach is to use a reservation system, where users or processes can reserve a certain number of units of the resource for a specific period of time.
5. Access control can also be implemented using access control lists (ACLs), which specify the users or processes that are allowed to access the resource and the level of access they have.
6. It is important to ensure that access control mechanisms are properly implemented and maintained to prevent unauthorized access to shared resources.



### Controlling Concurrent Accesses to Data Objects

In a real-time system, multiple tasks may need to access shared data objects concurrently. To ensure the correctness and consistency of the data, it is necessary to control the concurrent accesses to these data objects. Here are some key points to consider when controlling concurrent accesses to data objects in a real-time system:

1. **Mutual Exclusion**: Mutual exclusion is a mechanism that ensures that only one task can access a shared data object at a time. This can be achieved through the use of locks, semaphores, or monitors.

2. **Deadlock Prevention**: Deadlock is a situation where two or more tasks are blocked, waiting for each other to release resources. Deadlock prevention techniques, such as resource ordering or the banker's algorithm, can be used to prevent deadlock from occurring.

3. **Priority Inversion**: Priority inversion is a situation where a high-priority task is blocked by a lower-priority task that holds a lock on a shared resource. Priority inheritance or priority ceiling protocols can be used to prevent priority inversion.

4. **Real-Time Scheduling**: Real-time scheduling algorithms, such as rate-monotonic or earliest-deadline-first, can be used to schedule tasks in a way that ensures that all tasks meet their deadlines while accessing shared resources.

By considering these points and implementing appropriate mechanisms, it is possible to control concurrent accesses to data objects in a real-time system and ensure the correctness and consistency of the data.



## Unit 4 - Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. This type of communication is essential for many applications, including video conferencing, online gaming, and remote control systems.

1. **Protocols**: Real-time communication relies on specific protocols to ensure that data is transmitted quickly and reliably. Some common protocols used for real-time communication include RTP (Real-time Transport Protocol), RTCP (Real-time Transport Control Protocol), and SIP (Session Initiation Protocol).

2. **Latency**: Latency is the time it takes for a signal to travel from the sender to the receiver. In real-time communication, low latency is crucial to ensure that the communication feels natural and responsive.

3. **Quality of Service (QoS)**: QoS refers to the ability of a network to provide improved service to certain network traffic. This is important in real-time communication, as it helps to ensure that the communication is not disrupted by other network traffic.

4. **Bandwidth**: Bandwidth is the amount of data that can be transmitted over a network in a given period of time. Adequate bandwidth is essential for real-time communication, as it ensures that the data can be transmitted quickly and without interruption.

5. **Security**: Security is an important consideration in real-time communication, as the data being transmitted may be sensitive or confidential. Encryption and authentication are commonly used to secure real-time communication.




### Basic Concepts in Real time Communication

Real-time communication (RTC) refers to any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real-time communication include:
- Voice over landlines and mobile phones
- Video conferencing
- Instant messaging
- Online gaming

Real-time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the transfer.

Real-time communication is essential in many fields, including business, healthcare, and emergency services, where quick and reliable communication is critical.



### Soft and Hard RT Communication systems

Real-time communication systems can be classified into two categories: soft real-time and hard real-time.

1. **Soft real-time communication systems** are those in which the occasional delay or loss of data is acceptable. These systems are designed to handle a certain level of delay or data loss without significantly impacting the overall performance of the system. Examples of soft real-time communication systems include video streaming and online gaming.

2. **Hard real-time communication systems** are those in which any delay or loss of data is unacceptable. These systems are designed to ensure that data is delivered within a strict time frame, and any delay or loss of data can have serious consequences. Examples of hard real-time communication systems include control systems for nuclear power plants and air traffic control systems.

In summary, the main difference between soft and hard real-time communication systems is the level of tolerance for delay or data loss. Soft real-time systems can tolerate some delay or data loss, while hard real-time systems cannot. It is important to choose the appropriate type of real-time communication system for the specific application to ensure optimal performance.



### Model of Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. In the context of real-time systems, this communication must occur within a specified time frame to ensure the correct functioning of the system. Here are some key points to consider when discussing the model of real-time communication:

1. **Timing constraints:** Real-time communication must adhere to strict timing constraints to ensure that the system functions correctly. This means that messages must be delivered within a specified time frame, and any delays could result in system failure.

2. **Reliability:** The communication between parties must be reliable to ensure that messages are delivered correctly and without error. This can be achieved through the use of error detection and correction techniques, as well as the use of redundant communication channels.

3. **Synchronization:** In many real-time systems, it is important for the parties involved in the communication to be synchronized. This means that they must operate on the same time scale and be able to coordinate their actions.

4. **Protocols:** Real-time communication often relies on the use of specific protocols to ensure that the communication is carried out correctly. These protocols define the rules and procedures for exchanging information between parties.

5. **Network topology:** The topology of the network used for real-time communication can have a significant impact on the performance of the system. Factors such as the number of nodes, the distance between nodes, and the routing of messages can all affect the speed and reliability of the communication.

Overall, the model of real-time communication must take into account the specific requirements of the system in question, including timing constraints, reliability, synchronization, protocols, and network topology. By carefully considering these factors, it is possible to design a communication model that meets the needs of the real-time system.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

#### Priority-Based Service
- In a priority-based service discipline, packets are assigned a priority level based on their importance.
- Packets with higher priority levels are transmitted before packets with lower priority levels.
- This service discipline is useful in situations where some packets are more important than others, such as in real-time communication or emergency situations.

#### Weighted Round-Robin Service
- In a weighted round-robin service discipline, packets are assigned a weight based on their importance.
- The weight determines the number of times a packet is transmitted in a round-robin cycle.
- This service discipline is useful in situations where all packets are important, but some packets are more important than others.
- It provides a fair distribution of bandwidth among all packets while still giving priority to more important packets.

These service disciplines are commonly used in switched networks to ensure efficient and fair distribution of bandwidth among all packets. They are particularly useful in real-time communication, where timely delivery of packets is critical.



### Medium Access Control Protocols for Broadcast Networks

Medium Access Control (MAC) protocols are responsible for controlling access to a shared communication medium in broadcast networks. These protocols are essential for ensuring that data transmissions from different network nodes do not interfere with each other. Some of the key MAC protocols for broadcast networks include:

1. **Carrier Sense Multiple Access (CSMA):** This protocol is based on the principle of listening before transmitting. Nodes using CSMA will first check if the communication channel is free before attempting to transmit data. If the channel is busy, the node will wait for a random period of time before trying again.

2. **Collision Avoidance (CA):** This protocol is an extension of CSMA and is designed to further reduce the likelihood of collisions. In CA, nodes will transmit a short message, known as a Request to Send (RTS), before transmitting their data. If another node receives the RTS and is also ready to transmit, it will send a Clear to Send (CTS) message, indicating that the channel is free.

3. **Time Division Multiple Access (TDMA):** In TDMA, the communication channel is divided into time slots, with each node being assigned a specific time slot for transmission. This ensures that only one node is transmitting at any given time, eliminating the possibility of collisions.

4. **Frequency Division Multiple Access (FDMA):** Similar to TDMA, FDMA divides the communication channel into multiple frequency bands, with each node being assigned a specific frequency band for transmission. This also ensures that only one node is transmitting at any given time.

These are some of the key MAC protocols used in broadcast networks to ensure efficient and reliable communication. Each protocol has its own strengths and weaknesses, and the choice of protocol will depend on the specific requirements of the network.



### Unit 4 - Real Time Communication: Internet and Resource Reservation Protocols

- **Internet Protocol (IP)**: The Internet Protocol is responsible for routing data packets across a network. It is a connectionless protocol, meaning that it does not establish a dedicated end-to-end connection before transmitting data.

- **Resource Reservation Protocol (RSVP)**: RSVP is a signaling protocol used to reserve resources across a network for an integrated services Internet. It operates over an IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.

- **Real-time Transport Protocol (RTP)**: RTP is a protocol used for delivering audio and video over IP networks. It is used in conjunction with the Real-time Transport Control Protocol (RTCP) to provide end-to-end delivery services for data with real-time characteristics.

- **Real-time Streaming Protocol (RTSP)**: RTSP is a network control protocol used for controlling streaming media servers. It is used to establish and control media sessions between endpoints.

- **Session Initiation Protocol (SIP)**: SIP is a signaling protocol used for initiating, maintaining, modifying, and terminating real-time sessions that involve video, voice, messaging, and other communications applications and services between two or more endpoints on IP networks.




## Unit 5 - Real Time Operating Systems and Databases

Real-time operating systems (RTOS) and databases are essential components of many modern systems, including embedded systems, control systems, and data acquisition systems.

1. **Real-time operating systems (RTOS)** are designed to provide predictable and deterministic response times to events, allowing for the execution of time-critical tasks. RTOSs are commonly used in systems where timing is critical, such as in control systems, medical devices, and avionics.

2. **Real-time databases** are databases that are designed to handle real-time data, such as sensor data, stock market data, and other time-sensitive data. Real-time databases are optimized for fast data retrieval and processing, and are commonly used in systems where data must be processed quickly, such as in financial systems, control systems, and data acquisition systems.

3. **Key characteristics of RTOS** include pre-emptive multitasking, priority-based scheduling, and fast context switching. These features allow the RTOS to quickly respond to events and ensure that high-priority tasks are executed in a timely manner.

4. **Key characteristics of real-time databases** include fast data retrieval and processing, support for real-time data, and the ability to handle large volumes of data. Real-time databases are optimized for performance and are designed to provide fast access to data.

5. **Examples of RTOS** include VxWorks, QNX, and FreeRTOS. These operating systems are commonly used in embedded systems and other systems where timing is critical.

6. **Examples of real-time databases** include Oracle TimesTen, IBM Informix, and SAP HANA. These databases are commonly used in financial systems, control systems, and data acquisition systems.

7. **Applications of RTOS and real-time databases** include control systems, medical devices, avionics, financial systems, and data acquisition systems. These systems require fast and predictable response times, and the use of RTOS and real-time databases can help to ensure that these requirements are met.



### Features of RTOS

Real-time operating systems (RTOS) are designed to provide predictable and deterministic execution of tasks in real-time applications. Some of the key features of RTOS include:

1. **Deterministic behavior**: RTOS provides deterministic behavior, meaning that the system responds to events within a known and predictable time frame.

2. **Preemptive scheduling**: RTOS uses preemptive scheduling, which allows high-priority tasks to interrupt lower-priority tasks to ensure that critical tasks are completed on time.

3. **Fast context switching**: RTOS is designed to have fast context switching, which allows the system to quickly switch between tasks, reducing the overhead of task switching.

4. **Small memory footprint**: RTOS is designed to have a small memory footprint, which allows it to be used in resource-constrained environments.

5. **Real-time clock**: RTOS includes a real-time clock, which provides accurate timekeeping and can be used to schedule tasks.

6. **Inter-task communication**: RTOS provides mechanisms for inter-task communication, such as message queues, semaphores, and mutexes, which allow tasks to communicate and synchronize with each other.

7. **Interrupt handling**: RTOS provides efficient interrupt handling, which allows the system to quickly respond to external events.

These are some of the key features of RTOS that make it suitable for use in real-time applications. These features help ensure that the system can meet the timing requirements of the application and provide predictable and reliable behavior.



### Time Services

Time services are an essential component of real-time operating systems and databases. These services provide the ability to measure, represent, and manage time within the system. Some of the key features of time services include:

1. **Clock synchronization:** This refers to the process of synchronizing the clocks of different nodes in a distributed system to ensure that they all have the same notion of time. This is important for coordinating the execution of tasks across the system.

2. **Time representation:** Time services provide a way to represent time within the system. This can include the use of timestamps, time intervals, and other time-related data structures.

3. **Time management:** Time services provide mechanisms for managing time within the system. This can include the ability to set timers, schedule tasks, and perform other time-related operations.

4. **Time-related APIs:** Time services provide APIs that allow applications to interact with the time-related features of the system. This can include functions for getting the current time, setting timers, and performing other time-related operations.

Overall, time services play a critical role in ensuring the correct and timely execution of tasks in real-time operating systems and databases. They provide the foundation for many of the key features of these systems, including scheduling, synchronization, and fault tolerance.



### UNIX as RTOS

- UNIX is a multi-user, multi-tasking operating system that was originally developed in the late 1960s.
- It is widely used in both academic and commercial environments.
- UNIX is known for its stability, security, and flexibility.
- As a real-time operating system (RTOS), UNIX can provide guaranteed response times for critical tasks.
- This is achieved through the use of real-time scheduling algorithms and the ability to prioritize processes.
- UNIX also supports real-time inter-process communication, allowing for efficient data exchange between processes.
- These features make UNIX a suitable choice for real-time applications, such as control systems and data acquisition systems.
- Additionally, UNIX has a large and active development community, providing a wealth of resources and support for real-time development.




### POSIX Issues

POSIX (Portable Operating System Interface) is a set of standards that define how operating systems should behave. These standards are designed to ensure compatibility between different operating systems. However, there are several issues that arise when implementing POSIX standards in real-time operating systems and databases.

1. **Timing Constraints:** Real-time systems have strict timing constraints that must be met in order to function correctly. However, POSIX standards do not provide any guarantees for meeting these timing constraints. This can lead to issues when trying to implement real-time systems using POSIX-compliant operating systems.

2. **Scheduling:** POSIX standards do not specify any particular scheduling algorithm for real-time systems. This means that the scheduling algorithm used by a POSIX-compliant operating system may not be suitable for real-time applications.

3. **Priority Inversion:** Priority inversion is a problem that can occur in real-time systems when a low-priority task holds a resource that is needed by a high-priority task. POSIX standards do not provide any mechanisms for preventing or mitigating priority inversion.

4. **Memory Management:** Real-time systems often have strict memory requirements, and the memory management techniques used by POSIX-compliant operating systems may not be suitable for real-time applications.

5. **Interrupt Handling:** Real-time systems often rely on interrupts to respond to external events in a timely manner. However, the interrupt handling mechanisms provided by POSIX standards may not be suitable for real-time systems.

These are some of the issues that arise when implementing POSIX standards in real-time operating systems and databases. It is important to carefully consider these issues when designing and implementing real-time systems.



### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

Temporal data refers to data that represents the state of an entity at a particular point in time. It is used to track changes in data over time and is commonly used in real-time systems and databases. The following are some of the characteristics of temporal data:

1. **Time-stamped**: Temporal data is time-stamped, meaning that each data point is associated with a specific point in time.

2. **Historical**: Temporal data allows for the storage and retrieval of historical data, enabling users to view the state of an entity at any point in the past.

3. **Consistent**: Temporal data must be consistent, meaning that the data must accurately represent the state of the entity at the specified point in time.

4. **Accurate**: Temporal data must be accurate, meaning that the data must accurately represent the state of the entity at the specified point in time.

5. **Up-to-date**: Temporal data must be up-to-date, meaning that the data must accurately represent the current state of the entity.

6. **Queryable**: Temporal data must be queryable, meaning that users must be able to retrieve data for a specific point in time or range of time.

7. **Efficient**: Temporal data must be stored and retrieved efficiently, meaning that the system must be able to quickly retrieve data for a specific point in time or range of time.

8. **Scalable**: Temporal data must be scalable, meaning that the system must be able to handle large amounts of data and support a large number of users.

These are some of the key characteristics of temporal data that are important for real-time systems and databases. Understanding these characteristics can help in the design and implementation of effective real-time systems and databases that can handle temporal data.



### Temporal Consistency

Temporal consistency refers to the maintenance of the correct temporal relationships between data items in a real-time database. In a real-time system, data is often associated with a specific time or time interval, and it is important that this temporal information is accurately maintained and updated.

Some key points to consider when discussing temporal consistency in the context of real-time operating systems and databases include:

1. Temporal consistency is important for ensuring the correctness of real-time systems, as it helps to ensure that data is used and updated in a timely and accurate manner.

2. Temporal consistency can be achieved through the use of various techniques, such as timestamping, versioning, and concurrency control mechanisms.

3. Temporal consistency is closely related to other concepts in real-time systems, such as temporal validity and temporal accuracy.

4. Temporal consistency is an important consideration in the design and implementation of real-time databases, and can have a significant impact on the performance and reliability of real-time systems.

Overall, temporal consistency is a crucial aspect of real-time systems and databases, and is essential for ensuring the correct operation of these systems. It is important for developers and designers of real-time systems to carefully consider temporal consistency when designing and implementing these systems.



### Concurrency Control

Concurrency control is a technique used in real-time operating systems and databases to ensure that multiple transactions can be executed simultaneously without interfering with each other. This is important in real-time systems where multiple processes may need to access shared resources at the same time.

Some key points to remember about concurrency control are:

1. Concurrency control is used to ensure the consistency and integrity of data in a database or shared resource.
2. There are several techniques used for concurrency control, including locking, timestamping, and optimistic concurrency control.
3. Locking involves placing locks on data items to prevent other transactions from accessing them while they are being modified.
4. Timestamping assigns a unique timestamp to each transaction and uses this to determine the order in which transactions should be executed.
5. Optimistic concurrency control assumes that conflicts between transactions are rare and allows them to proceed without locking. Conflicts are detected and resolved when they occur.
6. Choosing the right concurrency control technique depends on the specific requirements of the system and the workload it is expected to handle.




### Overview of Commercial Real Time databases

A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing. This differs from traditional databases containing persistent data, mostly unaffected by time. For example, a stock market changes very rapidly and is dynamic.

Real-time databases are designed to collect, process, and/or enrich an incoming series of data points (i.e., a data stream) in real time, typically immediately after the data is created. This term does not refer to a discrete class of database management systems, but rather, applies to several types of databases.

At the most basic level, a commercial real-time database needs to be able to source critical industry information firms use to guide investment decisions. Data must not only be accurate, but also reflect real-time changes. Your team can’t spend their limited time manually inputting or updating information.

With a commercial real estate database, you’re in a stronger position to detect market patterns, pinpoint trends and work efficiently. In short, commercial real estate databases allow you to screen deals faster and more strategically, ultimately propelling your business forward.

