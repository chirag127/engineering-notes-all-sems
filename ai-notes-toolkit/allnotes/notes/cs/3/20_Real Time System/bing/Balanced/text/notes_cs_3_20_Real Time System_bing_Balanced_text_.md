

## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, or risk failure or unacceptable consequences.
- Real time systems are often used for applications that require high performance, reliability, safety, or security, such as avionics, robotics, industrial control, multimedia, gaming, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
- Hard real time systems are systems that must meet all their deadlines, otherwise the system may fail or cause severe damage. For example, a pacemaker, an airbag, or a missile guidance system are hard real time systems.
- Soft real time systems are systems that can tolerate some missed deadlines, but the quality of service or user experience may degrade. For example, a video streaming, a voice call, or a web server are soft real time systems.
- Real time systems have some common characteristics, such as concurrency, predictability, responsiveness, dependability, and adaptability.
- Concurrency means that a real time system can handle multiple events or tasks simultaneously, using parallel or distributed processing techniques.
- Predictability means that a real time system can guarantee the worst-case execution time and resource usage of its tasks, using scheduling algorithms and analysis methods.
- Responsiveness means that a real time system can react to events or inputs quickly, using interrupt mechanisms and priority schemes.
- Dependability means that a real time system can ensure the correctness and availability of its functions, using fault tolerance and recovery techniques.
- Adaptability means that a real time system can adjust to changing conditions or requirements, using feedback and control mechanisms.



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a computer system that **responds to input signals fast enough to keep an operation moving at its required speed**.
- A real-time system is also characterized by its ability to **produce the expected result within a defined deadline (timeliness)** and to **coordinate independent clocks and operate together in unison (time synchronization)**.
- A real-time system is one which **controls an environment by receiving data, processing them, and returning the results sufficiently quickly to affect the environment at that time**.
- A real-time system is subjected to **real-time, i.e., the response should be guaranteed within a specified timing constraint or the system should meet the specified deadline**.
- Examples of real-time systems are flight control systems, real-time monitors, gaming computers, videoconferencing systems, etc.



### Typical Real Time Applications

- A real-time application (RTA) is an application that requires a timely response from the underlying system or hardware to function correctly and meet user expectations.
- Real-time applications can be classified into two types: hard real-time and soft real-time.
- Hard real-time applications have strict deadlines and failure to meet them can result in catastrophic consequences, such as loss of life or damage to property. Examples of hard real-time applications are air traffic control, nuclear reactor control, and pacemakers.
- Soft real-time applications have more flexible deadlines and failure to meet them can result in degraded performance or quality of service, but not severe consequences. Examples of soft real-time applications are video conferencing, online gaming, and multimedia streaming.
- Some of the typical real-time applications are:

  - Digital control: This involves using sensors and actuators to monitor and control physical processes, such as temperature, pressure, speed, or position. Examples of digital control applications are industrial automation, automotive systems, and smart homes.
  - Optimal control: This involves using mathematical models and algorithms to optimize the performance or efficiency of a system, such as minimizing fuel consumption, maximizing profit, or reducing emissions. Examples of optimal control applications are power grid management, flight control, and traffic control.
  - Command and control: This involves using communication and coordination to manage complex and dynamic situations, such as military operations, emergency response, or disaster relief. Examples of command and control applications are battlefield management, fire fighting, and air traffic control.
  - Signal processing: This involves using mathematical techniques to analyze, transform, or synthesize signals, such as audio, video, or radar. Examples of signal processing applications are speech recognition, image processing, and encryption.
  - Tracking: This involves using sensors and algorithms to estimate the state or location of a moving object, such as a vehicle, a person, or a missile. Examples of tracking applications are navigation, surveillance, and missile guidance.
  - Real-time databases: This involves using data structures and protocols to store, retrieve, and update data in a timely and consistent manner, such as sensor data, transaction data, or event data. Examples of real-time databases are stock market databases, sensor networks, and online reservation systems.
  - Multimedia: This involves using audio, video, or graphics to create, transmit, or display content, such as music, movies, or games. Examples of multimedia applications are video conferencing, online gaming, and virtual reality.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System will be released on the following dates:
  - Lecture 1: Introduction and Overview of Real Time Systems - 16 March 2023
  - Lecture 2: Characteristics and Challenges of Real Time Systems - 18 March 2023
  - Lecture 3: Classification and Examples of Real Time Systems - 20 March 2023
  - Lecture 4: Real Time System Design Issues and Methodologies - 22 March 2023
  - Lecture 5: Real Time Scheduling Algorithms and Analysis - 24 March 2023
- The notes will be available on the course website and the learning management system (LMS) by 10:00 AM on the respective dates.
- The notes will be in PDF format and will contain the slides, diagrams, examples, and exercises covered in the lectures.
- The notes will also have references to the recommended textbooks and online resources for further reading and practice.
- The notes are meant to supplement the lectures and not to replace them. Students are expected to attend the lectures and participate in the discussions and activities.
- The notes will be helpful for preparing for the quizzes, assignments, and exams of the course. Students are advised to review the notes regularly and clarify any doubts with the instructor or the teaching assistants.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by the end of the week, i.e., by Friday, 17 March 2023, 11:59 PM.
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
  - Organization and structure of the notes
  - Clarity and readability of the notes
  - Adherence to the formatting and naming conventions
- The notes will carry 10% of the total marks for the subject of Real Time System.
- Late submissions will incur a penalty of 10% of the marks per day of delay.
- No submissions will be accepted after Monday, 20 March 2023, 11:59 PM.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also on the result being obtained within the time constraint.
- Every real-time system has a set of timing constraints that it has been designed to meet. If a system does not have timing constraints, it is not real-time.
- Timing constraints can be broken down into two categories :
  - Performance constraints: The constraints enforced on the response of the system are known as performance constraints. They specify the maximum or minimum time required for the system to react to an event or complete a task.
  - Reliability constraints: The constraints enforced on the frequency or probability of the system failures are known as reliability constraints. They specify the maximum or minimum number of failures or errors allowed for the system to function correctly.
- Timing constraints can be expressed using various constructs in requirements languages, such as deadlines, periodicity, jitter, latency, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual response time and failure rate of the system and compare them with the expected values.
- Timing constraints can be affected by various factors, such as hardware, software, network, environment, etc. Therefore, real-time systems need to have time synchronization and timeliness capabilities to coordinate independent clocks and operate together in unison.



### Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline, otherwise it is considered to have failed  .
- A hard real time system has absolute deadlines, meaning that missing a deadline can cause a catastrophic consequence, such as loss of life, damage to property, or violation of contract .
- A hard real time system must also coordinate independent clocks and operate together in unison, which is called time synchronization.
- A hard real time system is typically found interacting at a low level with physical hardware, in embedded systems, such as avionics, automotive, robotics, medical, industrial, and military applications.
- A hard real time system must have predictable and deterministic behavior, meaning that it must always produce the same output for the same input and execute the same sequence of operations in the same amount of time .
- A hard real time system must also have high reliability and availability, meaning that it must be able to handle faults and errors gracefully and resume normal operation as soon as possible .
- A hard real time system must also have low latency and jitter, meaning that it must respond quickly and consistently to external events and stimuli .
- A hard real time system must also have high performance and efficiency, meaning that it must be able to handle high workloads and utilize the available resources optimally .
- A hard real time system must also have low power consumption and heat dissipation, meaning that it must be able to operate for long periods of time without degrading the quality of service or damaging the hardware .
- A hard real time system must also have high security and safety, meaning that it must be able to protect the data and the system from unauthorized access and malicious attacks, and prevent or mitigate any harm to the users or the environment .



### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of delay or jitter in meeting its deadlines, without causing a catastrophic failure or a significant degradation of performance.
- A soft real-time system is typically used for applications that require timely but not exact responses, such as multimedia streaming, online gaming, video conferencing, etc.
- A soft real-time system can run on multiple cores and impose fewer restrictions on applications, but it may not guarantee the worst-case execution time or the schedulability of tasks.
- A soft real-time system can be contrasted with a hard real-time system, which is a system that must meet its deadlines precisely and deterministically, otherwise it may cause severe consequences, such as loss of life or property.
- A hard real-time system is typically used for applications that require strict timing constraints, such as flight control, nuclear reactor control, medical devices, etc.
- A hard real-time system usually runs on a single core and imposes strict requirements on applications, such as predictable memory access, bounded input/output, preemptive scheduling, etc.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Software that controls the audio and video playback on a smart TV.
  - Software that monitors and adjusts the traffic signals in a city.
  - Software that manages the inventory and orders in an online store.
  - Software that controls the temperature and humidity in a greenhouse.



### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .
- A workload model describes the applications supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, priority, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.)  .
- A resource model describes the resources available to the system, such as the CPU, memory, network, sensors, actuators, etc., their types (e.g., preemptive, non-preemptive, shared, exclusive, etc.), and their relations (e.g., hierarchy, contention, etc.) .
- A system model describes the policies and mechanisms used by the system to manage the workload and the resources, such as the scheduling algorithm, the synchronization protocol, the communication protocol, the fault tolerance technique, etc.  .
- A reference model can be used to analyze the feasibility, schedulability, and optimality of a real time system, as well as to compare and evaluate different design choices and trade-offs  .
- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .



### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job. For example, a CPU can be preempted by a higher priority job and resume the execution of the lower priority job later.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job. For example, a printer cannot be preempted by another job until it finishes printing the current job.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. For example, a dedicated CPU can only execute one job at a time.
- Shared processors or resources can be used by multiple jobs, but only one job can access them at a time. For example, a shared memory can be accessed by multiple jobs, but only one job can read or write to it at a time.
- Processors and resources can affect the performance and correctness of real-time systems. Therefore, they need to be managed and scheduled carefully to meet the timing constraints and quality of service requirements of the real-time applications  .



### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- Some common temporal parameters are :
  - Release time (r<sub>i</sub>): The earliest time at which a job or task can start its execution.
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job or task must finish its execution.
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job or task to complete its execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval in which a job or task can be feasibly executed. It is equal to D<sub>i</sub>.
- Temporal parameters are important for defining the performance and correctness of a real time system. They are used to determine the schedulability and feasibility of a real time workload, and to design appropriate scheduling algorithms and policies.
- Temporal parameters may be known in advance (static), or may vary depending on the system state and environment (dynamic). They may also be deterministic (fixed) or stochastic (random).
- Temporal parameters may have different levels of criticality, depending on the consequences of missing them. For example, a hard real time system may have strict temporal parameters that must be met at all times, while a soft real time system may have flexible temporal parameters that can tolerate some degree of deviation.



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period. A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The periodic task model assumes that each task has a known and constant period, execution time, and deadline, and that each task releases its first job at its phase, and then releases a new job at the start of each period .
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can be used to analyze the schedulability of a set of tasks under different scheduling algorithms, such as rate-monotonic, earliest-deadline-first, or fixed-priority . The schedulability analysis can be based on utilization, response time, or demand bound functions.



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal order of the jobs, while data dependency is caused by the communication or sharing of data among the jobs.
- Precedence constraints can be represented by a directed graph, called a precedence graph, where the vertices are the jobs and the edges indicate the order of execution. For example, if job J1 must execute before job J2, then there is an edge from J1 to J2 in the graph  .
- Data dependency cannot be captured by a precedence graph, as it depends on the data values and the synchronization mechanisms used by the jobs. For example, if job J1 writes to a shared variable that is read by job J2, then J2 is data dependent on J1, but this does not imply a precedence constraint between them .
- Precedence constraints and data dependency may affect the feasibility and optimality of the scheduling algorithms for real time systems, as they limit the possible choices of execution order and introduce additional overheads for synchronization and communication. Therefore, they must be taken into account in the design and analysis of real time systems  .



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling involves breaking a program into multiple threads or processes that can run concurrently and independently on the available resources .
- Real time scheduling requires a scheduler, a clock and a processing hardware element to coordinate the execution of tasks.
- Real time scheduling can be classified into two types: static and dynamic.
  - Static scheduling is done at compile time or design time, and does not change at run time. Static scheduling is suitable for predictable and periodic tasks that have fixed deadlines and priorities.
  - Dynamic scheduling is done at run time, and can change according to the system state and the arrival of new tasks. Dynamic scheduling is suitable for unpredictable and aperiodic tasks that have variable deadlines and priorities.
- Real time scheduling can also be classified into two categories: hard and soft.
  - Hard real time scheduling guarantees that all tasks will meet their deadlines, and any missed deadline will result in a system failure. Hard real time scheduling is used for safety-critical and time-critical applications, such as avionics, nuclear power plants and medical devices.
  - Soft real time scheduling tries to meet as many deadlines as possible, but some missed deadlines are tolerable and will not cause a system failure. Soft real time scheduling is used for performance-critical and quality-critical applications, such as multimedia, gaming and online services.
- Real time scheduling algorithms can be classified into three groups: preemptive, non-preemptive and cooperative.
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running, and resume it later when the higher priority task is completed or blocked. Preemptive scheduling can reduce the response time and the deadline miss ratio of tasks, but it can also increase the context switch overhead and the resource contention.
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running, and waits until the lower priority task is completed or blocked. Non-preemptive scheduling can reduce the context switch overhead and the resource contention, but it can also increase the response time and the deadline miss ratio of tasks.
  - Cooperative scheduling is a hybrid of preemptive and non-preemptive scheduling, where a task can voluntarily yield the processor to another task, or request the processor from another task. Cooperative scheduling can balance the trade-offs between preemptive and non-preemptive scheduling, but it requires the tasks to cooperate and communicate with each other.
- Some examples of real time scheduling algorithms are:
  - Rate monotonic scheduling (RMS): a static, preemptive and hard real time scheduling algorithm that assigns priorities to tasks based on their periods, such that the shorter the period, the higher the priority.
  - Earliest deadline first scheduling (EDF): a dynamic, preemptive and soft real time scheduling algorithm that assigns priorities to tasks based on their deadlines, such that the earlier the deadline, the higher the priority.
  - Least laxity first scheduling (LLF): a dynamic, preemptive and soft real time scheduling algorithm that assigns priorities to tasks based on their laxity, which is the difference between their deadline and their remaining execution time, such that the smaller the laxity, the higher the priority.
  - Round robin scheduling (RR): a dynamic, preemptive and soft real time scheduling algorithm that assigns equal priorities to all tasks, and allocates the processor to each task for a fixed time slice in a circular order.
  - Priority inheritance protocol (PIP): a technique to prevent priority inversion, which is a situation where a higher priority task is blocked by a lower priority task that holds a shared resource, and the lower priority task is preempted by a medium priority task. PIP allows the lower priority task to inherit the priority of the higher priority task until it releases the resource.
  - Priority ceiling protocol (PCP): a technique to prevent priority inversion and deadlock, which is a situation where two or more tasks are waiting for each other to release a shared resource. PCP assigns a ceiling priority to each resource, which is the highest priority of any task that can access the resource, and prevents a task from accessing a resource if its priority is lower than the ceiling priority of any resource



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution time to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that the system meets its timing requirements and performs its functionality correctly. There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the environment. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, and period, are known at design time. The scheduler uses a precomputed table that specifies which task to execute at each time instant. The table is generated offline using an algorithm that guarantees the feasibility of the schedule. The advantage of this approach is that it has low runtime overhead and predictable behavior. The disadvantage is that it is inflexible and cannot handle dynamic changes or uncertainties in the system or the environment  .

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft or firm real time systems, where some of the properties of the tasks, such as arrival time, execution time, or deadline, are not known at design time or may vary at runtime. The scheduler assigns a priority to each task based on some criteria, such as deadline, period, or criticality, and selects the highest priority task to execute at each time instant. The priority of the tasks may be fixed or may change dynamically depending on the state of the system or the environment. The advantage of this approach is that it is flexible and can handle dynamic changes or uncertainties in the system or the environment. The disadvantage is that it has higher runtime overhead and less predictable behavior  .

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority and are scheduled in a circular order. Each task is allocated a fixed amount of time, called a time slice or a quantum, to execute. If a task finishes before its time slice expires, it relinquishes the processor to the next task in the queue. If a task does not finish within its time slice, it is preempted and moved to the end of the queue. The advantage of this approach is that it is simple and fair. The disadvantage is that it does not consider the timing constraints or the importance of the tasks .

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different weights that reflect their relative importance or urgency. The scheduler allocates a time slice to each task proportional to its weight. For example, if task A has a weight of 2 and task B has a weight of 1, then task A will get twice as much time as task B. The advantage of this approach is that it can differentiate between the tasks and give more time to the more important or urgent ones. The disadvantage is that it still does not consider the timing constraints or the deadlines of the tasks .



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a static schedule offline, before the system starts to execute, and follows the schedule at runtime.
- A static schedule is a sequence of scheduling decisions that specifies which job executes on which processor at any given time.
- A periodic static schedule is a cyclic schedule that repeats itself after a fixed period of time.
- This approach to scheduling hard real-time jobs is called the clock-driven or time-driven approach because each scheduling decision is made at a specific time, independent of events, such as job releases and completions, in the system.
- It is easy to see why a clock-driven system never exhibits the anomalous timing behavior of priority-driven systems.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling has some drawbacks, such as:
  - It may not be able to handle aperiodic or sporadic jobs well.
  - It may not be able to adapt to dynamic changes in the system state or workload.
  - It may waste processor time if the schedule is not fully utilized.
  - It may require a large amount of memory to store the schedule.



### Weighted Round Robin Approach

- The weighted round robin (WRR) algorithm is a variation of the basic round robin (RR) algorithm that assigns different weights to different jobs.
- The WRR algorithm has been used for scheduling real-time traffic in high-speed switched networks .
- The WRR algorithm works as follows:
  - Each job has a weight that represents its relative importance or priority.
  - The weight of a job determines the number of time slots that the job can execute in each round.
  - The jobs are scheduled in a circular order, and each job is allocated a number of time slots equal to its weight.
  - If a job finishes or blocks before using all its time slots, the remaining time slots are assigned to the next job in the queue.
  - If a job arrives while another job is executing, it is added to the end of the queue and waits for its turn.
- The WRR algorithm has the following advantages:
  - It is simple and easy to implement.
  - It can handle variable-length jobs and dynamic arrivals of jobs.
  - It can provide different levels of service to different jobs based on their weights.
- The WRR algorithm has the following disadvantages:
  - It may cause starvation of low-weight jobs if the high-weight jobs are long or frequent.
  - It may not meet the deadlines of real-time jobs if the weights are not properly assigned or adjusted.
  - It may not utilize the processor fully if some jobs finish or block early.



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally. A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level. Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
  - Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
  - Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state and events.
- Priority-driven scheduling can also be classified into two categories: preemptive and non-preemptive.
  - Preemptive priority-driven scheduling allows a higher-priority task to interrupt a lower-priority task that is currently executing and resume it later.
  - Non-preemptive priority-driven scheduling does not allow a higher-priority task to interrupt a lower-priority task that is currently executing and waits until it finishes.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications, by leveraging the priority inheritance and priority ceiling protocols to avoid priority inversion and deadlock problems.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters are known in advance and do not change during execution. A **dynamic system** is one where the tasks and their parameters may vary unpredictably during execution.
- Static systems are easier to analyze and validate than dynamic systems, since the worst-case scenarios can be determined offline. Dynamic systems require online analysis and adaptation to handle the changing workload and resource availability.
- Static systems can provide better performance guarantees than dynamic systems, since the tasks can be scheduled optimally based on their deadlines, priorities, and resource requirements. Dynamic systems may suffer from scheduling overhead, uncertainty, and suboptimal decisions due to incomplete or outdated information.
- Static systems are suitable for hard real-time systems, where missing a deadline can have catastrophic consequences. Dynamic systems are suitable for soft real-time systems, where missing a deadline can have acceptable or negligible consequences.
- Static systems use **static scheduling algorithms**, which assign fixed priorities or execution orders to the tasks before the system runs. Dynamic systems use **dynamic scheduling algorithms**, which determine the priorities or execution orders of the tasks as the system runs, based on the current state of the system and the environment.
- Static scheduling algorithms include **rate-monotonic scheduling (RMS)**, **deadline-monotonic scheduling (DMS)**, **earliest deadline first (EDF)**, and **least laxity first (LLF)**. Dynamic scheduling algorithms include **earliest deadline first (EDF)**, **least laxity first (LLF)**, **maximum urgency first (MUF)**, and **least slack time (LST)**.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems, which assign different priorities to each job of a task based on their deadlines or slack times.
- A deadline is the time by which a job must finish its execution, and a slack time is the difference between the deadline and the remaining execution time of a job.
- EDF schedules the job with the earliest deadline first, and LST schedules the job with the least slack time first.
- EDF and LST are optimal for uniprocessor systems, meaning that they can always meet the deadlines of all the tasks if there exists a feasible schedule.
- However, EDF and LST are not optimal for multiprocessor systems, meaning that they may miss some deadlines even if there exists a feasible schedule.
- EDF and LST have different advantages and disadvantages in terms of performance, complexity, and overhead.
- EDF has a lower context switch overhead than LST, because it only changes the priority of a job when a new job arrives or a job finishes.
- LST has a higher context switch overhead than EDF, because it changes the priority of a job whenever its slack time changes, which can happen frequently due to preemption or variation in execution time.
- EDF has a higher utilization than LST, because it can schedule more tasks with higher utilization without missing deadlines.
- LST has a lower utilization than EDF, because it may under-utilize the processor by leaving some idle time between jobs.
- EDF has a higher response time than LST, because it may delay the execution of some jobs with longer deadlines, which can affect the performance of interactive or soft real-time tasks.
- LST has a lower response time than EDF, because it tends to execute the jobs with shorter deadlines earlier, which can improve the performance of interactive or soft real-time tasks.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a static priority scheduling algorithm for periodic tasks in real-time systems.
- RMA assigns priorities to tasks based on their periods, with shorter periods having higher priorities.
- RMA is optimal for preemptive scheduling of periodic tasks with fixed deadlines, meaning that it can always meet the deadlines of all tasks if there exists a feasible schedule.
- RMA has some advantages over other scheduling algorithms, such as simplicity, predictability, and low overhead.
- RMA also has some limitations, such as not being suitable for tasks with variable periods, deadlines, or execution times, or for tasks with shared resources or dependencies.
- RMA can be analyzed for schedulability using the utilization bound test or the response time analysis. The utilization bound test is a sufficient but not necessary condition for schedulability, meaning that it may reject some schedulable task sets. The response time analysis is a necessary and sufficient condition for schedulability, meaning that it can accurately determine the schedulability of any task set.



### Offline Versus Online Scheduling

- Offline scheduling is a technique where the scheduling decisions are made before the system starts to execute. It requires the prior knowledge of the task parameters, such as arrival times, execution times, deadlines, resource requirements, etc. It generates a static schedule that is followed by the system at run-time. It is suitable for periodic and predictable tasks that have fixed deadlines and resource demands. It is also called table-driven scheduling .
- Online scheduling is a technique where the scheduling decisions are made during the system execution. It does not require the complete knowledge of the task parameters, but it can adapt to the dynamic changes in the system, such as task arrivals, preemptions, resource availability, etc. It generates a dynamic schedule that is updated by the system at run-time. It is suitable for aperiodic and unpredictable tasks that have variable deadlines and resource demands. It is also called event-driven scheduling .
- The advantages of offline scheduling are that it can guarantee the schedulability of the tasks, it can optimize the system performance, and it can reduce the scheduling overhead. The disadvantages of offline scheduling are that it cannot handle the uncertainties and variations in the system, it cannot respond to the user requests and feedback, and it cannot cope with the faults and failures in the system.
- The advantages of online scheduling are that it can handle the uncertainties and variations in the system, it can respond to the user requests and feedback, and it can cope with the faults and failures in the system. The disadvantages of online scheduling are that it cannot guarantee the schedulability of the tasks, it cannot optimize the system performance, and it can increase the scheduling overhead.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They are usually non-critical and can tolerate some delay in their execution. Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They are usually critical and have hard deadlines.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, or utilization. The scheduler always selects the highest priority job that is ready to execute. Clock driven systems are systems that assign fixed time slots to jobs based on their arrival pattern and execution time. The scheduler follows a pre-computed schedule that is determined offline.
- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs. The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to accommodate the variability and unpredictability of aperiodic and sporadic job arrivals.
- Some of the algorithms for scheduling aperiodic and sporadic jobs in priority driven systems are:
  - Background scheduling: Aperiodic jobs are executed only when there are no periodic or sporadic jobs ready. This ensures that periodic and sporadic jobs meet their deadlines, but may result in poor response time for aperiodic jobs.
  - Polling server: A periodic task with a fixed period and execution time is allocated to serve aperiodic jobs. The server has a lower priority than any periodic or sporadic job, and can be preempted at any time. The server polls for aperiodic jobs at the beginning of each period, and executes them if available. This improves the response time of aperiodic jobs, but may introduce some overhead and waste some server capacity.
  - Deferrable server: A periodic task with a fixed period and execution time is allocated to serve aperiodic jobs. The server has a higher priority than any periodic or sporadic job, and can preempt them if necessary. The server defers its execution until an aperiodic job arrives, and executes it as soon as possible. This further improves the response time of aperiodic jobs, but may cause some deadline misses for periodic or sporadic jobs.
  - Sporadic server: A periodic task with a variable period and execution time is allocated to serve aperiodic jobs. The server has a higher priority than any periodic or sporadic job, and can preempt them if necessary. The server adjusts its period and execution time based on the arrival and execution time of aperiodic jobs, and executes them as soon as possible. This provides the best response time for aperiodic jobs, but may require some online computation and monitoring of server parameters.
  - Slack stealing: Aperiodic jobs are executed by stealing the available slack time of periodic and sporadic jobs. The slack time of a job is the difference between its deadline and its remaining execution time. The scheduler maintains a priority queue of slack times for all periodic and sporadic jobs, and selects the job with the largest slack time to execute an aperiodic job. This maximizes the utilization of the system, but may require some online computation and monitoring of slack times.
  - Total bandwidth server: A periodic task with a fixed period and execution time is allocated to serve both aperiodic and sporadic jobs. The server has a higher priority than any periodic job, and can preempt them if necessary. The server splits its execution time into two portions: one for aperiodic jobs and one for sporadic jobs. The server executes aperiodic jobs in the first portion, and sporadic jobs in the second portion. The server adjusts the size of the portions based on the arrival and execution time of aperiodic and sporadic jobs. This provides a unified framework for scheduling both types of jobs, but may require some online computation and monitoring of server parameters.
- Some of the algorithms for scheduling aperiodic and sporadic jobs in clock driven systems are:
  - Offline scheduling: Aperiodic and sporadic jobs are assumed to have known arrival times and execution times, and are incorporated into the offline schedule along with periodic jobs. The scheduler follows the pre-computed schedule that assigns fixed time slots to all jobs. This ensures that all jobs meet their deadlines, but may not be feasible or realistic for aperiodic and sporadic jobs.
  - Online scheduling: Aperiodic and sporadic jobs are assumed to have unknown arrival times and execution times, and are accommodated into the



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, or network bandwidth, available to multiple users or processes.
- Resource sharing can improve the efficiency, performance, reliability, and scalability of a computer system, as well as reduce the cost and complexity of managing it.
- Resource sharing can be achieved by various methods, such as:
  - Multiprogramming: running multiple programs or processes on a single processor, by switching between them in a time-sharing manner.
  - Multiprocessing: using multiple processors or cores to execute multiple programs or processes simultaneously or in parallel.
  - Distributed computing: using multiple computers or devices connected by a network to perform a common task or service, by dividing the workload among them.
  - Cloud computing: using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer.
- Resource sharing can also involve different levels of abstraction, such as:
  - Physical: sharing the actual hardware components of a computer system, such as CPU, memory, disk, or network interface.
  - Logical: sharing the virtual or logical representation of a physical resource, such as a file, a process, a socket, or a database.
  - Application: sharing the functionality or service provided by an application or a software component, such as a web browser, a word processor, or a game engine.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel .
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock  .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for a resource is granted, and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention, and to ensure the correctness and timeliness of tasks  .
- RAC can be classified into two categories: non-preemptive and preemptive .
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource .
  - Preemptive RAC means that a task can be preempted by another task while holding a resource, but the resource is not released until the preempted task resumes and finishes its critical section .
- Some examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive RAC: Multiprocessor Priority Ceiling Protocol (MPCP), Multiprocessor Stack Resource Policy (MSRP), Multiprocessor Priority Inheritance Protocol (MPIP), etc .
- The choice of RAC protocol depends on the characteristics of the system, such as the number of processors, the type of resources, the priority assignment, the task model, etc .
- The performance of RAC protocols can be evaluated by metrics such as blocking time, response time, schedulability, utilization, etc .



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, so that it can finish its critical section as soon as possible  .
- The advantage of non-preemptive critical sections is that they prevent deadlock, which is a situation where two or more jobs are waiting for each other to release resources, and none of them can proceed  .
- The disadvantage of non-preemptive critical sections is that they can cause priority inversion, which is a situation where a high-priority job is blocked by a low-priority job that holds a resource, and the low-priority job cannot be preempted by a medium-priority job that does not need the resource  .
- Non-preemptive critical sections can also cause long blocking times, which is the amount of time that a job has to wait for a resource to become available, and this can affect the schedulability and performance of real-time systems  .
- Non-preemptive critical sections are suitable for systems that have low resource contention, short critical sections, and low blocking times  .



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) is a technique for sharing critical resources among different tasks without the occurrence of unbounded priority inversions.
- Priority inversion is a situation where a low-priority task holds a resource that is needed by a high-priority task, and the low-priority task is preempted by a medium-priority task, thus delaying the high-priority task indefinitely.
- The basic idea of PIP is that when a task blocks one or more higher-priority tasks, it ignores its original priority assignment and executes its critical section at an elevated priority level. After executing its critical section and releasing its locks, the task returns to its original priority level.
- PIP has the following rules:
  - Scheduling Rule: Ready tasks are scheduled on the processor preemptively in a priority-driven manner according to their current priority.
  - Priority Assignment Rule: At its release time, the current priority of every task is equal to its assigned priority. The task remains at this priority except under the condition stated in rule 3.
  - Priority Inheritance Rule: If a task J is blocked on a resource R that is currently locked by a task I, then the current priority of task I is set to the maximum of its current priority and the assigned priority of task J. This rule is applied transitively to handle nested resource requests and multiple inheritance situations.
  - Priority Restoration Rule: When a task releases a resource, its current priority is set to the maximum of its assigned priority and the current priority of all tasks that are blocked on any resource that it still holds.
- Priority-Ceiling Protocol (PCP) is another technique for sharing critical resources among different tasks without the occurrence of unbounded priority inversions.
- PCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling.
- PCP has two variants: Immediate Ceiling Priority Protocol (ICPP) and Original Ceiling Priority Protocol (OCPP).
- In ICPP, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource. A task can lock a resource only if its current priority is higher than the priority ceiling of all resources currently locked by other tasks. When a task locks a resource, its current priority is raised to the priority ceiling of that resource. When a task releases a resource, its current priority is restored to the maximum of its assigned priority and the priority ceiling of all resources that it still holds.
- In OCPP, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource. A task can lock a resource only if its current priority is higher than the priority ceiling of all resources currently locked by other tasks. When a task locks a resource, its current priority is not changed. When a task releases a resource, its current priority is restored to the maximum of its assigned priority and the priority ceiling of all resources that it still holds.
- The advantages of PCP over PIP are:
  - PCP prevents deadlock by ensuring that a task can lock a resource only if it does not block any higher-priority task.
  - PCP reduces the number of context switches by avoiding unnecessary priority changes.
  - PCP allows the schedulability analysis of tasks to be simpler and more efficient.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources without causing priority inversion or deadlock .
- In SBPCP, each resource is assigned a priority ceiling, which is equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use at that time.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its priority is higher than the current ceiling of the system.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock by ensuring that a task holding a resource cannot be blocked by a lower priority task.
  - It reduces the blocking time of a task by allowing it to lock multiple resources without being preempted by intermediate priority tasks.
  - It simplifies the analysis of the worst-case response time of a task by bounding the blocking time by the maximum priority ceiling of all the resources that the task may lock.
  - It allows tasks to share a run-time stack by allocating a stack segment to each resource and switching the stack pointer when a task locks or unlocks a resource. This reduces the memory requirement and the overhead of stack management.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The ceiling of the system is the highest priority ceiling of all the resources currently locked.
- A task can lock a resource only if its priority is higher than the ceiling of the system. Otherwise, it has to wait until the resource is released.
- This ensures that a task can be blocked by at most one lower priority task, and that task can be blocked by at most one lower priority task, and so on.
- This reduces the blocking time and improves the schedulability of the system.
- An example of a dynamic priority system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in deadline driven system is shown below :

| Time | Task | Resource | Priority | Priority Ceiling |
|------|------|----------|----------|------------------|
| 0    | T1   | X        | 1        | 1                |
| 1    | T1   | X        | 1        | 1                |
| 2    | T1   | X        | 1        | 1                |
| 3    | T1   | X        | 1        | 1                |
| 4    | T2   | Y        | 2        | 2                |
| 5    | T2   | Y        | 2        | 2                |
| 6    | T2   | Y        | 2        | 2                |
| 7    | T2   | Y        | 2        | 2                |
| 8    | T2   | Y        | 2        | 2                |
| 9    | T1   | X        | 2        | 2                |
| 10   | T1   | X        | 2        | 2                |
| 11   | T1   | X        | 2        | 2                |
| 12   | T1   | X        | 2        | 2                |
| 13   | T1   | X        | 2        | 2                |
| 14   | T2   | Y        | 1        | 1                |
| 15   | T2   | Y        | 1        | 1                |
| 16   | T2   | Y        | 1        | 1                |
| 17   | T2   | Y        | 1        | 1                |
| 18   | T2   | Y        | 1        | 1                |

- As we can see, the priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on. The priority ceiling of Y is 2 from time 4 to 9 and becomes 1 from time 9 to 14 and so on. The ceiling of the system is the maximum of the priority ceilings of X and Y at any time.
- Both tasks can meet their deadlines using the priority ceiling protocol.



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by other tasks in a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that mutual deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has less blocking time than static preemption ceiling protocol, but it requires more storage and computation overhead.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- Preemption threshold scheduling can reduce the number of context switches and increase the schedulability of real-time systems, but it may also cause long priority inversion.
- Preemption ceiling protocol can avoid long priority inversion by ensuring that a task can lock a resource only if its priority is higher than the preemption threshold of any task that can access that resource.
- Preemption ceiling protocol can also be applied to object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Preemption ceiling protocol can ensure that a task can invoke a method of an object only if its priority is higher than the ceiling priority of the object, which is the highest priority of any task that can invoke any method of the object.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to avoid deadlock and priority inversion, while ensuring schedulability and resource utilization.
- Some of the protocols for access control in multiple-unit resources are:
  - Highest Locker Protocol (HLP): The priority of a job is equal to the highest priority of any job that currently holds a lock on any unit of the same resource  .
  - Maximum Urgency First (MUF): The priority of a job is equal to the maximum of its own priority and the urgency of the resource it requests, where the urgency is the highest priority of any job that may request the same resource in the future  .
  - Priority Inheritance Protocol (PIP): The priority of a job is equal to the maximum of its own priority and the priority of any job that is blocked by it on any resource  .
  - Priority Ceiling Protocol (PCP): The priority of a job is equal to the maximum of its own priority and the ceiling of the resource it requests, where the ceiling is the highest priority of any job that may request the same resource in the future  .
- The advantages and disadvantages of these protocols depend on the characteristics of the system, such as the number of resources, the number of units per resource, the length of the critical sections, the degree of resource contention, and the priority assignment scheme.



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts by locking data objects before accessing them and releasing them after finishing the access. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and resolve them by aborting and restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the number and size of data objects, the frequency and duration of accesses, the degree of data sharing, the criticality and deadline of transactions, and the system workload and performance.



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on whether the parties are communicating at the same time or not.
- RTC can be text-based, voice-based, video-based, or a combination of these modalities.
- RTC can be one-to-one, one-to-many, or many-to-many, depending on the number of participants and the direction of communication.
- RTC can be mediated by different technologies, such as telephones, radios, computers, mobile devices, or the Internet.
- RTC can be used for various purposes, such as personal, social, educational, professional, or entertainment.
- RTC can have various benefits, such as enhancing collaboration, reducing isolation, increasing engagement, improving learning outcomes, or providing entertainment.
- RTC can also have various challenges, such as technical issues, privacy concerns, security risks, ethical dilemmas, or social norms.
- RTC can be influenced by various factors, such as the context, the purpose, the audience, the medium, the mode, the content, the tone, the style, or the etiquette of communication.
- RTC can be evaluated by various criteria, such as the effectiveness, the efficiency, the quality, the satisfaction, the feedback, or the impact of communication.



### Basic Concepts in Real Time Communication

- Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays .
- In RTC, there is always a direct path between the source and the destination, and the data is not stored en route to the destination .
- RTC can be synchronous or asynchronous, depending on whether the communication is time-bound or not.
- Examples of synchronous RTC are voice calls, video calls, live streaming, online gaming, etc. Examples of asynchronous RTC are email, text messaging, social media, etc.
- RTC can be based on different protocols, such as Session Initiation Protocol (SIP), Web Real-Time Communication (WebRTC), Real-Time Transport Protocol (RTP), etc .
- RTC can be used for various purposes, such as collaboration, education, entertainment, health care, emergency response, etc .
- RTC requires effective communication skills, such as listening, paying attention to nonverbal signals, managing stress, and asserting oneself.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT) .
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- Hard real-time systems are deterministic in nature, meaning that they guarantee to meet the deadlines for all tasks .
- Soft real-time systems are probabilistic in nature, meaning that they may occasionally miss the deadlines for some tasks, but with a very low probability .
- Hard real-time systems are used for applications that require strict timing constraints and cannot tolerate any delay or error, such as nuclear reactor control, air traffic control, or missile guidance  .
- Soft real-time systems are used for applications that can tolerate some delay or error, but still need to provide timely and accurate results, such as multimedia streaming, video conferencing, or online gaming  .
- Hard real-time systems require specialized hardware and software components that can support the timing requirements and handle the worst-case scenarios .
- Soft real-time systems can use general-purpose hardware and software components that can adapt to the varying workload and network conditions .
- Hard real-time systems are more complex and costly to design, implement, and maintain than soft real-time systems .
- Soft real-time systems are more flexible and scalable than hard real-time systems .



### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without storing data en route to the destination  .
- Examples of real time communication include voice calls, video calls, chat messages, online games, etc.
- Real time communication requires a network that can support the quality of service (QoS) parameters such as throughput, delay and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in delay among different messages.
- Real time communication can be classified into two types: hard real time and soft real time .
- Hard real time communication has strict deadlines and guarantees that the messages will be delivered within the specified time limit.
- Soft real time communication has relaxed deadlines and allows some degree of delay or loss of messages.
- A model of real time communication consists of the following components :
  - Sources and destinations: the end users of the communication system that generate and consume messages.
  - Hosts: the devices that host the sources and destinations and provide network interfaces.
  - Network: the medium that connects the hosts and enables data transmission.
  - Input and output queues: the buffers that store the incoming and outgoing messages at each host.
  - Input and output buffers: the memory areas that allocate space for the input and output queues.
  - Traffic model: the characterization of the messages in terms of inter-packet spacing, message length and reception deadline.
  - Scheduling algorithm: the method that determines the order of sending and receiving messages at each host.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) is a simple and fair priority-based service discipline that assigns a weight to each queue and serves them in a circular order, giving each queue a number of service slots proportional to its weight.
- WRR does not require a sorted priority queue, only a round-robin queue. It can guarantee the minimum bandwidth for each queue, but it cannot guarantee the delay jitter bound or satisfy diverse delay requirements.
- Weighted fair queuing (WFQ) is a more sophisticated priority-based service discipline that assigns a weight and a virtual finish time to each packet and serves them in the order of their virtual finish times. It can approximate the ideal generalized processor sharing (GPS) discipline, which allocates the server bandwidth to each queue according to its weight.
- WFQ can guarantee the delay bound, the delay jitter bound and the minimum bandwidth for each queue, but it requires a sorted priority queue and more computation than WRR.
- There are also other variants of priority-based service disciplines, such as strict priority (SP), probabilistic priority (PP), class-based weighted fair queuing (CBWFQ) and weighted fair priority queuing (WFPQ), that have different trade-offs between performance, fairness and complexity .



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission can reach all the nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but they suffer from collisions and low efficiency.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as token passing or polling. These protocols are reliable and fair, but they have high overhead and delay.
- Reservation-based protocols use a separate control channel or a dedicated time slot to reserve the access to the data channel, such as TDMA or CDMA. These protocols can provide guaranteed performance and quality of service, but they require synchronization and coordination among the nodes.
- Some MAC protocols combine different access strategies to achieve a trade-off between performance and complexity, such as ABROAD, which incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay.



### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP supports both soft state and hard state reservation models. Soft state reservation is dynamic and requires periodic refresh messages to maintain the reservation. Hard state reservation is static and requires explicit teardown messages to release the reservation.
- RSVP messages are classified into two types: PATH and RESV. PATH messages are sent by the sender to inform the receiver and the intermediate routers about the characteristics and requirements of the data flow. RESV messages are sent by the receiver to request and confirm the resource reservation along the path.
- RSVP uses filterspecs and flowspecs to specify the data flow and the QoS parameters. Filterspecs identify the sender and the receiver of the data flow. Flowspecs define the QoS requirements such as bandwidth, delay, and reliability.
- RSVP can interoperate with different QoS models such as Integrated Services (IntServ) and Differentiated Services (DiffServ). IntServ provides end-to-end QoS guarantees by reserving resources for each data flow. DiffServ provides QoS differentiation by classifying and marking data packets into different service classes.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations  .
- A real-time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, and online transactions .
- The main characteristics of real-time operating systems and databases are:
  - **Predictability**: The system must be able to guarantee that the tasks and queries will be completed within a specified deadline, regardless of the workload or the system state.
  - **Responsiveness**: The system must be able to react quickly to changes in the environment and the input data, and provide timely feedback to the users or other systems.
  - **Reliability**: The system must be able to handle failures and errors gracefully, and ensure the consistency and integrity of the data and the system state.
  - **Scalability**: The system must be able to handle increasing amounts of data and events, and provide high performance and availability.
- Some of the challenges and trade-offs of real-time operating systems and databases are:
  - **Scheduling**: The system must be able to allocate the CPU and other resources to the tasks and queries according to their priorities and deadlines, and avoid conflicts and starvation.
  - **Concurrency control**: The system must be able to coordinate the access and update of the shared data by multiple tasks and queries, and prevent data inconsistency and deadlock.
  - **Memory management**: The system must be able to allocate and deallocate the memory for the tasks and queries efficiently, and avoid fragmentation and memory leaks.
  - **Data freshness**: The system must be able to maintain the accuracy and timeliness of the data, and cope with the dynamic and uncertain nature of the data sources and the data quality.
  - **Data replication**: The system must be able to distribute and synchronize the data across multiple nodes or locations, and balance the trade-off between data availability and data consistency.



### Features of RTOS

- An RTOS is an operating system that has two key features: **predictability** and **determinism**. This means that it can guarantee that tasks will be completed within a specified time limit, and that the system will always respond in the same way to the same inputs.
- An RTOS is **small**, **fast**, **responsive**, and **efficient**. It occupies very less memory and consumes fewer resources than a general-purpose operating system. It can execute tasks quickly and handle interrupts with minimal latency.
- An RTOS supports **real-time scheduling** algorithms that assign priorities to tasks and ensure that the highest-priority task is always running. There are two types of real-time scheduling algorithms: **co-operative** and **pre-emptive**.
  - Co-operative scheduling: The task will run until the execution is completed. The kernel can only be set up in one way, and the task cannot be interrupted by another task.
  - Pre-emptive scheduling: Each task has a unique priority value. The higher the priority, the faster the task will be executed. The task can be interrupted by another task with a higher priority, and resume when the interrupting task is finished.
- An RTOS provides **inter-task communication** and **synchronization** mechanisms, such as **semaphores**, **mutexes**, **message queues**, **event flags**, and **mailboxes**. These mechanisms allow tasks to share data, coordinate actions, and avoid conflicts.
- An RTOS supports **memory management** techniques, such as **static memory allocation**, **dynamic memory allocation**, **memory pools**, and **memory protection**. These techniques allow tasks to access memory efficiently, securely, and reliably.
- An RTOS supports **device drivers** and **input/output** operations, such as **serial ports**, **network interfaces**, **timers**, and **analog-to-digital converters**. These operations allow tasks to interact with external devices and sensors.
- An RTOS supports **application programming interfaces** (APIs) that allow developers to create and modify tasks, configure system parameters, and use system services. These APIs are usually written in **C** or **C++** languages, and may be **standardized** or **proprietary**.



### Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.
- A real-time system can be classified into hard real-time and soft real-time based on the timing constraints .
  - A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
  - A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- Time services are the mechanisms that provide the real-time system with the ability to measure, synchronize, and control the passage of time.
- Time services can be divided into two categories: clock services and timer services.
  - Clock services are the functions that provide the real-time system with the access to a reliable and accurate source of time, such as a hardware clock or a network time protocol (NTP) server.
  - Timer services are the functions that allow the real-time system to schedule events or actions to occur at specific points in time, such as periodic tasks, timeouts, or alarms.
- Time services are essential for real-time systems because they enable the system to:
  - Monitor the execution time of tasks and ensure that they meet their deadlines.
  - Coordinate the activities of distributed components and ensure that they are synchronized.
  - Manage the resources and priorities of tasks and ensure that they are allocated fairly and efficiently.
  - Implement fault-tolerance and recovery mechanisms and ensure that the system can handle errors and failures.
- Time services are implemented by using real-time software components, such as synchronous programming languages, real-time operating systems (RTOSes), and real-time networks.
  - Synchronous programming languages are languages that explicitly express the temporal behavior and constraints of the system, such as Esterel, Lustre, or Signal.
  - Real-time operating systems (RTOSes) are operating systems that provide the system with the features and services needed to support real-time applications, such as preemptive scheduling, priority inheritance, inter-process communication, and memory management.
  - Real-time networks are networks that guarantee the timely and reliable delivery of messages between the system components, such as Ethernet, CAN, or TTP.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS is different from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing, which is the key feature of a RTOS.
- However, some variants of UNIX, such as Linux, have been modified to provide real-time capabilities by using patches, kernels, or extensions .
- Some examples of real-time applications that use Linux as a RTOS are NASA and Air Force Research Lab simulations, SpaceX launch vehicles and capsules, and industrial automation systems .
- Some advantages of using Linux as a RTOS are its open source nature, its large user base, its compatibility with various hardware platforms, and its rich set of features and libraries .
- Some challenges of using Linux as a RTOS are its complex and dynamic kernel, its lack of hard real-time guarantees, its dependency on external components, and its potential security and reliability issues .
- Some alternatives to Linux as a RTOS are QNX, VxWorks, FreeRTOS, RTAI, and Xenomai. These RTOSs have different features, architectures, and performance characteristics that may suit different real-time applications.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX-like systems, but it does not address the specific needs of real-time applications, such as predictable timing, priority scheduling, and inter-process communication.
- To address these needs, a real-time working group was established in POSIX, and it developed several extensions to the original standard, such as POSIX.1b (real-time extensions), POSIX.1c (threads), and POSIX.4 (timers and clocks).
- Some of the issues that POSIX real-time extensions address are:
  - Scheduling: POSIX.1b defines two scheduling policies for real-time applications: FIFO (first-in, first-out) and RR (round-robin). These policies allow the application to assign priorities to threads or processes, and ensure that the highest-priority runnable thread or process is always executed. POSIX.1b also defines a minimum number of priority levels that the system must support, and allows the application to query the system for its capabilities.
  - Synchronization: POSIX.1b defines several synchronization primitives for real-time applications, such as mutexes, condition variables, semaphores, and message queues. These primitives allow the application to coordinate the access to shared resources, and to communicate between threads or processes. POSIX.1b also defines the concept of priority inheritance, which prevents priority inversion, a situation where a low-priority thread or process blocks a high-priority one from accessing a shared resource.
  - Memory management: POSIX.1b defines a memory locking mechanism for real-time applications, which allows the application to lock some or all of its address space into physical memory, and prevent it from being swapped out by the system. This mechanism reduces the latency and jitter of the application, and ensures that it can meet its deadlines.
  - Signals: POSIX.1b defines a signal queueing mechanism for real-time applications, which allows the application to receive multiple instances of the same signal, and to process them in order of arrival. This mechanism prevents the loss of events, and allows the application to handle urgent events with higher priority. POSIX.1b also defines a set of real-time signals, which have higher priority than the standard signals, and can be delivered to specific threads or processes.



### Characteristics of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, timestamps, or events.
- Temporal data can be used to analyze patterns, trends, or changes over time in various domains, such as weather, traffic, demographics, etc.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be stored in different ways, such as using attributes, relations, or tables to capture the temporal aspects.
- Temporal data can be queried and manipulated using different techniques, such as temporal algebra, temporal logic, or temporal SQL.
- Temporal data can be visualized using different methods, such as graphs, charts, maps, or animations to show the temporal relationships.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date data, otherwise they may cause errors or failures in the system.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. Data staleness can be caused by delays in data acquisition, data transmission, or data processing.
  - Data inconsistency occurs when the data stored in the database is contradictory or conflicting with other data sources. Data inconsistency can be caused by concurrent updates, data replication, or data corruption.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the data sources when they detect a change in the physical environment. Triggered updates can reduce data staleness and improve data freshness.
  - Temporal validity, which is a property of data that specifies the time interval during which the data is valid and can be used by transactions. Temporal validity can help transactions to avoid reading outdated or inconsistent data.
  - Temporal constraints, which are constraints that specify the deadlines or the maximum allowable delays for data acquisition, data transmission, or data processing. Temporal constraints can help to ensure that data is delivered and processed in a timely manner.
  - Temporal locking, which is a concurrency control technique that prevents transactions from accessing or updating data that is being updated by another transaction. Temporal locking can help to avoid data inconsistency and ensure data isolation.



### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, where many events and actions occur simultaneously.
- Real-time systems (RTS) are systems that respond to their environment within specified time constraints .
- RTS are inherently concurrent and typically manage shared data resources, such as sensors, actuators, files, databases, etc .
- Concurrency control is the process of ensuring both logical and timing correctness of concurrent access to shared data resources in RTS.
- Logical correctness means that the concurrent access does not violate the integrity and consistency of the data.
- Timing correctness means that the concurrent access does not cause any deadline misses or timing anomalies in the system.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by using locks, timestamps, or serialization protocols to coordinate the access to shared data.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them by using validation, compensation, or restart mechanisms.
- Concurrency control techniques can also be classified into two levels: transaction level and object level.
- Transaction level concurrency control techniques deal with the synchronization of transactions, which are sequences of operations that access shared data and have atomicity, consistency, isolation, and durability (ACID) properties.
- Object level concurrency control techniques deal with the synchronization of objects, which are units of data that have identity, state, and behavior.
- Concurrency control techniques for RTS must consider the timing constraints and the priority of the transactions or objects, as well as the logical correctness and the performance of the system.
- Concurrency control techniques for RTS must also be adaptable to the dynamic and unpredictable nature of the real-time environment, such as varying workload, resource availability, and system state.
- Some examples of concurrency control techniques for RTS are: priority inheritance protocol, priority ceiling protocol, earliest deadline first protocol, timestamp ordering protocol, optimistic concurrency control with compensation, and adaptive concurrency control.



### Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for applications that require timely and consistent responses, such as accounting, banking, law, medical records, multimedia, process control, reservation systems, and scientific data analysis.
- Real-time databases have some special characteristics that distinguish them from traditional databases, such as:
  - Concurrency control: Real-time databases need to ensure that transactions do not interfere with each other and meet their deadlines, while maintaining data consistency and integrity.
  - Scheduling: Real-time databases need to assign priorities and deadlines to transactions and execute them in an optimal order, while avoiding conflicts and deadlocks.
  - Data freshness: Real-time databases need to ensure that the data they store and retrieve is up-to-date and reflects the current state of the system or environment.
  - Fault tolerance: Real-time databases need to cope with failures and errors, and provide mechanisms for recovery and backup.
- Some examples of commercial real-time databases are:
  - Raima Database Manager (RDM): A high-performance, embedded, in-memory database that supports SQL and NoSQL, and can run on various platforms and devices.
  - Firebase Realtime Database: A cloud-hosted database that stores data as JSON and synchronizes it in real-time to every connected client, and supports offline access and authentication.
  - Google Cloud Bigtable: A highly scalable, fully managed NoSQL database service that can handle large analytical and operational workloads, and offers high availability and low latency.
  - Dealpath: A cloud-based platform that provides data and workflow solutions for commercial real estate transactions, and integrates with various data sources and tools.

