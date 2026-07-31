

# Real Time System

- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization).
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- The term “real-time system” refers to any information processing system with hardware and software components that perform real-time application functions and can respond to events within predictable and specific time constraints.
- A real-time system has been described as one which "controls an environment by receiving data, processing them, and returning the results sufficiently quickly to affect the environment at that time".
- Real-time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare.
- Key Use Cases of Real-Time Systems include Flight Control, Industrial Controls Applications, Video Wall, Medical Imaging, Robotics.
- A real-time system means that the system is subjected to real-time, i.e., the response should be guaranteed within a specified timing constraint or the system should meet the specified deadline.
- Examples of real-time systems include flight control systems, real-time monitors, etc.




## Unit 1 - Introduction of Real Time System

A real-time system is a computer system that is designed to process data and provide output within a specific time frame. This time frame is known as the system's deadline, and it is determined by the requirements of the application for which the system is being used.

1. Real-time systems are used in a variety of applications, including process control, robotics, and avionics.
2. These systems are characterized by their ability to provide timely and accurate responses to external events.
3. Real-time systems can be classified into two categories: hard real-time systems and soft real-time systems.
4. Hard real-time systems have strict deadlines, and failure to meet these deadlines can result in catastrophic consequences.
5. Soft real-time systems, on the other hand, have more flexible deadlines, and failure to meet these deadlines may result in degraded system performance, but not catastrophic consequences.
6. The design of real-time systems requires careful consideration of factors such as scheduling, resource allocation, and fault tolerance.
7. Real-time systems are typically implemented using specialized hardware and software, and they often require the use of real-time operating systems.



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a computer system that is designed to process data and produce outputs in a timely manner.
- The main characteristic of a real-time system is its ability to meet specific timing constraints, also known as deadlines.
- Real-time systems are often used in applications where the timely processing of data is critical, such as in control systems, financial trading systems, and telecommunications networks.
- There are two main types of real-time systems: hard real-time systems and soft real-time systems.
- Hard real-time systems have strict timing constraints, and missing a deadline can result in a catastrophic failure of the system.
- Soft real-time systems have more flexible timing constraints, and missing a deadline may result in a degradation of performance, but not a complete failure of the system.
- Real-time systems are often implemented using specialized hardware and software, and require careful design and testing to ensure that they meet their timing constraints.



### Typical Real Time Applications

Real-time systems are computer systems that monitor, respond to, or control an external environment. These systems are subject to a real-time constraint, which means that they must respond to an event within a specific time frame. Here are some typical real-time applications:

1. **Industrial control systems:** These systems are used to control industrial processes such as manufacturing, chemical processing, and power generation. They must respond quickly to changes in the environment to maintain safe and efficient operation.

2. **Avionics systems:** These systems are used in aircraft to control flight, navigation, and communication. They must respond quickly to changes in the environment to ensure the safety of the aircraft and its passengers.

3. **Medical systems:** These systems are used in hospitals and clinics to monitor and treat patients. They must respond quickly to changes in a patient's condition to provide appropriate care.

4. **Telecommunications systems:** These systems are used to transmit and receive data over communication networks. They must respond quickly to changes in the network to maintain reliable communication.

5. **Multimedia systems:** These systems are used to process and display multimedia content such as audio, video, and graphics. They must respond quickly to user input to provide a smooth and responsive user experience.

6. **Defense systems:** These systems are used by the military to monitor and respond to threats. They must respond quickly to changes in the environment to protect national security.

7. **Financial systems:** These systems are used by banks and financial institutions to process transactions and manage accounts. They must respond quickly to changes in the market to maintain financial stability.

These are just a few examples of the many real-time applications that exist. Real-time systems are essential for the safe and efficient operation of many critical systems in our society.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Release times refer to the specific times at which the notes for Unit 1 - Introduction of Real Time System in the subject of Real Time System are made available to students.
- These release times may vary depending on the institution, course, and instructor.
- It is important for students to be aware of the release times for the notes in order to effectively plan their study schedule and ensure they have access to the necessary materials.
- Students can typically find information about the release times for the notes on their course syllabus or by contacting their instructor.
- It is recommended that students regularly check for updates on the release times for the notes to ensure they have the most up-to-date information.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Deadlines refer to the specific time by which a task must be completed.
- In the context of Real Time Systems, deadlines are critical as they ensure that the system responds to events in a timely manner.
- Missing a deadline in a Real Time System can have severe consequences, such as system failure or loss of data.
- It is important to set realistic deadlines for tasks in a Real Time System to ensure that they can be completed on time.
- Deadlines can be hard or soft. A hard deadline is one that must be met, while a soft deadline can be missed without causing major problems.
- In the subject of Real Time System, Unit 1 - Introduction of Real Time System, it is important to understand the concept of deadlines and their significance in the functioning of Real Time Systems.



### Timing Constraints

Timing constraints are an essential aspect of real-time systems. These constraints define the time limits within which a task or operation must be completed. There are two types of timing constraints: hard and soft.

1. **Hard timing constraints** are strict and must be met. Failure to meet a hard timing constraint can result in a system failure or unacceptable behavior. For example, in a flight control system, the response time for a control input must be within a certain time limit to ensure the safety of the aircraft.

2. **Soft timing constraints** are more flexible and can be missed occasionally without causing a system failure. However, missing a soft timing constraint can result in degraded system performance. For example, in a video streaming application, occasional frame drops are acceptable, but frequent frame drops can result in a poor user experience.

In summary, timing constraints define the time limits within which tasks or operations must be completed in a real-time system. These constraints can be hard or soft, and the consequences of missing them vary depending on the type of constraint and the system in question. It is important to carefully design and analyze real-time systems to ensure that all timing constraints are met.



### Hard Real Time Systems

- Hard real-time systems are systems in which the correctness of the system depends not only on the logical result of the computation, but also on the time at which the results are produced.
- In hard real-time systems, missing a deadline is considered a system failure.
- These systems are often used in safety-critical applications, where the failure to meet a deadline can result in serious consequences, such as loss of life or damage to property.
- Examples of hard real-time systems include air traffic control systems, nuclear power plant control systems, and medical equipment.
- Hard real-time systems require rigorous testing and verification to ensure that they meet their deadlines under all possible conditions.
- The design of hard real-time systems often involves the use of specialized scheduling algorithms and real-time operating systems to ensure that tasks are completed within their deadlines.
- In hard real-time systems, it is important to consider worst-case execution times and worst-case response times to ensure that the system can meet its deadlines even under the most demanding conditions.
- Hard real-time systems often have strict requirements for reliability, availability, and fault tolerance, as failures can have serious consequences.



### Soft Real Time Systems

- A soft real-time operating system is one where there is a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system.
- Soft real-time systems, though less precise, can be run on multiple cores and impose fewer restrictions on applications.
- Soft real-time is when a system continues to function even if it’s unable to execute within an allotted time.
- If the system has missed its deadline, it will not result in critical consequences. The system can continue to function, though with undesirable lower quality of output.
- Soft real-time systems are typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems include software that maintains and updates the flight plans for commercial airliners.




### Reference Models for Real Time Systems

Real-time systems are computer systems that are designed to interact with the external environment in a timely manner. These systems are used in a variety of applications, including control systems, multimedia systems, and communication systems. To ensure that real-time systems meet their timing requirements, several reference models have been developed. These models provide a framework for the design and analysis of real-time systems.

1. **Rate Monotonic Scheduling (RMS)**: This model is used for scheduling periodic tasks in a real-time system. In this model, tasks are assigned priorities based on their periods, with shorter periods being assigned higher priorities. The RMS model guarantees that all tasks will meet their deadlines if the total utilization of the system is less than or equal to a specific bound.

2. **Earliest Deadline First (EDF)**: This model is used for scheduling tasks with deadlines in a real-time system. In this model, tasks are assigned priorities based on their deadlines, with earlier deadlines being assigned higher priorities. The EDF model guarantees that all tasks will meet their deadlines if the total utilization of the system is less than or equal to 100%.

3. **Sporadic Server**: This model is used for scheduling aperiodic tasks in a real-time system. In this model, a server task is used to handle the execution of aperiodic tasks. The server is assigned a specific capacity and period, and it can execute aperiodic tasks whenever it has available capacity.

4. **Constant Bandwidth Server (CBS)**: This model is an extension of the sporadic server model. In this model, the server is assigned a specific bandwidth, which determines the amount of CPU time that the server can use in each period. The CBS model guarantees that the server will not exceed its assigned bandwidth, and it can be used to provide temporal isolation between different tasks in a real-time system.

These are some of the reference models used in the design and analysis of real-time systems. Each model has its own strengths and limitations, and the choice of model depends on the specific requirements of the system being designed.



### Processors and Resources

1. A processor is the central unit of a computer system that performs the majority of the processing tasks.
2. It is responsible for executing instructions, performing calculations, and managing the flow of data within the system.
3. Processors can vary in their architecture, clock speed, and number of cores, which can affect their performance and suitability for certain tasks.
4. In a real-time system, the processor must be able to handle the demands of the system and ensure that tasks are completed within their specified deadlines.
5. Resources refer to the various components and peripherals that are required for the system to function, such as memory, storage, and input/output devices.
6. These resources must be managed effectively to ensure that the system can operate efficiently and meet its real-time requirements.
7. In a real-time system, resource allocation and scheduling are critical to ensure that tasks are completed on time and the system can meet its performance goals.
8. Effective resource management can help to prevent bottlenecks and ensure that the system can operate at its full potential.




### Temporal Parameters of Real Time Workload

1. **Release time**: The time at which a task becomes available for execution.
2. **Deadline**: The time by which a task must complete its execution.
3. **Period**: The time interval between two consecutive releases of a periodic task.
4. **Computation time**: The time required for a task to complete its execution once it starts.
5. **Response time**: The time interval between the release of a task and the completion of its execution.
6. **Jitter**: The variation in the response time of a task.
7. **Lateness**: The difference between the completion time of a task and its deadline.
8. **Tardiness**: The amount of time by which the completion time of a task exceeds its deadline.

These temporal parameters are important for understanding and analyzing the behavior of real-time workloads. They are used to determine the schedulability of tasks and to design scheduling algorithms that can meet the timing constraints of real-time systems. Understanding these parameters is essential for the successful design and implementation of real-time systems.



### Periodic Task Model

- A periodic task is a task that is executed repeatedly at regular intervals.
- The interval between two consecutive executions of a periodic task is called the period of the task.
- The period of a task is usually specified as a fixed value, but it can also be specified as a range of values.
- The execution time of a periodic task is the time it takes for the task to complete one execution.
- The deadline of a periodic task is the time by which the task must complete its execution.
- The utilization of a periodic task is the ratio of its execution time to its period.
- A set of periodic tasks is said to be schedulable if there exists a scheduling algorithm that can schedule the tasks such that all their deadlines are met.
- The utilization bound of a set of periodic tasks is the maximum utilization that the set of tasks can have and still be schedulable.
- The rate-monotonic scheduling algorithm is a commonly used algorithm for scheduling periodic tasks. It assigns priorities to tasks based on their periods, with shorter periods having higher priorities.
- The earliest deadline first scheduling algorithm is another commonly used algorithm for scheduling periodic tasks. It assigns priorities to tasks based on their deadlines, with earlier deadlines having higher priorities.




### Precedence Constraints and Data Dependency

Precedence constraints and data dependencies are important concepts in real-time systems. Here are some key points to consider:

1. **Precedence constraints** refer to the order in which tasks must be executed. For example, in a real-time system, a task that processes sensor data may need to be executed before a task that uses the processed data to make a decision.

2. **Data dependencies** occur when the output of one task is used as the input of another task. In a real-time system, data dependencies can create precedence constraints, as the task that produces the data must be executed before the task that consumes the data.

3. Precedence constraints and data dependencies can affect the schedulability of a real-time system. If tasks are not scheduled in the correct order, the system may not be able to meet its deadlines.

4. To ensure that a real-time system meets its deadlines, it is important to carefully analyze the precedence constraints and data dependencies between tasks. This can help to identify potential scheduling conflicts and to develop a schedule that ensures that all tasks are executed in the correct order.

5. In some cases, it may be necessary to introduce additional synchronization mechanisms, such as semaphores or mutexes, to ensure that tasks are executed in the correct order and that data dependencies are properly managed.

Overall, understanding and managing precedence constraints and data dependencies is a critical part of designing and implementing effective real-time systems. By carefully analyzing these constraints and dependencies, it is possible to develop a schedule that ensures that all tasks are executed in the correct order and that the system meets its deadlines.



## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning tasks to resources in a way that ensures that all tasks meet their timing constraints. This is important in real-time systems, where tasks have deadlines that must be met in order for the system to function correctly.

Some key points to consider when studying real-time scheduling include:

1. **Scheduling algorithms:** There are several different algorithms that can be used for real-time scheduling, including Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), and Least Laxity First (LLF). Each algorithm has its own strengths and weaknesses, and the choice of algorithm will depend on the specific requirements of the system.

2. **Task characteristics:** The characteristics of the tasks being scheduled, such as their execution time, deadline, and priority, will affect the scheduling decisions. It is important to understand these characteristics in order to make effective scheduling decisions.

3. **Resource constraints:** Real-time systems often have limited resources, such as processing power and memory, and these constraints must be taken into account when scheduling tasks. Resource allocation and management is a key part of real-time scheduling.

4. **Overload conditions:** In some cases, the system may be overloaded, meaning that there are more tasks than can be completed within their deadlines. In these situations, the scheduler must make decisions about which tasks to prioritize and which to delay or drop.

Overall, real-time scheduling is a complex and challenging problem, and it is an important area of study for anyone working with real-time systems. By understanding the key concepts and techniques involved, it is possible to design and implement effective real-time scheduling solutions.



### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of allocating system resources to tasks in a way that ensures that all tasks meet their timing constraints. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline, the higher the priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the difference between its deadline and its remaining computation time. The smaller the laxity, the higher the priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of each task is fixed and does not change during the execution of the system.

These are some of the common approaches to real-time scheduling. Each approach has its own advantages and disadvantages, and the choice of approach depends on the specific requirements of the system being designed.



### Clock Driven Approach

The clock-driven approach is a scheduling method used in real-time systems. It is also known as time-driven or table-driven scheduling. In this approach, the scheduler uses a pre-computed table to determine when tasks should be executed. The table is computed offline, before the system starts running, and it specifies the start times of all tasks.

Some key points to note about the clock-driven approach are:

1. The schedule is computed offline, before the system starts running.
2. The schedule is fixed and does not change during runtime.
3. The schedule is based on the worst-case execution times of tasks.
4. The schedule is periodic, meaning that tasks are executed at regular intervals.
5. The schedule is deterministic, meaning that the behavior of the system is predictable.

This approach is suitable for systems with periodic tasks and fixed deadlines. It is also suitable for systems with a small number of tasks and low variability in task execution times. However, it may not be suitable for systems with a large number of tasks or high variability in task execution times, as the pre-computed schedule may not be able to accommodate all possible scenarios.

In summary, the clock-driven approach is a scheduling method used in real-time systems where the scheduler uses a pre-computed table to determine when tasks should be executed. It is suitable for systems with periodic tasks and fixed deadlines, but may not be suitable for systems with a large number of tasks or high variability in task execution times.



### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the relative importance of the task. The scheduler allocates CPU time to each task based on its weight.

Here are the key points to note about the Weighted Round Robin approach:

1. In WRR, tasks with higher weights are given more CPU time compared to tasks with lower weights.
2. The scheduler assigns time slices to each task in proportion to their weights.
3. The time slice for each task is calculated by dividing the weight of the task by the sum of the weights of all tasks.
4. Tasks with the same weight are scheduled in a round-robin fashion.
5. WRR is a fair scheduling algorithm, as it ensures that tasks with higher weights are given more CPU time, while tasks with lower weights are not starved of CPU time.
6. WRR is suitable for real-time systems where tasks have different priorities and importance.




### Priority Driven Approach

Priority-driven scheduling is a method used in real-time systems to schedule tasks based on their priority levels. In this approach, tasks with higher priority are executed before tasks with lower priority. This approach is commonly used in real-time systems where tasks have strict deadlines and must be completed within a certain time frame.

Some key points to note about priority-driven scheduling are:

1. Tasks are assigned priority levels based on their importance and urgency.
2. The scheduler selects the highest priority task that is ready to execute and assigns it to the processor.
3. If two or more tasks have the same priority level, the scheduler may use other criteria, such as task arrival time or task duration, to determine which task to execute first.
4. Priority-driven scheduling can be either static or dynamic. In static priority scheduling, the priority levels of tasks are fixed and do not change during the execution of the system. In dynamic priority scheduling, the priority levels of tasks may change during the execution of the system based on certain criteria, such as task deadlines or resource availability.
5. Priority-driven scheduling is commonly used in real-time systems where tasks have strict deadlines and must be completed within a certain time frame.



### Dynamic Versus Static Systems

In the context of real-time scheduling, systems can be classified as either dynamic or static. Here are some key points to understand the difference between the two:

1. **Static systems** use a fixed schedule that is determined before the system starts running. This schedule is based on the worst-case execution times of the tasks and their deadlines. The schedule is followed strictly, and tasks are executed in the order specified by the schedule.

2. **Dynamic systems**, on the other hand, make scheduling decisions on-the-fly, based on the current state of the system. The scheduler takes into account the actual execution times of the tasks, their deadlines, and other factors such as resource availability, to make scheduling decisions.

3. Static systems are generally easier to analyze and verify, as the schedule is known beforehand. However, they may not be as efficient as dynamic systems, as they do not take into account the actual execution times of the tasks.

4. Dynamic systems can be more efficient, as they can adapt to the current state of the system. However, they can be more difficult to analyze and verify, as the scheduling decisions are made on-the-fly.

5. In summary, static systems use a fixed, predetermined schedule, while dynamic systems make scheduling decisions on-the-fly. Static systems are generally easier to analyze and verify, while dynamic systems can be more efficient but more difficult to analyze.




### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two scheduling algorithms used in real-time systems. These algorithms are used to schedule tasks in a way that ensures that all tasks meet their deadlines.

1. **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest absolute deadline is scheduled first. EDF is an optimal scheduling algorithm for uniprocessor systems, meaning that if a feasible schedule exists, EDF will always find it.

2. **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time, which is the amount of time left until the task's deadline minus the task's remaining execution time. The task with the least slack time is scheduled first. LST is also an optimal scheduling algorithm for uniprocessor systems.

In summary, both EDF and LST are optimal scheduling algorithms for uniprocessor real-time systems. They ensure that all tasks meet their deadlines if a feasible schedule exists. These algorithms are commonly used in real-time systems to ensure timely execution of tasks.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time scheduling.
- It is a static priority algorithm, meaning that the priorities of tasks are assigned at design time and do not change during runtime.
- RMA assigns priorities to tasks based on their periods, with the task having the shortest period being assigned the highest priority.
- RMA is an optimal algorithm for scheduling periodic tasks on a uniprocessor system, meaning that if a set of tasks can be scheduled by any static priority algorithm, it can also be scheduled by RMA.
- The schedulability of a set of tasks under RMA can be determined using the Liu and Layland utilization bound, which states that a set of n periodic tasks is schedulable under RMA if the total utilization of the tasks is less than or equal to n(2^(1/n) - 1).
- RMA is a simple and effective algorithm for scheduling periodic tasks in real-time systems, but it has limitations when it comes to handling tasks with deadlines that are different from their periods or tasks with shared resources. In such cases, other scheduling algorithms may be more suitable.



### Offline Versus Online Scheduling

- **Offline scheduling** refers to the process of determining a schedule for a set of tasks before the system starts executing them. This type of scheduling is also known as **static scheduling**.
- In contrast, **online scheduling** refers to the process of making scheduling decisions as the system is executing tasks. This type of scheduling is also known as **dynamic scheduling**.
- Offline scheduling is typically used in systems where the set of tasks and their execution times are known in advance. This allows the scheduler to compute an optimal schedule that meets all the timing constraints of the system.
- Online scheduling is used in systems where the set of tasks or their execution times are not known in advance. In this case, the scheduler must make decisions based on the current state of the system and the tasks that are ready to execute.
- One advantage of offline scheduling is that it can result in a more efficient schedule since the scheduler has complete information about the tasks and their timing constraints. However, this approach is not suitable for systems where the task set or execution times are not known in advance.
- One advantage of online scheduling is that it can adapt to changes in the system, such as the arrival of new tasks or changes in task execution times. However, this approach can result in suboptimal schedules since the scheduler has limited information about the tasks and their timing constraints.
- In the context of real-time systems, both offline and online scheduling approaches can be used to ensure that all tasks meet their timing constraints. The choice of approach depends on the characteristics of the system and the tasks it needs to execute.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- **Aperiodic jobs** are tasks that do not have a regular arrival pattern and can arrive at any time.
- **Sporadic jobs** are tasks that have a minimum inter-arrival time between two consecutive jobs.
- In **Priority Driven Systems**, tasks are assigned priorities and are scheduled based on their priorities.
- In **Clock Driven Systems**, tasks are scheduled based on a pre-determined schedule that is calculated offline.
- Aperiodic and sporadic jobs can be scheduled in priority driven systems using techniques such as **slack stealing**, **deferrable servers**, and **sporadic servers**.
- In clock driven systems, aperiodic and sporadic jobs can be scheduled using techniques such as **time-driven scheduling** and **event-driven scheduling**.
- These techniques allow for the efficient scheduling of aperiodic and sporadic jobs in real-time systems, ensuring that all tasks meet their deadlines.




## Unit 3 - Resources Sharing

1. Resource sharing refers to the sharing of resources among multiple users or systems.
2. This can include sharing of hardware, software, data, and information.
3. Resource sharing can improve efficiency and reduce costs by allowing multiple users to access the same resources.
4. Examples of resource sharing include file sharing, printer sharing, and internet sharing.
5. Resource sharing can be implemented through various methods, such as networking, virtualization, and cloud computing.
6. Security and access control are important considerations when implementing resource sharing.
7. Resource sharing can also facilitate collaboration and cooperation among users.




### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- A resource access-control protocol, or simply an access-control protocol, is a set of rules that govern (1) when and under what conditions each request for resource is granted and (2) how jobs requiring resources are scheduled.
- Resource contention often leads to performance degradation in the applications contending for the shared resource. This can cause unexpected project delays, because processes contending for resources will be stalled until they can access the resource.
- Resource Access Control Protocols work to reduce the undesirable effect of resource contention. Resource contention affects the execution behavior and schedulability of jobs.
- One of the major objectives of resources access control is to minimize the undesirable effects of resource allocation.
- Access to resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section. If a lock request fails, the requesting job is blocked; a job holding a lock cannot be preempted by a higher priority job needing that lock.



### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, even if a higher priority task becomes ready to run.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- By ensuring that only one task can access the shared resource at a time, non-preemptive critical sections prevent race conditions and other synchronization issues.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms, such as semaphores, mutexes, or disabling interrupts.
- It is important to use non-preemptive critical sections judiciously, as they can introduce significant delays and reduce the responsiveness of the system.
- Careful design and analysis are required to ensure that the use of non-preemptive critical sections does not violate the timing constraints of the system.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage resource sharing and prevent priority inversion. Here are some key points to remember:

1. **Priority Inversion** occurs when a low-priority task holds a resource that a high-priority task needs, causing the high-priority task to be blocked and the low-priority task to continue executing.
2. **Priority-Inheritance Protocol (PIP)** is a solution to priority inversion where the low-priority task inherits the priority of the highest-priority task that is blocked by it. This allows the low-priority task to complete and release the resource, unblocking the high-priority task.
3. **Priority-Ceiling Protocol (PCP)** is another solution to priority inversion where each resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource. A task can only access a resource if its priority is higher than the current priority ceiling of the resource.
4. **Basic Priority Ceiling Protocol (BPCP)** is a variant of PCP where the priority ceiling of a resource is the highest priority of any task that may access the resource, regardless of whether the task is currently blocked or not.
5. Both PIP and PCP can prevent priority inversion, but PCP has the added benefit of preventing deadlock and reducing blocking time.

These are some basic concepts of Priority-Inheritance and Priority-Ceiling Protocols for resource sharing in real-time systems. It is important to understand these concepts for the Unit 3 - Resources Sharing in the subject of Real Time System.



### Stack Based Priority-Ceiling Protocol

- Stack-Based Priority Ceiling Protocol is based on original work to allow jobs to share a run-time stack, extended to control access to other resources.
- The protocol defines rules for the ceiling: When all resources are free, Π(t) = Ω; Π(t) is updated each time a resource is allocated or freed.
- Π(t) is the current priority ceiling of all resources.
- Priority Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways.
- Real-Time Systems are multitasking systems that involve the use of semaphore variables, signals, and events for job synchronization.
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource.
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time.
- The priority ceiling protocol can be used to control resource accesses in dynamic systems, provided the priority ceiling of each resource and the ceiling of the system are updated each time task priorities change.
- The protocol specifies a dynamic priority ceiling for each critical section, which is the earliest deadline of jobs that are currently in or will enter the critical section. Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section that is in use.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).



### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by lower priority tasks. Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling.
3. When a task locks a resource, the system's preemption ceiling is set to the maximum of the current preemption ceiling and the resource's preemption ceiling.
4. A task can be preempted only by tasks with a priority higher than the current preemption ceiling.
5. When a task releases a resource, the system's preemption ceiling is reset to the maximum preemption ceiling of all resources currently locked by tasks.

This protocol ensures that high priority tasks are not blocked by lower priority tasks and prevents priority inversion. It also ensures that tasks do not experience unbounded blocking, as the maximum blocking time is limited by the preemption ceiling of the resources. This makes the Preemption Ceiling Protocol a useful tool for managing resource sharing in real-time systems.



### Access Control in Multiple-Unit Resources

Access control in multiple-unit resources refers to the management of access to resources that have multiple units or instances. In a real-time system, these resources may include processors, memory, and I/O devices, among others. The goal of access control is to ensure that the system can effectively share these resources among multiple tasks or processes while maintaining the desired level of performance and predictability.

Some key points to consider when implementing access control in multiple-unit resources include:

1. **Resource allocation**: The system must have a mechanism for allocating resources to tasks or processes. This can be done using various algorithms, such as first-come-first-served, priority-based, or fair-share scheduling.

2. **Resource contention**: When multiple tasks or processes require access to the same resource, there may be contention for that resource. The system must have a mechanism for managing this contention, such as using locks or semaphores to ensure that only one task can access the resource at a time.

3. **Deadlock prevention**: When multiple tasks or processes are waiting for resources held by other tasks, a deadlock can occur. The system must have a mechanism for preventing deadlocks, such as using a resource allocation policy that ensures that resources are allocated in a way that prevents circular dependencies.

4. **Priority inversion**: When a high-priority task is blocked by a lower-priority task holding a resource, a priority inversion can occur. The system must have a mechanism for preventing or mitigating priority inversions, such as using priority inheritance or priority ceiling protocols.

Overall, access control in multiple-unit resources is a critical aspect of resource sharing in real-time systems. By effectively managing access to resources, the system can ensure that tasks or processes can execute predictably and meet their real-time constraints.



### Controlling Concurrent Accesses to Data Objects

1. **Introduction**: In a real-time system, multiple tasks may need to access shared data objects concurrently. To ensure data consistency and avoid race conditions, it is necessary to control the concurrent accesses to these data objects.

2. **Critical Section**: A critical section is a section of code that accesses shared data objects and must be executed atomically. Only one task can execute its critical section at a time.

3. **Mutual Exclusion**: Mutual exclusion is a mechanism to ensure that only one task can enter its critical section at a time. This can be achieved using various synchronization techniques such as semaphores, monitors, and message passing.

4. **Priority Inversion**: Priority inversion occurs when a high-priority task is blocked by a lower-priority task that holds a resource needed by the high-priority task. This can result in missed deadlines and reduced system performance.

5. **Priority Inheritance Protocol**: The priority inheritance protocol is a solution to the priority inversion problem. When a high-priority task is blocked by a lower-priority task, the lower-priority task inherits the priority of the high-priority task until it releases the resource.

6. **Priority Ceiling Protocol**: The priority ceiling protocol is another solution to the priority inversion problem. Each shared resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource. A task can only access a resource if its priority is higher than the priority ceiling of all resources currently held by lower-priority tasks.

7. **Conclusion**: Controlling concurrent accesses to data objects is essential in a real-time system to ensure data consistency and avoid race conditions. Various techniques such as mutual exclusion, priority inheritance, and priority ceiling can be used to achieve this. It is important to carefully design the system to avoid issues such as priority inversion.



## Unit 4 - Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. This type of communication is essential for many applications, including online gaming, video conferencing, and remote control of devices.

Some key points to consider when discussing real-time communication include:

1. **Latency**: This refers to the time it takes for a message to travel from the sender to the receiver. Low latency is essential for real-time communication, as any delay can disrupt the flow of the conversation.

2. **Bandwidth**: This refers to the amount of data that can be transmitted over a communication channel in a given period of time. High bandwidth is necessary for applications that require the transmission of large amounts of data, such as video conferencing.

3. **Reliability**: This refers to the ability of a communication system to deliver messages without errors or loss of data. Reliability is important for applications where the accuracy of the information being transmitted is critical.

4. **Security**: This refers to the measures taken to protect the confidentiality and integrity of the information being transmitted. Security is important for applications where sensitive information is being exchanged, such as financial transactions.

Real-time communication can be achieved through various technologies, including Voice over IP (VoIP), instant messaging, and video conferencing. These technologies use different protocols and standards to enable the exchange of information in real-time.

In summary, real-time communication is essential for many applications and is achieved through the use of various technologies and protocols. Key considerations when discussing real-time communication include latency, bandwidth, reliability, and security.



### Basic Concepts in Real time Communication

Real-time communication (RTC) refers to any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real-time communication include:
- Voice over landlines and mobile phones
- Online communication that happens in real-time

Effective communication involves more than just exchanging information. It's about understanding the emotion and intentions behind the information. Some skills that can help with effective communication include:
1. Becoming an engaged listener
2. Paying attention to nonverbal signals
3. Keeping stress in check
4. Asserting yourself



### Soft and Hard RT Communication systems

Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT). The difference between a hard and soft real-time communication system is the consequences of incorrect operation.

- **Hard Real-Time (HRT)**: Hard real-time systems have a strict time limit, or we can say deadlines. It is important to meet those deadlines, otherwise, the system is considered a system failure.

- **Soft Real-Time (SRT)**: In a soft real-time system, there is no mandatory requirement of completing the deadline for every task. Unlike hard real-time communication systems, soft real-time communication systems generally do not have the capacity to cause catastrophic harm upon a fault, which allows for non-deterministic, less rigorous network infrastructure.

Soft Real-time Communication is a communication system that is used to support soft real-time applications in a LAN. Soft real-time communication networks do not provide absolute Quality of Service (QoS) guarantee to applications. These networks always ensure prioritized treatment for real-time messages.



### Model of Real Time Communication

Real-time communication refers to the exchange of information between two or more parties with minimal delay. In the context of real-time systems, this communication must occur within a specified time frame to ensure the correct functioning of the system. Here are some key points to consider when discussing the model of real-time communication:

1. **Timing constraints:** Real-time communication must adhere to strict timing constraints to ensure that the system functions correctly. This means that messages must be delivered within a specified time frame, and any delays could result in system failure.

2. **Reliability:** The communication between parties must be reliable to ensure that messages are delivered correctly and without error. This can be achieved through the use of error detection and correction techniques, as well as the use of redundant communication channels.

3. **Synchronization:** In many real-time systems, it is important for the parties involved in the communication to be synchronized. This means that they must operate on the same time scale and be able to coordinate their actions.

4. **Protocols:** Real-time communication often relies on the use of specific protocols to ensure that the timing constraints and reliability requirements are met. These protocols can include time-triggered protocols, event-triggered protocols, and hybrid protocols.

5. **Network topology:** The topology of the network used for real-time communication can also play a role in the performance of the system. Factors such as the number of nodes, the distance between nodes, and the routing algorithms used can all impact the communication.

Overall, the model of real-time communication must take into account the specific requirements of the system, including timing constraints, reliability, synchronization, protocols, and network topology. By carefully considering these factors, it is possible to design a communication model that meets the needs of the real-time system.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- According to a priority-based service discipline, the transmission of ready packets is scheduled in a priority-driven manner. 
- Weighted Fair Queuing (WFQ) and Weighted Round Robin (WRR) scheduling are common approaches for scheduling packets in real-time communication networks .
- The PP discipline is based on the Strict Priority (SP) discipline with the difference that each priority queue is assigned a parameter as in Weighted Fair Queueing (WFQ) and Weighted Round Robin (WRR) disciplines .
- In a switched network, a downstream switch can begin to transmit an earlier portion of the message as soon as it receives the portion. It does not have to wait for the arrival of the rest of the message .
- The weighted round-robin approach does not require a sorted priority queue, only a round-robin queue .
- Many class service disciplines used for output queued switches have been proposed in the literature. These disciplines include the Class-Based Weighted Fair Queuing (CBWFQ) and the Weighted Fair Priority Queuing (WFPQ) techniques .
- A new WRR algorithm, called Rate-controlled Frame-based Weighted Round Robin (RFWRR) has been proposed which guarantees the delay jitter bound and satisfies a diverse set of delay requirements. The proposed algorithm divides the scheduler into two components: a rate controller and a frame-based WRR server .



### Medium Access Control Protocols for Broadcast Networks

Medium Access Control (MAC) protocols are responsible for controlling access to a shared communication medium in broadcast networks. These protocols are used to ensure that data transmissions from multiple devices do not interfere with each other, and that all devices have fair access to the medium.

There are several types of MAC protocols used in broadcast networks, including:

1. **Contention-based protocols:** These protocols allow multiple devices to compete for access to the medium. An example of a contention-based protocol is Carrier Sense Multiple Access with Collision Detection (CSMA/CD), which is used in Ethernet networks.

2. **Time-division multiple access (TDMA):** In TDMA, time is divided into slots, and each device is assigned a specific time slot for transmission. This ensures that only one device transmits at a time, avoiding collisions.

3. **Frequency-division multiple access (FDMA):** In FDMA, the available frequency band is divided into sub-bands, and each device is assigned a specific sub-band for transmission. This ensures that multiple devices can transmit simultaneously without interfering with each other.

4. **Code-division multiple access (CDMA):** In CDMA, each device is assigned a unique code, and the signals from multiple devices are transmitted simultaneously. The receiver uses the unique code to separate the signals from different devices.

These are some of the common MAC protocols used in broadcast networks. The choice of MAC protocol depends on the specific requirements of the network, such as the number of devices, the amount of data to be transmitted, and the level of interference.



### Internet and Resource Reservation Protocols

- The **Resource Reservation Protocol (RSVP)** is used in real-time systems for an efficient quality band transmission to a particular receiver .
- It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver .
- RSVP provides new Internet services with higher quality than best-effort by means of resource reservations .
- RSVP is a transport layer protocol that reserves resources across a network and can be used to deliver specific levels of Quality of Service (QoS) for application data streams .
- Resource reservation enables businesses to divide network resources by traffic of different types and origins, define limits, and prioritize traffic .
- There are several possible models how the use of resource reservation, based on RSVP or successor protocols, might evolve .



## Unit 5 - Real Time Operating Systems and Databases

1. **Real-Time Operating Systems (RTOS)**: An RTOS is an operating system designed to serve real-time applications that process data as it comes in, typically without buffer delays. The main objective of an RTOS is to provide a quick and predictable response to events.

2. **Characteristics of RTOS**: Some of the key characteristics of an RTOS include determinism, responsiveness, user control, reliability, and fail-safe operation.

3. **Types of RTOS**: There are two main types of RTOS: hard real-time and soft real-time. Hard real-time systems have strict timing constraints, while soft real-time systems have more relaxed timing constraints.

4. **Real-Time Databases**: A real-time database is a database system that is designed to handle workloads whose state is constantly changing. This is often used in applications that require fast, up-to-date information, such as stock trading or process control systems.

5. **Characteristics of Real-Time Databases**: Some of the key characteristics of real-time databases include concurrency control, data consistency, and the ability to handle large volumes of data.

6. **Real-Time Database Management Systems**: A real-time database management system (RTDBMS) is a database management system that is specifically designed to handle real-time data and workloads. These systems often have specialized features and capabilities to support the needs of real-time applications.

7. **Applications of Real-Time Systems**: Real-time systems and databases have a wide range of applications, including process control, stock trading, telecommunications, and military systems.



### Features of RTOS

Real-Time Operating Systems (RTOS) are designed to provide predictable and deterministic execution of tasks in real-time applications. Some of the key features of RTOS include:

1. **Deterministic behavior**: RTOS are designed to provide predictable and deterministic execution of tasks, which is essential for real-time applications.

2. **Preemptive scheduling**: RTOS use preemptive scheduling to ensure that high priority tasks are executed before lower priority tasks.

3. **Fast context switching**: RTOS are designed to minimize the time required for context switching between tasks, which is essential for real-time applications.

4. **Small memory footprint**: RTOS are designed to have a small memory footprint, which makes them suitable for use in embedded systems with limited memory.

5. **Real-time clock**: RTOS typically include a real-time clock, which provides accurate timekeeping and can be used to schedule tasks.

6. **Inter-task communication**: RTOS provide mechanisms for inter-task communication, such as message queues, semaphores, and mutexes.

7. **Interrupt handling**: RTOS are designed to handle interrupts in a timely and predictable manner, which is essential for real-time applications.

8. **Modularity**: RTOS are designed to be modular, which makes it easy to add or remove features as needed.

These are some of the key features of RTOS that make them suitable for use in real-time applications. It is important to note that not all RTOS have all of these features, and the specific features of an RTOS may vary depending on the specific requirements of the application.



### Time Services

Time services are an essential component of real-time operating systems and databases. These services provide the ability to measure, represent, and manage time within the system. Some of the key features of time services include:

1. **Clock synchronization:** This refers to the process of synchronizing the clocks of different nodes in a distributed system to ensure that they all have the same notion of time. This is important for coordinating the execution of tasks across the system.

2. **Time representation:** Time services provide a way to represent time within the system. This can include the use of timestamps, time intervals, and other data structures that allow the system to keep track of time.

3. **Time management:** Time services provide mechanisms for managing time within the system. This can include the ability to set timers, schedule tasks, and perform other operations that are dependent on time.

4. **Time-based coordination:** Time services can be used to coordinate the execution of tasks within the system based on time. This can include the use of time-triggered protocols, time-based scheduling algorithms, and other mechanisms that allow the system to perform actions at specific points in time.

Overall, time services play a critical role in ensuring the correct and timely execution of tasks in real-time operating systems and databases. They provide the foundation for many of the key features of these systems, including scheduling, synchronization, and coordination.



### UNIX as RTOS for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- UNIX is a multi-user, multi-tasking operating system that was originally developed in the late 1960s and early 1970s.
- It is widely used in both academic and commercial environments.
- UNIX is known for its stability, security, and flexibility.
- It is also known for its ability to handle large amounts of data and its support for multiple programming languages.
- UNIX can be used as a real-time operating system (RTOS) because it has features that support real-time processing.
- These features include the ability to prioritize processes, the ability to handle interrupts, and the ability to manage memory efficiently.
- In addition, UNIX has a rich set of tools and utilities that can be used to develop real-time applications.
- These tools include compilers, debuggers, and performance analysis tools.
- Overall, UNIX is a powerful and versatile operating system that can be used to develop and run real-time applications.



### POSIX Issues for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- POSIX stands for Portable Operating System Interface and is a proposed operating system interface standard based on the popular UNIX operating system.
- The main goal of POSIX is to support application portability at the source-code level.
- POSIX defines a standard way for an application to interface with the operating system.
- The original POSIX standard defines interfaces to core functions such as file operations, process management, signals, and devices.
- Subsequent releases of POSIX have also been defined to cover real-time extensions and multi-threading.
- The POSIX standard promotes portability of applications across different operating system platforms.
- This is especially important for applications designed for longevity, where the hardware and software infrastructure may change during the application's life cycle.
- The international standard POSIX standard has been adopted by virtually all operating systems in use and most real-time operating systems including: ThreadX, QNX, VxWorks, Integrity, LynxOS, and Unison OS.
- A real-time working group was established in POSIX to develop standards to add POSIX (or UNIX) the OS services that are needed by real-time applications.



### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

Temporal data refers to data that represents the state of an entity at a particular point in time. It is used to track changes in data over time and is commonly used in real-time systems and databases. Some characteristics of temporal data include:

1. **Time-stamped**: Temporal data is associated with a specific point in time, usually represented by a timestamp.

2. **Historical**: Temporal data can be used to track changes in data over time, allowing for the reconstruction of the state of an entity at any point in the past.

3. **Versioned**: Temporal data can be versioned, allowing for multiple versions of the same data to coexist.

4. **Consistent**: Temporal data must be consistent, meaning that the state of an entity at any point in time must be logically consistent with its state at other points in time.

5. **Queryable**: Temporal data must be queryable, allowing for the retrieval of data at a specific point in time or over a range of time.

6. **Concurrent**: Temporal data can be used to support concurrent access to data, allowing multiple users to access and modify data at the same time.

These are some of the key characteristics of temporal data that are important in the context of real-time systems and databases. Understanding these characteristics can help in the design and implementation of effective real-time systems and databases that can handle temporal data effectively.



### Temporal Consistency

Temporal consistency refers to the maintenance of the temporal relationships between data items in a real-time database. In a real-time system, data items have associated temporal constraints, such as deadlines or valid time intervals, and it is important to ensure that these constraints are met.

Some key points to consider when discussing temporal consistency in the context of real-time operating systems and databases include:

1. Temporal consistency is important in real-time systems because it ensures that data is up-to-date and accurate, which is critical for making timely and correct decisions.
2. Temporal consistency can be achieved through various techniques, such as using timestamps to track the age of data items and implementing concurrency control mechanisms to prevent conflicting updates.
3. Temporal consistency is closely related to other concepts in real-time systems, such as temporal validity and temporal coherence.
4. Ensuring temporal consistency in a real-time database can be challenging due to the need to balance the requirements of real-time performance and data consistency.
5. Temporal consistency is an important consideration in the design and implementation of real-time operating systems and databases.




### Concurrency Control

Concurrency control is the process of managing simultaneous access to a database by multiple users. It is an essential component of real-time operating systems and databases, as it ensures the consistency and integrity of data.

Here are some key points to remember about concurrency control:

1. Concurrency control is necessary to prevent conflicts that can arise when multiple users access the same data simultaneously.
2. There are several techniques for implementing concurrency control, including locking, timestamping, and optimistic concurrency control.
3. Locking involves placing locks on data items to prevent other users from accessing them while they are being modified.
4. Timestamping assigns a unique timestamp to each transaction and uses these timestamps to determine the order in which transactions should be executed.
5. Optimistic concurrency control assumes that conflicts are rare and allows transactions to proceed without locking. Conflicts are detected at the end of the transaction and resolved by rolling back and restarting the transaction.
6. Choosing the right concurrency control technique depends on the specific requirements of the system, including the level of concurrency, the frequency of conflicts, and the performance requirements.




### Overview of Commercial Real Time databases

A real-time database is a data store designed to collect, process, and/or enrich an incoming series of data points (i.e., a data stream) in real time, typically immediately after the data is created. This term does not refer to a discrete class of database management systems, but rather, applies to several types of databases.

A commercial database is one created for commercial purposes only and it’s available at a price. With a commercial real estate database, you’re in a stronger position to detect market patterns, pinpoint trends and work efficiently. In short, commercial real estate databases allow you to screen deals faster and more strategically, ultimately propelling your business forward.

At the most basic level, a commercial real estate database needs to be able to source critical industry information firms use to guide investment decisions. Data must not only be accurate, but also reflect real-time changes. Your team can’t spend their limited time manually inputting or updating information.

Some examples of commercial real-time databases include:
- Improvado: A popular database software tool that can help you aggregate all the marketing data for small and large enterprises in real-time.
- InfluxDB: Part of a comprehensive platform that supports the collection, storage, monitoring, visualization and alerting of time series data. It’s much more than just a time series database. The whole InfluxData platform is built from an open source db core.

