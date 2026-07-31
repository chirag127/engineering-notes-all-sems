

# Real Time System

A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). The term “real-time system” refers to any information processing system with hardware and software components that perform real-time application functions and can respond to events within predictable and specific time constraints.

## Types of Real-Time Systems
- **Hard real-time system**: This type of system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- **Soft real-time system**: This type of system can miss its deadline occasionally with some acceptably low probability.

## Applications of Real-Time Systems
- **Process Control Systems**: Process control systems are used in industrial applications where production is continuous.
- **Machine Vision**: Machine vision is used to help machines rapidly interpret data so they can see their surroundings.
- **Robotics**: Robotics is another application of real-time systems.
- **Flight Control**: Flight control is a key use case for real-time systems.
- **Industrial Controls Applications**: Industrial controls applications is another key use case for real-time systems.
- **Video Wall**: Video wall is another key use case for real-time systems.
- **Medical Imaging**: Medical imaging is another key use case for real-time systems.

Real-time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare.



## Unit 1 - Introduction of Real Time System

A real-time system is a computer system that is designed to process data and provide outputs within a specific time frame. This time frame is known as the system's deadline, and it is critical that the system meets this deadline in order to function correctly.

Some key points to consider when discussing real-time systems include:

1. Real-time systems are often used in applications where timing is critical, such as in control systems, financial trading, and telecommunications.
2. These systems are designed to provide predictable and consistent response times, ensuring that the system can meet its deadlines.
3. Real-time systems can be classified as either hard or soft, depending on the consequences of missing a deadline. In a hard real-time system, missing a deadline can result in catastrophic failure, while in a soft real-time system, missing a deadline may result in degraded performance.
4. The design of a real-time system must take into account the system's processing capabilities, the complexity of the tasks it must perform, and the timing constraints of the system.
5. Real-time systems often require specialized hardware and software in order to meet their performance requirements.



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A **Real-Time System** is a computer system that is designed to process data and provide outputs within a specific time frame.
- The system must respond to inputs and events within a predetermined time, known as the **deadline**.
- The correctness of the system depends not only on the logical correctness of the outputs but also on the time at which the outputs are produced.
- Real-Time Systems are often used in applications where there is a need for timely and accurate responses, such as in control systems, avionics, and telecommunications.
- Real-Time Systems can be classified into two types: **Hard Real-Time Systems** and **Soft Real-Time Systems**.
- In a **Hard Real-Time System**, missing a deadline can result in catastrophic consequences, such as loss of life or damage to equipment.
- In a **Soft Real-Time System**, missing a deadline may result in degraded performance, but the system can still continue to function.
- Real-Time Systems require careful design and implementation to ensure that all deadlines are met and the system operates correctly.




### Typical Real Time Applications

Real-time systems are computer systems that monitor, respond to, or control an external environment. These systems are subject to a real-time constraint, which means they must respond to an input or event within a specific time frame. Here are some typical real-time applications:

1. **Industrial automation and control:** Real-time systems are used to monitor and control industrial processes such as assembly lines, chemical plants, and power plants. These systems must respond quickly to changes in the environment to ensure safe and efficient operation.

2. **Telecommunications:** Real-time systems are used in telecommunications to process and transmit data, voice, and video signals. These systems must meet strict timing requirements to ensure that the signals are transmitted and received correctly.

3. **Transportation:** Real-time systems are used in transportation to monitor and control traffic, vehicles, and infrastructure. These systems must respond quickly to changes in traffic conditions to ensure safe and efficient transportation.

4. **Medical equipment:** Real-time systems are used in medical equipment to monitor and treat patients. These systems must respond quickly to changes in the patient's condition to provide effective treatment.

5. **Military systems:** Real-time systems are used in military systems to monitor and control weapons, vehicles, and communications. These systems must meet strict timing requirements to ensure that the military operations are carried out effectively.

6. **Gaming:** Real-time systems are used in gaming to provide a responsive and immersive gaming experience. These systems must respond quickly to user inputs to provide a smooth and realistic gaming experience.

7. **Multimedia:** Real-time systems are used in multimedia to process and display audio and video content. These systems must meet strict timing requirements to ensure that the content is displayed correctly and in sync.

These are just a few examples of the many real-time applications that exist. Real-time systems are used in a wide range of industries and applications to provide timely and accurate responses to events in the external environment.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Release times refer to the specific times at which the notes for Unit 1 - Introduction of Real Time System in the subject of Real Time System become available to students.
- These release times may vary depending on the institution, course, and instructor.
- It is important for students to check with their instructor or course syllabus for the specific release times for the notes of Unit 1.
- Staying up to date with the release times for the notes can help students stay on track with their studies and be prepared for exams.
- Some institutions may release the notes for Unit 1 all at once, while others may release them in sections or at specific intervals throughout the course.
- It is the responsibility of the student to ensure they have access to the notes and are aware of the release times.




### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Deadlines refer to the time by which a task or activity must be completed.
- In the context of Real Time Systems, deadlines are critical as they determine the success or failure of the system.
- Real Time Systems are designed to respond to events within a specific time frame, and failure to meet these deadlines can result in catastrophic consequences.
- Deadlines can be classified into two types: hard and soft.
- Hard deadlines are those that must be met without exception, while soft deadlines can be missed occasionally without causing significant harm to the system.
- The management of deadlines is an important aspect of Real Time Systems, and various techniques and algorithms are used to ensure that deadlines are met.
- These techniques include scheduling algorithms, resource allocation, and priority assignment.
- It is important to note that meeting deadlines is not the only goal of Real Time Systems, but it is a critical aspect that must be considered in the design and implementation of these systems.



### Timing Constraints

Timing constraints are a critical aspect of real-time systems. These constraints specify the time limits within which a task or set of tasks must be completed. There are two types of timing constraints: hard and soft.

1. **Hard timing constraints** are those that must be met, otherwise the system may fail or become unstable. For example, in a nuclear power plant, the control system must respond to changes in reactor conditions within a certain time frame to prevent a meltdown.

2. **Soft timing constraints** are those that are desirable but not critical. For example, in a multimedia application, it is desirable for the audio and video to be synchronized, but a small delay may be acceptable.

In real-time systems, it is important to ensure that all tasks meet their timing constraints. This can be achieved through careful design, scheduling, and resource allocation. Failure to meet timing constraints can result in degraded system performance or even catastrophic failure. Therefore, it is essential to thoroughly test and verify the timing behavior of a real-time system before deployment.



### Hard Real Time Systems

- Hard real-time systems are systems in which the correctness of the system depends not only on the logical result of the computation, but also on the time at which the results are produced.
- In hard real-time systems, missing a deadline is considered a system failure.
- These systems are often used in safety-critical applications, where the failure to meet a deadline can result in serious consequences, such as loss of life or damage to equipment.
- Examples of hard real-time systems include air traffic control systems, nuclear power plant control systems, and medical equipment.
- Hard real-time systems require rigorous testing and verification to ensure that they meet their deadlines under all possible conditions.
- The design of hard real-time systems often involves the use of specialized scheduling algorithms and real-time operating systems to ensure that tasks are completed within their deadlines.
- In hard real-time systems, it is important to consider worst-case execution times and to design the system to handle the worst-case scenarios.
- Hard real-time systems often have strict requirements for reliability, availability, and maintainability, as failures can have serious consequences.




### Soft Real Time Systems

Soft real-time systems are systems where the performance is degraded but not destroyed by failure to meet response time constraints. In other words, a late answer is still useful, but not as useful as an answer that is on time.

Some characteristics of soft real-time systems are:

1. They have flexible deadlines, meaning that missing a deadline is not catastrophic.
2. They are often used in multimedia, communication, and process control systems.
3. They prioritize the timely delivery of data over the accuracy of the data.
4. They often use statistical or probabilistic methods to guarantee a certain level of performance.

In summary, soft real-time systems are designed to provide a high level of performance, but they are not as strict as hard real-time systems in terms of meeting deadlines. They are often used in applications where a certain level of performance is desired, but not absolutely critical.



### Reference Models for Real Time Systems

Real-time systems are computer systems that are designed to interact with the external environment in a timely manner. These systems are used in a wide range of applications, including control systems, multimedia systems, and communication systems. To ensure that real-time systems meet their timing requirements, several reference models have been developed. These models provide a framework for the design and analysis of real-time systems.

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-based scheduling algorithm for periodic tasks. In this model, tasks are assigned priorities based on their periods, with shorter periods being assigned higher priorities. This model is widely used in the design of real-time systems.

2. **Earliest Deadline First (EDF)**: This is another priority-based scheduling algorithm for periodic tasks. In this model, tasks are assigned priorities based on their deadlines, with earlier deadlines being assigned higher priorities. This model is also widely used in the design of real-time systems.

3. **Sporadic Server**: This model is used to handle aperiodic tasks in a real-time system. In this model, a server task is created to handle the execution of aperiodic tasks. The server task is assigned a fixed priority and is scheduled along with the periodic tasks using a priority-based scheduling algorithm.

4. **Constant Bandwidth Server (CBS)**: This is an extension of the sporadic server model. In this model, the server task is assigned a variable priority and is scheduled using the EDF algorithm. This model provides better support for aperiodic tasks in a real-time system.

These are some of the reference models used in the design and analysis of real-time systems. These models provide a framework for ensuring that real-time systems meet their timing requirements. It is important to choose the appropriate model for the specific requirements of the real-time system being designed.



### Processors and Resources

1. **Processors** are the central processing units (CPUs) of a computer system that perform the computations and logical operations necessary to execute instructions and run programs.
2. **Resources** refer to the various hardware and software components that are required for a computer system to function, such as memory, storage, input/output devices, and operating systems.
3. In the context of real-time systems, processors and resources are critical components that must be carefully managed to ensure that the system can meet its timing constraints and performance requirements.
4. Real-time systems often require specialized processors and resources that are designed to handle the demands of real-time processing, such as high-speed processors, real-time operating systems, and dedicated hardware for input/output operations.
5. The allocation and scheduling of processors and resources in a real-time system must be carefully managed to ensure that all tasks can be completed within their specified deadlines.
6. Techniques such as priority scheduling, preemption, and resource reservation can be used to manage the allocation of processors and resources in a real-time system.
7. The efficient use of processors and resources is essential for the successful operation of a real-time system, and careful planning and management are required to ensure that the system can meet its performance and timing requirements.



### Temporal Parameters of Real Time Workload

1. **Release time**: The time at which a task becomes ready for execution.
2. **Deadline**: The time by which a task must complete its execution.
3. **Period**: The time interval between two consecutive releases of a periodic task.
4. **Execution time**: The time required for a task to complete its execution once it starts.
5. **Response time**: The time interval between the release of a task and the completion of its execution.
6. **Jitter**: The variation in the release times of a periodic task.
7. **Lateness**: The amount of time by which the completion of a task exceeds its deadline.
8. **Tardiness**: The amount of time by which the completion of a task exceeds its deadline, if the task completes after its deadline. Otherwise, tardiness is zero.
9. **Utilization**: The ratio of the execution time of a task to its period.

These temporal parameters are important in the design and analysis of real-time systems, as they determine the timing behavior of the system and its ability to meet the timing constraints of the tasks.



### Periodic Task Model

- A periodic task model is a model used in real-time systems to represent tasks that have a fixed period.
- In this model, tasks are released periodically at fixed intervals, and each task has a deadline by which it must be completed.
- The period of a task is the time interval between two consecutive releases of the task.
- The deadline of a task is the time by which the task must be completed after it is released.
- The execution time of a task is the time it takes for the task to complete its execution once it starts.
- The utilization of a task is the ratio of its execution time to its period.
- The schedulability of a set of periodic tasks is determined by whether all tasks can meet their deadlines under a given scheduling algorithm.
- Common scheduling algorithms for periodic tasks include Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF) scheduling.
- In RMS, tasks are assigned priorities based on their periods, with shorter period tasks having higher priorities.
- In EDF, tasks are assigned priorities based on their deadlines, with earlier deadline tasks having higher priorities.




### Precedence Constraints and Data Dependency

- Precedence constraints and data dependencies are important concepts in real-time systems.
- Precedence constraints refer to the order in which tasks must be executed. For example, in a real-time system, a task that processes sensor data must be executed before a task that uses the processed data to make a decision.
- Data dependencies refer to the relationship between tasks where the output of one task is used as the input of another task. For example, in a real-time system, a task that processes sensor data has a data dependency with a task that uses the processed data to make a decision.
- Precedence constraints and data dependencies must be carefully managed in real-time systems to ensure that tasks are executed in the correct order and that data is available when it is needed.
- Failure to properly manage precedence constraints and data dependencies can result in incorrect system behavior and can compromise the safety and reliability of the system.




## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning tasks to resources in a way that ensures that all tasks meet their timing constraints. This is important in real-time systems, where tasks have deadlines that must be met in order for the system to function correctly.

Some key points to consider when studying real-time scheduling include:

1. **Scheduling algorithms:** There are several different algorithms that can be used for real-time scheduling, including Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), and Least Laxity First (LLF). Each algorithm has its own strengths and weaknesses, and the choice of algorithm will depend on the specific requirements of the system.

2. **Task characteristics:** The characteristics of the tasks being scheduled, such as their execution time, deadline, and priority, will affect the scheduling decisions. It is important to understand these characteristics in order to make effective scheduling decisions.

3. **Resource constraints:** Real-time systems often have limited resources, such as processing power and memory, and these constraints must be taken into account when scheduling tasks. Resource allocation and management is a key part of real-time scheduling.

4. **Overload conditions:** In some cases, the system may be overloaded, meaning that there are more tasks than can be completed within their deadlines. In these situations, the scheduler must make decisions about which tasks to prioritize and which to delay or drop.

Overall, real-time scheduling is a complex and challenging problem, and it is an important area of study for anyone working with real-time systems. By understanding the key concepts and techniques involved, it is possible to design and implement effective real-time scheduling solutions.



### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of allocating system resources to tasks in a way that ensures all tasks meet their timing constraints. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where tasks are assigned priorities based on their periods. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their deadlines. The earlier the deadline, the higher the priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity, the higher the priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where tasks are assigned fixed priorities by the system designer.

These are some of the common approaches to real-time scheduling. Each approach has its own advantages and disadvantages, and the choice of approach depends on the specific requirements of the system being designed. It is important to carefully analyze the system and its timing constraints to determine the most appropriate scheduling approach.



### Clock Driven Approach

The clock-driven approach is a scheduling method used in real-time systems. It is also known as time-driven or table-driven scheduling. In this approach, a static schedule is created offline, before the system starts executing. The schedule is based on the known periodicity of tasks and their deadlines. The schedule is then stored in a table and is followed by the system during execution.

Some key points to note about the clock-driven approach are:

1. The schedule is created offline, before the system starts executing.
2. The schedule is based on the known periodicity of tasks and their deadlines.
3. The schedule is stored in a table and is followed by the system during execution.
4. This approach is suitable for systems with periodic tasks and fixed deadlines.
5. The schedule is static and does not change during execution.

This approach is commonly used in systems where the tasks have fixed, periodic deadlines and the workload is predictable. It is not suitable for systems with a dynamic workload or tasks with varying deadlines. In such cases, other scheduling methods, such as event-driven or priority-driven scheduling, may be more appropriate.



### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight that determines the length of its time slice.

1. In WRR, tasks with higher weights are given longer time slices, allowing them to execute for a longer period of time before being preempted by other tasks.
2. The time slice for each task is calculated by dividing the weight of the task by the sum of the weights of all tasks.
3. Once a task has completed its time slice, it is moved to the end of the queue and the next task in the queue is given the CPU.
4. If a task completes its execution before its time slice has expired, the remaining time is distributed among the other tasks in the queue.
5. WRR is commonly used in systems where tasks have different priorities, as it allows higher priority tasks to be given longer time slices and therefore more CPU time.

This approach can be useful in real-time systems where tasks have different levels of importance and need to be executed in a timely manner. However, it can also lead to starvation of lower priority tasks if the weights are not carefully chosen. It is important to carefully balance the weights of the tasks to ensure that all tasks are given a fair share of the CPU time.



### Priority Driven Approach

Priority-driven scheduling is a type of real-time scheduling in which tasks are assigned priorities and the scheduler selects the highest priority task to execute. This approach is used in real-time systems to ensure that critical tasks are completed on time.

Some key points to note about priority-driven scheduling are:

1. Tasks are assigned priorities based on their importance or urgency.
2. The scheduler selects the highest priority task to execute.
3. If two or more tasks have the same priority, the scheduler may use other criteria to determine which task to execute.
4. Priority-driven scheduling can be preemptive or non-preemptive.
5. In preemptive scheduling, a higher priority task can interrupt a lower priority task that is currently executing.
6. In non-preemptive scheduling, a lower priority task that is currently executing cannot be interrupted by a higher priority task.
7. Priority-driven scheduling can be used in both static and dynamic systems.
8. In static systems, priorities are assigned to tasks before the system starts executing.
9. In dynamic systems, priorities can change during the execution of the system.




### Dynamic Versus Static Systems

- **Dynamic systems** are systems that change over time, while **static systems** remain constant.
- In the context of real-time scheduling, dynamic systems refer to systems where the scheduling decisions are made at runtime, based on the current state of the system.
- In contrast, static systems refer to systems where the scheduling decisions are made offline, before the system starts executing.
- Dynamic scheduling algorithms are more flexible and can adapt to changes in the system, such as varying workload or resource availability.
- Static scheduling algorithms, on the other hand, are more predictable and easier to analyze, as the scheduling decisions are fixed and known in advance.
- The choice between dynamic and static scheduling depends on the specific requirements of the real-time system, such as the need for flexibility, predictability, and ease of analysis.
- Some common dynamic scheduling algorithms for real-time systems include Earliest Deadline First (EDF) and Least Laxity First (LLF).
- Some common static scheduling algorithms for real-time systems include Rate Monotonic (RM) and Deadline Monotonic (DM).



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- The Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) algorithms are two popular scheduling algorithms used in real-time systems.
- EDF is an optimal algorithm for scheduling periodic tasks with implicit deadlines on a uniprocessor system.
- This means that if a set of periodic tasks with implicit deadlines can be scheduled on a uniprocessor system, then EDF can find a feasible schedule for it.
- LST is an optimal algorithm for scheduling periodic tasks with arbitrary deadlines on a uniprocessor system.
- This means that if a set of periodic tasks with arbitrary deadlines can be scheduled on a uniprocessor system, then LST can find a feasible schedule for it.
- Both EDF and LST are dynamic priority algorithms, meaning that the priority of a task can change during its execution.
- EDF assigns the highest priority to the task with the earliest absolute deadline, while LST assigns the highest priority to the task with the least slack time.
- Slack time is the amount of time left until the task's deadline minus the remaining execution time of the task.
- Both EDF and LST have been proven to be optimal for their respective scenarios, meaning that no other scheduling algorithm can perform better in terms of schedulability.



### Rate Monotonic Algorithm

Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time scheduling. It is a static priority scheduling algorithm, which means that the priorities of tasks are assigned before the system starts running and do not change during execution.

Here are some key points to remember about the Rate Monotonic Algorithm:

1. RMA assigns priorities to tasks based on their periods. The shorter the period of a task, the higher its priority.
2. RMA is an optimal algorithm for scheduling periodic tasks on a uniprocessor system. This means that if a set of periodic tasks can be scheduled by any static priority algorithm, it can also be scheduled by RMA.
3. RMA is a preemptive algorithm, which means that a higher priority task can interrupt a lower priority task that is currently executing.
4. The schedulability of a set of tasks under RMA can be determined using the Liu and Layland utilization bound or the hyperbolic bound.
5. RMA is not suitable for scheduling tasks with deadlines that are different from their periods or for scheduling aperiodic or sporadic tasks.




### Offline Versus Online Scheduling

Offline scheduling and online scheduling are two approaches to scheduling tasks in a real-time system.

1. **Offline scheduling** involves determining a schedule for tasks before the system begins execution. This schedule is fixed and does not change during runtime. Offline scheduling is suitable for systems with predictable workloads, where the set of tasks and their execution times are known in advance.

2. **Online scheduling**, on the other hand, involves making scheduling decisions during runtime. The scheduler must respond to events as they occur and make decisions about which tasks to execute based on the current state of the system. Online scheduling is suitable for systems with unpredictable workloads, where the set of tasks and their execution times are not known in advance.

In summary, the choice between offline and online scheduling depends on the predictability of the workload in the real-time system. If the workload is predictable, offline scheduling can be used to determine a fixed schedule in advance. If the workload is unpredictable, online scheduling can be used to make scheduling decisions during runtime.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are tasks that do not have a fixed period or inter-arrival time. They arrive at irregular intervals and their execution time may vary.
- Sporadic jobs are similar to aperiodic jobs, but they have a minimum inter-arrival time constraint.
- In priority-driven systems, jobs are assigned priorities based on their importance or urgency. The scheduler selects the highest priority job for execution.
- In clock-driven systems, jobs are scheduled based on a pre-determined timetable. The scheduler selects the next job to execute based on the current time and the timetable.
- Aperiodic and sporadic jobs can be scheduled in priority-driven systems using techniques such as slack stealing, where the scheduler steals idle time from lower priority jobs to execute aperiodic or sporadic jobs.
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using techniques such as sporadic servers, where a server is allocated a fixed amount of time to execute aperiodic or sporadic jobs.
- These techniques allow for the efficient scheduling of aperiodic and sporadic jobs in real-time systems, ensuring that all jobs meet their deadlines and the system remains stable.




## Unit 3 - Resources Sharing

1. Resource sharing refers to the sharing of resources among multiple users or systems.
2. This can include sharing of physical resources, such as hardware, or logical resources, such as data or software.
3. Resource sharing can improve efficiency and reduce costs by allowing multiple users to access the same resources.
4. Common examples of resource sharing include file sharing, printer sharing, and internet sharing.
5. Resource sharing can be implemented through various methods, including networking, virtualization, and cloud computing.
6. Security and access control are important considerations when implementing resource sharing to ensure that resources are only accessed by authorized users.
7. Resource sharing can also facilitate collaboration and communication among users by allowing them to share information and work together on projects.
8. Resource sharing can be implemented on a local or global scale, with resources being shared within a single organization or among multiple organizations.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- A resource access-control protocol, or simply an access-control protocol, is a set of rules that govern (1) when and under what conditions each request for resource is granted and (2) how jobs requiring resources are scheduled.
- Resource contention often leads to performance degradation in the applications contending for the shared resource. This can cause unexpected project delays, because processes contending for resources will be stalled until they can access the resource.
- Resource Access Control Protocols work to reduce the undesirable effect of resource contention. Resource contention affects the execution behavior and schedulability of jobs.
- One of the major objectives of resources access control is to minimize the undesirable effects of resource allocation.
- Access to resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section. If a lock request fails, the requesting job is blocked; a job holding a lock cannot be preempted by a higher priority job needing that lock.



### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that are executed without interruption.
- This means that once a task enters a non-preemptive critical section, it cannot be preempted until it exits the critical section.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- This is achieved by ensuring that only one task can access the shared resource at a time.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms such as semaphores, mutexes, and monitors.
- These mechanisms ensure that only one task can enter the critical section at a time, while other tasks attempting to enter the critical section are blocked until the task currently in the critical section exits.
- Non-preemptive critical sections are commonly used in real-time systems to ensure predictable and deterministic behavior.
- However, the use of non-preemptive critical sections can also introduce challenges such as priority inversion and deadlock.
- To avoid these challenges, it is important to carefully design and implement non-preemptive critical sections in real-time systems.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage shared resources and prevent priority inversion.

1. **Priority-Inheritance Protocol**: This protocol is used to prevent priority inversion by temporarily raising the priority of a lower-priority task that holds a shared resource to the priority of the highest-priority task that is blocked and waiting for the resource. This ensures that the lower-priority task can complete its use of the shared resource and release it for the higher-priority task.

2. **Priority-Ceiling Protocol**: This protocol is used to prevent priority inversion, deadlocks, and unbounded priority inversion. It assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only lock a resource if its priority is higher than the current priority ceiling of all resources it currently holds or is attempting to lock.

These protocols are important for ensuring the correct and timely execution of tasks in real-time systems that share resources. They help to prevent situations where a higher-priority task is blocked by a lower-priority task, which can cause missed deadlines and other issues.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol is based on original work to allow jobs to share a run-time stack, extended to control access to other resources .
- In the statement of the rules of the stack-based, priority-ceiling protocol, we again use the term (current) ceiling ˆ f (t) of the system, which is the highest-priority ceiling of all the resources that are in use at time t Ω. is a nonexisting priority level that is lower than the lowest priority of all jobs.
- Stack Based Priority-ceiling Protocol has two rules:
  1. Scheduling Rule: After a job is released, it is blocked from starting execution until its assigned priority is higher.
  2. Allocation Rule: Whenever a job requests a resource, it is allocated the resource.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point. Both variants work by temporarily raising the priorities of tasks.
- Priority Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways. Real-Time Systems are multitasking systems that involve the use of semaphore variables, signals, and events for job synchronization.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time.
- The priority ceiling of a resource is the highest priority of any task that may lock the resource.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change.
- The protocol specifies a dynamic priority ceiling for each critical section which is the earliest deadline of jobs which are currently in or will enter the critical section.
- Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section which is in use.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).



### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by lower priority tasks. Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling.
3. When a task locks a resource, the system's preemption ceiling is set to the maximum of the current preemption ceiling and the resource's preemption ceiling.
4. A task can be preempted only by tasks with a priority higher than the current preemption ceiling.
5. When a task releases a resource, the system's preemption ceiling is reset to the maximum preemption ceiling of all resources currently locked by tasks.

This protocol ensures that high priority tasks are not blocked by lower priority tasks and prevents priority inversion. It is important to note that the preemption ceiling must be carefully assigned to each shared resource to ensure the correct functioning of the protocol.



### Access Control in Multiple-Unit Resources

Access control in multiple-unit resources refers to the management of access to resources that have multiple units or instances. In a real-time system, these resources may include processors, memory, and input/output devices.

1. One approach to access control in multiple-unit resources is to use a **fixed partitioning** scheme. In this approach, the resources are divided into fixed partitions, and each partition is assigned to a specific task or group of tasks. This approach can be simple to implement, but it may result in inefficient resource utilization if the partitions are not sized appropriately.

2. Another approach is to use **dynamic partitioning**, where the resources are allocated to tasks as needed. This approach can result in more efficient resource utilization, but it may be more complex to implement and may require more sophisticated resource management algorithms.

3. A third approach is to use a **hybrid scheme**, which combines elements of both fixed and dynamic partitioning. For example, some resources may be partitioned statically, while others are allocated dynamically.

4. In any approach to access control in multiple-unit resources, it is important to ensure that the resource allocation is done in a way that meets the real-time constraints of the system. This may involve using priority-based resource allocation algorithms, or implementing admission control mechanisms to ensure that the system does not become overloaded.

5. Additionally, it may be necessary to implement mechanisms for **resource sharing** and **resource contention resolution** to ensure that tasks can access the resources they need without interfering with each other.

In summary, access control in multiple-unit resources is an important aspect of resource management in real-time systems, and there are several approaches that can be used to manage access to these resources. The choice of approach will depend on the specific requirements of the system and the characteristics of the resources being managed.



### Controlling Concurrent Accesses to Data Objects

Controlling concurrent access to data objects is an important aspect of resource sharing in real-time systems. Here are some key points to consider:

1. **Concurrency control** is the process of managing simultaneous access to shared data objects to ensure data consistency and integrity.

2. **Locking** is a common technique used to control concurrent access to data objects. It involves placing a lock on a data object to prevent other processes from accessing it until the lock is released.

3. **Deadlocks** can occur when two or more processes are waiting for each other to release locks on data objects. Deadlock prevention and detection algorithms can be used to avoid or resolve deadlocks.

4. **Priority inversion** can occur when a high-priority process is blocked by a low-priority process holding a lock on a shared data object. Priority inheritance and priority ceiling protocols can be used to prevent priority inversion.

5. **Real-time databases** can be used to manage concurrent access to data objects in real-time systems. These databases use specialized concurrency control algorithms to ensure timely access to data while maintaining data consistency and integrity.

6. **Transaction processing** is another approach to controlling concurrent access to data objects. Transactions are used to group a series of operations on data objects into a single, atomic unit of work.

7. **Distributed systems** introduce additional challenges for controlling concurrent access to data objects. Distributed concurrency control algorithms, such as two-phase locking and timestamp ordering, can be used to manage concurrent access to data objects in distributed systems.

These are some of the key concepts and techniques for controlling concurrent access to data objects in real-time systems. Understanding these concepts is essential for effectively managing resource sharing in real-time systems.



## Unit 4 - Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. This type of communication is essential for many applications, including online gaming, video conferencing, and remote control of devices.

Some key points to consider when discussing real-time communication include:

1. **Latency**: Latency refers to the time it takes for a signal to travel from one point to another. In real-time communication, low latency is essential to ensure that the communication feels instantaneous.

2. **Bandwidth**: Bandwidth refers to the amount of data that can be transmitted over a communication channel in a given period of time. High bandwidth is necessary for applications that require the transmission of large amounts of data, such as video conferencing.

3. **Reliability**: Reliability refers to the ability of a communication system to deliver messages without errors or loss of data. In real-time communication, reliability is important to ensure that the communication is not disrupted.

4. **Security**: Security refers to the measures taken to protect communication from unauthorized access or interception. In real-time communication, security is important to ensure that the communication remains private and confidential.

5. **Protocols**: Protocols are sets of rules that define how communication takes place between different devices. In real-time communication, protocols are used to ensure that the communication is carried out in an orderly and efficient manner.

Real-time communication is an essential component of many modern applications and is a topic of ongoing research and development. By understanding the key concepts and technologies involved, we can better appreciate the challenges and opportunities presented by this rapidly evolving field.



### Basic Concepts in Real time Communication

1. **Definition**: Real-time communications (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

2. **Examples**: Real-time communication is any online communication that happens in real-time. Data is sent directly and instantly from the sender to the receiver and is not stored en route to the destination. The telephone is just one classic example of a real-time communication.

3. **Types**: Real-time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the transfer. Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).

4. **Advancements**: Real-time communication is being paired with what’s called deep learning and neural networks to improve RTC features such as speech analytics and voice bots. Using methods such as these can affect tools for live transcribing and video conferences. Machine learning and RTC bring better clarity in telecommunications, with both audio and video.



### Soft and Hard RT Communication systems

Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT). The difference between a hard and soft real-time communication system is the consequences of incorrect operation.

- Hard Real-Time (HRT) systems have a strict time limit, or we can say deadlines. It is important to meet those deadlines, otherwise, the system is considered a system failure.
- Soft Real-Time (SRT) systems generally do not have the capacity to cause catastrophic harm upon a fault, which allows for non-deterministic, less rigorous network infrastructure. In a soft real-time system, there is no mandatory requirement of completing the deadline for every task.



### Model of Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. In the context of real-time systems, this communication must occur within a specified time frame to ensure the correct functioning of the system. Here are some key points to consider when discussing the model of real-time communication:

1. **Timing constraints:** Real-time communication must adhere to strict timing constraints to ensure that the system functions correctly. This means that messages must be delivered within a specified time frame, and any delays could result in system failure.

2. **Reliability:** The communication between parties must be reliable to ensure that messages are delivered correctly and without error. This can be achieved through the use of error detection and correction techniques, as well as the use of redundant communication channels.

3. **Synchronization:** In many real-time systems, it is important for the parties involved in the communication to be synchronized. This means that they must operate on the same time scale and be able to coordinate their actions.

4. **Protocols:** Real-time communication often relies on the use of specific protocols to ensure that the timing constraints are met. These protocols can include time-triggered protocols, event-triggered protocols, and hybrid protocols that combine elements of both.

5. **Network topology:** The topology of the network used for real-time communication can also play a role in the model. For example, a star topology may be used to ensure that all parties can communicate directly with a central hub, while a ring topology may be used to ensure that messages can be passed between parties in a predictable manner.

Overall, the model of real-time communication must take into account the specific requirements of the system, including its timing constraints, reliability, synchronization, and the use of appropriate protocols and network topologies. By carefully considering these factors, it is possible to design a real-time communication model that meets the needs of the system and ensures its correct functioning.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- According to a priority-based service discipline, the transmission of ready packets is scheduled in a priority-driven manner. 
- Waited fair queuing (WFQ) and Waited round-robin scheduling are common approaches for scheduling the packets in real-time communication networks .
- In a switched network, a downstream switch can begin to transmit an earlier portion of the message as soon as it receives the portion. It does not have to wait for the arrival of the rest of the message .
- The weighted round-robin approach does not require a sorted priority queue, only a round-robin queue .
- Queue service disciplines are used to determine service priority, delay bound, jitter bound, and bandwidth .
- Among them, the Weighted Round Robin (WRR) technique has provided the most reasonable performance in guaranteeing both bandwidth and fairness requirements .
- A new WRR algorithm, called Rate-controlled Frame-based Weighted Round Robin (RFWRR), guarantees the delay jitter bound and satisfies a diverse set of delay requirements .
- Many class service disciplines used for output queued switches have been proposed in the literature. These disciplines include the Class-Based Weighted Fair Queuing (CBWFQ) and the Weighted Fair Priority Queuing (WFPQ) techniques .



### Medium Access Control Protocols for Broadcast Networks

Medium Access Control (MAC) protocols are used to coordinate the access of multiple devices to a shared communication medium. In broadcast networks, where all devices can transmit and receive data simultaneously, MAC protocols play a crucial role in ensuring efficient and fair use of the shared medium.

Some common MAC protocols for broadcast networks include:

1. **Aloha**: Aloha is a simple MAC protocol where devices transmit data whenever they have data to send. If two or more devices transmit at the same time, a collision occurs and the data is lost. To reduce the probability of collisions, devices use a random backoff time before retransmitting the data.

2. **Carrier Sense Multiple Access (CSMA)**: In CSMA, devices first sense the medium to check if it is idle before transmitting data. If the medium is busy, the device waits for a random backoff time before sensing the medium again. This reduces the probability of collisions but does not eliminate them completely.

3. **Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)**: CSMA/CA is an extension of CSMA where devices use a handshake mechanism to reserve the medium before transmitting data. This further reduces the probability of collisions but increases the overhead and delay.

4. **Time Division Multiple Access (TDMA)**: In TDMA, time is divided into slots and each device is assigned a specific time slot to transmit data. This eliminates collisions but requires synchronization and may result in inefficient use of the medium if some devices have more data to transmit than others.

These are some of the common MAC protocols used in broadcast networks. Each protocol has its own advantages and disadvantages and the choice of protocol depends on the specific requirements of the network.



### Internet and Resource Reservation Protocols

- The **Resource Reservation Protocol (RSVP)** is used in real-time systems for efficient quality band transmission to a particular receiver.
- RSVP provides new Internet services with higher quality than best-effort by means of resource reservations.
- It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- There are several possible models for how the use of resource reservation, based on RSVP or successor protocols, might evolve.
- Advances in wireless broadband communications have continued steadily over the last few years on the basis of wireless LAN and next generation (3G) mobile communications.




## Unit 5 - Real Time Operating Systems and Databases

1. **Real-Time Operating Systems (RTOS)**: An RTOS is an operating system designed to serve real-time applications that process data as it comes in, typically without buffer delays. The main objective of an RTOS is to provide a quick and predictable response to events.

2. **Characteristics of RTOS**: Some of the key characteristics of an RTOS include determinism, responsiveness, user control, reliability, and fail-safe operation.

3. **Types of RTOS**: There are two main types of RTOS: hard real-time systems and soft real-time systems. Hard real-time systems have strict timing constraints, while soft real-time systems have more relaxed timing constraints.

4. **Real-Time Databases**: A real-time database is a database system that is designed to handle workloads where transactions have timing constraints. Real-time databases are used in applications such as financial trading, telecommunications, and industrial control systems.

5. **Concurrency Control in Real-Time Databases**: Concurrency control is an important issue in real-time databases, as it ensures that transactions are executed in a timely and predictable manner. Some common concurrency control techniques used in real-time databases include locking, timestamp ordering, and optimistic concurrency control.

6. **Real-Time Database Design**: The design of a real-time database involves several considerations, such as the choice of data model, the use of indexes, and the design of the transaction processing system. The goal is to ensure that the database can handle the required workload while meeting the timing constraints of the application.

7. **Real-Time Database Management Systems**: A real-time database management system (RTDBMS) is a database management system that is designed to handle real-time workloads. Some examples of RTDBMSs include Oracle TimesTen, IBM Informix, and SAP HANA.



### Features of RTOS

Real-Time Operating Systems (RTOS) are designed to provide predictable and deterministic execution of tasks in real-time applications. Some of the key features of RTOS include:

1. **Deterministic behavior**: RTOS provides deterministic behavior, meaning that the system responds to events within a predictable time frame.

2. **Preemptive scheduling**: RTOS uses preemptive scheduling, which allows high-priority tasks to interrupt lower-priority tasks to ensure timely execution.

3. **Fast context switching**: RTOS is designed to have fast context switching, which allows the system to quickly switch between tasks, reducing the overhead of task switching.

4. **Small memory footprint**: RTOS is designed to have a small memory footprint, which allows it to be used in resource-constrained systems.

5. **Real-time clock**: RTOS typically includes a real-time clock, which provides accurate timekeeping for the system.

6. **Inter-task communication**: RTOS provides mechanisms for inter-task communication, such as message queues, semaphores, and mutexes, which allow tasks to communicate and synchronize with each other.

7. **Interrupt handling**: RTOS provides efficient interrupt handling, which allows the system to quickly respond to external events.

These are some of the key features of RTOS that make it suitable for use in real-time applications.



### Time Services

Time services are an essential component of real-time operating systems and databases. These services provide the ability to measure and keep track of time, which is critical for the correct operation of real-time systems.

Some key points to consider when studying time services in the context of real-time systems are:

1. Time services provide a way to measure the passage of time, typically through the use of timers or clocks. These can be hardware-based, such as a crystal oscillator, or software-based, such as a system clock.

2. Time services are used to schedule tasks and events in real-time systems. This is important for ensuring that tasks are executed at the correct time and in the correct order.

3. Time services can also be used to synchronize multiple systems or components. This is important for ensuring that all parts of a real-time system are operating in a coordinated manner.

4. In real-time databases, time services are used to manage the timing of transactions and to ensure that data is consistent and up-to-date.

5. Time services can be implemented in a variety of ways, depending on the requirements of the system. For example, some systems may use a global time service, while others may use local time services for individual components.

Overall, time services play a crucial role in the operation of real-time systems and databases, and a thorough understanding of these services is essential for anyone studying or working in this field.



### UNIX as RTOS for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- UNIX is a multi-user, multi-tasking operating system that was originally developed in the late 1960s.
- It is widely used in both academic and commercial settings, and has been the foundation for many other operating systems.
- UNIX is known for its stability, security, and flexibility, making it a popular choice for use as a real-time operating system (RTOS).
- An RTOS is an operating system that is designed to process data as it comes in, typically without buffering delays.
- This is important for applications that require a high level of responsiveness, such as industrial control systems, medical equipment, and financial trading systems.
- UNIX can be used as an RTOS because it has features such as preemptive multitasking, real-time scheduling, and inter-process communication.
- These features allow UNIX to handle multiple tasks simultaneously and to prioritize tasks based on their importance, ensuring that critical tasks are completed in a timely manner.
- Additionally, UNIX has a modular design, which allows developers to add or remove components as needed to meet the specific requirements of their real-time application.
- Overall, UNIX is a powerful and versatile operating system that can be used as an RTOS to meet the demanding requirements of real-time applications.



### POSIX Issues for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- POSIX stands for Portable Operating System Interface and is a proposed operating system interface standard based on the popular UNIX operating system. Its main goal is to support application portability at the source-code level.
- POSIX defines a standard way for an application to interface with the operating system. The original POSIX standard defines interfaces to core functions such as file operations, process management, signals, and devices.
- Subsequent releases of POSIX have also been defined to cover real-time extensions and multi-threading.
- The POSIX standard promotes portability of applications across different operating system platforms. This is especially important for applications designed for longevity, where the hardware and software infrastructure may change during the application's life cycle.
- The international standard POSIX standard has been adopted by virtually all operating systems in use and most real-time operating systems including ThreadX, QNX, VxWorks, Integrity, LynxOS, and Unison OS.
- A real-time working group was established in POSIX to develop standards to add POSIX (or UNIX) the OS services that are needed by real-time applications.



### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

Temporal data refers to data that represents the state of an entity at a particular point in time. It is used to track changes in data over time and is commonly used in real-time systems and databases. Some of the characteristics of temporal data include:

1. **Time-stamped**: Temporal data is time-stamped to indicate the time at which the data was recorded or is valid.
2. **Historical**: Temporal data can be used to track changes in data over time, allowing for the analysis of historical trends and patterns.
3. **Dynamic**: Temporal data is dynamic, meaning that it changes over time as new data is recorded or old data is updated.
4. **Consistent**: Temporal data must be consistent, meaning that the data must accurately represent the state of the entity at the time indicated by the time-stamp.
5. **Accurate**: Temporal data must be accurate, meaning that the data must accurately represent the state of the entity at the time indicated by the time-stamp.

Temporal data is commonly used in real-time systems and databases to track changes in data over time and to support real-time decision making. It is an important concept in the field of real-time systems and databases and is essential for the effective management of real-time data.



### Temporal Consistency

Temporal consistency refers to the maintenance of the temporal relationships between data items in a real-time database. In a real-time system, data items have associated temporal constraints, such as deadlines or valid time intervals, that must be satisfied in order for the system to function correctly.

Some key points to consider when studying temporal consistency in the context of real-time operating systems and databases are:

1. Temporal consistency is important for ensuring the correctness of real-time systems, as it ensures that data items are accessed and updated in a timely manner, in accordance with their associated temporal constraints.

2. Temporal consistency can be achieved through the use of various techniques, such as concurrency control mechanisms, real-time scheduling algorithms, and data replication.

3. Temporal consistency is closely related to other concepts in real-time systems, such as temporal validity, temporal accuracy, and temporal coherence.

4. The maintenance of temporal consistency can be challenging in distributed real-time systems, where data items may be replicated across multiple nodes and communication delays can impact the timely access and update of data.

5. The choice of techniques for achieving temporal consistency can have a significant impact on the performance and scalability of a real-time system, and must be carefully considered during the design and implementation of the system.




### Concurrency Control
Concurrency control is a method used to ensure that transactions are executed in a safe and consistent manner in a multi-user environment, such as a real-time database system. It is an essential component of real-time operating systems and databases, as it ensures the integrity of the data and prevents conflicts between transactions.

Some key points to consider when studying concurrency control in the context of real-time systems and databases are:

1. Concurrency control mechanisms are used to manage simultaneous access to shared data by multiple transactions.
2. These mechanisms ensure that the execution of transactions is serializable, meaning that the final state of the database is the same as if the transactions were executed one at a time.
3. Common concurrency control techniques include locking, timestamp ordering, and optimistic concurrency control.
4. The choice of concurrency control technique depends on the specific requirements of the real-time system or database, such as the level of concurrency, the frequency of conflicts, and the performance requirements.
5. Concurrency control is an important factor in the design and implementation of real-time systems and databases, as it can have a significant impact on the performance and reliability of the system.




### Overview of Commercial Real Time databases

- A real-time database is a data store designed to collect, process, and/or enrich an incoming series of data points (i.e., a data stream) in real time, typically immediately after the data is created.
- This term does not refer to a discrete class of database management systems, but rather, applies to several types of databases.
- A real-time database is a database system which uses real-time processing to handle workloads whose state is constantly changing.
- This differs from traditional databases containing persistent data, mostly unaffected by time.
- For example, a stock market changes very rapidly and is dynamic.
- At the most basic level, a commercial real estate database needs to be able to source critical industry information firms use to guide investment decisions.
- Data must not only be accurate, but also reflect real time changes.
- Your team can’t spend their limited time manually inputting or updating information.
- With a commercial real estate database, you’re in a stronger position to detect market patterns, pinpoint trends and work efficiently.
- In short, commercial real estate databases allow you to screen deals faster and more strategically, ultimately propelling your business forward.

