

# Real Time System

A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). The term “real-time system” refers to any information processing system with hardware and software components that perform real-time application functions and can respond to events within predictable and specific time constraints.

## Types of Real-Time Systems
- **Hard Real-Time System**: A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.

## Applications of Real-Time Systems
- **Process Control Systems**: Process control systems are used in industrial applications where production is continuous.
- **Machine Vision**: Machine vision is used to help machines rapidly interpret data so they can see their surroundings and respond accordingly.
- **Robotics**: Robotics is another application of real-time systems.

Real-time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare. Some key use cases include flight control, industrial controls applications, video wall, medical imaging, and robotics.



## Unit 1 - Introduction of Real Time System

A real-time system is a computer system that is designed to process data and produce outputs within a specific time frame. This time frame is known as the system's deadline, and it is critical that the system meets this deadline in order to function correctly.

Some key points to consider when discussing real-time systems include:

1. Real-time systems are used in a variety of applications, including control systems, telecommunications, and multimedia systems.
2. These systems are designed to respond to events as they occur, and must do so within a specific time frame.
3. The consequences of missing a deadline in a real-time system can range from minor inconvenience to catastrophic failure.
4. Real-time systems can be classified as either hard or soft, depending on the severity of the consequences of missing a deadline.
5. Hard real-time systems have strict deadlines that must be met, while soft real-time systems have more flexible deadlines.
6. The design of a real-time system must take into account the system's processing capabilities, as well as the timing requirements of the application.



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

A real-time system is a computer system that is designed to process data and produce outputs in a timely manner, often within strict time constraints. These systems are used in applications where the correct operation of the system depends not only on the logical correctness of the outputs, but also on the time at which the outputs are produced.

Some key characteristics of real-time systems include:
- They have deadlines for completing tasks.
- They must be able to respond to events in a timely manner.
- They often operate in environments where there is a high degree of uncertainty and unpredictability.
- They must be able to handle multiple tasks simultaneously.
- They must be able to recover quickly from failures.

Real-time systems are used in a wide range of applications, including industrial control systems, avionics, medical systems, and telecommunications. They are essential for ensuring the safe and efficient operation of these systems.



### Typical Real Time Applications

Real-time systems are computer systems that monitor, respond to, or control an external environment. These systems are subject to a real-time constraint, which means they must respond to an input or event within a specific time frame. Here are some typical real-time applications:

1. **Industrial control systems:** These systems are used to control industrial processes such as manufacturing, chemical processing, and power generation. They must respond quickly to changes in the process to maintain safety and efficiency.

2. **Avionics systems:** These systems are used in aircraft to control flight, navigation, and communication. They must respond quickly to changes in the aircraft's environment to ensure safe and efficient operation.

3. **Medical systems:** These systems are used in hospitals and other medical facilities to monitor and treat patients. They must respond quickly to changes in a patient's condition to provide appropriate care.

4. **Telecommunications systems:** These systems are used to transmit and receive data over communication networks. They must respond quickly to changes in network traffic to maintain efficient and reliable communication.

5. **Multimedia systems:** These systems are used to process and display multimedia content such as video and audio. They must respond quickly to user input to provide a smooth and responsive user experience.

6. **Defense systems:** These systems are used by the military to monitor and respond to threats. They must respond quickly to changes in the environment to provide effective defense.

7. **Financial systems:** These systems are used in the financial industry to process transactions and manage financial data. They must respond quickly to changes in the market to provide accurate and timely information.

These are just a few examples of the many real-time applications that exist. Real-time systems are used in a wide variety of industries and applications, and their importance continues to grow as technology advances.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Release times refer to the specific times at which the notes for Unit 1 - Introduction of Real Time System in the subject of Real Time System are made available to students.
- These release times may vary depending on the institution, course, and instructor.
- It is important for students to be aware of the release times for the notes in order to effectively plan their study schedule.
- Students can typically find information about the release times for the notes on their course syllabus or by contacting their instructor.
- It is recommended that students regularly check for updates regarding the release times for the notes to ensure that they have the most up-to-date information.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A deadline is a specific time or date by which a task must be completed.
- In the context of Real Time Systems, deadlines are critical as they determine the time by which a task must be completed to ensure the correct functioning of the system.
- Deadlines can be hard or soft.
- A hard deadline is one that must be met, and failure to do so can result in a system failure or other catastrophic consequences.
- A soft deadline, on the other hand, is one that is desirable to meet, but failure to do so will not result in a system failure.
- In Real Time Systems, it is important to carefully manage and schedule tasks to ensure that all deadlines are met.
- This can be achieved through the use of scheduling algorithms and careful system design.




### Timing Constraints

Timing constraints are a crucial aspect of real-time systems. These constraints specify the time limits within which a task must be completed. There are two types of timing constraints: hard and soft.

1. **Hard timing constraints**: These constraints must be met for the system to function correctly. Failure to meet a hard timing constraint can result in catastrophic consequences, such as loss of life or damage to equipment. For example, in an aircraft control system, the control signals must be generated within a specific time frame to ensure the safe operation of the aircraft.

2. **Soft timing constraints**: These constraints are desirable but not essential for the correct functioning of the system. Failure to meet a soft timing constraint may result in degraded system performance, but not catastrophic consequences. For example, in a video streaming application, the video frames should be displayed at a specific rate to ensure smooth playback. However, if a frame is delayed, the video playback may be momentarily disrupted, but the overall functioning of the system is not affected.

In summary, timing constraints are an essential aspect of real-time systems, and the system must be designed to meet these constraints to ensure correct and safe operation. Hard timing constraints must be met, while soft timing constraints are desirable but not essential.



### Hard Real Time Systems

- Hard real-time systems are systems in which the correctness of the system depends not only on the logical result of the computation, but also on the time at which the results are produced.
- In hard real-time systems, missing a deadline is considered a system failure.
- These systems are often used in safety-critical applications, where the failure to meet a deadline can result in serious consequences, such as loss of life or damage to equipment.
- Examples of hard real-time systems include air traffic control systems, nuclear power plant control systems, and medical equipment.
- Hard real-time systems often require specialized hardware and software to ensure that deadlines are met.
- The design of hard real-time systems involves careful consideration of the worst-case execution time of tasks, as well as the scheduling of tasks to ensure that all deadlines are met.
- Hard real-time systems often use priority-based scheduling algorithms, where higher priority tasks are given preference over lower priority tasks.
- In hard real-time systems, it is important to ensure that the system is able to handle all possible scenarios, including unexpected events and failures, without missing any deadlines.



### Soft Real Time Systems

- A soft real-time operating system is one where there is a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system.
- Soft real-time systems, though less precise, can be run on multiple cores and impose fewer restrictions on applications.
- Soft real-time is when a system continues to function even if it’s unable to execute within an allotted time.
- If the system has missed its deadline, it will not result in critical consequences. The system can continue to function, though with undesirable lower quality of output.
- Soft real-time systems are typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems include software that maintains and updates the flight plans for commercial airliners.




### Reference Models for Real Time Systems

Real-time systems are computer systems that monitor, respond to, or control an external environment. This environment is connected to the computer system through sensors, actuators, and other input-output interfaces. The system must provide a response within a specified time, otherwise, the system's performance will degrade or fail.

Here are some reference models for real-time systems:

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-driven algorithm for scheduling periodic tasks in a real-time system. The tasks are assigned priorities based on their periods, with the shortest period task having the highest priority.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm for real-time systems. The tasks are assigned priorities based on their deadlines, with the earliest deadline task having the highest priority.

3. **Least Laxity First (LLF)**: This is another dynamic priority scheduling algorithm for real-time systems. The tasks are assigned priorities based on their laxity, which is the difference between the task's deadline and its remaining computation time. The task with the least laxity has the highest priority.

4. **Sporadic Server**: This is a scheduling algorithm for handling aperiodic tasks in a real-time system. The sporadic server reserves a portion of the processor's capacity for handling aperiodic tasks, and schedules them using the EDF or LLF algorithm.

These are some of the reference models used in real-time systems. They provide a framework for designing and analyzing real-time systems to ensure that they meet their timing constraints.



### Processors and Resources

1. A processor is a hardware component that performs the basic operations of a computer system.
2. It is responsible for executing instructions, performing calculations, and managing the flow of data within the system.
3. Processors can be classified into different types based on their architecture, such as CISC (Complex Instruction Set Computing) and RISC (Reduced Instruction Set Computing).
4. In a real-time system, the processor must be able to execute tasks within a specified time frame to meet the system's requirements.
5. Resources refer to the hardware and software components that are required for the system to function.
6. These can include memory, storage, input/output devices, and network interfaces.
7. In a real-time system, the availability and allocation of resources must be carefully managed to ensure that the system can meet its performance requirements.
8. Resource management techniques, such as scheduling algorithms and priority assignment, can be used to optimize the use of resources in a real-time system.



### Temporal Parameters of Real Time Workload

Real-time systems are designed to process data and produce results within a specific time frame. The temporal parameters of a real-time workload refer to the timing constraints that must be met by the system in order to function correctly. These parameters include:

1. **Release time**: The time at which a task becomes ready for execution.
2. **Deadline**: The time by which a task must complete its execution.
3. **Period**: The time interval between consecutive releases of a periodic task.
4. **Execution time**: The time required for a task to complete its execution once it starts.
5. **Response time**: The time interval between the release of a task and the completion of its execution.

These temporal parameters are critical in the design and analysis of real-time systems, as they determine the system's ability to meet its timing constraints and provide the desired level of performance. Failure to meet these constraints can result in system failure or degraded performance. Therefore, it is important to carefully consider these parameters when designing and implementing real-time systems.



### Periodic Task Model

The periodic task model is a commonly used model in real-time systems. In this model, tasks are executed at regular intervals, with each execution referred to as a job. The time between consecutive jobs is called the period of the task. The following are some key points to note about the periodic task model:

1. **Period**: The period of a task is the time between consecutive jobs. It is assumed to be constant for each task.
2. **Deadline**: Each job has a deadline by which it must complete its execution. The deadline can be relative to the start of the job or the start of the period.
3. **Utilization**: The utilization of a task is the ratio of its execution time to its period. The total utilization of the system is the sum of the utilizations of all tasks.
4. **Schedulability**: A set of periodic tasks is schedulable if there exists a scheduling algorithm that can schedule all jobs to meet their deadlines.
5. **Scheduling algorithms**: Common scheduling algorithms for periodic tasks include Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF).




### Precedence Constraints and Data Dependency

Precedence constraints and data dependencies are important concepts in real-time systems. Here are some key points to understand about these topics:

1. **Precedence constraints** refer to the order in which tasks must be executed. For example, in a real-time system, a task that processes sensor data may need to be executed before a task that uses the processed data to make a decision.

2. **Data dependencies** occur when the output of one task is used as the input of another task. In a real-time system, this can create a chain of dependencies where the execution of one task depends on the completion of another task.

3. Precedence constraints and data dependencies can impact the schedulability of a real-time system. If tasks are not scheduled in the correct order, the system may not be able to meet its deadlines.

4. To ensure that a real-time system can meet its deadlines, it is important to carefully analyze the precedence constraints and data dependencies between tasks. This can help to identify potential bottlenecks and to design an efficient schedule for the system.

5. There are several techniques that can be used to manage precedence constraints and data dependencies in real-time systems. These include priority-based scheduling, resource reservation, and rate-monotonic scheduling.




## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning system resources to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines while maximizing system performance.

1. **Hard Real-Time Systems**: In hard real-time systems, missing a deadline can result in catastrophic consequences. Therefore, the scheduling algorithm must guarantee that all tasks meet their deadlines.
2. **Soft Real-Time Systems**: In soft real-time systems, missing a deadline is undesirable but not catastrophic. The scheduling algorithm aims to minimize the number of missed deadlines.
3. **Rate Monotonic Scheduling (RMS)**: RMS is a priority-based scheduling algorithm for periodic tasks in hard real-time systems. The priority of a task is inversely proportional to its period, i.e., the shorter the period, the higher the priority.
4. **Earliest Deadline First (EDF)**: EDF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is determined by its absolute deadline, i.e., the earlier the deadline, the higher the priority.
5. **Least Laxity First (LLF)**: LLF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is determined by its laxity, i.e., the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority.



### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of assigning priorities to tasks in a real-time system to ensure that they meet their deadlines. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period of a task, the higher its priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline of a task, the higher its priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the difference between its deadline and its remaining computation time. The smaller the laxity of a task, the higher its priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of a task is assigned by the system designer and does not change during the execution of the system.

These are some of the common approaches to real-time scheduling. Each approach has its advantages and disadvantages and the choice of approach depends on the specific requirements of the real-time system.



### Clock Driven Approach

The clock-driven approach is a scheduling method used in real-time systems. It is also known as time-driven or table-driven scheduling. In this approach, the scheduler uses a pre-computed table to determine when tasks should be executed. The table is computed offline, before the system starts running, and it is based on the worst-case execution times of the tasks, their deadlines, and their periods.

Here are some key points to remember about the clock-driven approach:

1. The scheduler uses a pre-computed table to determine when tasks should be executed.
2. The table is computed offline, before the system starts running.
3. The table is based on the worst-case execution times of the tasks, their deadlines, and their periods.
4. The clock-driven approach is suitable for systems with periodic tasks and fixed deadlines.
5. The clock-driven approach is not suitable for systems with aperiodic or sporadic tasks, or tasks with variable deadlines.
6. The clock-driven approach can be implemented using a cyclic executive or a time-driven scheduler.



### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the amount of resources it requires. The tasks are then scheduled in a round-robin fashion, with the task with the highest weight being given the most time to execute.

Some key points to note about the WRR approach are:

1. Tasks are assigned weights based on their resource requirements.
2. The scheduler allocates time to tasks in a round-robin fashion.
3. The task with the highest weight is given the most time to execute.
4. The weights can be adjusted dynamically to account for changes in resource requirements.
5. WRR can be used in both uniprocessor and multiprocessor systems.

This approach can be useful in real-time systems where tasks have varying resource requirements and need to be scheduled in a fair and efficient manner. It allows for the dynamic allocation of resources, ensuring that tasks with higher resource requirements are given more time to execute. However, it may not be suitable for all real-time systems, as it can result in longer waiting times for lower priority tasks. It is important to carefully evaluate the suitability of the WRR approach for a given real-time system before implementing it.



### Priority Driven Approach

Priority-driven scheduling is a method used in real-time systems to schedule tasks based on their priority levels. In this approach, tasks are assigned priorities, and the scheduler selects the task with the highest priority for execution. The following are some key points to note about priority-driven scheduling:

1. **Priority Assignment:** Priorities can be assigned to tasks either statically or dynamically. Static priority assignment involves assigning priorities to tasks at design time, while dynamic priority assignment involves assigning priorities to tasks at runtime based on certain criteria.

2. **Preemptive and Non-Preemptive Scheduling:** Priority-driven scheduling can be either preemptive or non-preemptive. In preemptive scheduling, a higher priority task can preempt a lower priority task that is currently executing, while in non-preemptive scheduling, a task must complete its execution before another task can be scheduled.

3. **Fixed and Dynamic Priority Scheduling:** Priority-driven scheduling can also be classified as fixed priority scheduling or dynamic priority scheduling. In fixed priority scheduling, the priorities of tasks do not change during runtime, while in dynamic priority scheduling, the priorities of tasks can change during runtime.

4. **Rate Monotonic and Deadline Monotonic Scheduling:** Two common fixed priority scheduling algorithms used in real-time systems are rate monotonic scheduling and deadline monotonic scheduling. In rate monotonic scheduling, tasks are assigned priorities based on their periods, with shorter period tasks being assigned higher priorities. In deadline monotonic scheduling, tasks are assigned priorities based on their relative deadlines, with tasks having earlier relative deadlines being assigned higher priorities.

5. **Earliest Deadline First Scheduling:** A common dynamic priority scheduling algorithm used in real-time systems is the earliest deadline first (EDF) scheduling algorithm. In EDF scheduling, tasks are assigned priorities based on their absolute deadlines, with tasks having earlier absolute deadlines being assigned higher priorities.

These are some of the key points to note about priority-driven scheduling in real-time systems. This approach can be used to effectively schedule tasks in a real-time system to meet their timing constraints.



### Dynamic Versus Static Systems

- **Dynamic systems** are systems that change over time, while **static systems** remain constant.
- In the context of real-time scheduling, dynamic systems refer to systems where the scheduling decisions are made at runtime, based on the current state of the system.
- Static systems, on the other hand, refer to systems where the scheduling decisions are made offline, before the system starts executing.
- Dynamic scheduling algorithms are more flexible and can adapt to changes in the system, such as varying workload or resource availability.
- Static scheduling algorithms, on the other hand, are more predictable and easier to analyze, as the scheduling decisions are made in advance.
- Examples of dynamic scheduling algorithms include Earliest Deadline First (EDF) and Least Laxity First (LLF).
- Examples of static scheduling algorithms include Rate Monotonic (RM) and Deadline Monotonic (DM).
- The choice between dynamic and static scheduling depends on the specific requirements of the system, such as the need for flexibility or predictability.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two algorithms used in real-time scheduling. These algorithms are used to schedule tasks in a way that ensures that all tasks meet their deadlines.

1. **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest absolute deadline is scheduled first. EDF is an optimal algorithm for scheduling tasks on a uniprocessor system, meaning that if a feasible schedule exists, EDF will find it.

2. **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time, which is the amount of time remaining until the task's deadline minus the task's remaining execution time. The task with the least slack time is scheduled first. LST is also an optimal algorithm for scheduling tasks on a uniprocessor system.

In summary, both EDF and LST are optimal algorithms for scheduling tasks on a uniprocessor system. They ensure that all tasks meet their deadlines if a feasible schedule exists. These algorithms are commonly used in real-time systems to ensure that all tasks are completed within their specified time constraints.



### Rate Monotonic Algorithm

Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time scheduling. It is a static priority algorithm, meaning that the priorities of tasks are assigned at design time and do not change during runtime. RMA is an optimal algorithm for scheduling periodic tasks on a uniprocessor system.

The key points of the Rate Monotonic Algorithm are:

1. Tasks are assigned priorities based on their periods, with the shortest period task having the highest priority.
2. A task with a higher priority will always preempt a task with a lower priority.
3. Tasks are scheduled based on their priorities, with the highest priority task being scheduled first.
4. If a task misses its deadline, it is considered to have failed.

RMA is widely used in real-time systems due to its simplicity and optimality. However, it has some limitations, such as the assumption that tasks have fixed periods and that they do not share resources. These limitations can be addressed by using other scheduling algorithms or by using techniques such as resource reservation.



# Offline Versus Online Scheduling

Offline scheduling and online scheduling are two approaches to scheduling in real-time systems.

## Offline Scheduling
- In offline scheduling, the schedule is determined before the system starts executing.
- The schedule is computed based on the worst-case execution times of the tasks and their deadlines.
- The schedule is fixed and does not change during the execution of the system.
- Offline scheduling is suitable for systems with periodic tasks and known worst-case execution times.

## Online Scheduling
- In online scheduling, the schedule is determined during the execution of the system.
- The scheduler makes scheduling decisions based on the current state of the system, such as the current execution times of the tasks and their deadlines.
- The schedule can change during the execution of the system to adapt to changes in the system.
- Online scheduling is suitable for systems with aperiodic tasks or tasks with unknown or variable execution times.

In summary, offline scheduling is suitable for systems with predictable behavior, while online scheduling is suitable for systems with unpredictable behavior. Both approaches have their advantages and disadvantages, and the choice of approach depends on the specific requirements of the system.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

Unit 2 - Real Time Scheduling in the subject of Real Time System

- Aperiodic jobs are tasks that do not have a regular arrival pattern and can arrive at any time.
- Sporadic jobs are tasks that have a minimum inter-arrival time between two consecutive jobs.
- Priority-driven systems assign priorities to tasks based on their importance and schedule them accordingly.
- Clock-driven systems schedule tasks based on a pre-determined time table.
- In priority-driven systems, aperiodic and sporadic jobs can be scheduled using techniques such as slack stealing, where the scheduler utilizes the slack time in the schedule to execute these jobs.
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using techniques such as sporadic servers, where a server task is assigned to handle these jobs and is scheduled at regular intervals.
- These techniques help to ensure that aperiodic and sporadic jobs are executed in a timely manner while not affecting the execution of periodic tasks.



## Unit 3 - Resources Sharing

Resource sharing refers to the sharing of resources among multiple users or programs. This can be done in various ways, including:

1. **Time-sharing:** This is a method of sharing a resource, such as a computer, by allowing multiple users to use it at different times. Each user is given a certain amount of time to use the resource before it is passed on to the next user.

2. **Space-sharing:** This is a method of sharing a resource, such as a hard drive, by dividing it into multiple sections and assigning each section to a different user or program.

3. **Network-based resource sharing:** This is a method of sharing resources, such as files or printers, over a network. Users can access the shared resources from their own computers.

4. **Virtualization:** This is a method of sharing resources, such as hardware or software, by creating virtual versions of the resources that can be used by multiple users or programs simultaneously.

Resource sharing can improve efficiency and reduce costs by allowing multiple users or programs to share the same resources. However, it can also introduce security risks if not properly managed. It is important to implement proper access controls and security measures to ensure that resources are shared safely and securely.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- A resource access-control protocol, or simply an access-control protocol, is a set of rules that govern when and under what conditions each request for resource is granted and how jobs requiring resources are scheduled.
- Resource contention often leads to performance degradation in the applications contending for the shared resource. This can cause unexpected project delays, because processes contending for resources will be stalled until they can access the resource.
- Resource Access Control Protocols work to reduce the undesirable effect of resource contention. Resource contention affects the execution behavior and schedulability of jobs.
- One of the major objectives of resources access control is to minimize the undesirable effects of resource allocation.
- Access to resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section. If a lock request fails, the requesting job is blocked; a job holding a lock cannot be preempted by a higher priority job needing that lock.



### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, regardless of the priority of other tasks.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- This is achieved by ensuring that only one task can enter the critical section at a time, while other tasks attempting to enter the critical section are blocked until the task currently in the critical section exits.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms such as semaphores, mutexes, and spinlocks.
- It is important to carefully design the use of non-preemptive critical sections to avoid issues such as priority inversion and deadlock.
- Priority inversion occurs when a lower priority task holds a resource needed by a higher priority task, causing the higher priority task to be blocked.
- Deadlock occurs when two or more tasks are blocked waiting for resources held by each other, resulting in a circular wait.
- To avoid these issues, it is important to follow best practices such as using the priority ceiling protocol and avoiding nested critical sections.




### Basic Priority-Inheritance and Priority-Ceiling Protocols

#### Unit 3 - Resources Sharing in Real Time System

1. **Priority-Inheritance Protocol**: This protocol is used to solve the problem of priority inversion. When a high-priority task is blocked by a lower-priority task that holds a shared resource, the lower-priority task inherits the priority of the higher-priority task until it releases the resource. This ensures that the high-priority task can access the shared resource as soon as possible.

2. **Priority-Ceiling Protocol**: This protocol is an extension of the Priority-Inheritance Protocol. It assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. When a task acquires a shared resource, its priority is raised to the priority ceiling of the resource. This prevents lower-priority tasks from accessing the resource and causing priority inversion.

3. **Comparison**: The Priority-Ceiling Protocol is more effective in preventing priority inversion and reducing blocking time than the Priority-Inheritance Protocol. However, it requires more information about the system and the tasks, and may be more complex to implement.

4. **Implementation**: Both protocols can be implemented in the operating system or in the application code. The choice of implementation depends on the specific requirements of the system and the tasks.

5. **Applications**: These protocols are commonly used in real-time systems where tasks have strict timing constraints and shared resources must be accessed in a timely manner. They can help to improve the predictability and performance of the system.



### Stack Based Priority-Ceiling Protocol

The Stack Based Priority-Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways . It is based on original work to allow jobs to share a run-time stack, extended to control access to other resources  .

In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource . The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .

There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behavior of the two ceiling schemes is identical from a scheduling viewpoint. Both variants work by temporarily raising the priorities of tasks .



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time .
- The priority ceiling protocol can be used to control resource accesses in dynamic systems, provided the priority ceiling of each resource and the ceiling of the system are updated each time task priorities change .
- The protocol specifies a dynamic priority ceiling for each critical section, which is the earliest deadline of jobs that are currently in or will enter the critical section. Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section that is in use .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP) .



### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by low priority tasks holding a shared resource.

The key points of the Preemption Ceiling Protocol are:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the current preemption ceiling of the system.
3. The preemption ceiling of the system is the maximum of the preemption ceilings of all resources currently locked by tasks.
4. A task can be preempted by a higher priority task only if the priority of the preempting task is higher than the preemption ceiling of the system.

This protocol ensures that a high priority task is never blocked by a lower priority task holding a shared resource. It also ensures that a task holding a shared resource is not preempted by a lower priority task, preventing priority inversion.



### Access Control in Multiple-Unit Resources

Access control in multiple-unit resources refers to the management of access to resources that have multiple units or instances, such as a pool of database connections or a set of printers. In a real-time system, it is important to ensure that access to these resources is managed in a way that meets the timing constraints of the system.

Some key points to consider when implementing access control in multiple-unit resources include:

1. **Resource allocation**: It is important to have a mechanism in place for allocating resources to tasks or processes that need them. This can be done using techniques such as resource reservation or priority-based allocation.

2. **Resource sharing**: In a real-time system, it may be necessary for multiple tasks or processes to share access to a resource. This can be managed using techniques such as time division multiplexing or fair scheduling.

3. **Resource contention**: When multiple tasks or processes are competing for access to a resource, it is important to have a mechanism in place for managing contention. This can be done using techniques such as priority inheritance or priority ceiling protocols.

4. **Resource release**: It is important to have a mechanism in place for releasing resources when they are no longer needed. This can help to prevent resource starvation and ensure that resources are available for other tasks or processes that need them.

Overall, access control in multiple-unit resources is an important aspect of resource sharing in real-time systems. By carefully managing access to resources, it is possible to ensure that the system meets its timing constraints and operates efficiently.



### Controlling Concurrent Accesses to Data Objects

In a real-time system, multiple tasks may need to access shared data objects concurrently. To ensure the correctness and consistency of the data, it is necessary to control the concurrent accesses to these data objects. Here are some points to consider when controlling concurrent accesses to data objects in a real-time system:

1. **Mutual Exclusion**: One approach to controlling concurrent accesses to data objects is to use mutual exclusion mechanisms, such as semaphores or monitors, to ensure that only one task can access a shared data object at a time.

2. **Priority Inheritance**: When using mutual exclusion mechanisms, it is important to consider the priority of the tasks accessing the shared data objects. If a high-priority task is blocked by a lower-priority task holding a lock on a shared data object, it can result in priority inversion. To avoid this, priority inheritance protocols can be used to temporarily raise the priority of the lower-priority task holding the lock.

3. **Transaction-based Approaches**: Another approach to controlling concurrent accesses to data objects is to use transaction-based mechanisms, such as optimistic concurrency control or timestamp ordering. These mechanisms allow multiple tasks to access shared data objects concurrently, but ensure that any conflicting accesses are detected and resolved.

4. **Real-time Scheduling**: When controlling concurrent accesses to data objects, it is important to consider the real-time scheduling of the tasks accessing the data. Real-time scheduling algorithms, such as rate-monotonic or earliest-deadline-first scheduling, can be used to ensure that tasks meet their timing constraints while accessing shared data objects.

These are some of the key points to consider when controlling concurrent accesses to data objects in a real-time system. By using appropriate mechanisms and protocols, it is possible to ensure the correctness and consistency of shared data objects while allowing multiple tasks to access them concurrently.



## Unit 4 - Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. This type of communication can take place through various mediums, including voice, video, and text.

1. **Voice Communication:** Voice communication is one of the most common forms of real-time communication. It involves the transmission of audio signals between two or more parties. This can be done through traditional telephone lines, or through internet-based services such as VoIP (Voice over Internet Protocol).

2. **Video Communication:** Video communication involves the transmission of both audio and visual signals between two or more parties. This can be done through video conferencing software, or through web-based services such as Skype or Zoom.

3. **Text Communication:** Text communication involves the exchange of written messages between two or more parties. This can be done through instant messaging services, or through web-based services such as email or social media.

Real-time communication is essential in many industries, including business, healthcare, and education. It allows for immediate feedback and collaboration, which can improve productivity and efficiency.



### Basic Concepts in Real time Communication

Real-time communication (RTC) refers to any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real-time communication include:
- Voice over landlines and mobile phones
- Online communication that happens in real-time

Effective communication involves more than just exchanging information. It's about understanding the emotion and intentions behind the information. Some skills that can help improve communication include:
1. Becoming an engaged listener
2. Paying attention to nonverbal signals
3. Keeping stress in check
4. Asserting yourself



### Soft and Hard RT Communication systems

Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).

- **Hard Real-Time (HRT)**: Hard real-time systems have a strict time limit, or we can say deadlines. It is important to meet those deadlines, otherwise, the system is considered a system failure . The difference between a hard and soft real-time communication system is the consequences of incorrect operation .

- **Soft Real-Time (SRT)**: In a soft real-time system, there is no mandatory requirement of completing the deadline for every task . Unlike hard real-time communication systems, soft real-time communication systems generally do not have the capacity to cause catastrophic harm upon a fault, which allows for non-deterministic, less rigorous network infrastructure . Soft Real-time Communication is a communication system that is used to support soft real-time applications in a LAN. Soft real-time communication networks do not provide absolute Quality of Service (QoS) guarantee to applications. These networks always ensure prioritized treatment for real-time messages .



### Model of Real Time Communication

Real-time communication is a model of communication where the transmission and processing of information occur with minimal delay. This model is essential in systems where timely delivery of data is critical. Here are some key points to consider when discussing the model of real-time communication:

1. **Timeliness**: In real-time communication, the timely delivery of information is critical. The system must be able to transmit and process data with minimal delay to ensure that the information is delivered on time.

2. **Reliability**: The system must be reliable and able to deliver data with a high degree of accuracy. This is important to ensure that the information being transmitted is correct and can be acted upon.

3. **Scalability**: The system must be able to scale to accommodate an increasing number of users or devices. This is important to ensure that the system can handle the increased load without compromising on performance.

4. **Security**: The system must be secure and able to protect the data being transmitted from unauthorized access. This is important to ensure that the information being transmitted is not compromised.

5. **Interoperability**: The system must be able to interoperate with other systems and devices. This is important to ensure that the system can communicate with other systems and devices to exchange information.

In summary, the model of real-time communication is characterized by timeliness, reliability, scalability, security, and interoperability. These characteristics are essential to ensure that the system can deliver information in a timely and accurate manner.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

#### Priority-Based Service
- In a priority-based service discipline, packets are assigned a priority level based on their importance.
- Packets with higher priority are transmitted before packets with lower priority.
- This can be useful in real-time communication where certain packets, such as voice or video, may need to be transmitted with minimal delay.

#### Weighted Round-Robin Service
- In a weighted round-robin service discipline, packets are transmitted in a round-robin fashion, but with different weights assigned to different queues.
- Queues with higher weights are given more opportunities to transmit their packets.
- This can be useful in situations where certain traffic flows need to be given higher priority, but not at the expense of completely starving other traffic flows.

These service disciplines can be used in switched networks to improve the performance of real-time communication. They can help ensure that time-sensitive packets are transmitted with minimal delay, while still providing fair access to the network for other traffic flows.



### Medium Access Control Protocols for Broadcast Networks

Medium Access Control (MAC) protocols are responsible for controlling access to a shared communication medium in broadcast networks. These protocols are essential for ensuring efficient and fair use of the shared medium, and for avoiding collisions between multiple transmissions.

There are several types of MAC protocols used in broadcast networks, including:

1. **Contention-based protocols:** These protocols allow multiple nodes to compete for access to the shared medium. Examples of contention-based protocols include Carrier Sense Multiple Access with Collision Detection (CSMA/CD) and Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA).

2. **Time-division multiple access (TDMA):** In TDMA, time is divided into slots and each node is assigned a specific time slot for transmission. This ensures that only one node transmits at a time, avoiding collisions.

3. **Frequency-division multiple access (FDMA):** In FDMA, the available frequency band is divided into multiple channels, and each node is assigned a specific channel for transmission. This also ensures that only one node transmits at a time, avoiding collisions.

4. **Code-division multiple access (CDMA):** In CDMA, each node is assigned a unique code for transmission. The codes are designed in such a way that multiple transmissions can occur simultaneously without interfering with each other.

These are some of the most commonly used MAC protocols in broadcast networks. Each protocol has its own advantages and disadvantages, and the choice of protocol depends on the specific requirements of the network.



### Internet and Resource Reservation Protocols

Unit 4 - Real Time Communication in the subject of Real Time System

1. **Introduction:** The Internet is a global system of interconnected computer networks that use the standard Internet protocol suite (TCP/IP) to link devices worldwide. Resource reservation protocols are used to reserve resources in a network to provide quality of service (QoS) guarantees for real-time communication.

2. **Resource Reservation Protocol (RSVP):** RSVP is a signaling protocol used to reserve resources across a network for an integrated services Internet. It operates over an IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.

3. **Differentiated Services (DiffServ):** DiffServ is a computer networking architecture that specifies a scalable mechanism for classifying and managing network traffic and providing QoS on modern IP networks. It uses a 6-bit differentiated services code point (DSCP) in the 8-bit differentiated services field (DS field) in the IP header for packet classification purposes.

4. **Multi-Protocol Label Switching (MPLS):** MPLS is a protocol for speeding up and shaping network traffic flows. It allows most packets to be forwarded at the layer 2 (switching) level rather than at the layer 3 (routing) level. MPLS can provide traffic engineering, VPNs, and QoS.

5. **Real-Time Transport Protocol (RTP):** RTP is a network protocol for delivering audio and video over IP networks. It is used in conjunction with the Real-Time Transport Control Protocol (RTCP) to provide QoS and synchronization for real-time media streams.

6. **Real-Time Streaming Protocol (RTSP):** RTSP is a network control protocol designed for use in entertainment and communications systems to control streaming media servers. It provides "VCR-style" remote control functionality for audio and video streams, such as pause, fast forward, and rewind.

7. **Session Initiation Protocol (SIP):** SIP is a signaling protocol used for initiating, maintaining, modifying, and terminating real-time sessions that include video, voice, messaging, and other communications applications and services between two or more endpoints on IP networks.

8. **Conclusion:** Resource reservation protocols play a crucial role in providing QoS guarantees for real-time communication over the Internet. These protocols include RSVP, DiffServ, MPLS, RTP, RTSP, and SIP, among others. Understanding these protocols is essential for the design and implementation of real-time systems that rely on the Internet for communication.



## Unit 5 - Real Time Operating Systems and Databases

Real-time operating systems (RTOS) and databases are essential components of many modern systems, including embedded systems, control systems, and data processing systems.

1. **Real-time operating systems (RTOS)**: An RTOS is an operating system designed to support real-time applications that process data as it comes in, typically without buffering delays. The key characteristic of an RTOS is its ability to provide a predictable and deterministic response to events, which is essential for many real-time applications.

2. **Real-time databases**: A real-time database is a database system that is designed to handle workloads where the time it takes to process a transaction is critical. Real-time databases are used in applications where data must be processed quickly and accurately, such as in financial trading systems, telecommunications systems, and industrial control systems.

3. **Key features of RTOS and real-time databases**: Some of the key features of RTOS and real-time databases include:
    - Predictable and deterministic response times
    - Efficient handling of real-time data
    - Support for concurrent processing
    - High reliability and availability
    - Support for real-time transactions

4. **Applications of RTOS and real-time databases**: RTOS and real-time databases are used in a wide range of applications, including:
    - Embedded systems, such as automotive systems, medical devices, and consumer electronics
    - Control systems, such as industrial control systems and robotics
    - Data processing systems, such as financial trading systems and telecommunications systems.



### Features of RTOS

Real-Time Operating Systems (RTOS) are designed to provide predictable and deterministic execution of tasks in real-time applications. Here are some of the key features of RTOS:

1. **Deterministic behavior**: RTOS is designed to provide predictable and deterministic behavior, which means that the system will always respond to events within a known and fixed amount of time.

2. **Preemptive scheduling**: RTOS uses a preemptive scheduling algorithm, which means that the highest priority task will always be executed first, even if it means interrupting a lower priority task.

3. **Fast context switching**: RTOS is designed to have a very fast context switching time, which means that the system can quickly switch between tasks, allowing for more efficient use of the processor.

4. **Small memory footprint**: RTOS is designed to have a small memory footprint, which means that it requires very little memory to operate, making it suitable for use in embedded systems with limited memory.

5. **Real-time clock**: RTOS typically includes a real-time clock, which provides accurate timekeeping and can be used to schedule tasks at specific times.

6. **Inter-task communication**: RTOS provides mechanisms for inter-task communication, such as message queues, semaphores, and mutexes, which allow tasks to communicate and synchronize with each other.

7. **Interrupt handling**: RTOS is designed to handle interrupts in a timely and predictable manner, allowing for fast and efficient response to external events.

These are some of the key features of RTOS that make it suitable for use in real-time applications. It is important to note that not all RTOS have all of these features, and the specific features and capabilities of an RTOS will vary depending on the specific implementation.



### Time Services

Time services are an essential component of real-time operating systems and databases. These services provide the ability to measure and keep track of time, which is critical for the correct operation of real-time systems.

1. **Clocks**: Clocks are used to measure the passage of time. They can be hardware-based, such as crystal oscillators, or software-based, such as system clocks.

2. **Timers**: Timers are used to trigger events at specific times or after specific intervals. They can be one-shot, meaning they trigger once and then stop, or periodic, meaning they trigger repeatedly at regular intervals.

3. **Time synchronization**: Time synchronization is the process of ensuring that all clocks in a distributed system are synchronized to a common time source. This is important for coordinating the actions of multiple components in a real-time system.

4. **Time-stamping**: Time-stamping is the process of recording the time at which an event occurred. This is useful for tracking the sequence of events and for measuring the performance of real-time systems.

5. **Real-time clocks**: Real-time clocks are hardware devices that keep track of the current date and time, even when the system is powered off. They are often used in embedded systems to maintain accurate timekeeping.

These are some of the key time services used in real-time operating systems and databases. They play a crucial role in ensuring the correct operation of real-time systems.



### UNIX as RTOS

UNIX is a multi-user, multi-tasking operating system that was originally developed in the late 1960s and early 1970s. It is widely used in both academia and industry, and has been the basis for many other operating systems.

As a real-time operating system (RTOS), UNIX has several features that make it suitable for use in real-time systems:

1. **Preemptive multitasking:** UNIX allows multiple processes to run concurrently, with the scheduler able to preempt a running process to allow another process to run. This is important in real-time systems, where tasks must be completed within strict time constraints.

2. **Priority-based scheduling:** In UNIX, processes can be assigned different priorities, with higher priority processes being given more CPU time than lower priority processes. This is useful in real-time systems, where some tasks may be more time-critical than others.

3. **Inter-process communication:** UNIX provides several mechanisms for inter-process communication, including pipes, message queues, and shared memory. These mechanisms allow processes to communicate and synchronize with each other, which is important in real-time systems where multiple tasks may need to coordinate their actions.

4. **Real-time signals:** UNIX supports real-time signals, which are a way for processes to receive notifications of events in a timely manner. This is useful in real-time systems, where timely notification of events is important.

Overall, UNIX has many features that make it suitable for use as an RTOS in real-time systems. However, it is important to note that not all versions of UNIX are suitable for use in real-time systems, and some customization may be necessary to meet the specific requirements of a particular real-time system.



### POSIX Issues for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- POSIX stands for Portable Operating System Interface and is a proposed operating system interface standard based on the popular UNIX operating system. Its main goal is to support application portability at the source-code level.
- POSIX defines a standard way for an application to interface with the operating system. The original POSIX standard defines interfaces to core functions such as file operations, process management, signals, and devices.
- Subsequent releases of POSIX have also been defined to cover real-time extensions and multi-threading.
- The POSIX standard promotes portability of applications across different operating system platforms. This is especially important for applications designed for longevity, where the hardware and software infrastructure may change during the application's life cycle.
- The international standard POSIX standard has been adopted by virtually all operating systems in use and most real-time operating systems including ThreadX, QNX, VxWorks, Integrity, LynxOS, and Unison OS.
- A real-time working group was established in POSIX to develop standards to add POSIX (or UNIX) the OS services that are needed by real-time applications.



### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

Temporal data refers to data that represents the state of an entity at a particular point in time. It is used to track changes in data over time and is commonly used in real-time systems and databases. The following are some of the characteristics of temporal data:

1. **Time-stamped**: Temporal data is time-stamped to indicate the time at which the data was recorded or is valid.

2. **Historical**: Temporal data can be used to track changes in data over time, allowing for the analysis of historical trends and patterns.

3. **Versioned**: Temporal data can be versioned to allow for the storage and retrieval of multiple versions of the same data at different points in time.

4. **Consistent**: Temporal data must be consistent, meaning that the data must accurately represent the state of the entity at the specified time.

5. **Accurate**: Temporal data must be accurate, meaning that the data must be recorded and stored in a manner that ensures its accuracy and reliability.

6. **Granularity**: The granularity of temporal data refers to the level of detail at which the data is recorded and stored. The granularity of temporal data can vary depending on the needs of the system and the requirements of the data.

7. **Queryable**: Temporal data must be queryable, meaning that it must be possible to retrieve and analyze the data using queries and other data analysis tools.



### Temporal Consistency

Temporal consistency refers to the maintenance of the correct temporal relationships between data items in a real-time database. In a real-time system, data is often time-sensitive and must be updated or retrieved within specific time constraints. Temporal consistency ensures that the data in the database remains valid and up-to-date, even as the system operates in real-time.

Some key points to consider when discussing temporal consistency in real-time databases include:

1. Temporal consistency is important in real-time systems because it ensures that the data used by the system is accurate and up-to-date.
2. Temporal consistency can be achieved through various techniques, such as using timestamps to track the age of data items and implementing consistency protocols to ensure that data is updated in a timely manner.
3. Temporal consistency is closely related to other concepts in real-time databases, such as temporal validity and temporal accuracy.
4. Maintaining temporal consistency can be challenging in real-time systems, as it requires careful coordination between the database and the real-time application.

Overall, temporal consistency is a crucial aspect of real-time databases, as it helps to ensure that the data used by the system is accurate and up-to-date, even as the system operates in real-time. It is important for developers and designers of real-time systems to carefully consider temporal consistency when designing and implementing real-time databases.



### Concurrency Control

Concurrency control is a technique used in real-time operating systems and databases to ensure that multiple transactions can be executed simultaneously without interfering with each other. This is important in real-time systems where multiple processes may need to access shared resources at the same time.

Some of the key points to consider when discussing concurrency control in real-time systems and databases are:

1. **Locking:** One common approach to concurrency control is to use locks to prevent multiple transactions from accessing the same resource at the same time. This can be done using various locking mechanisms, such as shared locks, exclusive locks, and optimistic locks.

2. **Timestamp ordering:** Another approach to concurrency control is to use timestamps to determine the order in which transactions should be executed. This can help to prevent conflicts and ensure that transactions are executed in a consistent manner.

3. **Multiversion concurrency control:** This approach involves maintaining multiple versions of the data in the database, allowing transactions to access the version of the data that was current at the time the transaction started. This can help to reduce conflicts and improve performance in some cases.

4. **Deadlock prevention and detection:** Deadlocks can occur when multiple transactions are waiting for each other to release locks on resources. Techniques such as deadlock prevention and detection can be used to avoid or resolve these situations.

Overall, concurrency control is an important aspect of real-time operating systems and databases, and there are various techniques and approaches that can be used to ensure that transactions can be executed concurrently without interfering with each other. It is important to carefully consider the specific requirements of the system when choosing a concurrency control approach.



### Overview of Commercial Real Time databases

A real-time database is a data store designed to collect, process, and/or enrich an incoming series of data points (i.e., a data stream) in real time, typically immediately after the data is created. This term does not refer to a discrete class of database management systems, but rather, applies to several types of databases .

A commercial database is one created for commercial purposes only and it’s available at a price . At the most basic level, a commercial real estate database needs to be able to source critical industry information firms use to guide investment decisions. Data must not only be accurate, but also reflect real time changes .

With a commercial real estate database, you’re in a stronger position to detect market patterns, pinpoint trends and work efficiently. In short, commercial real estate databases allow you to screen deals faster and more strategically, ultimately propelling your business forward .

Some examples of commercial real-time databases include InfluxDB, which is part of a comprehensive platform that supports the collection, storage, monitoring, visualization and alerting of time series data .

