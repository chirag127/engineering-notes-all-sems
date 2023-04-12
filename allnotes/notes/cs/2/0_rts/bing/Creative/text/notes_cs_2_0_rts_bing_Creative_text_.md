

# Real Time System

A real time system is an information processing system that can respond to events within predictable and specific time constraints . A real time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). A real time system can be classified into two types based on the timing constraints:

- **Hard real time system**: This type of system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur . Examples of hard real time systems are flight control systems, nuclear power plant control systems, and pacemakers.
- **Soft real time system**: This type of system can miss its deadline occasionally with some acceptably low probability. Missing the deadline may have degraded performance, but not a system failure. Examples of soft real time systems are video streaming, online gaming, and voice over IP.

Real time systems are used in a variety of industries and applications, such as process control systems, machine vision, robotics, medical imaging, video wall, and industrial controls applications . Real time systems require special hardware and software components that can handle the timing requirements and the concurrency issues of the system. Some of the challenges and techniques of designing and implementing real time systems are:

- **Scheduling**: The process of allocating the system resources (such as CPU, memory, and I/O devices) to the tasks that need to be executed in a real time system. Scheduling algorithms aim to optimize the system performance and meet the deadlines of the tasks. Some of the common scheduling algorithms for real time systems are rate-monotonic scheduling, earliest deadline first scheduling, and least laxity first scheduling.
- **Synchronization**: The process of coordinating the execution of multiple tasks that share the same resources or data in a real time system. Synchronization mechanisms aim to prevent data inconsistency and deadlock situations. Some of the common synchronization mechanisms for real time systems are priority inheritance protocol, priority ceiling protocol, and stack resource policy.
- **Communication**: The process of exchanging data and messages between the tasks or components of a real time system. Communication protocols aim to ensure the reliability and timeliness of the data transmission. Some of the common communication protocols for real time systems are time-triggered protocol, event-triggered protocol, and CAN bus protocol.
- **Fault tolerance**: The ability of a real time system to continue functioning correctly in the presence of faults or errors. Fault tolerance techniques aim to detect, isolate, and recover from the faults and maintain the system availability and safety. Some of the common fault tolerance techniques for real time systems are redundancy, checkpointing, and voting.



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
- Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failures or unacceptable losses. For example, a nuclear reactor control system, an air traffic control system, or a pacemaker.
- Soft real time systems are systems that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- Real time systems have some common characteristics, such as concurrency, unpredictability, resource constraints, dependability, and adaptability.
- Concurrency means that a real time system may have multiple tasks or processes running simultaneously, and they may need to communicate or synchronize with each other.
- Unpredictability means that a real time system may face uncertain or dynamic events or inputs, and it may need to handle them in a timely and correct manner.
- Resource constraints means that a real time system may have limited or scarce resources, such as memory, CPU, power, bandwidth, etc., and it may need to optimize their utilization or allocation.
- Dependability means that a real time system may have to ensure its correctness, reliability, availability, safety, and security, and it may need to cope with faults or errors.
- Adaptability means that a real time system may have to adjust its behavior or parameters according to the changing environment or requirements, and it may need to learn from its experience or feedback.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System.

### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic real time system is a system that has events or inputs that occur at regular intervals, and the deadlines are known in advance. For example, a sensor that samples data every 10 milliseconds, or a task that executes every second.
- An aperiodic real time system is a system that has events or inputs that occur at irregular intervals, and the deadlines are not known in advance. For example, a user request, a network packet, or an interrupt.
- A real time system can also be classified into two types based on the complexity of the system: simple and complex.
- A simple real time system is a system that has a single processor, a single task, and a single resource. For example, a thermostat, a calculator, or a stopwatch.
- A complex real time system is a system that has multiple processors, multiple tasks, and multiple resources. For example, a robotic arm, a smart phone, or a self-driving car.



### Typical Real Time Applications

A real-time application, or RTA, is an application that functions within a time frame that the user senses as immediate or current. The latency must be less than a defined value, usually measured in seconds. The use of real-time applications is part of real-time computing.

Some examples of real-time applications are:

- **Process Control Systems**: Process control systems are used in industrial applications where production is continuous and interruptions cannot happen. For example, chemical plants, power plants, oil refineries, etc. These systems monitor and control the physical processes and ensure safety, efficiency, and quality .
- **Machine Vision**: Machine vision is used to help machines rapidly interpret data so they can see their surroundings and make decisions quickly based on that visual input. For example, face recognition, autonomous vehicles, barcode scanners, etc. These systems require high-speed processing and low-latency communication .
- **Robotics**: Robotics is the field of engineering that deals with the design, construction, operation, and application of robots. Robots are machines that can perform tasks that are difficult, dangerous, or repetitive for humans. For example, industrial robots, surgical robots, humanoid robots, etc. These systems require real-time sensing, actuation, and coordination .
- **Manufacturing**: Manufacturing is the process of transforming raw materials into finished products. Manufacturing systems use real-time applications to optimize production, reduce waste, and improve quality. For example, computer-aided design (CAD), computer-aided manufacturing (CAM), computer numerical control (CNC), etc. These systems require real-time feedback, scheduling, and control .
- **Healthcare and Patient Monitoring**: Healthcare and patient monitoring systems use real-time applications to provide medical services and care to patients. For example, electrocardiogram (ECG), electroencephalogram (EEG), magnetic resonance imaging (MRI), etc. These systems require real-time data acquisition, analysis, and display .

Other examples of real-time applications are:

- **Multimedia Applications**: Multimedia applications are applications that involve the use of multiple media types, such as audio, video, text, graphics, etc. For example, video conferencing, online gaming, streaming services, etc. These applications require real-time synchronization, compression, and transmission.
- **Real-Time Databases**: Real-time databases are databases that store and process data that are time-sensitive and dynamic. For example, stock price quotation systems, track records databases, real-time file systems, etc. These databases require real-time consistency, concurrency, and recovery.
- **Peripheral Equipment**: Peripheral equipment are devices that are connected to a computer system to provide additional functionality or input/output capabilities. For example, keyboards, mice, printers, scanners, etc. These devices require real-time communication, buffering, and error handling.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System will be released on **Monday, March 20, 2023** at **10:00 AM GMT**.
- The notes will be available on the course website and the learning management system (LMS) for download and viewing.
- The notes will cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time system modeling and analysis techniques
  - Real time scheduling algorithms and policies
- The notes will also include self-assessment questions, exercises, and references for further reading.
- The notes are expected to take about **two hours** to read and understand.
- The notes are mandatory for the course and will be the basis for the quizzes, assignments, and exams.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are due on **Friday, March 24, 2023** by **11:59 PM**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in **Markdown** format and uploaded to the **Moodle** platform.
- The notes should be **clear, concise, and accurate**. They should include **diagrams, tables, and equations** where appropriate.
- The notes should follow the **style and citation guidelines** provided by the instructor.
- The notes will be graded based on the following criteria:
  - Completeness and coverage of the topics
  - Quality and clarity of the writing
  - Correctness and relevance of the information
  - Originality and creativity of the presentation
  - Adherence to the format and guidelines
- The notes are worth **10%** of the final grade for the subject of Real Time System.
- Late submissions will incur a penalty of **10%** per day, up to a maximum of **50%**. No submissions will be accepted after **Wednesday, March 29, 2023**.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Time constraints related with real-time systems simply mean that time interval allotted for the response of the ongoing program. This deadline means that the task should be completed within this time interval.
- Real-time systems are responsible for the completion of all tasks within their time intervals.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.
- Timing constraints associated with the real-time system are classified to identify the different types of timing constraints in a real-time system. Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Performance Constraints are further classified into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between occurrence of two consecutive events.
  - Duration Constraint: Duration constraint describes the maximum time interval for which an event can occur.
- Reliability Constraints are further classified into two types:
  - Periodicity Constraint: A periodicity constraint describes the regularity of occurrence of an event.
  - Synchronization Constraint: A synchronization constraint describes the coordination of occurrence of two or more events.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval logic, or event calculus.
- Timing constraints can be validated using automatic test systems that can measure the actual response time and behavior of the system under different scenarios.



### Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- A hard real time system is typically found interacting at a low level with physical hardware, in embedded systems .
- Examples of hard real time systems are nuclear power plant control, air traffic control, missile guidance, medical devices, automotive systems, etc.  .
- A hard real time system has the following characteristics  :
  - The size of data and code is small and fixed.
  - The response time is in milliseconds or microseconds.
  - The peak load performance should be predictable and consistent.
  - The safety is critical and the system must be reliable and fault-tolerant.
  - The system must handle concurrent events and prioritize tasks according to their deadlines.
  - The system must use real time operating systems (RTOS) that support scheduling, synchronization, communication, and resource management for real time tasks.



### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing catastrophic failure or unacceptable degradation of performance  .
- A soft real-time system has a deadline for each task, but missing the deadline occasionally does not have disastrous consequences. The usefulness of the results produced by a soft real-time system decreases gradually with an increase in tardiness.
- Examples of soft real-time systems include:
  - Software that maintains and updates the flight plans for commercial airliners. The flight plans must be kept reasonably current, but they can operate with the latency of a few seconds.
  - Live audio-video systems, such as video conferencing, streaming, or gaming. These systems require low latency and high quality, but can tolerate some occasional glitches or delays .
  - Telephone switches, which handle the routing and switching of voice calls. These systems must provide fast and reliable service, but can cope with some dropped or delayed calls.
- Characteristics of soft real-time systems include:
  - They can run on multiple cores and impose fewer restrictions on applications than hard real-time systems.
  - They can use dynamic memory allocation, virtual memory, and preemptive scheduling, which are not feasible for hard real-time systems .
  - They can handle non-deterministic events and inputs, such as user interactions, network traffic, or sensor data .
  - They can trade off between timeliness and quality of service, depending on the system requirements and the available resources .



### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .

- A workload model describes the applications supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, priority, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.)  .
- A resource model describes the resources available to the system, such as the CPU, memory, network, sensors, actuators, etc., their types (e.g., preemptive, non-preemptive, shared, exclusive, etc.), and their relations (e.g., hierarchy, contention, etc.) .
- A system model describes the policies and mechanisms used by the system to manage the workload and the resources, such as the scheduling algorithm, the synchronization protocol, the communication protocol, the fault tolerance strategy, etc. .

- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- The RCS architecture consists of a hierarchical structure of nodes, each of which performs a specific function, such as sensing, planning, controlling, or coordinating .
- The RCS architecture also defines the interfaces and protocols for communication and coordination among the nodes, as well as the methods for error detection and recovery .



### Processors and Resources for the notes of the Unit 1 - Introduction of Real Time System

- A real-time system is a system that must respond to events or inputs within a specified time interval, or risk failure or degradation of performance.
- A real-time system consists of hardware and software components that interact with the physical world and perform computations within the time constraints imposed by the system.
- Processors are also known as active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission links.
- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Example: printer, disk, memory.
- Processors and resources can be classified into two types: dedicated and shared. Dedicated processors or resources are allocated exclusively to a single job or task, while shared processors or resources can be used by multiple jobs or tasks, subject to some scheduling or arbitration policy.
- Processors and resources can also be classified into two types: preemptive and non-preemptive. Preemptive processors or resources can be interrupted and resumed by higher priority jobs or tasks, while non-preemptive processors or resources cannot be interrupted once they are allocated to a job or task.
- Processors and resources can affect the timing and performance of real-time systems. For example, a processor with a higher speed or a resource with a lower latency can improve the response time of a real-time system. However, processors and resources can also introduce delays or uncertainties, such as context switching, blocking, contention, or failure.
- Processors and resources can be managed by different techniques, such as allocation, scheduling, synchronization, or fault tolerance. These techniques aim to optimize the utilization and reliability of processors and resources, while meeting the timing and functional requirements of real-time systems.



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The earliest time at which the job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which the job must finish execution. It may be hard (must be met) or soft (can be missed with some penalty).
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for the job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The time interval in which the job can be feasibly executed by the system. It is equal to D<sub>i</sub> + jitter.
- The temporal parameters of a job may depend on the arrival pattern of the job, which can be periodic, sporadic, or aperiodic.
- The temporal parameters of a job may also depend on the precedence constraints among the jobs, which specify the order of execution of the jobs.
- The temporal parameters of a job are used to analyze the schedulability and performance of the real time system .



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks in the system.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a scheduling algorithm that can guarantee that all the jobs of the task meet their deadlines.
- A set of periodic tasks is said to be feasible if there exists a scheduling algorithm that can guarantee that all the jobs of all the tasks meet their deadlines.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline slack Si for each task τi, to allow the flexibility that the actual deadline of a job may be at most Si time units earlier or later than the exact end time of the period.
- The periodic task model can be further extended by adding a priority Pi for each task τi, to specify the relative importance of the task in the system. A higher priority task can preempt a lower priority task if they are ready to execute at the same time.



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the scheduling of jobs in real time systems.
- Precedence constraints are the restrictions on the order of execution of jobs that are imposed by the logic or functionality of the system. For example, a job that computes the average of some data must execute after the job that collects the data.
- Data dependency is the dependency of a job on the data produced or consumed by another job. For example, a job that displays the temperature on a screen must execute after the job that reads the temperature sensor.
- Precedence constraints and data dependency can be represented by a directed graph called the precedence graph, where the vertices are the jobs and the edges are the constraints or dependencies. A job can only start execution if all its predecessors have completed execution.
- Precedence constraints and data dependency can affect the feasibility and optimality of the scheduling algorithms for real time systems. Some algorithms may not be able to schedule a set of jobs with precedence constraints or data dependency, while others may require additional information or modifications to handle them. For example, the earliest deadline first (EDF) algorithm can schedule a set of independent periodic jobs optimally, but it may fail or require priority inheritance to schedule a set of periodic jobs with precedence constraints or data dependency.



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and reliable performance of the system, as well as to maximize the utilization of the available resources .
- Real time scheduling can be classified into two categories: **hard real time** and **soft real time** .
  - Hard real time scheduling requires that every task must meet its deadline, otherwise the system may fail or cause severe consequences .
  - Soft real time scheduling allows some tasks to miss their deadlines occasionally, without compromising the overall functionality of the system .
- Real time scheduling can also be classified into two types: **static** and **dynamic** .
  - Static real time scheduling assigns priorities and schedules to tasks before the system starts running, and does not change them during the execution .
  - Dynamic real time scheduling adjusts the priorities and schedules of tasks based on the current state of the system, such as the arrival of new tasks, the completion of existing tasks, or the occurrence of events .
- Some of the common real time scheduling algorithms are: **rate monotonic**, **earliest deadline first**, **least laxity first**, **round robin**, and **priority inheritance** .
  - Rate monotonic scheduling assigns fixed priorities to tasks based on their periods, such that the shorter the period, the higher the priority .
  - Earliest deadline first scheduling assigns dynamic priorities to tasks based on their deadlines, such that the earlier the deadline, the higher the priority .
  - Least laxity first scheduling assigns dynamic priorities to tasks based on their laxity, which is the difference between the deadline and the remaining execution time, such that the smaller the laxity, the higher the priority .
  - Round robin scheduling assigns equal priorities to tasks and executes them in a circular order, giving each task a fixed time slice .
  - Priority inheritance scheduling allows a task to inherit the priority of another task that is blocked by it, in order to avoid priority inversion .
- Real time scheduling can be implemented using various tools and platforms, such as **Linux**, **RTOS**, **Calendly**, and **Sinnaps**   .
  - Linux is a popular operating system that supports real time scheduling using various mechanisms, such as **real time policies**, **real time signals**, **real time timers**, and **real time locks**.
  - RTOS is a type of operating system that is designed for real time applications, and provides features such as **preemptive multitasking**, **fast context switching**, **low interrupt latency**, and **minimal overhead**.
  - Calendly is an online scheduling software that allows users to book appointments and meetings in real time, and integrates with various platforms, such as **Google Calendar**, **Outlook**, **Zoom**, and **Salesforce**.
  - Sinnaps is a cloud project management software that enables real time scheduling and collaboration for teams and organizations, and offers features such as **Gantt charts**, **critical path analysis**, **resource optimization**, and **risk management**.



### Common Approaches to Real Time Scheduling

- Real time scheduling is the process of allocating CPU time to tasks that have timing constraints, such as deadlines or periodicity.
- Real time scheduling aims to ensure that tasks meet their timing requirements, while maximizing system utilization and minimizing overhead.
- There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the environment.
- Some of the common approaches are:

  - **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival times, execution times, deadlines, and periods, are known at design time. In this approach, a static schedule is computed offline, based on the worst-case scenarios, and stored in a table. The table specifies the start and end times of each task for each cycle. A timer interrupts the system at predefined instants and triggers the execution of the next task in the table. This approach guarantees that all tasks will meet their deadlines, but it is inflexible and cannot handle dynamic changes or uncertainties in the system   .

  - **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft or firm real time systems, where some of the properties of the tasks, such as arrival times, execution times, or deadlines, are not known at design time, or may vary at run time. In this approach, each task is assigned a priority, which may be static or dynamic, and the scheduler selects the highest priority task that is ready to run at each instant. The priority of a task may depend on various factors, such as its deadline, its period, its criticality, or its resource requirements. This approach is more flexible and adaptable than the clock-driven approach, but it may not guarantee that all tasks will meet their deadlines, and it may incur more overhead due to context switches and priority computations   .

  - **Round-robin approach**: This approach is a special case of the priority-driven approach, where all tasks have the same priority, and the scheduler uses a circular queue to select the next task to run. Each task is allocated a fixed amount of CPU time, called a time slice or a quantum, and when the time slice expires, the task is preempted and moved to the end of the queue, and the next task in the queue is selected. This approach is simple and fair, but it may not be suitable for real time systems, as it does not consider the timing requirements of the tasks, and it may cause unnecessary preemptions and delays .

  - **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where each task is assigned a weight, which reflects its relative importance or resource demand, and the scheduler allocates CPU time to each task proportional to its weight. For example, a task with a weight of 2 will receive twice as much CPU time as a task with a weight of 1. This approach is more flexible and responsive than the round-robin approach, but it still does not consider the timing requirements of the tasks, and it may cause unnecessary preemptions and delays .



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when .
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known .
- A schedule of the jobs is computed off-line and is stored for use at run-time .
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling can handle periodic tasks and aperiodic tasks with known arrival times.
- Clock-driven scheduling can also handle sporadic tasks with known minimum inter-arrival times and deadlines.
- Clock-driven scheduling can be implemented using cyclic executives or table-driven schedulers.
- Clock-driven scheduling has some drawbacks, such as:
  - It may not be able to handle dynamic changes in the system or the environment.
  - It may not be able to handle tasks with unknown or variable execution times.
  - It may not be able to handle tasks with unknown or variable arrival times.
  - It may not be able to handle tasks with soft or imprecise deadlines.
  - It may not be able to utilize the processor efficiently.
  - It may require a lot of memory to store the schedule.
  - It may require a lot of computation time to generate the schedule.



### Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which gives equal shares of the processor to ready jobs in a circular order.
- Rather than giving all the ready jobs equal shares of the processor, weighted round robin assigns different weights to different jobs  .
- The weight of a job represents the fixed number of service opportunities or the fixed fraction of the processor time that the job receives in each cycle .
- The higher the weight of a job, the more service opportunities or processor time it gets.
- Weighted round robin can improve the performance and fairness of real-time scheduling by giving higher priority to more urgent or important jobs .
- However, weighted round robin may also introduce more overhead and complexity in the scheduling algorithm and the weight assignment .
- Weighted round robin may also delay the completion of every job, especially if there are precedence constraints among the jobs .
- Therefore, weighted round robin should be carefully designed and configured to balance the trade-offs between performance, fairness, overhead, and complexity .



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Examples of static priority-driven scheduling algorithms are rate-monotonic scheduling (RMS) and deadline-monotonic scheduling (DMS).
- Examples of dynamic priority-driven scheduling algorithms are earliest deadline first (EDF) and least laxity first (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to prioritize critical tasks and reduce the interference from non-critical tasks.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as the lack of priority inheritance, the heterogeneity of hardware platforms, and the complexity of the middleware layer.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters are known in advance and do not change during execution. A **dynamic system** is one where the tasks and their parameters may vary unpredictably during execution.
- Static systems can be **validated** before execution, meaning that it can be proven that the system will meet all the deadlines and constraints under all possible scenarios. Dynamic systems cannot be validated in general, as the workload and the environment may change at any time.
- Static systems use **static scheduling**, which assigns fixed priorities to tasks before execution. Dynamic systems use **dynamic scheduling**, which adjusts the priorities of tasks during execution based on their deadlines, resource requirements, or other factors.
- Static scheduling is **simpler** and **faster** than dynamic scheduling, as it does not require any runtime decisions or overhead. Dynamic scheduling is **more flexible** and **adaptive** than static scheduling, as it can handle unpredictable changes and optimize the system performance.
- Static systems provide **guaranteed** and **predictable** behavior, which is desirable for **hard real-time systems** that have strict deadlines and safety-critical requirements. Dynamic systems provide **better performance** and **resource utilization**, which is desirable for **soft real-time systems** that have relaxed deadlines and quality-of-service requirements.
- Static systems are suitable for **simple** and **regular** real-time systems, such as periodic tasks that have fixed execution times and deadlines. Dynamic systems are suitable for **complex** and **irregular** real-time systems, such as aperiodic tasks that have variable execution times and deadlines, or tasks that depend on external events or inputs.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. This means that EDF can schedule any set of tasks that has a feasible schedule under these conditions.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. This means that LST can schedule any set of tasks that has a feasible schedule under these conditions.
- However, EDF and LST are not optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements. In these cases, EDF and LST may fail to produce a feasible schedule even if one exists.
- EDF and LST may also under-utilize the CPU, thus decreasing the efficiency and throughput of the system. This happens when there are idle slots in the schedule or when tasks are executed earlier than necessary.
- EDF and LST can be combined to enhance the performance of real-time task scheduling. For example, one can use EDF for tasks without precedence constraints and LST for tasks with precedence constraints. This can improve the schedulability and utilization of the system.



### Rate Monotonic Algorithm for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

- Rate Monotonic Algorithm (RMA) is a static-priority preemptive scheduling algorithm for real-time systems    .
- The static priorities are assigned to tasks based on their periods, so that the shorter the period, the higher the priority   .
- The algorithm is optimal for periodic tasks with fixed deadlines, meaning that no other static-priority algorithm can schedule a task set that RMA cannot   .
- The algorithm is simple and easy to implement, but it has some limitations, such as:
  - It does not consider the actual execution time or the deadline of the tasks, only their periods .
  - It does not handle aperiodic or sporadic tasks well, as they may have unpredictable periods or arrival times .
  - It may not utilize the processor fully, as some tasks may have long idle times between their executions .
- The algorithm has a sufficient and necessary schedulability test, which is based on the utilization factor of the tasks   . The utilization factor of a task is the ratio of its execution time to its period. The schedulability test is:

  - For n tasks, if the sum of their utilization factors is less than or equal to n(2^(1/n) - 1), then the task set is schedulable by RMA   .
  - For n tasks, if the sum of their utilization factors is greater than n(2^(1/n) - 1), then the task set may or may not be schedulable by RMA   .
  - For n tasks, if the sum of their utilization factors is greater than 1, then the task set is not schedulable by RMA or any other algorithm   .

- The algorithm can be extended or modified to handle different types of tasks, such as deadline-monotonic scheduling, which assigns priorities based on deadlines instead of periods  , or sporadic server, which allocates a fixed amount of time for aperiodic or sporadic tasks  .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have the prior information related to the task parameters and has to make decisions based on the current state of the system.
- Offline scheduling has the advantage of being optimal, predictable, and easy to implement, but it has the disadvantage of being inflexible, unable to handle dynamic events, and requiring a lot of offline computation.
- Online scheduling has the advantage of being adaptable, responsive, and able to handle uncertainties, but it has the disadvantage of being suboptimal, complex, and requiring a lot of run-time overhead.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive jobs, but no fixed arrival pattern. They have hard or firm deadlines and are usually generated by external events. Examples are interrupts, sensor readings, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a predefined schedule that is computed offline. The scheduler follows the schedule and switches jobs at predefined instants. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in real-time systems is to balance the responsiveness of the system to these jobs and the schedulability of the periodic tasks that have hard deadlines and fixed arrival patterns.
- There are different approaches to schedule aperiodic and sporadic jobs in priority driven and clock driven systems, such as:

  - Background scheduling: This approach assigns the lowest priority to aperiodic and sporadic jobs and executes them only when no periodic task is ready. This ensures that periodic tasks meet their deadlines, but it may result in poor response time for aperiodic and sporadic jobs.
  - Polling servers: This approach assigns a fixed priority and a budget to a server task that handles aperiodic and sporadic jobs. The server task is periodically replenished with its budget and can execute aperiodic and sporadic jobs until its budget is exhausted. This improves the responsiveness of the system to aperiodic and sporadic jobs, but it may introduce some overhead and waste some budget if no aperiodic or sporadic job is available.
  - Deferrable servers: This approach is similar to polling servers, but the server task can defer its execution until an aperiodic or sporadic job arrives. This reduces the overhead and waste of budget, but it may increase the blocking time of periodic tasks that have lower priority than the server task.
  - Sporadic servers: This approach is designed for sporadic jobs that have hard or firm deadlines. The server task has a fixed priority and a budget that is replenished only when a sporadic job arrives. The server task can execute sporadic jobs until its budget is exhausted or its deadline is reached. This ensures that sporadic jobs meet their deadlines, but it may result in poor utilization of the processor if the sporadic jobs are short or infrequent.
  - Slack stealing: This approach exploits the available slack time of periodic and sporadic jobs to execute aperiodic jobs. The slack time of a job is the difference between its deadline and its worst-case execution time. The scheduler monitors the slack time of all jobs and assigns the highest priority to an aperiodic job when there is enough slack time to complete it without affecting the schedulability of other jobs. This improves the response time of aperiodic jobs, but it may require complex calculations and frequent updates of the slack time.
  - Time-driven scheduling: This approach is used in clock driven systems, where the schedule is computed offline and stored in a table. The scheduler can reserve some slots in the table for aperiodic and sporadic jobs and assign them priorities based on the slot position. The scheduler can also use slack stealing to execute aperiodic jobs in the unused slots of periodic tasks. This simplifies the online scheduling, but it may require a large table and a flexible hardware platform to support dynamic switching of jobs.



## Unit 3 - Resources Sharing

- Resource sharing refers to the sharing of library resources by certain participating libraries among themselves on the basis of the principle of co-operation.
- Resource sharing can also apply to the sharing of research tools, materials, and services by multiple projects, investigators, or institutions.
- Resource sharing is a way of ensuring that all the necessary resources are available and used efficiently to complete a project or meet a business objective.
- Resources can be natural or human-made, such as sources of supply, support, wealth, revenue, quality, information, or expertise.
- Resource sharing can have various benefits, such as reducing costs, increasing access, improving quality, enhancing collaboration, and promoting innovation.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP): A low-priority task that holds a resource inherits the priority of the highest-priority task that is blocked by it, until it releases the resource.
  - Priority ceiling protocol (PCP): A task can lock a resource only if its priority is higher than the ceiling of the resource, which is the highest priority of any task that can access the resource. A task that locks a resource inherits the ceiling of the resource, until it releases the resource.
  - Stack resource policy (SRP): A task can lock a resource only if its preemption level, which is assigned based on the resource usage, is higher than the system ceiling, which is the highest preemption level of any locked resource. A task that locks a resource raises the system ceiling to its preemption level, until it releases the resource.



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- This protocol ensures that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of non-preemptive critical sections are:
  - Simplicity: no need for complex locking or signaling mechanisms to protect the critical sections .
  - Deadlock-freedom: no job can be blocked by another job holding a resource, so deadlock can never occur  .
- The disadvantages of non-preemptive critical sections are:
  - Priority inversion: a high-priority job may be delayed by a low-priority job that is executing a critical section .
  - Resource underutilization: a job holding a resource may not use it for the entire duration of the critical section, wasting the resource and delaying other jobs that need it .
  - Unbounded blocking: a job may be blocked for an indefinite amount of time by another job that is executing a long or unbounded critical section .



### Basic Priority-Inheritance and Priority-Ceiling Protocols for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use preemptive scheduling and mutual exclusion.
- PIP and PCP aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources, and to prevent deadlocks and priority inversions.
- PIP works by temporarily raising the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it. This way, the low-priority task can finish using the resource and release it to the blocked task sooner.
- PCP works by assigning a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource. A task can only lock a resource if its priority is higher than the ceiling priority of all the resources that are currently locked. This way, the low-priority tasks are prevented from locking resources that may be needed by high-priority tasks.
- The main differences between PIP and PCP are:

  - PIP is greedy while PCP is not. PIP lets a task lock a resource whenever it is free, while PCP may deny a task from locking a resource even if it is free, if the task's priority is lower than the ceiling priority of any locked resource.
  - PIP requires minimum support from the operating system, while PCP requires maximum support. PIP only needs to change the priority of a task when it locks or unlocks a resource, while PCP needs to keep track of the ceiling priority of all the locked resources and compare it with the priority of the requesting task.
  - PIP cannot prevent deadlocks, while PCP can. PIP may cause a circular wait among tasks that lock multiple resources, while PCP avoids this by enforcing a strict order of locking resources based on their ceiling priorities.
  - PIP may cause unbounded priority inversion, while PCP guarantees bounded priority inversion. PIP may allow a low-priority task to hold a resource for a long time if it is preempted by other tasks that are not blocked by it, while PCP limits the blocking time of a high-priority task by the maximum execution time of a lower-priority task that can lock any resource needed by the high-priority task.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource .
- SBPCP has the following properties :
  - It prevents priority inversion by ensuring that a higher priority job can always preempt a lower priority job that is using a resource.
  - It prevents deadlock by ensuring that a job can only request a resource if its priority is equal to or higher than the ceiling priority of the resource.
  - It bounds the blocking time of a job by the maximum execution time of a lower priority job that can access the same resource.
  - It is optimal for fixed-priority scheduling, meaning that it can schedule any set of jobs that is schedulable by any other fixed-priority protocol.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority-ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The priority-ceiling protocol works by temporarily raising the priorities of tasks that access shared resources to the priority ceiling of the resource they are accessing. This prevents lower-priority tasks from preempting higher-priority tasks that need the same resource .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point.
- OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to execute and has a resource request pending .
- The priority-ceiling protocol has several advantages over other synchronization techniques, such as priority inheritance protocol, such as:
  - It avoids deadlock by preventing circular waiting among tasks that need multiple resources .
  - It bounds the blocking time of any task by at most one critical section of a lower-priority task .
  - It reduces the number of context switches and the overhead of priority management .
  - It allows for simple and efficient implementation in both static and dynamic priority systems .
- The priority-ceiling protocol also has some limitations, such as:
  - It requires a priori knowledge of the resource requirements of each task and the priority ceiling of each resource .
  - It may cause unnecessary blocking of lower-priority tasks that do not contend for the same resources as higher-priority tasks .
  - It may not be optimal for some task sets and resource allocation policies .



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems.
- It aims to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- It assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is temporarily raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- This protocol ensures that a task can be blocked by at most one lower-priority task, and that a task can access a resource only if it is the highest-priority task in the system.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the system design.
- Dynamic preemption ceiling protocol assigns a variable ceiling priority to each resource based on the priority of the task that locks it.
- Static preemption ceiling protocol is simpler and faster, but dynamic preemption ceiling protocol is more flexible and can handle deadline-driven systems.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that have more than one unit of the same type, such as printers, disks, or communication channels.
- Access control in multiple-unit resources is the problem of ensuring that jobs that need to use one or more units of a resource can do so without violating the timing constraints of themselves or other jobs.
- Access control in multiple-unit resources can be classified into two categories: static and dynamic.
  - Static access control assigns a fixed number of units of a resource to each job or task, based on its worst-case resource demand. Static access control is simple and predictable, but may lead to underutilization of resources or deadlock if the resource demand is not known in advance or varies at run-time.
  - Dynamic access control allows jobs or tasks to request and release units of a resource at run-time, based on their actual resource demand. Dynamic access control is more flexible and efficient, but may lead to priority inversion, blocking, or deadlock if the resource allocation is not coordinated properly.
- Several protocols have been proposed for dynamic access control in multiple-unit resources, such as the Priority Inheritance Protocol (PIP), the Priority Ceiling Protocol (PCP), the Stack Resource Policy (SRP), and the Multiprocessor Priority Ceiling Protocol (MPCP).
  - PIP is a protocol that allows a job that is blocked by a lower-priority job that holds a resource to inherit the priority of the blocked job, thus preventing transitive blocking and reducing the blocking time. PIP is simple and easy to implement, but may lead to chained blocking, priority inversion, or deadlock in some cases.
  - PCP is a protocol that assigns a priority ceiling to each resource, which is the highest priority of any job that may request that resource. A job can lock a resource only if its priority is higher than the priority ceiling of all the resources currently locked by other jobs, thus preventing deadlock and reducing the blocking time. PCP is more complex and requires more information than PIP, but guarantees bounded blocking and avoids priority inversion.
  - SRP is a protocol that assigns a preemption level to each job, which is the highest priority of any job that may preempt that job. A job can lock a resource only if its preemption level is higher than the preemption level of all the jobs that have locked or may lock that resource, thus preventing deadlock and reducing the blocking time. SRP is similar to PCP, but uses preemption levels instead of priorities, and allows nested resource requests.
  - MPCP is a protocol that extends PCP to multiprocessor systems, where each processor has a local priority ceiling and a global priority ceiling. A job can lock a resource only if its priority is higher than the local priority ceiling of its processor and the global priority ceiling of all the processors, thus preventing deadlock and reducing the blocking time. MPCP is more complex and requires more information than PCP, but guarantees bounded blocking and avoids priority inversion in multiprocessor systems.



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause data inconsistency and violate the correctness of the system.
- To prevent data inconsistency, concurrency control algorithms are needed to regulate the concurrent accesses to data objects and ensure data consistency.
- Concurrency control algorithms for real time systems should also consider the timing constraints of the jobs and avoid unnecessary blocking or aborting of critical jobs.
- There are two main types of concurrency control algorithms for real time systems: pessimistic and optimistic.
  - Pessimistic algorithms prevent data conflicts by locking the data objects before accessing them and releasing them after accessing them. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol .
  - Optimistic algorithms allow data conflicts to occur and detect them after accessing the data objects. If a conflict is detected, the conflicting jobs are aborted and restarted. Examples of optimistic algorithms are timestamp ordering, multiversion concurrency control, and validation-based protocols .
- The choice of concurrency control algorithm depends on the characteristics of the system, such as the number and size of data objects, the frequency and duration of data accesses, the degree of data contention, the criticality and deadline of the jobs, and the overhead of locking, aborting, and restarting .



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on whether the parties are communicating at the same time or not.
- RTC can be text-based, voice-based, video-based, or a combination of these modalities.
- RTC can be one-to-one, one-to-many, or many-to-many, depending on the number of participants and the direction of communication.
- RTC can be mediated by different technologies, such as telephones, radios, computers, mobile devices, or the Internet.
- RTC can be used for various purposes, such as personal, social, educational, professional, or entertainment.
- RTC can have various benefits, such as enhancing collaboration, reducing isolation, increasing engagement, improving learning outcomes, or providing entertainment.
- RTC can also have various challenges, such as technical issues, privacy concerns, security risks, ethical dilemmas, or social norms.
- RTC can be influenced by various factors, such as the context, the purpose, the audience, the medium, the content, the tone, the feedback, or the etiquette of communication.
- RTC can be improved by various strategies, such as planning, preparing, practicing, adapting, listening, responding, clarifying, summarizing, or evaluating communication.



### Basic Concepts in Real Time Communication

- Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays .
- In RTC, there is always a direct path between the source and the destination, and the data is not stored en route to the destination .
- RTC is synonymous with live communication, as opposed to offline or asynchronous communication.
- RTC is essential for applications that require timely and accurate delivery of data, such as voice, video, gaming, and collaboration .
- RTC can be implemented using various protocols and hardware media, depending on the requirements and constraints of the application.
- Some examples of RTC protocols are:
  - Real-time Transport Protocol (RTP): A standard protocol for delivering audio and video over IP networks.
  - Real-time Control Protocol (RTCP): A companion protocol to RTP that provides feedback and control information for RTP sessions.
  - Real-time Streaming Protocol (RTSP): A protocol for controlling the delivery of streaming media over IP networks.
  - Real-time Messaging Protocol (RTMP): A protocol for streaming audio, video, and data over the internet, mainly used by Adobe Flash applications.
  - Web Real-Time Communication (WebRTC): A set of APIs and protocols that enable browser-based RTC applications without plugins or downloads.
- Some examples of RTC hardware media are:
  - Ethernet: A family of wired network technologies that support high-speed and reliable data transmission.
  - Wi-Fi: A wireless network technology that allows devices to communicate over radio waves.
  - Bluetooth: A wireless technology that enables short-range communication between devices.
  - Cellular: A wireless network technology that uses cellular towers to provide voice and data services to mobile devices.
  - Satellite: A wireless network technology that uses satellites to provide global coverage and communication.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- A **hard real-time communication system** is one that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable loss  .
- Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and pacemakers  .
- A **soft real-time communication system** is one that can tolerate some deadline misses, but the quality of service may degrade  .
- Examples of soft real-time communication systems are video conferencing, online gaming, and multimedia streaming  .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic .
- Hard real-time communication systems require strict timing guarantees and predictable behavior, while soft real-time communication systems can adapt to varying network conditions and resource availability .
- Hard real-time communication systems are often implemented using dedicated hardware and specialized protocols, while soft real-time communication systems can use general-purpose hardware and standard protocols .
- Hard real-time communication systems are more challenging to design, test, and verify, while soft real-time communication systems are more flexible and scalable .
- Hard real-time communication systems are suitable for safety-critical and mission-critical applications, while soft real-time communication systems are suitable for performance-critical and user-centric applications  .



### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without storing data en route to the destination  .
- Real time communication can involve voice, video, text, or data transmission over landlines, mobile phones, VoIP, or other network protocols .
- Real time communication requires a traffic model, a network model, and a quality of service model to ensure the timely and reliable delivery of messages .

#### Real Time Traffic Model

- The real time traffic model describes the characteristics of the messages that are generated by the sources and delivered to the destinations on a continuous basis .
- The traffic model can include periodic, aperiodic, and sporadic messages, each with different inter-packet spacing, message length, and reception deadline .
- The traffic model can be represented by a tuple of the form Mi = (pi, ei, Di), where pi is the inter-packet spacing, ei is the message length, and Di is the reception deadline of message Mi .
- This traffic model is also called the peak rate model in real time communication .

#### Network Model

- The network model describes the structure and behavior of the network that connects the sources and destinations of the messages .
- The network model can include the network topology, the routing algorithms, the link capacities, the queuing disciplines, the buffer sizes, and the network protocols .
- The network model can affect the throughput, delay, and jitter of the messages in the network .

#### Quality of Service Model

- The quality of service model describes the performance requirements and guarantees of the real time communication .
- The quality of service model can include the metrics, the parameters, the policies, and the mechanisms to measure and ensure the quality of service .
- The quality of service model can involve trade-offs between different metrics, such as bandwidth, latency, reliability, availability, and security .
- The quality of service model can also involve service level agreements, admission control, resource reservation, and congestion control .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Priority-based service disciplines can provide different delay and jitter bounds for different classes of packets, as well as guarantee bandwidth and fairness requirements.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns a weight to each queue and serves packets from each queue in a round-robin fashion according to their weights .
- WRR can be implemented without a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of the scheduler.
- WRR can also be combined with other techniques, such as rate control and frame-based scheduling, to improve the performance and flexibility of the service discipline.
- Some examples of WRR-based service disciplines are:
  - Weighted fair queuing (WFQ), which assigns weights to queues based on the packet arrival rates and the desired bandwidth allocation.
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server, and guarantees the delay jitter bound and satisfies diverse delay requirements.
  - Class-based weighted fair queuing (CBWFQ), which extends WFQ to support multiple classes of traffic with different priority levels and bandwidth guarantees.
  - Weighted fair priority queuing (WFPQ), which combines WFQ and strict priority queuing to provide both bandwidth and priority guarantees to different classes of traffic.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel by multiple nodes or transmitters.
- Broadcast networks are networks where a single transmission can be received by all nodes in the network, such as wireless networks or bus networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use direct, asynchronous competition between neighboring nodes to determine which node will transmit next. Examples include Aloha and CSMA. These protocols are simple, but suffer from collisions and low channel utilization.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next. Examples include token passing and polling. These protocols avoid collisions, but introduce overhead and delay.
- Reservation-based protocols use a separate control channel or a dedicated time slot to reserve the channel for data transmission. Examples include TDMA and CDMA. These protocols can achieve high channel utilization and bounded access delay, but require synchronization and coordination among nodes.
- ABROAD is an adaptive MAC protocol for reliable broadcast transmission in wireless networks. It incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay. It provides worst-case performance guarantees while remaining adaptive to local changes in traffic load and node connectivity. It outperforms broadcast protocols based on reliable unicast packet delivery schemes, such as the IEEE 802.11 MAC standard .



### Internet and Resource Reservation Protocols for Real Time Communication

- Internet protocols are the set of rules and standards that enable communication and data exchange over the Internet.
- Real time communication is the transmission and reception of data with minimal delay and high reliability, such as voice, video, or multimedia applications.
- Internet protocols for real time communication need to provide quality of service (QoS) guarantees, such as bandwidth, delay, jitter, and packet loss, to meet the requirements of real time applications.
- Resource reservation protocols are one of the approaches to provide QoS guarantees over the Internet by allocating network resources along the end-to-end path of a real time communication session.
- Resource reservation protocols can be classified into two categories: sender-initiated and receiver-initiated.
- Sender-initiated protocols, such as Integrated Services (IntServ), require the sender to initiate the resource reservation process by sending a request message to each network device along the path, and wait for the confirmation from each device before starting the data transmission.
- Receiver-initiated protocols, such as Differentiated Services (DiffServ), require the receiver to initiate the resource reservation process by sending a request message to the network devices along the path, and then inform the sender about the QoS level that can be achieved.
- Resource Reservation Protocol (RSVP) is a receiver-initiated protocol that supports both IntServ and DiffServ models. It allows the receiver to specify the QoS requirements for a real time communication session, and request the network devices along the path to reserve the necessary resources for the session.
- RSVP operates in two phases: reservation setup and reservation maintenance. In the reservation setup phase, the receiver sends a PATH message to the sender, which contains the information about the receiver's address and the QoS requirements. The sender then sends a RESV message to the receiver, which contains the information about the sender's address and the QoS parameters. The RESV message travels along the same path as the PATH message, and requests the network devices to reserve the resources for the session. The network devices reply with a RESVCONF message to confirm the reservation. In the reservation maintenance phase, the sender and the receiver periodically exchange PATH and RESV messages to refresh the reservation and update the QoS parameters.
- RSVP has several features, such as:
  - Soft state: RSVP does not maintain hard state information about the reservations, but relies on periodic refresh messages to keep the reservations alive. This allows RSVP to adapt to dynamic network conditions and recover from failures.
  - Scalability: RSVP can scale to large networks by using aggregation and filtering techniques to reduce the number of reservation messages and the amount of state information.
  - Heterogeneity: RSVP can support heterogeneous receivers with different QoS requirements by using multicast and merging techniques to create shared or distinct reservations for different receiver groups.
  - Flexibility: RSVP can support different QoS models, such as IntServ and DiffServ, by using different reservation styles and traffic specifications to define the QoS parameters and the resource allocation methods.



## Unit 5 - Real Time Operating Systems and Databases

- A **real-time operating system (RTOS)** is an operating system that guarantees to process data and events within a predefined time limit, usually in the order of milliseconds or microseconds .
- A **real-time database system (RTDBS)** is a database system that supports database operations with real-time constraints, such as deadlines, priorities, and consistency.
- Real-time operating systems and databases are used in applications that require fast and predictable responses to external stimuli, such as industrial control, flight control, telecommunication, and real-time simulation .
- Some of the characteristics and challenges of real-time operating systems and databases are:
  - **Concurrency**: Multiple tasks or transactions may need to access the same data or resources at the same time, which may cause conflicts or inconsistencies. RTOS and RTDBS need to provide mechanisms for synchronization, mutual exclusion, and deadlock prevention .
  - **Scheduling**: RTOS and RTDBS need to allocate CPU time and other resources to tasks or transactions according to their timing requirements, such as deadlines, periods, and execution times. RTOS and RTDBS need to use scheduling algorithms that can optimize the system performance and meet the timing constraints .
  - **Memory management**: RTOS and RTDBS need to manage the memory space for tasks or transactions, which may have different memory requirements and lifetimes. RTOS and RTDBS need to use memory allocation and deallocation techniques that can reduce memory fragmentation and overhead .
  - **Fault tolerance**: RTOS and RTDBS need to handle errors and failures that may occur during the system operation, such as hardware faults, software bugs, or external disturbances. RTOS and RTDBS need to provide mechanisms for error detection, recovery, and compensation .
- Some of the examples of real-time operating systems and databases are:
  - **Azure RTOS**: A commercial RTOS developed by Microsoft that provides real-time multithreading, inter-thread communication and synchronization, and memory management.
  - **FreeRTOS**: An open source RTOS that supports multiple architectures and platforms, and provides preemptive and cooperative scheduling, inter-task communication, and memory management.
  - **ScyllaDB**: A distributed NoSQL database that provides high performance, scalability, and availability for operational data, and supports real-time transactions and analytics.
  - **InfluxDB**: A time series database that stores and processes data that are indexed by time, and supports real-time ingestion, querying, and visualization.



### Features of RTOS

- An RTOS is an operating system that has two key features: **predictability** and **determinism**. This means that it can guarantee that tasks will be completed within a specified time limit, and that the system will always respond in the same way to the same inputs.
- An RTOS is **small**, **fast**, **responsive**, and **efficient** . It occupies very less memory and consumes fewer resources than a general-purpose operating system. It can execute tasks quickly and switch between them with minimal overhead.
- An RTOS supports **real-time applications** that have strict timing constraints and high reliability requirements . Examples of such applications are embedded systems, industrial control systems, robotics, avionics, and multimedia .
- An RTOS uses different **scheduling algorithms** to manage the execution of tasks according to their priorities, deadlines, and resource needs. Some common scheduling algorithms are co-operative scheduling, pre-emptive scheduling, rate-monotonic scheduling, and earliest deadline first scheduling.
- An RTOS provides various **services** and **features** to facilitate the development and deployment of real-time applications, such as inter-task communication, synchronization, memory management, device drivers, file systems, network protocols, and debugging tools .



### Time Services

- Time services are the mechanisms that provide the notion of time and temporal ordering in real-time systems.
- Time services are essential for real-time systems because they enable the specification, verification, and enforcement of timing constraints and deadlines.
- Time services can be classified into two categories: **time representation** and **time synchronization**.
- Time representation is the way of encoding and manipulating the values of time in a system. It can be based on different models, such as physical time, logical time, or hybrid time.
- Physical time is the time measured by physical clocks, such as quartz oscillators or atomic clocks. It is also called wall-clock time or absolute time. Physical time is continuous, linear, and universal.
- Logical time is the time defined by the order of events in a system. It is also called causal time or relative time. Logical time is discrete, partial, and local.
- Hybrid time is the combination of physical and logical time. It is used to capture both the temporal order and the temporal distance of events in a system. Hybrid time is continuous, partial, and local.
- Time synchronization is the process of aligning the clocks of different devices or processes in a system. It can be based on different methods, such as clock skew estimation, clock drift compensation, clock offset correction, or clock agreement.
- Clock skew estimation is the technique of measuring the difference between the clocks of two devices or processes. It can be done by exchanging timestamps or using external reference signals.
- Clock drift compensation is the technique of adjusting the frequency of a clock to match the frequency of a reference clock. It can be done by using feedback control or feedforward control.
- Clock offset correction is the technique of adding or subtracting a constant value to a clock to match the value of a reference clock. It can be done by using one-way or two-way message exchanges.
- Clock agreement is the technique of reaching a consensus on the value of a clock among multiple devices or processes. It can be done by using voting algorithms or averaging algorithms.
- Time services can be implemented in different levels of a system, such as hardware, operating system, middleware, or application.
- Hardware time services are the physical devices that generate and distribute time signals, such as oscillators, timers, counters, or buses.
- Operating system time services are the software components that manage and access the hardware time services, such as clock drivers, interrupt handlers, or system calls.
- Middleware time services are the software components that provide time services to the applications, such as time protocols, time libraries, or time services.
- Application time services are the software components that use the time services to implement the functionality and logic of the applications, such as time stamps, time triggers, or time constraints.

: https://www.geeksforgeeks.org/real-time-systems/
: https://www.intel.com/content/www/us/en/robotics/real-time-systems.html



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing, which is the key feature of a RTOS.
- However, some variants of UNIX, such as Linux, have been modified to provide real-time capabilities by adding patches or modules to the kernel . These modifications aim to reduce the latency and jitter of the system, and to improve the predictability and responsiveness of the tasks .
- Some examples of real-time applications that use Linux as a RTOS are human-in-the-loop simulations, launch vehicles, and spacecrafts . However, using Linux as a RTOS also poses some challenges, such as compatibility, security, testing, and certification .



### POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a set of standards that define how an application should interact with an operating system.
- POSIX aims to achieve portability, interoperability, and compatibility among different operating systems, especially for applications that require long-term maintenance and support.
- POSIX includes over 30 individual standards, covering various aspects of operating system services, such as file operations, process management, signals, devices, threads, and real-time extensions.
- POSIX real-time extensions are defined in the POSIX.1b and POSIX.1j standards, which specify the additional features and functions that are needed by real-time applications, such as timers, clocks, semaphores, message queues, shared memory, priority scheduling, and asynchronous I/O .
- POSIX real-time extensions aim to provide deterministic and predictable behavior for real-time applications, by allowing them to specify deadlines, priorities, and resource requirements, and by ensuring that the operating system can meet these demands in a timely manner.
- POSIX real-time extensions also aim to provide flexibility and scalability for real-time applications, by allowing them to use different scheduling policies, such as fixed priority, earliest deadline first, and round-robin, and by supporting both hard and soft real-time constraints.
- POSIX real-time extensions are not mandatory for an operating system to be POSIX-compliant, but they are widely adopted by many real-time operating systems, such as QNX, VxWorks, LynxOS, and RTLinux.
- POSIX real-time extensions are not sufficient for all real-time applications, as they do not address some issues that are specific to certain domains, such as distributed systems, fault tolerance, security, and multimedia.
- POSIX real-time extensions are also not optimal for some real-time applications, as they may introduce some overhead and complexity, such as system calls, context switches, and memory management, that may affect the performance and responsiveness of the system.
- POSIX real-time extensions are therefore a trade-off between portability and efficiency, and they should be used with caution and evaluation, depending on the requirements and characteristics of the real-time application.



### Characteristics of Temporal Data

- Temporal data is the data that is **related to time** in some way, and allows other data to be **placed in a chronological sequence**, or to be **analyzed chronologically**.
- Temporal data can be **uni-temporal, bi-temporal or tri-temporal**, depending on how many aspects of time are considered.
- The temporal aspects usually include **valid time**, **transaction time** or **decision time**.
  - Valid time is the time period during or event time at which a fact is **true in the real world**. For example, the date of birth of a person is a valid time attribute.
  - Transaction time is the time period during or event time at which a fact is **stored in the database**. For example, the date of entry of a person's record in the database is a transaction time attribute.
  - Decision time is the time period during or event time at which a fact is **used for decision making**. For example, the date of approval of a loan application is a decision time attribute.
- Temporal data can be **discrete** or **continuous**, depending on whether the time values are **finite** or **infinite**.
  - Discrete temporal data is the data that has a **finite number of time values** or **intervals**. For example, the dates of holidays in a year are discrete temporal data.
  - Continuous temporal data is the data that has an **infinite number of time values** or **intervals**. For example, the temperature of a region over time is continuous temporal data.
- Temporal data can be **static** or **dynamic**, depending on whether the data **changes** or **remains constant** over time.
  - Static temporal data is the data that **does not change** over time. For example, the date of birth of a person is static temporal data.
  - Dynamic temporal data is the data that **changes** over time. For example, the salary of a person is dynamic temporal data.
- Temporal data can be **absolute** or **relative**, depending on whether the time values are **independent** or **dependent** on other time values.
  - Absolute temporal data is the data that has time values that are **independent** of other time values. For example, the date of a historical event is absolute temporal data.
  - Relative temporal data is the data that has time values that are **dependent** on other time values. For example, the duration of a movie is relative temporal data.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to use accurate and up-to-date data to perform time-critical tasks and make correct decisions.
- Temporal consistency can be violated if the data in the database becomes stale or outdated due to the dynamic nature of the physical environment or the delays in the data acquisition and processing.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates: updating the data in the database whenever there is a significant change in the physical environment.
  - Periodic updates: updating the data in the database at regular intervals based on the data freshness requirements.
  - Temporal validity: assigning a validity interval to each data item and checking if the data is still valid before using it.
  - Temporal constraints: specifying the maximum allowable difference between the data in the database and the physical environment and enforcing it by rejecting or aborting transactions that violate it.



### Concurrency Control

- Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the database.
- Concurrency control is especially important for real-time database systems, where transactions have timing constraints and must be completed before their deadlines.
- Concurrency control in real-time database systems should consider both data consistency and timing constraints, and adapt to changes in the operating environment and guarantee the completion of critical transactions.

### Concurrency Control Methods

- There are two main methods of concurrency control: locking-based and timestamp-based.
- Locking-based methods use locks to prevent concurrent transactions from accessing the same data item in conflicting modes (read or write).
- Locking-based methods can be classified into two-level locking, tree locking, and graph locking, depending on the granularity and structure of the data items.
- Locking-based methods can also be classified into pessimistic and optimistic, depending on the assumption of the likelihood of conflicts.
- Pessimistic locking methods acquire locks before accessing data items, and release them after finishing the operations.
- Optimistic locking methods do not use locks, but validate the transactions at the end to detect and resolve conflicts.
- Timestamp-based methods use timestamps to order the transactions and ensure serializability.
- Timestamp-based methods assign a unique timestamp to each transaction, and use it to determine the precedence and validity of the operations.
- Timestamp-based methods can be classified into basic, Thomas, and multiversion, depending on the way of handling outdated read and write operations.

### Concurrency Control Challenges in Real-Time Database Systems

- Concurrency control in real-time database systems faces some challenges that are not present in conventional database systems.
- One challenge is to balance the trade-off between data consistency and timing constraints.
- Data consistency requires that concurrent transactions are serializable, which may cause delays and missed deadlines.
- Timing constraints require that transactions are completed before their deadlines, which may cause data inconsistency and violations of serializability.
- Another challenge is to cope with the dynamic and unpredictable nature of the real-time environment.
- The real-time environment may change due to external events, system failures, or resource availability.
- The concurrency control method should be able to adapt to these changes and prioritize the critical transactions over the less important ones.
- A third challenge is to handle the distributed and decomposable nature of the real-time database.
- The real-time database may be distributed over multiple nodes, and the transactions may be decomposable into subtransactions.
- The concurrency control method should be able to coordinate the distributed and decomposable transactions and ensure their atomicity and serializability.

### Concurrency Control Examples in Real-Time Database Systems

- One example of a concurrency control method for real-time database systems is the **priority ceiling protocol**.
- The priority ceiling protocol is a locking-based method that assigns a priority ceiling to each data item, which is the highest priority of any transaction that can lock it.
- The priority ceiling protocol prevents deadlock and priority inversion by allowing a transaction to lock a data item only if its priority is higher than the priority ceiling of any locked data item.
- The priority ceiling protocol can be extended to handle distributed and decomposable transactions by using a global priority ceiling and a local priority ceiling for each node.
- Another example of a concurrency control method for real-time database systems is the **earliest deadline first with concurrency control (EDF-CC)**.
- The EDF-CC is a timestamp-based method that assigns a deadline to each transaction, and uses it as the timestamp for ordering the transactions.
- The EDF-CC ensures serializability by aborting and restarting any transaction that violates the timestamp order.
- The EDF-CC also ensures timeliness by scheduling the transactions according to their deadlines, and aborting any transaction that misses its deadline.
- The EDF-CC can be modified to handle different levels of data consistency and timing constraints by using different abort and restart policies.



### Overview of Commercial Real Time databases for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have some special characteristics that distinguish them from traditional databases, such as:
  - Timeliness: the ability to provide reliable and consistent responses within specified deadlines.
  - Concurrency: the ability to handle multiple transactions or queries simultaneously without compromising data integrity or performance.
  - Predictability: the ability to guarantee a certain level of service quality and resource utilization under varying workloads and system conditions.
  - Availability: the ability to ensure data accessibility and recoverability in case of failures or disruptions.
- Real-time databases can be classified into two types based on their timing constraints:
  - Hard real-time databases: these databases must meet all the deadlines, otherwise the system may fail or cause severe consequences. Examples of hard real-time applications are air traffic control, nuclear power plant control, and missile guidance systems.
  - Soft real-time databases: these databases can tolerate some deadline misses, but the system performance or quality may degrade. Examples of soft real-time applications are online gaming, video streaming, and e-commerce.
- Some of the commercial real-time databases available in the market are  :
  - Raima Database Manager (RDM): a high-performance, embedded, in-memory database that supports hard and soft real-time applications. It offers ACID transactions, SQL and NoSQL interfaces, replication, encryption, compression, and high availability features.
  - Altus Group: a data and analytics platform that provides historical and current information on commercial real estate markets, transactions, and properties. It offers data integration, visualization, valuation, and forecasting tools.
  - CoStar: a leading provider of commercial real estate data and analytics, covering more than 5.5 million properties and 18 billion square feet of space. It offers market research, leasing, sales, and tenant data, as well as online marketplaces and software solutions.
  - Google Cloud Firestore: a scalable, serverless, NoSQL database service for large analytical and operational workloads. It offers up to 99.999% availability, real-time synchronization, offline support, and security features. It can process more than 5 billion requests per second at peak, and with more than 10 Exabytes of data under management.

