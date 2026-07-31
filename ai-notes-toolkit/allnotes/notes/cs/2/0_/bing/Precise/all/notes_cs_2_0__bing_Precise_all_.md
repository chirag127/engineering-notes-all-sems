

# Real Time System

A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.

The term “real-time system” refers to any information processing system with hardware and software components that perform real-time application functions and can respond to events within predictable and specific time constraints.

Applications of Real-Time Systems include:
- Process Control Systems: used in industrial applications where production is continuous.
- Machine Vision: used to help machines rapidly interpret data so they can see their surroundings.
- Robotics: used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare.

A real-time system has been described as one which "controls an environment by receiving data, processing them, and returning the results sufficiently quickly to affect the environment at that time". For example flight control systems, real-time monitors, etc.

Types of real-time systems based on timing constraints are hard real-time systems and soft real-time systems.



## Unit 1 - Introduction of Real Time System

A real-time system is a computer system that is designed to process data and provide output in a timely manner. The term "real-time" refers to the ability of the system to respond to events or inputs within a specific time frame, which is typically measured in milliseconds or microseconds.

Some key points to consider when discussing real-time systems include:

1. Real-time systems are used in a variety of applications, including industrial control, aviation, and telecommunications.
2. These systems are designed to provide predictable and reliable performance, even in the face of unexpected events or inputs.
3. Real-time systems can be classified as either hard or soft, depending on the consequences of missing a deadline.
4. Hard real-time systems have strict timing constraints, and missing a deadline can result in catastrophic consequences.
5. Soft real-time systems have more relaxed timing constraints, and missing a deadline may result in degraded performance, but not catastrophic consequences.
6. Real-time systems often use specialized hardware and software to achieve their performance goals.
7. The design of real-time systems requires careful consideration of factors such as timing, concurrency, and fault tolerance.




# Unit 1 - Introduction of Real Time System

### Definition

A real-time system is a computer system that is designed to process data and provide outputs within a specific time frame. This time frame is known as the system's deadline, and it is determined by the requirements of the application for which the system is being used. Real-time systems are used in a wide range of applications, including process control, avionics, and multimedia systems.

Some key characteristics of real-time systems include:

- **Deterministic:** Real-time systems must provide outputs within a specific time frame, and the time it takes for the system to respond to an input must be predictable.

- **Responsive:** Real-time systems must be able to respond quickly to changes in their inputs.

- **Reliable:** Real-time systems must be able to operate reliably, even in the face of unexpected events or failures.

- **Concurrent:** Real-time systems often need to perform multiple tasks simultaneously.

Real-time systems can be classified into two main categories: hard real-time systems and soft real-time systems. Hard real-time systems have strict deadlines, and missing a deadline can result in a catastrophic failure of the system. Soft real-time systems, on the other hand, have more flexible deadlines, and missing a deadline may result in degraded performance, but not a complete failure of the system.

In summary, a real-time system is a computer system designed to process data and provide outputs within a specific time frame, with key characteristics including determinism, responsiveness, reliability, and concurrency. These systems can be classified as hard or soft real-time systems, depending on the strictness of their deadlines.



# Typical Real Time Applications

Real-time systems are computer systems that monitor, respond to, or control an external environment. These systems are subject to a real-time constraint, which means that they must respond to events within a certain time frame. Here are some typical real-time applications:

1. **Process Control Systems:** These systems are used to control industrial processes such as chemical plants, oil refineries, and power plants. They monitor and control the physical processes in real-time to ensure that the plant operates safely and efficiently.

2. **Avionics Systems:** These systems are used in aircraft to control flight, navigation, and communication. They must operate in real-time to ensure the safety of the aircraft and its passengers.

3. **Medical Systems:** These systems are used in hospitals to monitor and control medical equipment such as heart monitors, ventilators, and infusion pumps. They must operate in real-time to ensure the safety of the patients.

4. **Telecommunications Systems:** These systems are used to transmit voice, data, and video signals over long distances. They must operate in real-time to ensure that the signals are transmitted and received without delay.

5. **Multimedia Systems:** These systems are used to play audio and video content in real-time. They must operate in real-time to ensure that the content is played smoothly and without interruption.

6. **Defense Systems:** These systems are used by the military to monitor and control weapons, vehicles, and other equipment. They must operate in real-time to ensure the safety and effectiveness of military operations.

7. **Transportation Systems:** These systems are used to control traffic, trains, and other forms of transportation. They must operate in real-time to ensure the safety and efficiency of transportation.

These are just a few examples of the many real-time applications that exist. Real-time systems are essential for the safe and efficient operation of many critical systems in our society.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Release times refer to the specific times at which the notes for Unit 1 - Introduction of Real Time System in the subject of Real Time System will be made available to students.
- These release times may vary depending on the institution, course, and instructor.
- It is important for students to be aware of the release times for the notes in order to plan their study schedule accordingly.
- Students can typically find information about the release times for the notes on their course syllabus or by contacting their instructor.
- It is recommended that students regularly check for updates regarding the release times for the notes to ensure that they have the most up-to-date information.




### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Deadlines refer to the time by which a specific task or activity must be completed.
- In the context of Real Time Systems, deadlines are critical as they determine the time by which a specific computation or response must be completed.
- Missing a deadline in a Real Time System can have severe consequences, such as system failure or loss of data.
- It is important to carefully plan and manage deadlines in Real Time Systems to ensure that all tasks are completed on time.
- There are various techniques and methods that can be used to manage deadlines in Real Time Systems, such as scheduling algorithms and priority assignment.
- It is important to regularly review and monitor deadlines to ensure that they are being met and to make adjustments as necessary.




# Timing Constraints

Timing constraints are an essential aspect of real-time systems. These constraints specify the time limits within which a task must be completed. In real-time systems, the correctness of the system depends not only on the logical results of the computations but also on the time at which the results are produced.

There are two types of timing constraints in real-time systems:

1. **Hard real-time constraints:** These constraints specify a strict deadline for the completion of a task. Failure to meet the deadline can result in catastrophic consequences, such as loss of life or damage to equipment. Examples of hard real-time systems include air traffic control systems and nuclear power plant control systems.

2. **Soft real-time constraints:** These constraints specify a deadline for the completion of a task, but the consequences of missing the deadline are not catastrophic. Instead, the quality of service may degrade, but the system will continue to function. Examples of soft real-time systems include multimedia systems and online gaming systems.

In summary, timing constraints are a critical aspect of real-time systems, and the type of constraint (hard or soft) determines the consequences of missing a deadline. It is essential to carefully design and implement real-time systems to ensure that all timing constraints are met.



### Hard Real Time Systems

- A hard real-time system is also known as an immediate real-time system.
- It is a hardware or software that must operate within the confines of a stringent deadline .
- The application is considered to have failed if it does not complete its function within the given allocated time span .
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- Hard real-time systems are typically found interacting at a low level with physical hardware, in embedded systems.
- Early video game systems such as the Atari 2600 and Cinematronics vector graphics had hard real-time requirements because of the nature of the graphics and timing hardware.
- In hard real-time system, the size of data is fixed and response time is in milliseconds.
- Peak load performance should be predictable and safety is critical.




### Soft Real Time Systems

- A soft real-time operating system is one where there is a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system.
- Soft real-time systems, though less precise, can be run on multiple cores and impose fewer restrictions on applications.
- Soft real-time is when a system continues to function even if it’s unable to execute within an allotted time.
- If the system has missed its deadline, it will not result in critical consequences.
- The system can continue to function, though with undesirable lower quality of output.
- Soft real-time systems are typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems include software that maintains and updates the flight plans for commercial airliners.



# Reference Models for Real Time Systems

Real-time systems are computer systems that monitor, respond to, or control an external environment. This environment is connected to the computer system through sensors, actuators, and other input-output interfaces. The system must respond to events within a specified time frame, otherwise, the system's performance will degrade or fail.

There are several reference models for real-time systems, including:

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-based scheduling algorithm for real-time systems. It assigns priorities to tasks based on their rate of execution, with the highest rate tasks being assigned the highest priority.

2. **Earliest Deadline First (EDF)**: This is another priority-based scheduling algorithm for real-time systems. It assigns priorities to tasks based on their deadlines, with the earliest deadline tasks being assigned the highest priority.

3. **Sporadic Server**: This is a scheduling algorithm that is used to handle aperiodic tasks in real-time systems. It assigns a server task to handle the execution of aperiodic tasks, and the server task is scheduled using one of the other scheduling algorithms (such as RMS or EDF).

4. **Constant Bandwidth Server (CBS)**: This is a scheduling algorithm that is used to handle tasks with variable execution times in real-time systems. It assigns a server task to handle the execution of these tasks, and the server task is scheduled using one of the other scheduling algorithms (such as RMS or EDF).

These are some of the reference models used in real-time systems. Each model has its own advantages and disadvantages, and the choice of model depends on the specific requirements of the system being designed.



### Processors and Resources

Processors and resources are essential components of a real-time system. Here are some key points to consider when studying this topic:

1. A processor is the central processing unit (CPU) of a computer system that executes instructions and performs calculations.
2. In a real-time system, the processor must be able to execute tasks within a specified time frame to meet the system's real-time requirements.
3. Resources refer to the hardware and software components that are required for the system to function, such as memory, storage, and input/output devices.
4. Resource management is crucial in a real-time system to ensure that tasks are executed efficiently and within their time constraints.
5. Real-time systems may use specialized processors and resources that are designed to meet the specific needs of the system, such as low power consumption or high-speed processing.
6. The allocation and scheduling of processors and resources can have a significant impact on the performance of a real-time system.




### Temporal Parameters of Real Time Workload

Real-time systems are computer systems that are designed to operate within a specific time frame. The temporal parameters of a real-time workload refer to the timing constraints that must be met by the system in order to function correctly. These parameters include:

1. **Deadline**: This is the time by which a task must be completed. Deadlines can be hard or soft. A hard deadline is one that must be met, while a soft deadline is one that can be missed without causing a system failure.

2. **Period**: This is the time interval between the start of two consecutive instances of a task. The period is typically constant for periodic tasks, but can vary for aperiodic tasks.

3. **Release time**: This is the time at which a task becomes ready for execution. The release time is typically specified relative to the start of the system or the start of a hyperperiod.

4. **Response time**: This is the time it takes for a task to complete once it has been released. The response time includes the time the task spends waiting for resources, as well as the time it takes to execute.

5. **Jitter**: This is the variation in the response time of a task. Jitter can be caused by variations in the release time, execution time, or resource availability.

These temporal parameters are critical to the correct operation of a real-time system, and must be carefully managed to ensure that the system meets its timing constraints.



# Periodic Task Model

In the context of real-time systems, a periodic task model is a commonly used model for representing recurring tasks. In this model, tasks are characterized by the following parameters:

1. **Period**: The time interval between two consecutive releases of the task.
2. **Computation time**: The worst-case execution time of the task.
3. **Deadline**: The time by which the task must complete its execution.

In a periodic task model, tasks are released periodically, with each release separated by the task's period. The task must complete its execution within its deadline, which is typically equal to or less than its period.

This model is widely used in the design and analysis of real-time systems, as it provides a simple and predictable way to represent recurring tasks. It is particularly useful for systems with hard real-time constraints, where tasks must complete within strict deadlines.



# Precedence Constraints and Data Dependency

Precedence constraints and data dependencies are important concepts in real-time systems. They refer to the relationships between tasks and the order in which they must be executed.

- **Precedence constraints** specify the order in which tasks must be executed. For example, in a manufacturing process, a task that assembles a product may need to be completed before a task that packages the product.

- **Data dependencies** occur when the output of one task is used as the input of another task. For example, in a weather forecasting system, a task that collects data from sensors may need to be completed before a task that processes the data to generate a forecast.

- In real-time systems, precedence constraints and data dependencies must be carefully managed to ensure that tasks are completed in the correct order and that data is available when it is needed.

- Failure to properly manage precedence constraints and data dependencies can result in incorrect or incomplete results, missed deadlines, and other problems.

- Real-time scheduling algorithms and techniques can be used to manage precedence constraints and data dependencies in real-time systems.

- These algorithms and techniques take into account the timing requirements of tasks, the availability of resources, and other factors to ensure that tasks are executed in the correct order and that data is available when it is needed.

- In summary, precedence constraints and data dependencies are important concepts in real-time systems that must be carefully managed to ensure the correct and timely execution of tasks. Real-time scheduling algorithms and techniques can be used to manage these relationships and ensure the correct operation of the system.



## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning CPU time to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines, while maximizing system performance.

1. **Hard Real-Time Systems**: In hard real-time systems, missing a deadline can result in catastrophic consequences. Therefore, the scheduling algorithm must guarantee that all tasks meet their deadlines.

2. **Soft Real-Time Systems**: In soft real-time systems, missing a deadline is not catastrophic, but can result in degraded system performance. The scheduling algorithm tries to ensure that all tasks meet their deadlines, but it is not guaranteed.

3. **Rate Monotonic Scheduling (RMS)**: RMS is a priority-based scheduling algorithm for periodic tasks in hard real-time systems. The priority of a task is inversely proportional to its period, i.e., the shorter the period, the higher the priority.

4. **Earliest Deadline First (EDF)**: EDF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is determined by its absolute deadline, i.e., the earlier the deadline, the higher the priority.

5. **Least Laxity First (LLF)**: LLF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is determined by its laxity, i.e., the difference between its deadline and its remaining computation time. The smaller the laxity, the higher the priority.

6. **Scheduling in Multiprocessor Systems**: In multiprocessor systems, tasks can be scheduled on multiple processors. There are two main approaches to scheduling in multiprocessor systems: partitioned scheduling and global scheduling.

7. **Partitioned Scheduling**: In partitioned scheduling, tasks are statically assigned to processors, and each processor runs its own scheduling algorithm.

8. **Global Scheduling**: In global scheduling, tasks are dynamically assigned to processors, and a single scheduling algorithm is used to schedule tasks on all processors.



# Common Approaches to Real Time Scheduling

Real-time scheduling is the process of assigning CPU time to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines while maximizing system performance. Here are some common approaches to real-time scheduling:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline, the higher the priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. Laxity is the difference between the time remaining until the task's deadline and the time required to complete the task.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of each task is fixed and does not change during the execution of the system.

5. **Round Robin Scheduling:** This is a simple scheduling algorithm where each task is given an equal time slice to execute. If a task does not complete within its time slice, it is preempted and moved to the end of the queue.

These are some of the common approaches to real-time scheduling. Each approach has its advantages and disadvantages, and the choice of scheduling algorithm depends on the specific requirements of the real-time system.



### Clock Driven Approach

The clock-driven approach is a real-time scheduling method used in real-time systems. It is also known as time-driven or table-driven scheduling. Here are some key points to note about this approach:

1. In the clock-driven approach, the scheduler uses a pre-computed schedule or a table to determine when tasks should be executed.
2. The schedule is computed offline, before the system starts running, and is based on the worst-case execution times of the tasks, their deadlines, and their periods.
3. The schedule is typically stored in a table, which is indexed by the current time. At each clock tick, the scheduler consults the table to determine which task, if any, should be executed next.
4. The clock-driven approach is well-suited for periodic tasks with fixed deadlines and execution times.
5. This approach is commonly used in hard real-time systems, where missing a deadline can have catastrophic consequences.
6. One advantage of the clock-driven approach is its predictability. Since the schedule is computed offline, the system behavior is deterministic and can be analyzed to ensure that all deadlines are met.
7. However, the clock-driven approach is less flexible than other scheduling methods, such as priority-driven scheduling. It is not well-suited for tasks with variable execution times or for aperiodic tasks.
8. Additionally, the clock-driven approach can be computationally intensive, as the schedule must be recomputed whenever the system configuration changes.




### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the relative importance of the task. The scheduler allocates CPU time to each task based on its weight, with higher-weighted tasks receiving more CPU time than lower-weighted tasks.

The steps involved in the WRR algorithm are as follows:

1. The scheduler maintains a list of all tasks, sorted in descending order of their weights.
2. The scheduler selects the first task in the list and allocates it a time slice equal to its weight.
3. The task is then moved to the end of the list, and the next task is selected.
4. This process is repeated until all tasks have been allocated a time slice.
5. The scheduler then starts again from the beginning of the list.

The WRR algorithm ensures that higher-weighted tasks are given priority over lower-weighted tasks, while still ensuring that all tasks receive some CPU time. This makes it a suitable algorithm for real-time systems, where tasks may have different levels of importance and urgency.



### Priority Driven Approach

Priority driven approach is a scheduling method used in real-time systems. In this approach, tasks are assigned priorities based on their importance and urgency. The scheduler then selects the task with the highest priority for execution. This approach is commonly used in real-time systems because it ensures that the most important tasks are completed first.

Some key points to remember about priority driven approach are:

1. Tasks are assigned priorities based on their importance and urgency.
2. The scheduler selects the task with the highest priority for execution.
3. This approach ensures that the most important tasks are completed first.
4. Priority driven approach is commonly used in real-time systems.




### Dynamic Versus Static Systems

- **Dynamic systems** are systems that change over time. In the context of real-time scheduling, this means that the scheduling decisions are made at runtime, based on the current state of the system.

- **Static systems**, on the other hand, are systems that do not change over time. In the context of real-time scheduling, this means that the scheduling decisions are made offline, before the system starts running, and do not change during runtime.

- The choice between a dynamic and a static system depends on the specific requirements of the system. Dynamic systems are more flexible and can adapt to changing conditions, but they require more computational resources to make scheduling decisions at runtime. Static systems are less flexible, but they require less computational resources, as the scheduling decisions are made offline.

- In real-time systems, it is important to ensure that all tasks meet their deadlines. In a dynamic system, the scheduler can make decisions at runtime to ensure that all tasks meet their deadlines, even if the system conditions change. In a static system, the scheduler must ensure that all tasks will meet their deadlines under all possible conditions, as the scheduling decisions cannot be changed at runtime.

- In summary, the choice between a dynamic and a static system depends on the specific requirements of the system, including its flexibility, computational resources, and the need to ensure that all tasks meet their deadlines.



# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two scheduling algorithms used in real-time systems. These algorithms are used to schedule tasks in a way that ensures that all tasks meet their deadlines.

- **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest absolute deadline is scheduled first. EDF is an optimal algorithm for scheduling tasks on a single processor, meaning that if a feasible schedule exists, EDF will find it.

- **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time, which is the amount of time left until the task's deadline minus the task's remaining execution time. The task with the least slack time is scheduled first. LST is also an optimal algorithm for scheduling tasks on a single processor.

In summary, both EDF and LST are optimal algorithms for scheduling tasks on a single processor in real-time systems. They ensure that all tasks meet their deadlines if a feasible schedule exists.



# Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems (RTOS) with a static-priority scheduling class.
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority.
- It is a procedure for assigning fixed priorities to tasks to maximize their “schedulability”.
- A task set is considered schedulable if all tasks meet all deadlines all the time.
- The algorithm is simple: Assign the priority of each task according to its period, so that the shorter the period the higher the priority.



# Offline Versus Online Scheduling

Offline scheduling and online scheduling are two approaches to scheduling tasks in a real-time system.

## Offline Scheduling
- In offline scheduling, the schedule is determined before the system starts executing.
- The schedule is computed based on the worst-case execution times of the tasks and their deadlines.
- The schedule is fixed and does not change during the execution of the system.
- Offline scheduling is suitable for systems with periodic tasks and known worst-case execution times.

## Online Scheduling
- In online scheduling, the schedule is determined at runtime.
- The scheduler makes decisions based on the current state of the system, such as the current execution times of the tasks and their deadlines.
- The schedule can change during the execution of the system to adapt to changes in the system.
- Online scheduling is suitable for systems with aperiodic tasks or tasks with unknown or varying execution times.

In summary, offline scheduling is suitable for systems with predictable behavior, while online scheduling is suitable for systems with unpredictable behavior. The choice between offline and online scheduling depends on the characteristics of the system and its tasks.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

In real-time systems, there are three types of tasks: periodic, aperiodic, and sporadic. Periodic tasks have a fixed period and deadline, while aperiodic and sporadic tasks have variable arrival times and deadlines. Scheduling aperiodic and sporadic jobs in priority-driven and clock-driven systems is an important aspect of real-time scheduling.

## Priority Driven Systems

In priority-driven systems, tasks are assigned priorities based on their importance, and the scheduler selects the highest priority task to execute. Aperiodic and sporadic jobs can be scheduled using several techniques in priority-driven systems:

1. **Background Scheduling**: Aperiodic and sporadic jobs are assigned the lowest priority and are executed only when no other higher priority tasks are ready to execute. This approach ensures that periodic tasks are not affected by the execution of aperiodic and sporadic jobs, but it may result in long response times for aperiodic and sporadic jobs.

2. **Polling Servers**: A polling server is a periodic task with a fixed period and a fixed execution time. At each period, the server checks if there are any aperiodic or sporadic jobs ready to execute. If there are, the server executes one of the jobs for its fixed execution time. This approach can reduce the response time of aperiodic and sporadic jobs, but it may affect the schedulability of periodic tasks.

3. **Deferrable Servers**: A deferrable server is similar to a polling server, but it can defer its execution if there are no aperiodic or sporadic jobs ready to execute. This approach can improve the schedulability of periodic tasks, but it may result in longer response times for aperiodic and sporadic jobs.

4. **Sporadic Servers**: A sporadic server is a task with a minimum inter-arrival time and a fixed execution time. When an aperiodic or sporadic job arrives, the server is activated and executes the job for its fixed execution time. This approach can provide good response times for aperiodic and sporadic jobs, but it may affect the schedulability of periodic tasks.

## Clock Driven Systems

In clock-driven systems, tasks are scheduled based on a pre-computed schedule. Aperiodic and sporadic jobs can be scheduled using several techniques in clock-driven systems:

1. **Time-Triggered Scheduling**: In time-triggered scheduling, aperiodic and sporadic jobs are assigned specific time slots in the schedule. When a job arrives, it is executed in its assigned time slot. This approach ensures that periodic tasks are not affected by the execution of aperiodic and sporadic jobs, but it may result in long response times for aperiodic and sporadic jobs.

2. **Slack Stealing**: In slack stealing, the scheduler computes the slack time, which is the amount of time that can be used to execute aperiodic and sporadic jobs without affecting the schedulability of periodic tasks. When an aperiodic or sporadic job arrives, the scheduler checks if there is enough slack time to execute the job. If there is, the job is executed, and the slack time is updated. This approach can provide good response times for aperiodic and sporadic jobs, but it requires the scheduler to compute the slack time at runtime.

In conclusion, scheduling aperiodic and sporadic jobs in priority-driven and clock-driven systems is a complex task that requires careful consideration of the trade-offs between the response time of aperiodic and sporadic jobs and the schedulability of periodic tasks. Several techniques can be used to schedule aperiodic and sporadic jobs in both priority-driven and clock-driven systems, and the choice of technique depends on the specific requirements of the system.



## Unit 3 - Resources Sharing

1. **Introduction:** Resource sharing refers to the sharing of resources among multiple users or systems. This can include sharing of hardware, software, data, or information.

2. **Types of Resource Sharing:** There are several types of resource sharing, including:
    - **Hardware Resource Sharing:** This involves sharing of physical resources such as printers, scanners, and storage devices among multiple users or systems.
    - **Software Resource Sharing:** This involves sharing of software resources such as applications and operating systems among multiple users or systems.
    - **Data Resource Sharing:** This involves sharing of data resources such as databases and files among multiple users or systems.
    - **Information Resource Sharing:** This involves sharing of information resources such as knowledge and expertise among multiple users or systems.

3. **Benefits of Resource Sharing:** Resource sharing can provide several benefits, including:
    - **Cost Savings:** By sharing resources, organizations can reduce the cost of purchasing and maintaining multiple resources.
    - **Improved Efficiency:** Resource sharing can improve efficiency by allowing multiple users or systems to access the same resources simultaneously.
    - **Increased Collaboration:** Resource sharing can facilitate collaboration among users or systems by allowing them to share data and information.

4. **Challenges of Resource Sharing:** Despite its benefits, resource sharing can also present several challenges, including:
    - **Security:** Sharing resources can increase the risk of unauthorized access or data breaches.
    - **Compatibility:** Ensuring compatibility among different systems and resources can be challenging.
    - **Management:** Managing shared resources can be complex and require specialized expertise.

5. **Conclusion:** Resource sharing is an important concept that can provide significant benefits, but it also presents several challenges that must be carefully managed. By understanding the different types of resource sharing, their benefits, and their challenges, organizations can make informed decisions about how to share resources effectively.



# Effect of Resource Contention and Resource Access Control (RAC)

- A resource access-control protocol, or simply an access-control protocol, is a set of rules that govern when and under what conditions each request for resource is granted and how jobs requiring resources are scheduled .
- Resource contention often leads to performance degradation in the applications contending for the shared resource. This can cause unexpected project delays, because processes contending for resources will be stalled until they can access the resource .
- Resource Access Control Protocols work to reduce the undesirable effect of resource contention. Resource contention affects the execution behavior and schedulability of jobs .
- One of the major objectives of resource access control is to minimize the undesirable effects of resource allocation .
- Access to resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section. If a lock request fails, the requesting job is blocked; a job holding a lock cannot be preempted by a higher priority job needing that lock .



### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, even if a higher priority task becomes ready to run.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- By ensuring that only one task can access the shared resource at a time, non-preemptive critical sections prevent race conditions and other synchronization issues.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms, such as semaphores, mutexes, or disabling interrupts.
- It is important to use non-preemptive critical sections judiciously, as they can impact the responsiveness of the system by delaying the execution of higher priority tasks.
- Careful design and analysis are required to ensure that the use of non-preemptive critical sections does not result in priority inversion or other undesirable behavior.



# Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are two protocols belonging to the priority inheritance protocols class. Both protocols solve the uncontrolled priority inversion problem.

## Priority-Inheritance Protocol

The basic priority inheritance protocol is a synchronization protocol for shared resources in real-time systems. It is used to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.

## Priority-Ceiling Protocol

The priority ceiling protocol is another synchronization protocol for shared resources in real-time systems. It is better than the priority inheritance protocol in many ways. It reduces the worst-case task-blocking time to at most the duration of execution of a single critical section of a lower-priority task. This protocol also prevents the formation of deadlocks.

The allocation rule of priority ceiling protocol is different from that of priority inheritance protocol. In the case of priority ceiling protocol, a job may be denied its requested resource even when the resource is free at the time.

## Comparison

Priority Inheritance protocols are greedy while Priority Ceiling protocols are not. The priority ceiling protocol is better than the priority inheritance protocol in many ways.

## References

: Priority inheritance protocols: an approach to real-time synchronization | IEEE Journals & Magazine | IEEE Xplore
: Priority Ceiling Protocol - GeeksforGeeks
: Priority ceiling protocol - Wikipedia
: Difference between Priority Inheritance and Priority Ceiling Protocols - Benchpartner



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways.
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource.
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point. Both variants work by temporarily raising the priorities of tasks.
- The ceiling priority protocol Stack-Based Priority Ceiling Protocol Based on original work to allow jobs to share a run-time stack, extended to control access to other resources .
- In the statement of the rules of the stack-based, priority-ceiling protocol, we again use the term (current) ceiling ˆ f (t) of the system, which is the highest-priority ceiling of all the resources that are in use at time t Ω. is a nonexisting priority level that is lower than the lowest priority of all jobs.




# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority among all the tasks that may access the resource. For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The protocol specifies a dynamic priority ceiling for each critical section which is the earliest deadline of jobs which are currently in or will enter the critical section. Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section which is in use .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behavior of the two variants is different .




# Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by low priority tasks holding shared resources.

Here are some key points to note about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the current preemption ceiling of the system, which is the maximum of the preemption ceilings of all resources currently locked by other tasks.
3. When a task locks a resource, the system's preemption ceiling is raised to the preemption ceiling of the resource.
4. A task can be preempted only by tasks with a priority higher than the current preemption ceiling of the system.
5. When a task releases a resource, the system's preemption ceiling is lowered to the maximum of the preemption ceilings of all resources still locked by other tasks.

This protocol ensures that high priority tasks are not blocked by low priority tasks holding shared resources, and also prevents unbounded priority inversion. It is commonly used in real-time systems to ensure timely execution of high priority tasks.



### Access Control in Multiple-Unit Resources

Access control in multiple-unit resources refers to the management of access to resources that have multiple units or instances. In a real-time system, these resources may include processors, memory, and input/output devices, among others. The goal of access control is to ensure that the system operates efficiently and effectively while maintaining the desired level of security and protection.

Some key points to consider when implementing access control in multiple-unit resources include:

1. **Resource allocation**: The system must have a mechanism for allocating resources to tasks or processes that require them. This may involve assigning priorities to tasks or using a scheduling algorithm to determine which tasks should be given access to resources at any given time.

2. **Resource protection**: The system must have measures in place to protect resources from unauthorized access or use. This may involve implementing access controls, such as user authentication and authorization, to ensure that only authorized users can access resources.

3. **Resource sharing**: In a multiple-unit resource environment, it is often necessary for tasks or processes to share resources. The system must have a mechanism for managing resource sharing to ensure that all tasks have fair access to resources and that resource contention is minimized.

4. **Resource monitoring**: The system must have a mechanism for monitoring resource usage to ensure that resources are being used efficiently and effectively. This may involve tracking resource usage and implementing measures to prevent resource overuse or underuse.

In summary, access control in multiple-unit resources is an important aspect of resource sharing in real-time systems. It involves managing the allocation, protection, sharing, and monitoring of resources to ensure that the system operates efficiently and effectively while maintaining the desired level of security and protection.



### Controlling Concurrent Accesses to Data Objects

Controlling concurrent accesses to data objects is an important aspect of resource sharing in real-time systems. Here are some key points to consider:

1. **Concurrency control** is the process of managing simultaneous access to shared data objects by multiple processes or threads to ensure data consistency and integrity.

2. **Locking** is a common method used to control concurrent access to data objects. It involves placing a lock on a data object to prevent other processes or threads from accessing it until the lock is released.

3. **Deadlocks** can occur when multiple processes or threads are waiting for each other to release locks on data objects. Deadlock prevention and detection algorithms can be used to avoid or resolve deadlocks.

4. **Priority inversion** can occur when a high-priority process or thread is blocked by a lower-priority process or thread holding a lock on a data object. Priority inheritance and priority ceiling protocols can be used to prevent or mitigate priority inversion.

5. **Transactional memory** is an alternative approach to controlling concurrent access to data objects. It allows multiple processes or threads to execute transactions on shared data objects concurrently, with the system ensuring data consistency and integrity.

These are some of the key concepts and techniques used to control concurrent accesses to data objects in real-time systems. Understanding and applying these concepts can help ensure that shared data objects are accessed and updated in a consistent and reliable manner.



## Unit 4 - Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. This type of communication is essential for many applications, including video conferencing, online gaming, and remote control systems.

Some key points to consider when discussing real-time communication include:

1. **Latency**: Latency refers to the time it takes for a signal to travel from one point to another. In real-time communication, low latency is essential to ensure that the communication is as close to instantaneous as possible.

2. **Bandwidth**: Bandwidth refers to the amount of data that can be transmitted over a communication channel in a given period of time. High bandwidth is necessary for applications that require the transmission of large amounts of data, such as video conferencing.

3. **Reliability**: Reliability refers to the ability of a communication system to deliver data without errors. In real-time communication, reliability is important to ensure that the information being transmitted is received correctly.

4. **Security**: Security refers to the measures taken to protect the confidentiality and integrity of the information being transmitted. In real-time communication, security is important to prevent unauthorized access to the information being transmitted.

5. **Protocols**: Protocols are the rules and standards that govern the exchange of information between parties. In real-time communication, protocols are used to ensure that the communication is carried out in an orderly and predictable manner.

Real-time communication is an essential component of many modern applications and is a topic of ongoing research and development. By understanding the key concepts and considerations involved in real-time communication, we can better design and implement systems that meet the needs of users.



# Basic Concepts in Real time Communication

Real-time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real-time communication include:
- Voice over landlines and mobile phones
- Online communication that happens in real-time

Effective communication is about more than just exchanging information. It's about understanding the emotion and intentions behind the information.

Some skills for effective communication include:
1. Becoming an engaged listener
2. Paying attention to nonverbal signals
3. Keeping stress in check
4. Asserting yourself



### Soft and Hard RT Communication systems

Real-time communication systems can be classified into two categories: soft real-time and hard real-time.

1. **Soft real-time communication systems** are those in which the occasional delay or loss of data is acceptable. These systems are designed to handle a certain level of delay or data loss without significantly impacting the overall performance of the system. Examples of soft real-time communication systems include video streaming, online gaming, and VoIP (Voice over IP) telephony.

2. **Hard real-time communication systems** are those in which any delay or loss of data is unacceptable. These systems are designed to provide guaranteed, deterministic response times and are typically used in safety-critical applications such as aviation, industrial control, and medical systems. Examples of hard real-time communication systems include avionics communication systems, industrial control systems, and medical monitoring systems.

In summary, the main difference between soft and hard real-time communication systems is the level of tolerance for delay and data loss. Soft real-time systems can tolerate some delay and data loss, while hard real-time systems cannot. It is important to choose the appropriate type of real-time communication system for the specific application to ensure that the system performs as expected.



### Model of Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. In the context of real-time systems, this communication must occur within a specified time frame to ensure the correct functioning of the system. Here are some key points to consider when discussing the model of real-time communication:

1. **Timing constraints:** Real-time communication must adhere to strict timing constraints to ensure that the system functions correctly. This means that messages must be delivered within a specified time frame, and any delays could result in system failure.

2. **Reliability:** The communication between parties must be reliable to ensure that messages are delivered correctly and without error. This can be achieved through the use of error detection and correction techniques, as well as the use of redundant communication channels.

3. **Synchronization:** In many real-time systems, it is important for the parties involved in the communication to be synchronized. This means that they must operate on the same time scale and be able to coordinate their actions.

4. **Protocols:** Real-time communication often relies on the use of specific protocols to ensure that the timing constraints are met and that the communication is reliable. These protocols can include time-triggered protocols, event-triggered protocols, and hybrid protocols.

5. **Network topology:** The topology of the network used for real-time communication can also play a role in the model. For example, a star topology may be used to ensure that all parties can communicate directly with one another, while a ring topology may be used to ensure that messages are delivered in a predictable manner.

Overall, the model of real-time communication must take into account the specific requirements of the system, including its timing constraints, reliability, synchronization, and the use of appropriate protocols and network topologies. By carefully considering these factors, it is possible to design a real-time communication model that meets the needs of the system and ensures its correct functioning.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- According to a priority-based service discipline, the transmission of ready packets is scheduled in a priority-driven manner. 
- Weighted Fair Queuing (WFQ) and Weighted Round Robin (WRR) scheduling are common approaches for scheduling packets in real-time communication networks .
- The Priority-Based Service discipline is based on the Strict Priority (SP) discipline, with the difference that each priority queue is assigned a parameter, as in WFQ and WRR disciplines .
- The parameter determines the probability with which its corresponding queue is served when it is polled by the server .
- In a switched network, a downstream switch can begin to transmit an earlier portion of the message as soon as it receives the portion. It does not have to wait for the arrival of the rest of the message .
- The Weighted Round-Robin approach does not require a sorted priority queue, only a round-robin queue .
- Many class service disciplines used for output queued switches have been proposed in the literature, including the Class-Based Weighted Fair Queuing (CBWFQ) and the Weighted Fair Priority Queuing (WFPQ) techniques .
- A new WRR algorithm, called Rate-controlled Frame-based Weighted Round Robin (RFWRR), has been proposed, which guarantees the delay jitter bound and satisfies a diverse set of delay requirements. The proposed algorithm divides the scheduler into two components: a rate controller and a frame-based WRR server .



# Medium Access Control Protocols for Broadcast Networks

Medium Access Control (MAC) protocols are used to coordinate the access of multiple devices to a shared communication medium. In broadcast networks, where all devices can potentially communicate with each other, MAC protocols play a crucial role in ensuring efficient and fair use of the shared medium.

Some common MAC protocols for broadcast networks include:

1. **Aloha**: Aloha is a simple MAC protocol where devices transmit data whenever they have data to send. If two or more devices transmit at the same time, a collision occurs and the data is lost. To reduce the probability of collisions, devices can use a random backoff time before retransmitting the data.

2. **Carrier Sense Multiple Access (CSMA)**: In CSMA, devices first listen to the medium to check if it is idle before transmitting data. If the medium is busy, the device waits for a random backoff time before trying again. This reduces the probability of collisions but does not eliminate them completely.

3. **Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)**: CSMA/CA is an extension of CSMA where devices use a handshake mechanism to reserve the medium before transmitting data. This further reduces the probability of collisions but increases the overhead and delay.

4. **Time Division Multiple Access (TDMA)**: In TDMA, time is divided into slots and each device is assigned a specific time slot to transmit data. This eliminates collisions but requires synchronization and may result in inefficient use of the medium if some devices have more data to transmit than others.

These are some of the common MAC protocols used in broadcast networks. Each protocol has its own advantages and disadvantages and the choice of protocol depends on the specific requirements of the network.



# Internet and Resource Reservation Protocols

Unit 4 - Real Time Communication in the subject of Real Time System

1. **Introduction**: The Internet is a global network of interconnected computer networks that communicate using standardized communication protocols. Resource reservation protocols are used to reserve resources such as bandwidth, processing power, and memory for real-time communication.

2. **Resource Reservation Protocol (RSVP)**: RSVP is a protocol used to reserve resources for real-time communication on the Internet. It operates at the transport layer of the OSI model and is used to reserve resources for both unicast and multicast communication.

3. **RSVP Operation**: RSVP operates by sending messages between the sender and receiver of a communication. The sender sends a PATH message to the receiver, which contains information about the resources required for the communication. The receiver then sends a RESV message back to the sender, which reserves the resources for the communication.

4. **RSVP Messages**: RSVP uses several types of messages to reserve resources and manage communication. These include PATH, RESV, PATHERR, RESVERR, PATHTEAR, and RESVTEAR messages.

5. **RSVP and Quality of Service (QoS)**: RSVP can be used to provide Quality of Service (QoS) for real-time communication. QoS refers to the ability to provide a guaranteed level of performance for a communication, such as a minimum bandwidth or maximum delay.

6. **Other Resource Reservation Protocols**: There are several other resource reservation protocols that can be used for real-time communication on the Internet. These include the Next Steps in Signaling (NSIS) protocol and the Common Open Policy Service (COPS) protocol.

7. **Conclusion**: Resource reservation protocols, such as RSVP, are important for ensuring that real-time communication on the Internet can meet the performance requirements of the application. These protocols allow resources to be reserved for communication, ensuring that the communication can proceed with the desired level of performance.



## Unit 5 - Real Time Operating Systems and Databases

1. **Real-Time Operating Systems (RTOS)**: An RTOS is an operating system designed to serve real-time applications that process data as it comes in, typically without buffer delays. It is time-bound and guarantees a predictable response time to events.

2. **Characteristics of RTOS**: Some of the key characteristics of an RTOS include determinism, responsiveness, user control, reliability, and fail-safe operation.

3. **Types of RTOS**: There are two main types of RTOS: Hard Real-Time Systems and Soft Real-Time Systems. Hard Real-Time Systems have strict deadlines and missing a deadline can result in a catastrophic failure. Soft Real-Time Systems have more flexible deadlines and missing a deadline may result in degraded performance but not a catastrophic failure.

4. **Real-Time Databases**: A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing. It is designed to provide a predictable response time to transactions and queries.

5. **Characteristics of Real-Time Databases**: Some of the key characteristics of real-time databases include concurrency control, predictability, data consistency, and temporal data management.

6. **Applications of Real-Time Systems**: Real-time systems are used in a wide range of applications, including industrial control systems, avionics, medical systems, telecommunications, and multimedia systems.



# Features of RTOS

Real-Time Operating Systems (RTOS) are operating systems designed for real-time applications. These applications require a quick response time and high reliability. Here are some of the key features of RTOS:

1. **Deterministic**: RTOS is designed to provide a predictable response time to events. This means that the time it takes for the system to respond to an event is known and consistent.

2. **Preemptive**: RTOS uses a preemptive scheduling algorithm, which means that the highest priority task will always be executed first. This ensures that critical tasks are completed on time.

3. **Multitasking**: RTOS supports multitasking, which means that multiple tasks can be executed concurrently. This allows for efficient use of system resources.

4. **Memory Management**: RTOS provides efficient memory management, which ensures that memory is allocated and deallocated in a timely and efficient manner.

5. **Inter-task Communication**: RTOS provides mechanisms for inter-task communication, such as message queues, semaphores, and mutexes. This allows tasks to communicate and synchronize with each other.

6. **Reliability**: RTOS is designed to be reliable and to provide a high level of fault tolerance. This ensures that the system can continue to operate even in the event of a failure.

These are some of the key features of RTOS that make it suitable for real-time applications. These features ensure that the system can respond quickly and reliably to events, making it an ideal choice for applications that require a high level of responsiveness and reliability.



### Time Services

Time services are an essential component of real-time operating systems and databases. These services provide the ability to measure and manage the passage of time, which is critical for the correct operation of real-time systems.

Some of the key features of time services in real-time systems include:

1. **Clock synchronization:** This refers to the process of ensuring that the clocks of all the nodes in a distributed system are synchronized, so that they all show the same time. This is important for coordinating the actions of the different nodes in the system.

2. **Time-stamping:** Time-stamping is the process of recording the time at which an event occurs. This is important for tracking the sequence of events in a real-time system, and for ensuring that actions are taken in the correct order.

3. **Timers:** Timers are used to trigger actions at specific points in time. For example, a timer might be used to trigger an alarm at a specific time, or to start a process after a certain amount of time has elapsed.

4. **Real-time clocks:** Real-time clocks are hardware devices that keep track of the current time, even when the system is powered off. These clocks are typically battery-powered, and are used to maintain the correct time when the system is restarted.

Overall, time services play a crucial role in ensuring the correct operation of real-time systems, by providing the ability to measure and manage the passage of time. These services are essential for coordinating the actions of different nodes in a distributed system, and for ensuring that events occur in the correct sequence.



# UNIX as RTOS

- UNIX is a multi-user, multi-tasking operating system that was originally developed in the late 1960s.
- It is widely used in both academic and commercial environments.
- UNIX is known for its stability, security, and flexibility.
- It is capable of handling multiple users and processes simultaneously, making it a suitable choice for use as a real-time operating system (RTOS).
- An RTOS is an operating system that is designed to process data as it comes in, typically without buffering delays.
- This is important in applications where timely processing of data is critical, such as in control systems or data acquisition systems.
- UNIX can be used as an RTOS because it has features such as preemptive multitasking, which allows the operating system to interrupt a running process and switch to another process that requires immediate attention.
- This ensures that high-priority tasks are completed in a timely manner.
- Additionally, UNIX has a robust set of inter-process communication (IPC) mechanisms, which allow processes to communicate with each other and coordinate their actions.
- This is important in real-time systems, where multiple processes may need to work together to achieve a common goal.
- Overall, UNIX is a powerful and versatile operating system that can be used as an RTOS in a variety of applications.



# POSIX Issues

POSIX (Portable Operating System Interface) is an operating system interface standard based on the UNIX operating system. Its main goal is to support application portability at the source-code level.

- POSIX defines a standard way for an application to interface with the operating system.
- The original POSIX standard defines interfaces to core functions such as file operations, process management, signals, and devices.
- Subsequent releases of POSIX have also been defined to cover real-time extensions and multi-threading.
- The POSIX standard promotes portability of applications across different operating system platforms.
- This is especially important for applications designed for longevity, where the hardware and software infrastructure may change during the application's life cycle.
- A real-time working group was established in POSIX to develop standards to add the OS services that are needed by real-time applications.
- The international standard POSIX standard has been adopted by virtually all operating systems in use and most real-time operating systems including ThreadX, QNX, VxWorks, Integrity, LynxOS, and Unison OS.




### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

Temporal data refers to data that represents the state of an entity at a particular point in time. It is used to track changes in data over time and is commonly used in real-time systems and databases. The following are some of the characteristics of temporal data:

1. **Time-stamped**: Temporal data is time-stamped to indicate the time at which the data was recorded or is valid. This allows the data to be ordered chronologically and enables the tracking of changes over time.

2. **Historical**: Temporal data maintains a history of changes to the data. This allows the data to be queried and analyzed to understand how the data has changed over time.

3. **Consistent**: Temporal data must be consistent, meaning that the data must accurately represent the state of the entity at the time indicated by the time-stamp. This requires that the data be recorded accurately and that any changes to the data be recorded in a timely manner.

4. **Granularity**: The granularity of temporal data refers to the level of detail at which the data is recorded. The granularity of the data will depend on the requirements of the system and the nature of the data being recorded.

5. **Queryable**: Temporal data must be queryable, meaning that it must be possible to retrieve and analyze the data. This requires that the data be stored in a structured manner and that appropriate query mechanisms be available.

6. **Scalable**: Temporal data must be scalable, meaning that the system must be able to handle increasing amounts of data over time. This requires that the system be designed to accommodate growth in the volume of data and that appropriate storage and processing mechanisms be in place.

These are some of the key characteristics of temporal data in the context of real-time systems and databases. Understanding these characteristics is important when designing and implementing systems that use temporal data.



# Temporal Consistency

Temporal consistency refers to the maintenance of the correct temporal relationships between data items in a real-time system. This is important in real-time systems and databases, where data must be consistent and up-to-date in order to ensure the correct operation of the system.

Some key points to consider when discussing temporal consistency in the context of real-time operating systems and databases include:

1. Temporal consistency is important for ensuring that data is up-to-date and accurate in real-time systems.
2. Real-time databases must be designed to maintain temporal consistency, by ensuring that data is updated in a timely manner and that old data is not used.
3. Temporal consistency can be achieved through the use of various techniques, such as timestamping, versioning, and concurrency control.
4. The maintenance of temporal consistency can be challenging in distributed real-time systems, where data may be stored and accessed across multiple nodes.
5. Temporal consistency is closely related to other concepts in real-time systems, such as temporal validity and temporal accuracy.

Overall, temporal consistency is a crucial aspect of real-time systems and databases, and must be carefully considered in the design and implementation of these systems. It is important to ensure that data is consistent and up-to-date in order to ensure the correct operation of the system.



### Concurrency Control

Concurrency control is a critical component of real-time operating systems and databases. It refers to the management of simultaneous execution of transactions in a shared database system. The goal of concurrency control is to ensure the consistency and correctness of the data in the database, while allowing multiple transactions to execute concurrently.

Here are some key points to consider when studying concurrency control in the context of real-time operating systems and databases:

1. Concurrency control mechanisms are used to ensure that transactions do not interfere with each other and that the database remains in a consistent state.

2. There are several techniques for implementing concurrency control, including locking, timestamp ordering, and optimistic concurrency control.

3. Locking is a commonly used technique for concurrency control. It involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously.

4. Timestamp ordering is another technique for concurrency control. It assigns a timestamp to each transaction and uses these timestamps to determine the order in which transactions should be executed.

5. Optimistic concurrency control is a technique that assumes that conflicts between transactions are rare. It allows transactions to execute without acquiring locks, and checks for conflicts at the end of the transaction.

6. Concurrency control is particularly important in real-time systems, where transactions must be executed within strict time constraints.

7. Real-time databases may use specialized concurrency control mechanisms to ensure that transactions meet their deadlines.




# Overview of Commercial Real Time databases

A real-time database is a data store designed to collect, process, and/or enrich an incoming series of data points (i.e., a data stream) in real time, typically immediately after the data is created. This term does not refer to a discrete class of database management systems, but rather, applies to several types of databases.

A commercial database is one created for commercial purposes only and it’s available at a price. With a commercial real estate database, you’re in a stronger position to detect market patterns, pinpoint trends and work efficiently. In short, commercial real estate databases allow you to screen deals faster and more strategically, ultimately propelling your business forward.

At the most basic level, a commercial real estate database needs to be able to source critical industry information firms use to guide investment decisions. Data must not only be accurate, but also reflect real time changes. Your team can’t spend their limited time manually inputting or updating information.

