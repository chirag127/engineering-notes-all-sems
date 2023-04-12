

# Real Time System

A real time system is a system that can process and respond to events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to handle concurrent and unpredictable events, and to coordinate with other systems that may have different clocks or time scales.

There are two main types of real time systems based on the consequences of missing the deadlines:

- **Hard real time systems**: These systems have absolute deadlines that must be met, otherwise the system will fail or cause severe damage. For example, a flight control system, a nuclear reactor control system, or a pacemaker are hard real time systems. These systems require high reliability, predictability, and fault tolerance.
- **Soft real time systems**: These systems have relative deadlines that can be missed occasionally, but the quality of service or performance will degrade. For example, a video streaming system, a voice recognition system, or a gaming system are soft real time systems. These systems require high responsiveness, adaptability, and efficiency.

Some of the applications of real time systems are:

- Process control systems: These systems are used in industrial applications where production is continuous and requires precise and timely control of physical processes. For example, a chemical plant, a power plant, or a steel mill are process control systems.
- Machine vision: These systems are used to help machines rapidly interpret data so they can see their surroundings and perform tasks. For example, a face recognition system, a self-driving car, or a barcode scanner are machine vision systems.
- Robotics: These systems are used to control the movements and actions of robots that can interact with the physical world. For example, a robotic arm, a drone, or a surgical robot are robotics systems.



## Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization).
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur. For example, flight control systems, airbag systems, etc. .
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. For example, video streaming, online gaming, etc..
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities.
- A real-time system can have different types of tasks: periodic, aperiodic, and sporadic.
- A periodic task is a task that has a fixed interval between successive executions. For example, sensor readings, heartbeat signals, etc..
- An aperiodic task is a task that has a variable interval between successive executions. For example, user inputs, network requests, etc..
- A sporadic task is a task that has a minimum interval between successive executions. For example, emergency signals, alarms, etc..
- A real-time system can have different types of scheduling algorithms: static, dynamic, preemptive, and non-preemptive.
- A static scheduling algorithm assigns priorities to tasks before execution. For example, rate-monotonic scheduling, deadline-monotonic scheduling, etc..
- A dynamic scheduling algorithm assigns priorities to tasks during execution. For example, earliest deadline first scheduling, least laxity first scheduling, etc..
- A preemptive scheduling algorithm allows a higher priority task to interrupt a lower priority task. For example, round-robin scheduling, shortest remaining time first scheduling, etc..
- A non-preemptive scheduling algorithm does not allow a higher priority task to interrupt a lower priority task. For example, first come first served scheduling, shortest job first scheduling, etc..



### Definition of Real-Time System

- A real-time system is a computer system that **responds to input signals fast enough to keep an operation moving at its required speed**.
- A real-time system is also characterized by its ability to **produce the expected result within a defined deadline (timeliness)** and to **coordinate independent clocks and operate together in unison (time synchronization)**.
- A real-time system is one that **controls an environment by receiving data, processing them, and returning the results sufficiently quickly to affect the environment at that time**.
- A real-time system is subjected to **real-time, i.e., the response should be guaranteed within a specified timing constraint or the system should meet the specified deadline**.
- Examples of real-time systems are flight control systems, real-time monitors, gaming computers, videoconferencing systems, etc.



### Typical Real Time Applications

- A real-time application (RTA) is an application that requires a program to respond to stimuli within a specific and predictable time frame.
- Real-time applications are often used for tasks that involve critical operations, such as digital control, signal processing, command and control, tracking, and multimedia.
- Some examples of real-time applications are:

  - **Video conferencing**: This application allows users to communicate with each other using audio and video streams over the Internet. It requires low latency and high bandwidth to ensure smooth and synchronized communication.
  - **Voice over Internet Protocol (VoIP)**: This application enables users to make phone calls over the Internet using digital packets of data. It requires low jitter and packet loss to ensure clear and uninterrupted voice quality.
  - **Online gaming**: This application allows users to play games with other players over the Internet. It requires fast and consistent response times to ensure fair and enjoyable gameplay.
  - **Community storage applications**: These applications allow users to store and access data on a distributed network of servers. They require high availability and reliability to ensure data integrity and security.
  - **Some e-commerce applications**: These applications allow users to buy and sell goods and services online. They require timely and accurate processing of transactions and orders to ensure customer satisfaction and trust.
  - **Real-time operating system (RTOS)**: This is a type of operating system that is designed to handle real-time tasks with minimal delays and interruptions. It provides features such as preemptive scheduling, priority-based interrupts, and memory management to ensure predictable and deterministic behavior.
  - **Instant messaging (IM) applications**: These applications allow users to send and receive text, audio, and video messages over the Internet. They require low latency and high throughput to ensure fast and seamless communication.
  - **Team collaboration applications**: These applications allow users to work together on projects and tasks over the Internet. They require real-time synchronization and coordination of data and actions to ensure effective and efficient collaboration.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System will be released on **Friday, 17 March 2023** at **10:00 AM GMT**.
- The notes will be available on the **course website** and the **learning management system**.
- The notes will cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time system modeling and analysis techniques
  - Real time system verification and validation methods
- The notes will be in the form of **PDF files** and **video lectures**.
- The notes will be accompanied by **self-assessment quizzes** and **practice exercises**.
- The notes will be **mandatory** for the students to study and prepare for the **Unit 1 test** which will be held on **Friday, 31 March 2023** at **10:00 AM GMT**.
- The notes will also be **useful** for the students to revise and review the concepts for the **final exam** which will be held on **Friday, 28 April 2023** at **10:00 AM GMT**.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by the end of the week, i.e., by Sunday, 19 March 2023, 11:59 PM.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in a clear, concise, and accurate manner, using proper terminology and notation.
- The notes should be formatted according to the guidelines given in the syllabus, using markdown syntax.
- The notes should be submitted as a single file, named as `RTS_Unit1_Notes_YourName.md`, to the online platform specified by the instructor.
- The notes will be evaluated based on the following criteria:
  - Completeness and correctness of the content
  - Organization and clarity of the presentation
  - Adherence to the format and style requirements
  - Originality and creativity of the examples and explanations
- The notes will carry 10% of the total marks for the subject of Real Time System.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also on the result being obtained within the time constraint.
- Time constraints related with real-time systems mean that there is a time interval allotted for the response of the ongoing program. This deadline means that the task should be completed within this time interval.
- Real-time systems are responsible for the completion of all tasks within their time intervals.
- Timing constraints associated with the real-time system are classified to identify the different types of timing constraints in a real-time system. Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Performance Constraints are further divided into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events.
  - Duration Constraint: A duration constraint describes the maximum or minimum time interval for which an event should occur or a condition should hold.
- Reliability Constraints are further divided into two types:
  - Synchronization Constraint: A synchronization constraint describes the order or precedence of events or conditions in the system.
  - Consistency Constraint: A consistency constraint describes the relationship or dependency of events or conditions in the system.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval logic, or graphical notations.
- Timing constraints can be validated using automatic test systems that can measure the actual response time and behavior of the system and compare them with the expected values.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.



### Hard Real Time Systems

- A hard real time system is a system that must meet strict deadlines for its tasks, otherwise it may cause serious consequences or failure  .
- A hard real time system is also known as an immediate real time system .
- Examples of hard real time systems are air traffic control systems, nuclear power plant control systems, missile guidance systems, etc.
- A hard real time system must have the following characteristics  :
  - The size of data and code is small and fixed.
  - The response time is in milliseconds or microseconds.
  - The peak load performance should be predictable and consistent.
  - The safety and reliability are critical and must be ensured by rigorous testing and verification.
  - The system must be able to handle concurrent events and interrupts with minimal latency.
  - The system must be able to synchronize with external clocks and devices.
- A hard real time system is different from a soft real time system, which can tolerate some degree of deadline misses or delays without causing failure .
- Examples of soft real time systems are multimedia applications, online gaming, video conferencing, etc .
- A hard real time system requires a specialized operating system that can support its timing and synchronization requirements  .
- Examples of hard real time operating systems are QNX, VxWorks, RTLinux, etc.
- A hard real time system may also use dedicated hardware or processors that can optimize its performance and reduce its complexity .
- Examples of hard real time hardware or processors are Intel® Time Coordinated Computing (Intel® TCC), Intel® Time Sensitive Networking (Intel® TSN), etc .



### Soft Real Time Systems

- A soft real time system is a system that has timing requirements, but not strict deadlines.  
- A soft real time system can tolerate some delay or jitter in the execution of tasks, without causing critical failure or unacceptable degradation of performance.   
- A soft real time system can run on multiple cores and impose fewer restrictions on applications than a hard real time system. 
- Examples of soft real time systems are multimedia streaming, video conferencing, online gaming, etc.  
- Characteristics of soft real time systems are:
  - They have a small window of time for program completion, rather than a precise moment. 
  - They can miss some deadlines occasionally, with low probability and acceptable consequences.  
  - They can adapt to varying workload and resource availability. 
  - They can trade off quality of output for timeliness of execution.



### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .
- A workload model describes the applications supported by the system, such as the set of tasks or jobs, their parameters, their dependencies, and their deadlines  .
- A resource model describes the resources available to the system, such as the CPU, memory, network, sensors, and actuators, their types and relations among them .
- A system model describes the system behavior, such as the scheduling policy, the resource allocation, the synchronization, and the fault tolerance mechanisms .
- A reference model can be used to analyze, design, and compare different real time systems, and to evaluate their feasibility, schedulability, and optimality .
- An example of a reference model is the Real-time Control System (RCS) architecture, which combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, and image processing .



### Processors and Resources

- Processors and resources are the two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are capable of executing tasks and controlling other resources. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. They are shared by multiple tasks and require mutual exclusion for access. Examples of resources are memory, files, sensors, and actuators.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors and resources can be interrupted and resumed by higher priority tasks. They allow for more flexibility and responsiveness in real-time systems.
- Non-preemptable processors and resources cannot be interrupted and resumed by higher priority tasks. They require careful scheduling and allocation to avoid blocking and deadlock in real-time systems.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors and resources are assigned to a single task or a group of tasks with the same priority. They reduce the overhead and complexity of scheduling and synchronization in real-time systems.
- Shared processors and resources are accessed by multiple tasks with different priorities. They increase the utilization and efficiency of system components in real-time systems.
- Processors and resources can have different characteristics and requirements for real-time systems, such as speed, capacity, reliability, availability, and power consumption .
- Processors and resources can be designed and optimized for real-time systems using various hardware and software techniques, such as time-coordinated computing, time-sensitive networking, real-time operating systems, and real-time programming languages .



### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that define its timing constraints and requirements.
- The temporal parameters of a job are  :
  - Release time (ri): The earliest time at which a job can start execution. It may be known exactly or within a range [r-, r+] (jitter).
  - Absolute deadline (di): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (Di): The maximum time allowed for a job to finish execution after its release time. It is equal to di - ri.
  - Feasible interval [(ri, di)]: The time interval in which a job can be feasibly scheduled and executed. It is equal to Di.
- The temporal parameters of a job depend on the characteristics of the real time system, such as the workload, the scheduling algorithm, the resource availability, and the performance metrics.
- The temporal parameters of a job can be used to analyze and verify the temporal behavior and correctness of a real time system, such as the schedulability, the response time, the utilization, and the deadline miss ratio.



### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline.
- Phase is the time at which the first instance of the task is released.
- Period is the time interval between two consecutive releases of the task.
- Execution time is the worst-case time required by the task to complete its execution.
- Deadline is the time by which the task must finish its execution.
- A periodic task can be represented by a tuple: T = <Φ, P, e, D>, where Φ is the phase, P is the period, e is the execution time, and D is the deadline.
- The periodic task model is a deterministic workload model that can accurately capture many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission.
- The periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a task may be at most J time units earlier or later than the exact start time of the period.
- The periodic task model can be analyzed using various scheduling algorithms, such as rate-monotonic, earliest-deadline-first, and fixed-priority.




### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal dependencies among jobs, such as control flow or synchronization. For example, a job J1 may need to finish before another job J2 can start, or a job J3 may need to wait for a signal from another job J4.
- Data dependency is imposed by the communication or sharing of data among jobs, such as input/output or shared memory. For example, a job J5 may need to read some data produced by another job J6, or a job J7 may need to write some data to a shared buffer accessed by another job J8.
- Precedence constraints and data dependency can be represented by a directed graph G = (J, <), where J is the set of jobs and < is the set of edges. Each edge (Ji, Jk) indicates that Ji is a predecessor of Jk, and Jk is a successor of Ji. This graph is called the precedence graph.
- Precedence constraints and data dependency can affect the feasibility and optimality of scheduling algorithms for real time systems. For example, some scheduling algorithms may assume that jobs are independent, which may not be true if there are precedence constraints or data dependency. Some scheduling algorithms may need to consider the precedence graph or the data dependency graph to ensure that jobs are executed in a correct and consistent order.



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their periods, execution times, deadlines, and priorities. Static scheduling is suitable for systems that have fixed and periodic tasks, and that do not require much flexibility or adaptability .
  - Dynamic scheduling is done at run time or during the system execution. It is based on the current state of the system, such as the availability of resources, the arrival of new tasks, the completion of existing tasks, and the occurrence of events. Dynamic scheduling is suitable for systems that have variable and aperiodic tasks, and that require more flexibility and adaptability .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and improve the schedulability of the system, but it can also introduce more overhead and complexity .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running. The higher priority task has to wait until the lower priority task finishes or is blocked. Non-preemptive scheduling can reduce the overhead and complexity, but it can also increase the response time and degrade the schedulability of the system .
- Real time scheduling algorithms are the rules or methods that determine which task to execute next in a system. There are many real time scheduling algorithms, such as rate monotonic, earliest deadline first, least laxity first, etc. Each algorithm has its own advantages and disadvantages, and its own assumptions and conditions for ensuring the schedulability of the system .
- Real time scheduling analysis is the process of verifying and testing the performance and correctness of the system and the algorithms under different scenarios and workloads. Real time scheduling analysis can be done using mathematical models, simulation tools, or empirical methods .



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution priorities and time slots to tasks or processes that have timing constraints. Real time systems are those whose correctness depends on both functionality and timing. There are different approaches to real time scheduling, depending on the characteristics and requirements of the system and the tasks. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, period, etc., are known at design time. The scheduler uses a precomputed table or a cyclic executive to determine which task to execute at each time instant. The advantage of this approach is that it is simple, predictable, and easy to verify. The disadvantage is that it is inflexible, wasteful of resources, and cannot handle dynamic or aperiodic tasks.

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft real time systems, where some of the properties of the tasks, such as arrival time, execution time, deadline, etc., are not known at design time or may vary at run time. The scheduler assigns a priority to each task based on some criteria, such as deadline, criticality, urgency, etc., and selects the highest priority task to execute at each time instant. The advantage of this approach is that it is flexible, adaptive, and can handle dynamic or aperiodic tasks. The disadvantage is that it is complex, unpredictable, and hard to verify.

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority and are scheduled in a circular order based on a fixed time slice or quantum. It is commonly used for time-shared systems, where the goal is to provide fair and responsive service to all the tasks. The advantage of this approach is that it is simple, fair, and easy to implement. The disadvantage is that it does not consider the timing constraints or the importance of the tasks, and may cause deadline misses or starvation.

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different weights or priorities and are scheduled in a circular order based on a variable time slice or quantum. The quantum of each task is proportional to its weight or priority. It is commonly used for multimedia systems, where the goal is to provide differentiated and quality-of-service (QoS) aware service to the tasks. The advantage of this approach is that it is simple, fair, and QoS aware. The disadvantage is that it does not consider the timing constraints or the urgency of the tasks, and may cause deadline misses or starvation.



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling .
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A schedule of the jobs is computed off-line and is stored for use at run-time.
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling can handle periodic tasks and aperiodic tasks with known arrival times.
- Clock-driven scheduling can also handle tasks with precedence constraints and resource sharing.
- Clock-driven scheduling can be implemented using table-driven or cyclic executive methods.
- Table-driven method uses a precomputed table that specifies the start time and end time of each job.
- Cyclic executive method uses a precomputed cyclic schedule that specifies the execution order of jobs in each cycle.
- Clock-driven scheduling has some advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement.
    - It is efficient and has low overhead.
    - It can guarantee the deadlines of hard real-time tasks.
    - It can avoid priority inversion and deadlock problems.
  - Disadvantages:
    - It is inflexible and cannot handle dynamic changes in the system.
    - It is pessimistic and may waste CPU time.
    - It is difficult to design and verify the schedule off-line.
    - It may not be suitable for tasks with variable execution times or arrival times.



### Weighted Round Robin Approach

- Weighted round robin (WRR) is a scheduling algorithm for tasks or data flows that generalizes the round robin algorithm by assigning different weights to different tasks or queues.
- WRR is a preemptive algorithm that can be used for scheduling real-time traffic in high-speed switched networks or for scheduling processes in a CPU .
- WRR approximates the generalized processor sharing (GPS) algorithm in a less computationally intensive way than weighted fair queueing (WFQ) by transmitting an amount of packets or executing an amount of instructions proportional to the weight of each task or queue in every round.
- WRR retains the advantage of round robin in eliminating starvation and also integrates priority scheduling by giving higher weights to higher priority tasks or queues.
- WRR is designed for maximum throughput in most scenarios, but it may increase the waiting time and response time for longer or heavier tasks or queues as they have to wait for their turn in every round.
- WRR can be implemented using several techniques, such as static or dynamic weights, deficit counters, or virtual clock.



### Priority Driven Approach

- Priority driven approach is a class of scheduling algorithms that never leave any resource idle intentionally.
- A resource becomes idle only when no job requiring the resource is ready for execution.
- It is an event driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur.
- Priority driven approach is useful for more dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events.
- Priority driven approach assigns a priority level to each job and executes the jobs in the order of their priority.
- Higher-priority jobs are executed before lower-priority jobs and can preempt lower-priority jobs if they arrive while the lower-priority jobs are running.
- Priority driven approach can improve the real-time performance and predictability of real-time systems by reducing the response time and deadline misses of critical jobs.
- Priority driven approach can be implemented using different priority assignment schemes, such as fixed priority, dynamic priority, or hybrid priority.
- Priority driven approach can also be classified into preemptive or non-preemptive, depending on whether a job can be interrupted by a higher-priority job or not.
- Priority driven approach has some challenges, such as priority inversion, blocking, and resource contention, which need to be addressed by using appropriate protocols and mechanisms.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival times, execution times, deadlines, etc.) are known in advance and do not change during the system execution. A static system can be validated before it runs and can use a fixed priority scheduling algorithm to assign tasks to processors. Static systems are suitable for hard real-time systems where the workload is predictable and the timing constraints are strict.   
- A **dynamic system** is one where the tasks and their attributes may vary unpredictably during the system execution. A dynamic system cannot be validated before it runs and may need a dynamic priority scheduling algorithm to assign tasks to processors. Dynamic systems are suitable for soft or firm real-time systems where the workload is variable and the timing constraints are flexible.   
- Static systems have the advantage of being easier to analyze and verify, but they have the disadvantage of being less adaptable and responsive to changing conditions. Dynamic systems have the advantage of being more flexible and efficient, but they have the disadvantage of being harder to analyze and verify.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems, where tasks have deadlines and preemption is allowed.
- EDF assigns priorities to tasks based on their absolute deadlines. The earlier the deadline, the higher the priority.
- LST assigns priorities to tasks based on their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The smaller the slack, the higher the priority.
- EDF and LST are optimal in the sense that they always produce a feasible schedule if one exists, i.e., they can meet all the deadlines of the tasks on a single processor.
- The optimality of EDF and LST can be proved by contradiction. Suppose there is a feasible schedule S produced by some other algorithm A, but not by EDF or LST. Then, we can transform S into an EDF or LST schedule by swapping the tasks at the scheduling points, without violating any deadlines. This contradicts the assumption that EDF or LST cannot produce a feasible schedule.
- EDF and LST have different advantages and disadvantages. EDF is simpler to implement and has lower overhead, but it may suffer from deadline misses due to transient overloads. LST is more robust to overloads and can handle aperiodic tasks better, but it requires more information and computation.



### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority .
- RMA is preemptive, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always meet the deadlines of a set of periodic tasks if any static priority assignment algorithm can.
- RMA has a simple schedulability test, which is based on the utilization factor of the tasks. The utilization factor of a task is the ratio of its execution time to its period .
- The schedulability test for RMA is:

  - For n tasks, the total utilization factor U must be less than or equal to n(2^(1/n) - 1), which is approximately 0.69 for large n .
  - For n tasks, if the total utilization factor U is less than or equal to n/2, then the tasks are always schedulable by RMA .
  - For n tasks, if the total utilization factor U is greater than n/2, then the tasks may or may not be schedulable by RMA, and a more detailed analysis is needed .

- RMA has some advantages and disadvantages, such as:

  - Advantages: simple, easy to implement, optimal for periodic tasks, low overhead, predictable .
  - Disadvantages: not optimal for aperiodic or sporadic tasks, may waste processor time, may cause priority inversion, may not meet all deadlines if the utilization factor is too high .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, priority, and resource requirement of all tasks for all time . A table is generated that contains the necessary scheduling decisions for use during the run-time . Offline scheduling is suitable for systems that have predictable and periodic tasks with fixed parameters . Offline scheduling can achieve optimal performance and guarantee schedulability of all tasks . However, offline scheduling is not flexible and adaptive to dynamic changes in the system, such as arrival of new tasks, variation of execution time, or failure of resources .
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system . The scheduler does not have prior knowledge about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task . Online scheduling can be either static or dynamic . Static online scheduling assigns a fixed priority to each task and schedules the tasks according to their priorities . Dynamic online scheduling assigns a variable priority to each task and schedules the tasks according to their current parameters, such as deadline, execution time, or slack time . Online scheduling is suitable for systems that have unpredictable and aperiodic tasks with variable parameters . Online scheduling can handle dynamic changes in the system and provide flexibility and adaptability . However, online scheduling may not achieve optimal performance and may not guarantee schedulability of all tasks .



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival or execution pattern, and have soft deadlines or no deadlines at all.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive jobs, and have hard or firm deadlines.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, and schedule the highest priority job at any given time.
- Clock driven systems are systems that schedule jobs based on a pre-defined table that specifies the start and end times of each job in each cycle.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs.
- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to accommodate the variability of aperiodic jobs and the unpredictability of sporadic jobs.

- Some of the algorithms for scheduling aperiodic and sporadic jobs in priority driven systems are:

  - Background scheduling: aperiodic jobs are executed only when no periodic or sporadic jobs are ready, and have the lowest priority in the system. This algorithm guarantees the schedulability of periodic and sporadic jobs, but may result in poor response times for aperiodic jobs.
  - Polling server: a periodic task with a fixed period and execution time is created to serve aperiodic jobs. The server has a priority higher than some periodic tasks, and can preempt them to execute aperiodic jobs. This algorithm improves the responsiveness of aperiodic jobs, but may cause deadline misses for periodic tasks with lower priority than the server.
  - Deferrable server: similar to the polling server, but the server can defer its execution if no aperiodic jobs are ready, and use its unused capacity later in the same period. This algorithm reduces the interference of the server on periodic tasks, but may still cause deadline misses for periodic tasks with lower priority than the server.
  - Sporadic server: similar to the deferrable server, but the server has a minimum inter-arrival time between successive executions, and can replenish its capacity after each execution. This algorithm allows the server to handle sporadic jobs as well as aperiodic jobs, but may still cause deadline misses for periodic tasks with lower priority than the server.
  - Slack stealing: aperiodic jobs are executed by stealing the slack time of periodic and sporadic jobs, where slack time is the difference between the worst-case execution time and the actual execution time of a job. This algorithm maximizes the utilization of the system, and can complete aperiodic jobs early, but requires the knowledge of the slack time of all jobs in the system.

- Some of the algorithms for scheduling aperiodic and sporadic jobs in clock driven systems are:

  - Spare capacity scheduling: aperiodic jobs are executed in the spare slots of the schedule table, where spare slots are the intervals that are not allocated to any periodic or sporadic jobs. This algorithm guarantees the schedulability of periodic and sporadic jobs, but may result in poor response times for aperiodic jobs if the spare capacity is low.
  - Dynamic adjustment of the schedule table: the schedule table is modified at run time to accommodate aperiodic and sporadic jobs, by shifting or swapping the slots of periodic jobs. This algorithm improves the responsiveness of aperiodic and sporadic jobs, but may cause deadline misses for periodic jobs if the modifications are not feasible or safe.
  - Hybrid scheduling: a combination of clock driven and priority driven scheduling, where aperiodic and sporadic jobs are handled by a priority driven algorithm, and periodic jobs are handled by a clock driven algorithm. This algorithm allows the flexibility of priority driven scheduling and the predictability of clock driven scheduling, but may require complex coordination and synchronization between the two algorithms.



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of one computer system available to other computer systems on a network.
- Resource sharing can improve the efficiency, performance, reliability, and scalability of distributed systems by allowing multiple users and applications to access and utilize the same resources.
- Resource sharing can also enable collaboration, communication, and coordination among users and applications by allowing them to exchange data and information.
- Some examples of resources that can be shared on a network are:

  - Hardware resources, such as printers, scanners, disks, memory, CPU, etc.
  - Software resources, such as applications, databases, files, etc.
  - Data resources, such as documents, images, videos, etc.
  - Information resources, such as web pages, news, blogs, etc.

- Resource sharing can be classified into two types:

  - Centralized resource sharing, where the resources are managed and controlled by a single server or a group of servers on the network. The clients request the resources from the server and the server grants or denies the requests. The server is responsible for maintaining the security, consistency, and availability of the resources. Examples of centralized resource sharing are client-server systems, file servers, print servers, etc.
  - Distributed resource sharing, where the resources are distributed among multiple nodes on the network. The nodes cooperate and coordinate with each other to provide the resources to the clients. The nodes are responsible for managing their own resources and communicating with other nodes. Examples of distributed resource sharing are peer-to-peer systems, distributed databases, distributed file systems, etc.

- Resource sharing can involve different levels of abstraction and granularity, depending on the type and nature of the resources and the requirements of the users and applications. Some examples of different levels of resource sharing are:

  - Physical resource sharing, where the physical devices or components of the resources are shared among multiple users or applications. For example, sharing a printer, a disk, or a CPU among different processes or users.
  - Logical resource sharing, where the logical entities or representations of the resources are shared among multiple users or applications. For example, sharing a file, a database, or a web page among different processes or users.
  - Functional resource sharing, where the functions or services of the resources are shared among multiple users or applications. For example, sharing a printing service, a database service, or a web service among different processes or users.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause priority inversion, timing anomalies, or deadlock.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, while a medium-priority task preempts the low-priority task.
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for a resource is granted, and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention, and to ensure the correctness and timeliness of tasks.
- RAC is especially important for priority-driven systems, where tasks have different levels of urgency and importance.
- RAC can be classified into two categories: non-preemptive and preemptive.
- Non-preemptive RAC means that a task that holds a resource cannot be preempted by another task until it releases the resource.
- Preemptive RAC means that a task that holds a resource can be preempted by another task, but the resource is not released until the original task resumes and finishes its critical section.
- Examples of non-preemptive RAC protocols are: non-preemptive critical sections (NPCS), priority ceiling protocol (PCP), and stack resource policy (SRP).
- Examples of preemptive RAC protocols are: preemptive critical sections (PCS), priority inheritance protocol (PIP), and immediate ceiling priority protocol (ICPP).
- Each RAC protocol has its own advantages and disadvantages, such as blocking time, response time, memory overhead, and implementation complexity.
- The choice of RAC protocol depends on the characteristics of the system, such as the number and type of resources, the number and priority of tasks, and the timing constraints.



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- When a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- This protocol is called non-preemptive critical section protocol (NPCS) .
- The advantages of NPCS are:
  - It is simple and easy to implement .
  - It prevents deadlock, as no job is ever preempted when it holds any resource  .
  - It preserves the order of resource requests, as no job can jump ahead of another job that is waiting for the same resource .
- The disadvantages of NPCS are:
  - It may cause priority inversion, as a high-priority job may be blocked by a low-priority job that is holding a resource .
  - It may cause resource underutilization, as a resource may be idle while a job that is holding it is executing a non-critical section .
  - It may cause long response times, as a job may have to wait for a long time to access a resource that is held by another job .



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Both protocols aim to prevent or reduce priority inversion, which is a situation where a higher-priority task is blocked by a lower-priority task that holds a shared resource.
- Priority inversion can cause deadline misses, reduced throughput, and increased response time for real-time tasks.

#### Priority-Inheritance Protocol

- The basic idea of priority-inheritance protocol is to temporarily raise the priority of a task that holds a resource to the highest priority of any task that is waiting for the same resource.
- This way, the resource-holding task can finish its critical section and release the resource as soon as possible, reducing the blocking time for the higher-priority tasks.
- The priority of the resource-holding task is restored to its original value after releasing the resource.
- The priority-inheritance protocol can be implemented using a priority queue for each resource, where the tasks that request the resource are inserted in the order of their priorities.
- The priority-inheritance protocol guarantees that the blocking time of a task is bounded by the duration of the longest critical section of a lower-priority task that shares a resource with it.
- The priority-inheritance protocol is greedy, meaning that it allows a task to access a resource whenever the resource is free, regardless of the priorities of other tasks that may request the same resource later.

#### Priority-Ceiling Protocol

- The basic idea of priority-ceiling protocol is to assign a priority ceiling to each resource, which is the highest priority of any task that can access the resource.
- A task can access a resource only if its priority is higher than the priority ceilings of all the resources that are currently held by other tasks.
- This way, the priority-ceiling protocol prevents a task from being blocked by a lower-priority task that does not hold the requested resource, which is called avoidance blocking.
- The priority-ceiling protocol also prevents deadlock, which is a situation where a set of tasks are waiting for each other's resources in a circular manner.
- The priority-ceiling protocol can be implemented using a global variable that stores the highest priority ceiling of all the resources that are currently held by any task.
- The priority-ceiling protocol guarantees that the blocking time of a task is bounded by the duration of the shortest critical section of a lower-priority task that shares a resource with it.
- The priority-ceiling protocol is not greedy, meaning that it may withhold access to a free resource, causing a task to be blocked by a lower-priority task that may request the same resource later.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource.
- SBPCP has two rules: a scheduling rule and an allocation rule.
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time.
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource.
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the blocking time of a job is at most the execution time of one critical section of a higher priority job.
- SBPCP also prevents deadlock, since a job can only request a resource if its priority is equal to the ceiling priority of the resource, and the ceiling priorities are assigned in a non-decreasing order.
- SBPCP is an improvement over the Original Ceiling Priority Protocol (OCPP) and the Immediate Ceiling Priority Protocol (ICPP), which are two variants of the Priority Ceiling Protocol (PCP) that work by temporarily raising the priorities of jobs that access resources.
- SBPCP reduces the number of priority changes and context switches compared to OCPP and ICPP, and also allows for dynamic priority assignment of jobs.
- SBPCP is suitable for systems that have a fixed set of resources and a known set of jobs that can access them.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-Ceiling Protocol (PCP) is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- PCP works by temporarily raising the priorities of tasks that access shared resources and blocking tasks that have lower priorities than the ceiling of the system.
- PCP can be applied to dynamic priority systems, where the priorities of the periodic tasks change with time, but the resources required by each task remain constant.
- To use PCP in dynamic priority systems, the following steps are needed:
  - Assign a priority ceiling to each resource, which is the highest priority of any task that may access it.
  - Update the priority ceiling of each resource and the ceiling of the system each time task priorities change.
  - When a task requests a resource, check if its priority is higher than the ceiling of the system. If yes, grant the resource and raise the task's priority to the ceiling of the resource. If no, block the task and put it in a waiting queue.
  - When a task releases a resource, restore its original priority and check the waiting queue for the highest priority task that can be granted the resource.
- PCP ensures that at any time, at most one resource is accessed by more than one task, and the tasks that access the same resource are executed in the order of their original priorities.
- PCP also ensures that a task can be blocked by at most one lower priority task, and the blocking time is bounded by the worst-case execution time of the lower priority task.



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems to avoid unbounded priority inversion and mutual deadlock.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources that are held by other tasks, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the current ceiling of the system, which is the maximum of the ceilings of all the locked resources.
- A task that locks a resource inherits the ceiling of that resource, and cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceilings of the resources at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceilings of the resources at run time, based on the actual priorities of the tasks that request them.
- Dynamic preemption ceiling protocol has lower overhead and better response time than static preemption ceiling protocol, but requires more storage space and is applicable only to fixed preemption-level systems.
- Fixed preemption-level systems are a class of dynamic-priority systems, such as deadline-driven systems, where the priority of a task does not change during its execution.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable.
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section.
- The challenge of access control in multiple-unit resources is to prevent deadlock and priority inversion, while ensuring schedulability and resource utilization.
- There are different protocols for access control in multiple-unit resources, such as:
  - The Priority Inheritance Protocol (PIP): A job that locks a resource inherits the priority of the highest-priority job that is blocked on that resource. The priority is restored when the resource is unlocked.
  - The Priority Ceiling Protocol (PCP): Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource. A job can lock a resource only if its priority is higher than the priority ceiling of all locked resources. A job that locks a resource inherits the priority ceiling of that resource. The priority is restored when the resource is unlocked.
  - The Stack Resource Policy (SRP): Each job has a preemption level, which is the highest priority of any resource that it can lock. A job can lock a resource only if its preemption level is higher than the preemption level of all jobs that have locked any resource. A job that locks a resource inherits the preemption level of the highest-priority job that is blocked on that resource. The preemption level is restored when the resource is unlocked.
  - The Multiprocessor Priority Ceiling Protocol (MPCP): A generalization of PCP for multiprocessor systems. Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource on any processor. A job can lock a resource only if its priority is higher than the priority ceiling of all locked resources on any processor. A job that locks a resource inherits the priority ceiling of that resource. The priority is restored when the resource is unlocked.



### Controlling Concurrent Accesses to Data Objects

- In real time systems, data objects are shared resources that can be accessed by multiple concurrent tasks or transactions.
- Controlling concurrent accesses to data objects is important to ensure data consistency and to meet timing constraints of real time tasks or transactions.
- There are two main approaches for controlling concurrent accesses to data objects: pessimistic and optimistic.
- Pessimistic approaches prevent conflicts by locking data objects before accessing them. Examples of pessimistic approaches are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
- Optimistic approaches allow conflicts to occur and resolve them later by aborting or restarting transactions. Examples of optimistic approaches are timestamp ordering, multiversion concurrency control, and validation .
- The choice of the concurrency control approach depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, and the available resources.
- The performance of the concurrency control approach can be measured by metrics such as the number of aborted transactions, the number of missed deadlines, the response time, and the throughput.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real-Time Database Systems - ResearchGate
: Concurrency Control in Real-Time Database Systems - Springer



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on whether the parties are communicating at the same time or not.
- RTC can be mediated by various technologies, such as voice, video, text, or data.
- RTC can be used for various purposes, such as collaboration, entertainment, education, or emergency response.
- RTC can be classified into three types: one-to-one, one-to-many, and many-to-many.
- One-to-one RTC is a direct communication between two parties, such as a phone call or a chat.
- One-to-many RTC is a broadcast communication from one party to many others, such as a webinar or a podcast.
- Many-to-many RTC is a group communication among multiple parties, such as a video conference or a multiplayer game.
- RTC can have different levels of quality, security, and reliability, depending on the requirements and constraints of the application and the network.
- RTC can face various challenges, such as latency, jitter, packet loss, bandwidth limitations, and interoperability issues.



### Basic Concepts in Real Time Communication

- Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays .
- In RTC, there is always a direct path between the source and the destination. The term real time is synonymous with live.
- RTC is necessary to support real time guarantees of real time computing, which is a type of computing that requires a system to respond within a specified time constraint.
- RTC protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.
- Examples of RTC include voice over landlines and mobile phones, video conferencing, instant messaging, online gaming, live streaming, and telemedicine .
- RTC tools are software applications or platforms that enable RTC between users, such as Skype, Zoom, WhatsApp, Discord, and WebRTC.
- RTC challenges include ensuring quality of service (QoS), security, scalability, interoperability, and compatibility across different devices, networks, and standards  .



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable loss   . For example, a nuclear reactor control system, a flight control system, or a pacemaker system are hard real-time communication systems  .
- A soft real-time communication system is one that can tolerate some deadline misses, without causing severe damage or degradation of performance   . For example, a video conferencing system, a multimedia streaming system, or a web server are soft real-time communication systems  .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic. This means that hard real-time communication systems can guarantee the worst-case execution time and response time, while soft real-time communication systems can only provide statistical guarantees or average values.
- Hard real-time communication systems require strict scheduling algorithms and protocols, while soft real-time communication systems can use more flexible and adaptive methods . For example, hard real-time communication systems may use priority-based, preemptive, or deadline-driven scheduling, while soft real-time communication systems may use round-robin, fair, or feedback-based scheduling .
- Hard real-time communication systems have higher complexity and cost, while soft real-time communication systems have lower complexity and cost   . This is because hard real-time communication systems need to ensure the worst-case scenario, while soft real-time communication systems can optimize for the average-case scenario   .
- Hard real-time communication systems have higher reliability and safety, while soft real-time communication systems have higher usability and efficiency   . This is because hard real-time communication systems need to avoid any failure or loss, while soft real-time communication systems can trade-off some quality or accuracy for better performance or user experience   .



### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without intermediate storage  .
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic includes periodic, aperiodic and sporadic messages, each with different characteristics and requirements.
- Real time traffic can be modeled by tuples of inter-packet spacing, message length and reception deadline, such as Mi = (pi, ei, Di).
- Real time control consists of commands and feedback signals that are exchanged between controllers and controlled devices in a real time system.
- Real time control requires timely and reliable delivery of messages, as well as synchronization and coordination among controllers and devices.
- Real time control can be modeled by state machines, Petri nets, timed automata or other formal methods.
- In the model of real time communication, end users of the message application systems are sources and destinations residing in different hosts .
- The network interface of each host contains input queue and output queue, which are allocated to input and output buffers to store queuing information .
- The network consists of routers, switches and links that interconnect the hosts and provide the communication service .
- The network can be characterized by parameters such as bandwidth, delay, jitter, loss rate and error rate .
- The performance of real time communication depends on factors such as throughput, delay and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time .
- Delay is the time elapsed from the moment a message is generated by the source to the moment it is received by the destination .
- Jitter is the variation of delay over time, which can cause problems for applications that require constant or predictable timing .
- The goal of real time communication is to meet the quality of service (QoS) requirements of the applications, such as bounded delay, guaranteed throughput, minimum jitter and maximum reliability .
- To achieve this goal, various techniques and protocols can be used, such as reservation, admission control, scheduling, routing, congestion control, error control and synchronization .
- Real time communication is widely used in many domains, such as voice, video, gaming, telemedicine, industrial automation, robotics, smart grid and Internet of Things  .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are scheduling algorithms that assign different priorities to different classes of packets in a switched network, such as a router or a switch.
- The packets with higher priority are transmitted before the packets with lower priority, according to some predefined order or policy.
- Priority-based service disciplines can improve the quality of service (QoS) for real-time communication, such as voice or video, by reducing the delay and jitter of the packets.
- However, priority-based service disciplines can also cause starvation or unfairness for the packets with lower priority, especially when the network is congested or overloaded.
- Weighted round-robin (WRR) is a simple and popular priority-based service discipline that can provide some degree of fairness and differentiation among different classes of packets.
- WRR assigns a weight to each priority queue, which determines the number of packets or bytes that can be transmitted from that queue in each round.
- WRR cycles through the non-empty priority queues in a circular order, and transmits a fixed amount of packets or bytes from each queue, according to its weight, before moving to the next queue.
- WRR can guarantee a minimum bandwidth allocation for each priority queue, and can also accommodate different packet sizes and arrival rates.
- However, WRR can also introduce large delay and jitter variations for the packets, especially when the weights are not proportional to the traffic demands or the packet sizes of each priority queue.
- Moreover, WRR can be inefficient or unfair when some priority queues are empty or underutilized, as it wastes the transmission opportunities or bandwidth that could be used by other queues.
- To overcome these limitations, several variants or extensions of WRR have been proposed, such as weighted fair queuing (WFQ), class-based weighted fair queuing (CBWFQ), weighted fair priority queuing (WFPQ), and rate-controlled frame-based weighted round robin (RFWRR).
- These algorithms aim to provide better QoS guarantees, such as delay bounds, jitter bounds, or proportional fairness, for different classes of packets, by using more sophisticated mechanisms, such as virtual time, virtual finish time, rate control, or frame size, to schedule the packets.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols are mechanisms that allow several users or transmitters to access a common medium or channel.
- MAC protocols play an important role in the development of both wired and wireless networks, especially in broadcast networks where a single transmitter can reach multiple receivers .
- MAC protocols can be classified into two main categories: random access and scheduling .
- Random access protocols allow users to transmit whenever they have data to send, without any coordination with other users. However, this may result in collisions, where two or more users transmit at the same time and interfere with each other. Examples of random access protocols are ALOHA, slotted ALOHA, and carrier sense multiple access with collision detection (CSMA/CD) .
- Scheduling protocols require users to follow some rules or algorithms to determine when they can transmit, avoiding collisions. Examples of scheduling protocols are time division multiple access (TDMA), frequency division multiple access (FDMA), and code division multiple access (CDMA) .
- In wireless networks, MAC protocols face additional challenges, such as hidden terminal problem, exposed terminal problem, fading, and mobility .
- Hidden terminal problem occurs when two users are within the transmission range of a common receiver, but not within each other's transmission range. This may cause them to transmit simultaneously and collide at the receiver .
- Exposed terminal problem occurs when a user is within the transmission range of two other users, but not within their mutual transmission range. This may prevent the user from transmitting to one of them, even though the other one is not receiving any transmission .
- Fading is the variation of signal strength due to multipath propagation, shadowing, and interference. This may cause transmission errors or losses .
- Mobility is the movement of users or nodes in the network. This may cause changes in the network topology, link quality, and interference patterns .
- To cope with these challenges, wireless MAC protocols need to be adaptive, reliable, and efficient.
- Adaptive MAC protocols can adjust their parameters or behavior according to the network conditions, such as channel quality, traffic load, or node density.
- Reliable MAC protocols can ensure the successful delivery of packets, by using techniques such as acknowledgments, retransmissions, error correction, or diversity.
- Efficient MAC protocols can maximize the network throughput, by using techniques such as channel access control, collision avoidance, power control, or spatial reuse.
- An example of an adaptive and reliable MAC protocol for broadcast networks is ABROAD, which uses a combination of contention and scheduling to achieve high performance and reliability.
- ABROAD divides the channel into slots, and assigns a slot to each node based on its priority and channel quality. Nodes with higher priority or better channel quality get earlier slots, while nodes with lower priority or worse channel quality get later slots or no slots at all.
- ABROAD also uses a feedback mechanism, where the receiver broadcasts an acknowledgment (ACK) packet after each slot, indicating the status of the received packet. If the ACK is positive, the sender can move to the next packet. If the ACK is negative, the sender can retransmit the packet in the next slot or a later slot, depending on the channel quality.
- ABROAD can adapt to the network conditions by dynamically adjusting the slot assignment and the retransmission strategy, based on the feedback from the receiver and the channel quality estimation.
- ABROAD can achieve high reliability and efficiency, by reducing the collision probability, increasing the transmission success rate, and utilizing the channel resources.



### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource reservation protocols are network control protocols that enable Internet applications to obtain specific qualities of service (QoS) for their data flows or streams.
- QoS is the ability of a network to provide different levels of service to different applications or users, based on their needs and preferences.
- Resource reservation protocols use resource reservation and admission control mechanisms to establish and maintain QoS.
- Resource reservation is the process of allocating network resources (such as bandwidth, buffer, CPU, etc.) to a data flow along its end-to-end path through the network.
- Admission control is the process of deciding whether a new data flow can be admitted to the network without violating the QoS guarantees of the existing flows.
- Resource reservation protocols can be classified into two categories: sender-initiated and receiver-initiated.
- Sender-initiated protocols are initiated by the sender of the data flow, who specifies the QoS requirements and requests the network to reserve resources accordingly.
- Receiver-initiated protocols are initiated by the receiver of the data flow, who specifies the QoS requirements and requests the network to reserve resources accordingly.
- An example of a sender-initiated protocol is the Integrated Services (IntServ) model, which uses the Resource Reservation Protocol (RSVP) to signal the QoS needs of a data flow along the devices in the end-to-end path through the network.
- An example of a receiver-initiated protocol is the Differentiated Services (DiffServ) model, which uses the Differentiated Services Code Point (DSCP) field in the IP header to mark the packets of a data flow with a certain QoS level, and relies on the network devices to provide the appropriate QoS treatment based on the DSCP value.
- Resource reservation protocols can be used for both multicast and unicast data flows.
- Multicast data flows are data flows that are sent from one sender to multiple receivers, such as videoconferencing or online gaming.
- Unicast data flows are data flows that are sent from one sender to one receiver, such as IP telephony or video streaming.
- Resource reservation protocols can be used for both real-time and non-real-time data flows.
- Real-time data flows are data flows that have strict QoS requirements, such as timeliness, jitter, and delay, and cannot tolerate significant variations in network performance, such as videoconferencing or IP telephony.
- Non-real-time data flows are data flows that have less strict QoS requirements, such as reliability and throughput, and can tolerate some variations in network performance, such as web browsing or file transfer.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can process data and events that have critically defined time constraints.
- An RTOS is different from a general-purpose operating system, such as Windows or Linux, which are designed for time-sharing and multitasking applications.
- An RTOS provides features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS can be used for deeply embedded applications, such as industrial control, telephone switching, flight control, and real-time simulations.
- A real-time database system (RTDBS) is a database system that can perform database operations with real-time constraints.
- An RTDBS is different from a conventional database system, such as Oracle or MySQL, which are designed for batch processing and data warehousing applications.
- An RTDBS provides features such as real-time transactions, concurrency control, data consistency, and recovery.
- An RTDBS can be based on SQL or NoSQL, and can be used for operational databases and business analytics applications .
- A real-time database system can interact with a real-time operating system to provide data services for real-time applications.



### Features of RTOS

- A real-time operating system (RTOS) is an operating system with two key features: **predictability** and **determinism**. This means that it will execute tasks quickly and efficiently, responding as expected every time.
- An RTOS is **small**, **fast**, **responsive**, and **deterministic**. It occupies very less memory and consumes fewer resources.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment. An RTOS needs to have **processing time requirements** that are fully understood and bound rather than just kept as a minimum.
- An RTOS can use different **scheduling algorithms** to manage the tasks, such as co-operative scheduling, pre-emptive scheduling, or hybrid scheduling. The choice of the algorithm depends on the application and the system requirements.
- An RTOS can provide various **services** to the tasks, such as inter-task communication, synchronization, memory management, timer management, interrupt handling, and device drivers. These services help the tasks to perform their functions and interact with the hardware and other tasks.
- An RTOS can support different **types** of tasks, such as periodic, aperiodic, or sporadic tasks. The type of the task determines its frequency, deadline, and priority.
- An RTOS can also support different **modes** of operation, such as normal mode, idle mode, or power-saving mode. The mode of operation affects the performance and the power consumption of the system.



### Time Services

- Time services are the mechanisms that provide the functionality of measuring, synchronizing, and controlling the time in real-time systems.
- Time services are essential for real-time systems because they enable the system to meet the deadlines, coordinate the activities, and monitor the performance of the system.
- Time services can be classified into two categories: time measurement and time synchronization.
- Time measurement is the process of determining the current time or the elapsed time between two events. Time measurement can be done using hardware or software timers, clocks, or counters.
- Time synchronization is the process of ensuring that the clocks of different devices or processes are aligned or agree on a common time reference. Time synchronization can be done using internal or external methods, such as network protocols, GPS signals, or atomic clocks.
- Time services can also provide other functions, such as time stamping, time scheduling, time monitoring, and time adjustment.
- Time stamping is the process of attaching a time value to a data item or an event. Time stamping can be used for logging, auditing, or ordering purposes.
- Time scheduling is the process of allocating time slots or resources to different tasks or processes according to their priorities, deadlines, or dependencies. Time scheduling can be used for managing concurrency, load balancing, or resource allocation.
- Time monitoring is the process of observing or measuring the time-related behavior or performance of the system or its components. Time monitoring can be used for detecting errors, faults, or anomalies, or for optimizing the system.
- Time adjustment is the process of modifying or correcting the time values or the clocks of the system or its components. Time adjustment can be used for compensating for drift, delay, or skew, or for synchronizing the system.
- Time services can be implemented using different hardware and software components, such as timers, clocks, counters, interrupts, schedulers, protocols, or algorithms .
- Time services can be evaluated using different criteria, such as accuracy, precision, resolution, stability, scalability, or reliability .
- Time services can be applied to various domains and applications, such as industrial control, telephone switching, flight control, real-time simulation, or time and attendance systems .



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing, which is the key feature of a RTOS.
- However, some variants of UNIX, such as Linux, have been modified to add real-time capabilities to the kernel architecture designed for general purpose computing .
- Some examples of using Linux as a RTOS are NASA and the Air Force Research Lab for human-in-the-loop (HITL) simulation, and SpaceX for its Falcon launch vehicles and Dragon capsules .
- The challenges of using Linux as a RTOS include:
  - The need to patch the kernel with real-time extensions, such as PREEMPT_RT, which can introduce bugs and compatibility issues .
  - The difficulty of isolating and testing the real-time performance of the system, especially in complex and dynamic environments .
  - The trade-off between latency and throughput, which can affect the quality of service and the resource utilization of the system .
  - The lack of standardization and certification for real-time Linux, which can limit its adoption and trustworthiness in safety-critical domains .



### POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a family of standards that define a common interface for operating systems, especially UNIX-based ones.
- POSIX aims to promote portability and interoperability of applications across different platforms, by specifying the services and interfaces that an operating system should provide.
- POSIX also covers extensions for real-time systems, which are systems that have strict timing constraints and need to respond to events within a specified deadline.
- POSIX real-time extensions include specifications for:
  - Scheduling policies and parameters, such as priority-based preemptive scheduling and deadline scheduling.
  - Timers and clocks, such as high-resolution timers and monotonic clocks.
  - Synchronization primitives, such as mutexes, condition variables, semaphores, and barriers.
  - Memory management, such as memory locking and mapping.
  - Signals and signal handlers, such as real-time signals and queues.
  - Message passing and interprocess communication, such as message queues, pipes, and sockets.
  - Asynchronous I/O and notification, such as aio_read, aio_write, and sigevent.
- POSIX real-time issues include:
  - The trade-off between portability and performance, as some POSIX features may not be optimal or efficient for real-time systems, and some real-time features may not be widely supported or implemented by different operating systems.
  - The complexity and variability of the POSIX standards, as there are many optional and conditional features, and different levels of conformance and compliance, which may affect the compatibility and consistency of applications.
  - The lack of verification and validation tools, as there are few methods and metrics to measure and test the real-time behavior and performance of POSIX systems and applications.
  - The gap between theory and practice, as some POSIX features may not be fully or correctly implemented by operating systems, or may not be used or understood by application developers, which may lead to errors and failures in real-time systems.



### Characteristics of Temporal Data

- Temporal data is the data that is **valid only for a prescribed time**. It becomes **invalid or obsolete** after a certain period of time .
- Temporal data can represent **time in some form**, such as dates, timestamps, intervals, durations, or periods. It can also represent **events or phenomena** that occur or change over time, such as weather, traffic, demographics, etc.
- Temporal data can be **analyzed chronologically** to study patterns, trends, correlations, or causations. It can also be **placed in a chronological sequence** to show the order or history of events or changes.
- Temporal data can have different **temporal aspects** or dimensions, such as **valid time**, **transaction time**, or **decision time**. Valid time is the time when a fact is true in the real world. Transaction time is the time when a fact is stored or updated in the database. Decision time is the time when a fact is known or decided by an agent.
- Temporal data can be stored and managed in **temporal databases**, which are databases that support temporal data types, operations, and queries. Temporal databases can be **uni-temporal**, **bi-temporal**, or **tri-temporal**, depending on how many temporal aspects they capture.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not match the current state of the physical environment. This can happen due to delays in data acquisition, transmission, processing, or storage.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other. This can happen due to concurrent updates, replication, or failures.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the occurrence of some events, such as data changes, deadlines, or transactions. Triggered updates can reduce data staleness by refreshing the data in the database as soon as possible.
  - Absolute validity, which is a temporal consistency constraint that requires the data stored in the database to be within a predefined limit of the current state of the physical environment. Absolute validity can prevent data staleness by discarding the data that are too old or inaccurate.
  - Relative validity, which is a temporal consistency constraint that requires the data read by a transaction to be within a predefined limit of the data written by another transaction. Relative validity can prevent data inconsistency by ensuring that the transactions see a consistent view of the data.
  - Serialization, which is a concurrency control technique that orders the execution of transactions in a way that preserves the logical consistency of the data. Serialization can prevent data inconsistency by avoiding conflicts and anomalies among transactions.



### Concurrency Control

- Concurrency control is a database management systems (DBMS) concept that is used to address occur with a multi-user system.
- Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity.
- A transaction is a logical unit of work that accesses or modifies one or more data items in a database.
- A transaction is said to be successfully completed if and only if, it satisfies the ACID properties, namely, atomicity, consistency, isolation, and durability.
- A concurrent execution of a set of transactions is said to be serializable if and only if the database operations carried out by them is equivalent to some serial execution of these transactions.
- Serializability is a desirable property for concurrency control, as it ensures the correctness and consistency of the database state.

### Concurrency Control in Real-Time Database Systems

- A real-time database system (RTDBS) is a database system that supports applications with timing constraints, such as deadline, response time, and freshness.
- A real-time transaction is a transaction that has a deadline, which is the time by which it must be completed.
- A real-time transaction is said to be feasible if it can be completed within its deadline.
- A real-time transaction is said to be schedulable if it can be assigned a priority such that it is feasible under a given scheduling policy.
- A real-time transaction is said to be correct if it is both serializable and feasible.
- Concurrency control in RTDBS is about ensuring the correctness of real-time transactions by restricting concurrent transactions to be serializable and schedulable.
- Concurrency control in RTDBS faces many challenges, such as handling data conflicts, data freshness, data replication, data partitioning, and distributed transactions.
- Concurrency control in RTDBS can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control methods prevent data conflicts by locking data items before accessing them, and aborting transactions that violate the serializability or schedulability constraints.
- Optimistic concurrency control methods allow data conflicts to occur, but detect and resolve them at the end of transactions, by validating the serializability and schedulability constraints.
- Pessimistic concurrency control methods are suitable for applications with high data contention and low abort tolerance, while optimistic concurrency control methods are suitable for applications with low data contention and high abort tolerance.
- Some examples of pessimistic concurrency control methods for RTDBS are: priority inheritance protocol, priority ceiling protocol, two-phase locking protocol, and timestamp ordering protocol.
- Some examples of optimistic concurrency control methods for RTDBS are: optimistic concurrency control with backward validation, optimistic concurrency control with forward validation, and multiversion concurrency control.



### Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for applications that require timely and consistent responses, such as accounting, banking, law, medical records, multimedia, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases guarantee that transactions meet their deadlines, otherwise the system may fail. They are suitable for critical systems, such as avionics, nuclear power plants, and military applications.
  - Soft real-time databases allow some transactions to miss their deadlines, but try to minimize the number and severity of such violations. They are suitable for non-critical systems, such as e-commerce, online gaming, and social media.
- Some of the attributes of live real-time databases are:
  - High availability: The database should be accessible and operational at all times, even in the event of failures or disasters.
  - High performance: The database should be able to process transactions and queries with low latency and high throughput, while maintaining data consistency and integrity.
  - High scalability: The database should be able to handle increasing workloads and data volumes, without compromising availability or performance.
  - High reliability: The database should be able to recover from errors and faults, and ensure data durability and correctness.
  - High security: The database should be able to protect data from unauthorized access, modification, or deletion, and comply with relevant regulations and standards.
  - High adaptability: The database should be able to support different data models, query languages, and access methods, and accommodate changing requirements and user preferences.
  - High interoperability: The database should be able to communicate and integrate with other systems and applications, and support data exchange and migration.
  - High usability: The database should be easy to use and manage, and provide user-friendly interfaces and tools.
  - High affordability: The database should be cost-effective and offer a good return on investment, and provide flexible pricing and licensing options.
- Some of the examples of commercial real-time databases are:
  - Google Cloud Firestore: A scalable, serverless, NoSQL document database for web, mobile, and server development. It offers real-time synchronization, offline support, and ACID transactions.
  - Google Cloud Bigtable: A highly performant, fully managed NoSQL database service for large analytical and operational workloads. It offers high availability, low latency, and consistency.
  - Google Cloud Spanner: A fully managed, relational database service that combines the benefits of SQL and NoSQL. It offers global scalability, strong consistency, and high availability.
  - Google Cloud Memorystore: A fully managed, in-memory data store service for Redis and Memcached. It offers sub-millisecond latency, high throughput, and automatic scaling.
  - Google Cloud SQL: A fully managed, relational database service for MySQL, PostgreSQL, and SQL Server. It offers high performance, availability, and security, and supports various frameworks and tools.

