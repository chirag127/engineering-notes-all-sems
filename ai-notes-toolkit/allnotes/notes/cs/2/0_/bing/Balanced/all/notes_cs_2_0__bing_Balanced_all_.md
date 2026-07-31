

# Real Time System

A real time system is an information processing system that can respond to events within predictable and specific time constraints. The system must produce the expected result within a defined deadline, otherwise it may cause a system failure or undesirable consequences. A real time system also needs to coordinate independent clocks and operate together in unison (time synchronization).

Some examples of real time systems are:

- Process control systems: These systems are used in industrial applications where production is continuous and requires precise and timely control of physical processes, such as chemical plants, power plants, oil refineries, etc. 
- Machine vision: These systems are used to help machines rapidly interpret data so they can see their surroundings and perform tasks, such as object recognition, face detection, barcode scanning, etc. 
- Robotics: These systems are used to control the movements and actions of robots, such as industrial robots, autonomous vehicles, drones, etc. Robotics systems need to sense the environment, plan the actions, and execute them in real time. 
- Flight control systems: These systems are used to control the flight of aircraft, such as airplanes, helicopters, rockets, etc. Flight control systems need to monitor the sensors, adjust the actuators, and maintain the stability and safety of the flight. 

There are two types of real time systems based on the timing constraints:

- Hard real time systems: These systems have absolute deadlines, and if those deadlines are missed, a system failure or a catastrophic event will occur. For example, a flight control system must respond to the pilot's commands within milliseconds, otherwise the aircraft may crash. 
- Soft real time systems: These systems have relative deadlines, and if those deadlines are missed, the system performance or quality of service will degrade, but not fail. For example, a video streaming system must deliver the frames within a certain time, otherwise the video quality will be poor, but not stop. 

Some characteristics of real time systems are:

- Concurrency: A real time system may have multiple tasks or processes running at the same time, and they need to be coordinated and synchronized to avoid conflicts and ensure correctness.
- Determinism: A real time system must behave predictably and consistently, and produce the same output for the same input and state, regardless of the external factors or disturbances.
- Reliability: A real time system must be able to handle errors and faults, and recover from them quickly and gracefully, without compromising the system functionality or safety.
- Efficiency: A real time system must be able to utilize the available resources, such as CPU, memory, disk, network, etc., optimally and effectively, and avoid wastage or overload.



# Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization) .
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system .
  - A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur . For example, flight control systems, nuclear power plants, etc.
  - A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail . For example, video streaming, online gaming, etc.
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities .
- A real-time system can have various applications in domains such as robotics, industrial automation, healthcare, aerospace, etc. .



# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or stimuli within a specified time interval, or risk severe consequences.
- A real time system can be classified into two types: hard real time and soft real time.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic failure or loss of life. For example, a nuclear reactor control system, a pacemaker, or an air traffic control system.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming service, a voice recognition system, or a multimedia application.
- A real time system consists of three main components: sensors, processors, and actuators.
- Sensors are devices that monitor the physical environment and generate events or stimuli for the system.
- Processors are devices that execute the software tasks or processes that respond to the events or stimuli.
- Actuators are devices that perform actions or outputs based on the results of the software tasks or processes.
- A real time system must satisfy two main requirements: functional correctness and temporal correctness.
- Functional correctness means that the system must produce the correct outputs for the given inputs.
- Temporal correctness means that the system must produce the outputs within the specified time constraints or deadlines.



# Typical Real Time Applications

- A real-time application (RTA) is an application that has strict time constraints on its performance and reliability.
- Real-time applications often interact with the physical world and require fast and accurate responses to external events.
- Some examples of real-time applications are:

  - **Video conferencing**: This application allows users to communicate with each other through video and audio streams over the internet. It requires low latency and high bandwidth to ensure smooth and synchronized communication. 
  - **Voice over Internet Protocol (VoIP)**: This application enables users to make phone calls over the internet using digital signals. It requires low jitter and packet loss to ensure clear and uninterrupted voice quality. 
  - **Online gaming**: This application allows users to play games with other players over the internet. It requires low latency and high throughput to ensure responsive and consistent gameplay. 
  - **Community storage applications**: These applications allow users to share and access data from distributed storage devices over the internet. They require high availability and consistency to ensure data integrity and security. 
  - **Some e-commerce applications**: These applications allow users to buy and sell goods and services over the internet. They require high scalability and reliability to handle large volumes of transactions and requests. 
  - **Real-time operating system (RTOS)**: This is a type of operating system that is designed to run real-time applications. It provides features such as preemptive scheduling, priority-based interrupts, and real-time memory management to ensure timely and predictable execution of tasks. 
  - **Instant messaging (IM) applications**: These applications allow users to send and receive text, voice, and video messages over the internet. They require low latency and high availability to ensure fast and reliable communication. 
  - **Team collaboration applications**: These applications allow users to work together on projects and tasks over the internet. They require high concurrency and synchronization to ensure accurate and up-to-date information sharing. 
  - **Digital control**: This is a type of real-time application that uses sensors and actuators to control physical processes and systems. It requires high precision and stability to ensure optimal performance and safety. Examples of digital control applications are industrial automation, robotics, and avionics.  
  - **Optimal control**: This is a type of real-time application that uses mathematical models and algorithms to optimize the performance and efficiency of physical processes and systems. It requires high computation and accuracy to ensure optimal solutions and trade-offs. Examples of optimal control applications are power management, traffic control, and smart grids. 
  - **Command and control**: This is a type of real-time application that uses sensors and actuators to monitor and control complex and dynamic environments. It requires high robustness and adaptability to ensure situational awareness and decision making. Examples of command and control applications are military operations, air traffic control, and emergency management. 
  - **Signal processing**: This is a type of real-time application that uses mathematical techniques and algorithms to analyze and manipulate signals such as sound, image, and video. It requires high speed and quality to ensure information extraction and enhancement. Examples of signal processing applications are speech recognition, image processing, and video compression. 
  - **Tracking**: This is a type of real-time application that uses sensors and algorithms to estimate and predict the position and motion of objects and entities. It requires high accuracy and reliability to ensure tracking performance and security. Examples of tracking applications are radar, GPS, and face recognition. 
  - **Real-time databases**: These are databases that store and process data that have temporal constraints and dependencies. They require high consistency and timeliness to ensure data validity and freshness. Examples of real-time databases are stock market databases, sensor network databases, and multimedia databases. 
  - **Multimedia**: These are applications that use multiple types of media such as text, audio, and video to convey information and entertainment. They require high bandwidth and synchronization to ensure media quality and interactivity. Examples of multimedia applications are web streaming, video conferencing, and virtual reality.



# Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events within a specified time interval, otherwise it may cause undesirable consequences or failure.
- A real time system consists of a set of tasks that have deadlines and priorities, and a scheduler that assigns the processor to the tasks according to some algorithm.
- A task is a unit of work that can be executed by the processor. A task can be periodic, aperiodic, or sporadic, depending on its arrival pattern.
- A periodic task is a task that arrives at regular intervals, such as every 10 milliseconds. A periodic task has a fixed period, which is the time between two consecutive arrivals, and a fixed execution time, which is the maximum time required to complete the task.
- An aperiodic task is a task that arrives at irregular intervals, such as a user input or a sensor reading. An aperiodic task has a variable inter-arrival time, which is the time between two consecutive arrivals, and a variable execution time, which is the maximum time required to complete the task.
- A sporadic task is a special case of an aperiodic task, where the inter-arrival time has a lower bound, such as at least 5 milliseconds. A sporadic task has a minimum inter-arrival time, which is the shortest time between two consecutive arrivals, and a variable execution time, which is the maximum time required to complete the task.
- A task has a release time, which is the time when the task becomes available for execution. For a periodic task, the release time is equal to the arrival time. For an aperiodic or sporadic task, the release time may be different from the arrival time, depending on the scheduling policy.
- A task has a deadline, which is the time by which the task must finish its execution. A deadline can be hard or soft, depending on the consequences of missing it. A hard deadline is a deadline that must be met, otherwise the system may fail or cause severe damage. A soft deadline is a deadline that can be missed, but with some degradation in the system performance or quality of service.
- A task has a priority, which is a value that indicates the importance or urgency of the task. A priority can be static or dynamic, depending on how it is assigned. A static priority is a priority that is fixed and does not change during the system execution. A dynamic priority is a priority that can vary and change during the system execution, depending on the scheduling algorithm or the task parameters.



# Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by the end of the week, i.e., by Friday, 17 March 2023.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in a clear and concise manner, using proper terminology and notation.
- The notes should include diagrams, tables, graphs, and equations wherever necessary to illustrate the concepts and methods.
- The notes should be formatted according to the guidelines given by the instructor, such as font size, margin, spacing, etc.
- The notes should be submitted in a PDF file, with the file name as "RTS_Unit1_Notes_YourName.pdf".
- The notes should be uploaded to the online platform specified by the instructor, before the deadline.
- The notes will be evaluated based on the following criteria:
  - Completeness and accuracy of the content
  - Organization and presentation of the material
  - Clarity and coherence of the language
  - Adherence to the format and style guidelines
- The notes will carry 10% of the total marks for the subject of Real Time System.



# Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System

- Timing constraints are a vital attribute in real-time systems.
- Timing constraints decide the total correctness of the result in real-time systems.
- The correctness of results in real-time system does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Every real-time system has a set of timing constraints that it has been designed to meet.
- If a system doesn't have timing constraints, it is not real-time.
- Timing constraints can be broken down into two categories:
  - Event response: The ability to react to external events within a specified time interval.
  - Task scheduling: The ability to execute a set of tasks within their deadlines and resource constraints.
- Timing constraints can be expressed using various constructs in requirements languages, such as:
  - Temporal operators: To specify the order, duration, frequency, and periodicity of events and tasks.
  - Logical operators: To specify the conditions, dependencies, and alternatives of events and tasks.
  - Quantifiers: To specify the number, range, and scope of events and tasks.
  - Variables: To specify the parameters, values, and states of events and tasks.
- Timing constraints can be validated using automatic test systems that can:
  - Measure the actual response time and execution time of events and tasks.
  - Compare the actual and expected results of events and tasks.
  - Check the compliance and consistency of timing constraints with the system specifications and requirements.
- Timing constraints are essential for real-time computing, which is the ability to produce the expected result by a specific deadline.
- Timing constraints also require time synchronization, which is the capability of agents to coordinate independent clocks and operate together in unison.



# Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- Examples of hard real time systems are air traffic control systems, nuclear power plant control systems, missile guidance systems, etc.  .
- Characteristics of hard real time systems are:
  - The size of data and tasks is usually small and fixed .
  - The response time is in milliseconds or microseconds .
  - The peak load performance should be predictable and consistent .
  - The safety is critical and the system must be reliable and fault-tolerant  .
  - The system must be able to handle concurrent events and interrupts .
  - The system must be able to communicate with other real time systems using protocols such as Time-Sensitive Networking (TSN) .



# Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a failure or a significant degradation of performance  .
- A soft real-time system has a **small window of time** for program completion rather than a precise moment due to a bit of jitter from the operating system.
- A soft real-time system can be run on **multiple cores** and impose fewer restrictions on applications.
- A soft real-time system can **miss some deadlines** occasionally acceptably with low probability.
- A soft real-time system can continue to function, though with **undesirable lower quality of output**.
- A soft real-time system is typically used to solve issues of **concurrent access** and the need to keep a number of **connected systems up-to-date** through changing situations.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video.
  - Online gaming.
  - Multimedia applications.



# Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements :
  - A workload model that specifies the applications supported by the system, such as tasks, jobs, parameters, deadlines, resource dependencies, etc.
  - A resource model that describes the resources available to the system, such as CPU, memory, network, sensors, actuators, etc., and their types and relations.
  - A system model that defines the policies and mechanisms used by the system to manage the workload and the resources, such as scheduling, synchronization, communication, fault tolerance, etc.
- An example of a reference model is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- A reference model can be used to compare and evaluate different real time systems, to identify the common and unique features, and to guide the design and implementation of new systems .



# Processors and Resources for Real Time System

- A real time system is a system that must respond to events or inputs within a specified time constraint, often called a deadline.
- Processors and resources are two important components of a real time system, as they affect the performance, reliability, and functionality of the system.
- Processors are also known as active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission links.
- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can use it at a time. Example: printer, disk, memory.
- Processors and resources can be classified into different types based on their characteristics and requirements. Some of the common types are:
  - Dedicated processors and resources: These are allocated to a single job or task and cannot be used by any other job or task. They provide high performance and predictability, but also high cost and low utilization. Example: a processor that runs a single real time application.
  - Shared processors and resources: These are available to multiple jobs or tasks and can be used by any of them based on some scheduling policy. They provide low cost and high utilization, but also low performance and unpredictability. Example: a processor that runs multiple applications, some of which are real time and some are not.
  - Preemptive processors and resources: These can be interrupted and taken away from a job or task by a higher priority job or task. They provide flexibility and responsiveness, but also overhead and complexity. Example: a processor that supports preemptive multitasking.
  - Non-preemptive processors and resources: These cannot be interrupted and taken away from a job or task by a higher priority job or task. They provide simplicity and stability, but also rigidity and delay. Example: a resource that requires mutual exclusion.
  - Time-sensitive processors and resources: These have strict timing requirements and must be accessed or used within a certain time window. They provide timeliness and accuracy, but also challenges and constraints. Example: a processor that supports time-coordinated computing (TCC) or time-sensitive networking (TSN) .
  - Time-insensitive processors and resources: These do not have strict timing requirements and can be accessed or used at any time. They provide flexibility and convenience, but also latency and uncertainty. Example: a processor that supports real time data processing.
- Processors and resources can also be categorized into different levels based on their location and function in a real time system. Some of the common levels are:
  - Cloud level: This is the highest level of processors and resources, where data is stored and processed in large-scale servers and data centers. This level provides high scalability and availability, but also high latency and cost. Example: a cloud service that performs real time analytics.
  - Edge level: This is the intermediate level of processors and resources, where data is stored and processed in local devices and networks. This level provides low latency and cost, but also low scalability and availability. Example: an edge device that performs real time computing .
  - Sensor level: This is the lowest level of processors and resources, where data is generated and collected by sensors and actuators. This level provides high accuracy and timeliness, but also high power consumption and complexity. Example: a sensor that monitors real time events.



# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time instant when the job becomes available for execution.
  - **Absolute deadline (d<sub>i</sub>)**: The time instant by which the job must finish its execution.
  - **Relative deadline (D<sub>i</sub>)**: The time interval between the release time and the absolute deadline of the job.
  - **Feasible interval ([r<sub>i</sub>, d<sub>i</sub>])**: The time interval during which the job can be executed by the system.
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from other parameters such as periodicity, frequency, or latency .
- The temporal parameters of a job can be used to determine its priority, schedulability, and performance in a real time system .



# Periodic Task Model

- A periodic task model is a deterministic workload model that describes many hard real-time applications .
- A periodic task is one that repeats itself after a fixed time interval.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > where:
  - Φi is the phase of the task, which is the time between the start of the system and the release of the first job of the task.
  - Pi is the period of the task, which is the time between two consecutive releases of the task's jobs.
  - ei is the worst-case execution time of the task, which is the maximum time required by any job of the task to complete on a given processor.
  - Di is the relative deadline of the task, which is the maximum time allowed for any job of the task to finish after its release.
- A periodic task is said to be feasible if there exists a schedule that meets all the deadlines of the task's jobs.
- A periodic task is said to be synchronous if all the tasks have zero phase, i.e., Φi = 0 for all i.
- A periodic task is said to be asynchronous if at least one task has a nonzero phase, i.e., Φi > 0 for some i.
- A periodic task model can be extended by adding a jitter Ji for each task Ti, which is the maximum deviation of the actual release time of a job from the exact start time of the period.
- A periodic task model can also be extended by adding a deadline monotonic priority Pi for each task Ti, which is a fixed priority assigned to the task based on its deadline, i.e., the shorter the deadline, the higher the priority.



# Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real-time systems.
- Precedence constraints are imposed by the logical or temporal dependencies among jobs, such as control flow or synchronization. For example, a job J1 may need to finish before another job J2 can start, or a job J3 may need to wait for a signal from another job J4.
- Data dependency is imposed by the communication or sharing of data among jobs, such as input/output or shared memory. For example, a job J5 may need to read the data produced by another job J6, or a job J7 may need to write to a shared variable accessed by another job J8.
- Precedence constraints and data dependency can be represented by a directed graph G = (J, <), where J is the set of jobs and < is the relation that indicates the order or dependency among jobs. This graph is called the precedence graph or the dependency graph.
- Precedence constraints and data dependency can affect the schedulability and feasibility of real-time systems, as they may introduce delays, conflicts, or deadlocks among jobs. Therefore, they need to be considered in the design and analysis of real-time systems.



# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or design time, and does not change at run time. Static scheduling is suitable for systems that have fixed and known tasks and resources, and that do not require flexibility or adaptability .
  - Dynamic scheduling is done at run time, and can change according to the system state and the arrival of new tasks. Dynamic scheduling is suitable for systems that have variable and unpredictable tasks and resources, and that require flexibility and adaptability .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently executing, and resume it later when the higher priority task is completed or blocked .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently executing, and waits until the lower priority task is completed or blocked before executing the higher priority task .
- Real time scheduling algorithms are the rules and methods that determine how to assign priorities and order tasks for execution in a real time system .
- Some examples of real time scheduling algorithms are:
  - Rate monotonic scheduling (RMS): a static and preemptive algorithm that assigns priorities to tasks based on their periods, such that the shorter the period, the higher the priority .
  - Deadline monotonic scheduling (DMS): a static and preemptive algorithm that assigns priorities to tasks based on their deadlines, such that the shorter the deadline, the higher the priority .
  - Earliest deadline first scheduling (EDF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their deadlines, such that the earliest the deadline, the higher the priority .
  - Least laxity first scheduling (LLF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their laxity, which is the difference between their deadline and their remaining execution time, such that the smaller the laxity, the higher the priority .
  - Fixed priority scheduling (FPS): a static and preemptive or non-preemptive algorithm that assigns fixed priorities to tasks based on some criteria, such as user preference, task importance, or task type .
  - Round robin scheduling (RR): a static and preemptive or non-preemptive algorithm that assigns equal priorities to tasks and executes them in a circular order for a fixed time slice or quantum .
- Real time scheduling analysis is the process of verifying and validating the correctness and feasibility of a real time scheduling algorithm for a given system and task set .
- Real time scheduling analysis can be done using different methods, such as:
  - Utilization bound test: a sufficient but not necessary condition that checks if the total utilization of the tasks is less than or equal to a certain bound, depending on the algorithm and the number of tasks .
  - Response time analysis: a method that calculates the worst-case response time of each task, which is the time from its arrival to its completion, and compares it with its deadline .
  - Simulation: a method that models the system and the tasks and executes them using the algorithm, and observes the results and the performance .
- Real time scheduling tools are software applications that help users to create, manage, and analyze real time schedules for different systems and tasks .
- Some examples of real time scheduling tools are:
  - Sinnaps: a cloud-based project management tool that supports real time scheduling and collaboration for complex and dynamic projects.
  - Calendly: a free online appointment scheduling tool that allows users



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning tasks to processors or resources in a way that meets the timing constraints of the system. Real time systems are those whose correctness depends on both the functionality and the timing of the tasks. There are different approaches to real time scheduling, depending on the characteristics and requirements of the system. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, period, etc., are known at design time. In this approach, a schedule is computed offline and stored in a table. The table specifies which task to execute at each time instant. A timer or a clock triggers the execution of the tasks according to the table. This approach is simple, predictable, and easy to implement, but it has some drawbacks, such as lack of flexibility, poor resource utilization, and difficulty in handling aperiodic or sporadic tasks  .

- **Round-robin approach**: This approach is a commonly used technique in time-shared systems. It is based on allocating a fixed time slice or quantum to each task in a circular order. The tasks are scheduled in a repetitive manner, and each task gets a chance to execute for a quantum. If a task finishes before its quantum expires, it relinquishes the processor. If a task does not finish within its quantum, it is preempted and moved to the end of the queue. This approach is fair, simple, and easy to implement, but it does not consider the timing constraints or the priorities of the tasks. It may result in poor response time, missed deadlines, and low throughput .

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where each task is assigned a weight that reflects its relative importance or priority. The weight determines the length of the quantum that the task receives. A task with a higher weight gets a longer quantum than a task with a lower weight. This approach tries to balance the fairness and the priority of the tasks, but it still does not guarantee the satisfaction of the timing constraints. It may also suffer from high overhead and context switching cost .

- **Priority-driven approach**: This approach is based on assigning a priority to each task, and scheduling the tasks according to their priorities. The task with the highest priority gets the processor, and preempts any lower priority task that is currently executing. The priority of a task can be static or dynamic, depending on whether it is fixed or changes over time. Static priorities are usually assigned based on the characteristics of the tasks, such as period, deadline, criticality, etc. Dynamic priorities are usually computed based on the current state of the system, such as the remaining execution time, the deadline, the slack, etc. This approach is more flexible, adaptable, and efficient than the previous approaches, but it requires more complex algorithms and mechanisms to determine and manage the priorities. It also faces some challenges, such as priority inversion, deadline misses, and resource contention   .

Some examples of priority-driven scheduling algorithms are:

- **Rate-monotonic scheduling (RMS)**: This is a static priority scheduling algorithm, where the priority of a task is inversely proportional to its period. The task with the shortest period has the highest priority, and the task with the longest period has the lowest priority. This algorithm is optimal for preemptive scheduling of periodic tasks with implicit deadlines (equal to their periods) and fixed execution times. It guarantees that all the tasks will meet their deadlines if the total utilization of the system is less than or equal to a certain bound .

- **Deadline-monotonic scheduling (DMS)**: This is a static priority scheduling algorithm, where the priority of a task is inversely proportional to its relative deadline. The task with the shortest deadline has the highest priority, and the task with the longest deadline has the lowest priority. This algorithm is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines and fixed execution times. It guarantees that all the tasks will meet their deadlines if the total utilization of the system is less than or equal to 100% .

- **Earliest-deadline-first scheduling (EDF)**: This is a dynamic priority scheduling algorithm, where the



# Clock Driven Approach

- Clock driven approach is a scheduling method for hard real-time systems that require predictable and deterministic behaviour.
- In clock driven approach, the system executes tasks according to a predetermined schedule, which is computed offline before the system starts  .
- The schedule is based on the known parameters of the tasks, such as their periods, deadlines, execution times, and resource requirements .
- The schedule is usually cyclic, meaning that it repeats itself after a fixed amount of time, called the cycle or frame .
- The schedule specifies at which time instants, called scheduling points, the system should switch from one task to another  .
- The scheduling points are determined by the interrupts received from a clock, hence the name clock driven.
- The advantages of clock driven approach are:
  - It guarantees that all tasks will meet their deadlines, as long as the schedule is feasible .
  - It avoids the overhead of dynamic scheduling decisions at runtime, which can be significant for hard real-time systems .
  - It simplifies the analysis and verification of the system's timing behaviour .
- The disadvantages of clock driven approach are:
  - It requires that all the task parameters are known and fixed in advance, which may not be realistic for some applications .
  - It may not be able to handle sporadic or aperiodic tasks, which have unpredictable arrival times or deadlines .
  - It may not be able to adapt to changes in the system's state or environment, such as faults, failures, or resource variations .
  - It may waste processor time and energy by executing tasks that are not necessary or urgent .



# Weighted Round Robin Approach

- The weighted round robin approach is a generalization of the round robin approach for scheduling real-time tasks or traffic.
- In the round robin approach, each ready task is given an equal share of the processor for a fixed time quantum.
- In the weighted round robin approach, each ready task is given a fixed number of time quanta based on its weight, which reflects its priority or importance .
- The weight of a task can be determined by various factors, such as its deadline, its arrival rate, its resource requirements, or its service level agreement.
- The weighted round robin approach can achieve better performance and fairness than the round robin approach, especially for tasks with different weights.
- The weighted round robin approach can also be used for scheduling real-time traffic in high-speed switched networks, where different packets or flows may have different weights based on their quality of service requirements .
- The advantages of the weighted round robin approach are:
  - It is simple and easy to implement.
  - It does not require preemption or context switching.
  - It can handle tasks or traffic with variable arrival rates and service times.
  - It can provide proportional allocation of the processor or bandwidth to different tasks or traffic.
- The disadvantages of the weighted round robin approach are:
  - It may not be optimal for tasks or traffic with strict deadlines or jitter constraints.
  - It may introduce unnecessary delay or overhead for tasks or traffic with low weights.
  - It may not be scalable or efficient for a large number of tasks or traffic with different weights.



# Priority Driven Approach

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
- However, priority-driven scheduling also faces some challenges in ROS 2, such as the lack of a unified priority model, the heterogeneity of hardware platforms, and the complexity of the middleware layer.



# Dynamic Versus Static Systems

- A **static system** is a system that has a fixed set of tasks and a predefined schedule for executing them. A static system does not change its behavior or structure in response to external events or inputs. A static system can be validated before execution and can guarantee the timing constraints of the tasks. A static system is suitable for hard real-time systems that require deterministic and predictable behavior. A static system may provide poor performance in terms of overall response time and resource utilization. A static system may not be able to handle dynamic changes in the workload or the environment. A static system may be difficult to design and maintain.   

- A **dynamic system** is a system that has a variable set of tasks and a flexible schedule for executing them. A dynamic system can adapt its behavior or structure in response to external events or inputs. A dynamic system cannot be validated before execution and may not guarantee the timing constraints of the tasks. A dynamic system is suitable for soft real-time systems that require adaptive and responsive behavior. A dynamic system may provide better performance in terms of overall response time and resource utilization. A dynamic system may be able to handle dynamic changes in the workload or the environment. A dynamic system may be easier to design and maintain.   

- A **real-time scheduling** algorithm is an algorithm that assigns tasks to processors or resources in a real-time system. A real-time scheduling algorithm can be classified as static or dynamic. A static scheduling algorithm determines the task priorities and the task order before the system runs. A dynamic scheduling algorithm determines the task priorities and the task order as the system runs. A static scheduling algorithm is faster and simpler than a dynamic scheduling algorithm, but it is less flexible and adaptable. A dynamic scheduling algorithm is slower and more complex than a static scheduling algorithm, but it is more flexible and adaptable.    

- A **centralized scheduling** algorithm is a scheduling algorithm that makes all the scheduling decisions at one central site or processor. A centralized scheduling algorithm is easier to implement and coordinate, but it may introduce a single point of failure and a communication bottleneck. A **distributed scheduling** algorithm is a scheduling algorithm that makes the scheduling decisions at multiple sites or processors. A distributed scheduling algorithm is harder to implement and coordinate, but it may improve the reliability and scalability of the system. A centralized scheduling algorithm can be static or dynamic, but a distributed scheduling algorithm is usually dynamic.



# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A deadline is the time by which a task must finish its execution, and a slack is the difference between the deadline and the remaining execution time of a task.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, that is, a schedule that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as well as for non-preemptive scheduling of periodic tasks with implicit deadlines (equal to their periods).
- LST is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines and constrained deadlines (less than or equal to their periods), as well as for non-preemptive scheduling of periodic tasks with implicit deadlines.
- EDF and LST may not be optimal for other types of tasks, such as aperiodic tasks, tasks with precedence constraints, tasks with resource sharing, or tasks with variable execution times.
- EDF and LST may also have some drawbacks, such as high overhead, poor response time, low utilization, and deadline misses in overload scenarios.
- EDF and LST can be combined or modified to enhance their performance and overcome their limitations, such as using slack stealing, slack reclamation, or hybrid algorithms.



# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is feasible (i.e., that can be scheduled by some algorithm)  .
- RMA has a simple schedulability test that can determine if a set of periodic tasks is feasible or not. The test is based on the utilization factor of the tasks, which is the ratio of the execution time to the period of each task  .
- The schedulability test for RMA is:

  - For n tasks, the utilization factor of each task is Ui = Ci / Ti, where Ci is the execution time and Ti is the period of task i.
  - The total utilization factor of the system is U = sum of Ui for i = 1 to n.
  - The system is schedulable by RMA if U <= n * (2^(1/n) - 1), which is the utilization bound for RMA  .

- RMA has some advantages and disadvantages as a real-time scheduling algorithm. Some of them are:

  - Advantages:
    - Simple and easy to implement.
    - Optimal for periodic tasks.
    - Low overhead and predictable behavior.
    - Suitable for hard real-time systems that require guaranteed deadlines  .
  - Disadvantages:
    - Not optimal for aperiodic or sporadic tasks.
    - Not suitable for systems with dynamic priorities or varying execution times.
    - May cause priority inversion, which is a situation where a low priority task holds a shared resource that a high priority task needs, and the high priority task is blocked by a medium priority task that does not need the resource  .



# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, priority, and resource requirement of all tasks for all time .
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system . The scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task .
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way. However, offline scheduling has the disadvantage of being inflexible and impractical, as the scheduler cannot handle any changes or uncertainties in the system, such as task arrival, execution time, or resource availability.
- Online scheduling has the advantage of being adaptive and responsive, as the scheduler can react to the dynamic behavior of the system and adjust the schedule accordingly. However, online scheduling has the disadvantage of being suboptimal and unpredictable, as the scheduler may not be able to meet the deadlines of all the tasks or guarantee the quality of service.
- Online scheduling can be further classified into static and dynamic scheduling. Static scheduling is a type of online scheduling that assigns a fixed priority to each task and schedules the tasks according to their priorities. Dynamic scheduling is a type of online scheduling that assigns a variable priority to each task and schedules the tasks according to their current priorities.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling. Examples of online scheduling algorithms are rate-monotonic scheduling, earliest deadline first scheduling, and least laxity first scheduling.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have random arrival times and no deadlines. Sporadic jobs are jobs that have random arrival times and hard deadlines.
- Priority driven systems are systems that assign priorities to jobs and schedule them according to their priorities. Clock driven systems are systems that schedule jobs according to a predefined table that is based on the system clock.
- Scheduling aperiodic and sporadic jobs in priority driven systems can be done by using one of the following methods:
  - Background scheduling: Aperiodic and sporadic jobs are executed only when there are no periodic jobs ready to run. This method guarantees that periodic jobs meet their deadlines, but it may result in long response times for aperiodic and sporadic jobs.
  - Polling servers: A periodic task is created to serve aperiodic and sporadic jobs. The server task has a fixed priority and a fixed budget of execution time per period. When the server task is executed, it checks if there are any aperiodic or sporadic jobs in the queue and executes them until the budget is exhausted or the queue is empty. This method reduces the response times of aperiodic and sporadic jobs, but it may cause deadline misses for periodic jobs if the server priority is too high or the server budget is too large.
  - Deferrable servers: A periodic task is created to serve aperiodic and sporadic jobs. The server task has a fixed priority and a fixed budget of execution time per period. However, unlike the polling server, the server task can defer its execution until there are aperiodic or sporadic jobs in the queue. This method improves the utilization of the server budget and reduces the interference of the server task on periodic tasks, but it may still cause deadline misses for periodic jobs if the server priority is too high or the server budget is too large.
  - Sporadic servers: A periodic task is created to serve sporadic jobs. The server task has a fixed priority and a variable budget of execution time per period. The budget is replenished whenever a sporadic job arrives, up to a maximum value. The server task executes sporadic jobs until the budget is exhausted or the queue is empty. This method adapts to the arrival rate of sporadic jobs and reduces the response times of sporadic jobs, but it may cause deadline misses for periodic jobs if the server priority is too high or the maximum budget is too large.
  - Slack stealing: Aperiodic and sporadic jobs are executed by stealing the slack time of periodic and sporadic jobs. The slack time of a job is the amount of time that the job can be delayed without causing a deadline miss. A slack stealing algorithm monitors the slack time of all jobs in the system and schedules aperiodic and sporadic jobs whenever there is enough slack time available. This method maximizes the utilization of the system and minimizes the response times of aperiodic and sporadic jobs, but it requires accurate estimation of the execution times and deadlines of all jobs in the system.
- Scheduling aperiodic and sporadic jobs in clock driven systems can be done by using one of the following methods:
  - Offline scheduling: Aperiodic and sporadic jobs are scheduled offline along with periodic jobs, based on their worst-case arrival times and execution times. The resulting schedule is stored in a table and executed by the system clock. This method guarantees that all jobs meet their deadlines, but it requires a priori knowledge of the arrival times and execution times of all jobs in the system and it may result in low utilization of the system.
  - Online scheduling: Aperiodic and sporadic jobs are scheduled online along with periodic jobs, based on their actual arrival times and execution times. The system clock executes the periodic jobs according to a predefined table, but it can switch to aperiodic or sporadic jobs whenever they arrive, if they have higher priority than the current periodic job. This method allows for dynamic adaptation to the arrival times and execution times of aperiodic and sporadic jobs, but it may cause deadline misses for periodic jobs if the aperiodic or sporadic jobs have higher priority than the periodic jobs.



## Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, or network bandwidth, available to multiple users or processes.

Resource sharing can have several benefits, such as:

- Improving the efficiency and utilization of the system resources
- Reducing the cost and complexity of the system administration
- Enhancing the scalability and reliability of the system
- Enabling the collaboration and communication among the users or processes

Resource sharing can also pose some challenges, such as:

- Managing the access and allocation of the shared resources
- Ensuring the security and privacy of the shared resources
- Handling the conflicts and contention among the users or processes
- Dealing with the heterogeneity and compatibility of the system components

Resource sharing can be implemented at different levels of the system architecture, such as:

- Hardware level: The physical resources of the system, such as CPU, memory, disk, or printer, are shared by using techniques such as multiprogramming, virtualization, or spooling.
- Software level: The logical resources of the system, such as files, databases, or applications, are shared by using techniques such as file systems, distributed databases, or middleware.
- Network level: The network resources of the system, such as bandwidth, routers, or servers, are shared by using techniques such as packet switching, routing protocols, or load balancing.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for a resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource. This may cause blocking or priority inversion, but it avoids timing anomalies and deadlock.
  - Preemptive RAC means that a task can be preempted by another task even if it holds a resource, but the resource is not released until the preempted task resumes. This may cause timing anomalies or deadlock, but it avoids blocking and priority inversion.
- Some examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc.
  - Preemptive RAC: Wait-Free Protocol (WFP), Abort-and-Restart Protocol (ARP), etc.



# Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access of shared resources in real time systems  .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- NPCS has the following properties:
  - It is simple and easy to implement .
  - It prevents deadlock, since no job is ever preempted when it holds any resource  .
  - It preserves the feasibility of the system, since the priority inversion is bounded by the length of the critical section .
  - It may cause blocking, since a lower priority job may hold a resource that a higher priority job needs .
  - It may cause priority inversion, since a higher priority job may be blocked by a lower priority job that holds a resource .
  - It may cause resource underutilization, since a job may hold a resource longer than necessary .
- NPCS can be improved by using priority inheritance or priority ceiling protocols, which reduce the blocking and priority inversion .



# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Real-time systems are systems that have strict timing constraints and must respond to events within a specified deadline.
- Resource access control is the problem of ensuring that concurrent tasks do not interfere with each other when accessing shared resources, such as memory, devices, or semaphores.
- Interference can cause priority inversion, which is a situation where a higher-priority task is blocked by a lower-priority task that holds a resource needed by the higher-priority task.
- Priority inversion can lead to missed deadlines, reduced performance, and even deadlock in real-time systems.

## Priority-Inheritance Protocol

- The priority-inheritance protocol (PIP) is a method for eliminating unbounded priority inversion by temporarily raising the priority of a task that holds a resource needed by a higher-priority task.
- The basic idea of PIP is that when a higher-priority task requests a resource that is locked by a lower-priority task, the lower-priority task inherits the priority of the higher-priority task until it releases the resource.
- This way, the lower-priority task can finish its critical section faster and unblock the higher-priority task, reducing the blocking time and avoiding deadlock.
- PIP has the following properties:
  - A task can be blocked by at most one lower-priority task at a time.
  - The blocking time of a task is bounded by the longest critical section of any lower-priority task.
  - A task can inherit multiple priorities if it holds multiple resources that are requested by multiple higher-priority tasks.
  - A task can release its resources in any order, regardless of the order of acquisition.

## Priority-Ceiling Protocol

- The priority-ceiling protocol (PCP) is a method for minimizing the blocking time of a task to at most one critical section of a lower-priority task, and preventing deadlock and unnecessary blocking.
- The basic idea of PCP is that each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource. A task can only lock a resource if its priority is higher than the priority ceiling of all the resources currently locked by other tasks.
- This way, a task can avoid being blocked by a lower-priority task that does not hold the requested resource, and also avoid creating a circular dependency of resource requests that can cause deadlock.
- PCP has the following properties:
  - A task can be blocked by at most one lower-priority task at a time.
  - The blocking time of a task is bounded by the shortest critical section of any lower-priority task.
  - A task can inherit only one priority, which is the highest priority ceiling of all the resources it holds.
  - A task must release its resources in the reverse order of acquisition.

## Differences between PIP and PCP

- PIP is greedy, while PCP is not. PIP allows a task to lock a resource whenever the resource is free, while PCP may deny a task access to a free resource if its priority is lower than the priority ceiling of another locked resource.
- PCP is more restrictive, but also more predictable than PIP. PCP prevents unnecessary blocking and deadlock, but also imposes a fixed order of resource acquisition and release, while PIP allows more flexibility, but also more uncertainty in resource access control.
- PCP requires a priori knowledge of the resource usage of each task, while PIP does not. PCP needs to assign a priority ceiling to each resource based on the highest priority of any task that can access it, while PIP does not need any information about the resource usage of the tasks.



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use at the time.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered to the highest priority ceiling of the remaining locked resources.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock.
  - It reduces the blocking time of high-priority tasks by allowing them to preempt lower-priority tasks that are using resources.
  - It simplifies the analysis of the worst-case response time of tasks by bounding the blocking time to the maximum execution time of any lower-priority task that can lock a resource.
  - It reduces the memory requirement by allowing tasks to share a common stack.



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no deadlock can occur.
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

| Task | Period | Execution Time | Resource |
| --- | --- | --- | --- |
| T1 | 2 | 0.9 | X |
| T2 | 5 | 2.3 | Y |

- The priority of T1 is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority of T2 is 2 from time 0 to 5 and becomes 1 from time 5 to 10 and so on.
- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 10 and so on.
- The system ceiling is 0 initially and changes according to the resource locks and releases.
- The execution of the tasks with the priority ceiling protocol is shown below:

| Time | Task | Resource | System Ceiling |
| --- | --- | --- | --- |
| 0 | T1 starts | - | 0 |
| 0.1 | T1 locks X | X | 1 |
| 0.5 | T2 starts | - | 1 |
| 0.9 | T1 releases X | - | 0 |
| 0.9 | T1 finishes | - | 0 |
| 2 | T1 starts | - | 0 |
| 2.1 | T1 locks X | X | 1 |
| 2.3 | T2 finishes | - | 1 |
| 2.9 | T1 releases X | - | 0 |
| 2.9 | T1 finishes | - | 0 |
| 4 | T1 starts | - | 0 |
| 4.1 | T1 locks X | X | 2 |
| 4.9 | T1 releases X | - | 0 |
| 4.9 | T1 finishes | - | 0 |
| 5 | T2 starts | - | 0 |
| 5.1 | T2 locks Y | Y | 1 |
| 7.4 | T2 releases Y | - | 0 |
| 7.4 | T2 finishes | - | 0 |
| 8 | T1 starts | - | 0 |
| 8.1 | T1 locks X | X | 2 |
| 8.9 | T1 releases X | - | 0 |
| 8.9 | T1 finishes | - | 0 |
| 10 | T2 starts | - | 0 |
| 10.1 | T2 locks Y | Y | 1 |
| 12.4 | T2 releases Y | - | 0 |
| 12.4 | T2 finishes | - | 0 |

- As we can see, the priority ceiling protocol ensures that T1 is not blocked by T2 when it needs X, and that



# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems to avoid unbounded priority inversion and mutual deadlock.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is boosted to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better responsiveness than static preemption ceiling protocol, but it requires more memory and complex data structures.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can improve the schedulability, reduce the context switches, and decrease the memory requirements of fixed priority systems.
- However, PTS may lead to long priority inversion and inconsistent object states in object-oriented real-time systems, which require synchronization considerations.
- To solve this problem, a dual ceiling protocol can be used, which combines the advantages of PTS and preemption ceiling protocol.
- Dual ceiling protocol assigns two ceiling priorities to each resource: a preemption ceiling and a blocking ceiling.
- A task can lock a resource only if its priority is higher than the blocking ceiling of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is boosted to the preemption ceiling of that resource, and it cannot be preempted by any task whose priority is lower than its threshold priority.
- Dual ceiling protocol ensures that a task can be blocked by at most one lower-priority task, that deadlock is impossible, and that object states are consistent.
- Dual ceiling protocol can achieve better performance and scalability than preemption ceiling protocol and PTS alone.



# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that have more than one unit of the same type, such as printers, disks, or CPUs.
- Access control in multiple-unit resources is the problem of ensuring that jobs that need to use one or more units of a resource can do so without violating the timing constraints of themselves or other jobs.
- Access control in multiple-unit resources is more complex than in single-unit resources, because there may be different ways of allocating the units to the jobs, and different policies for resolving conflicts and blocking.
- Some of the challenges and trade-offs in access control in multiple-unit resources are:
  - How to allocate the units to the jobs: statically or dynamically, based on priority or demand, with or without preemption, etc.
  - How to handle blocking: when a job cannot get all the units it needs, should it wait, release some units, or abort?
  - How to handle deadlock: when two or more jobs are waiting for each other's units, how to detect and resolve the deadlock?
  - How to analyze the worst-case response time and schedulability of the jobs: what are the assumptions and bounds on the resource usage and blocking behavior?
- Some of the existing protocols and algorithms for access control in multiple-unit resources are:
  - Priority inheritance protocol (PIP): a job inherits the highest priority of the jobs waiting for its units, and releases all its units when it finishes its critical section.
  - Priority ceiling protocol (PCP): a job can lock a resource only if its priority is higher than the ceiling of the resource, which is the highest priority of any job that may lock the resource.
  - Preemption ceiling protocol (PRCP): a job can preempt another job only if its priority is higher than the ceiling of the resource that the preempted job is using.
  - Maximum urgency first (MUF): a job is assigned a dynamic priority based on its deadline and the number of units it needs, and the units are allocated to the highest priority job.
  - Banker's algorithm: a job declares its maximum demand for each resource in advance, and the system grants the units only if the resulting state is safe, i.e., there is a way to finish all the jobs without deadlock.



# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real-time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timeliness.
- Concurrency control algorithms for real-time systems can be classified into two categories: pessimistic and optimistic.
- Pessimistic algorithms prevent conflicts from occurring by enforcing mutual exclusion or serialization among conflicting accesses. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
- Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- The choice of concurrency control algorithm depends on the characteristics of the system, such as the degree of data contention, the number of data objects, the size of transactions, the deadline requirements, and the system overhead.



## Unit 4 - Real Time Communication

Real time communication is the exchange of information between two or more parties without any significant delay. It allows the parties to interact with each other in a natural and spontaneous way, as if they were in the same physical location. Real time communication can be synchronous or asynchronous, depending on whether the parties are available at the same time or not.

Some examples of real time communication are:

- Voice calls: The parties can talk to each other using their voice over a phone line, a computer network, or a wireless connection. Voice calls can be one-to-one or one-to-many, depending on the number of participants. Voice calls can also be integrated with other media, such as video or text, to create a richer communication experience.
- Video calls: The parties can see each other's face and body language, as well as hear their voice, over a video link. Video calls can be one-to-one or one-to-many, depending on the number of participants and the bandwidth available. Video calls can also be integrated with other media, such as text or graphics, to create a more interactive communication experience.
- Text chat: The parties can send and receive short text messages to each other over a computer network or a wireless connection. Text chat can be one-to-one or one-to-many, depending on the number of participants and the platform used. Text chat can also be integrated with other media, such as voice, video, or images, to create a more expressive communication experience.
- Instant messaging: The parties can send and receive text messages, as well as other media, such as voice, video, images, or files, to each other over a computer network or a wireless connection. Instant messaging can be one-to-one or one-to-many, depending on the number of participants and the platform used. Instant messaging can also support features such as presence, status, emoticons, stickers, or encryption, to create a more personalized and secure communication experience.
- Social media: The parties can share and consume content, such as text, images, videos, or links, with each other over a computer network or a wireless connection. Social media can be one-to-one or one-to-many, depending on the number of participants and the platform used. Social media can also support features such as likes, comments, reactions, hashtags, or groups, to create a more engaging and social communication experience.

Some benefits of real time communication are:

- It can reduce the time and cost of travel, as the parties can communicate with each other from anywhere and anytime.
- It can improve the quality and efficiency of communication, as the parties can use multiple media and modes to convey their message and feedback.
- It can enhance the relationship and trust between the parties, as they can see and hear each other's emotions and expressions.
- It can increase the collaboration and creativity between the parties, as they can share and co-create content and ideas in real time.

Some challenges of real time communication are:

- It can require high bandwidth and low latency, as the parties need to transmit and receive large amounts of data in real time.
- It can depend on the availability and compatibility of the devices, software, and platforms, as the parties need to use the same or compatible tools and standards to communicate with each other.
- It can pose privacy and security risks, as the parties need to protect their data and identity from unauthorized access or misuse.
- It can cause communication overload and fatigue, as the parties need to manage and respond to multiple and constant streams of information and interaction.



# Basic Concepts in Real Time Communication

Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Remote control and teleoperation

Some basic concepts in real time communication are:

- Bandwidth: The amount of data that can be transmitted or received per unit of time. It is usually measured in bits per second (bps) or megabits per second (Mbps). Bandwidth affects the quality and speed of RTC.
- Latency: The time it takes for a signal to travel from the source to the destination and back. It is usually measured in milliseconds (ms) or seconds. Latency affects the responsiveness and synchronicity of RTC.
- Jitter: The variation in latency over time. It is caused by network congestion, packet loss, or other factors. Jitter affects the smoothness and continuity of RTC.
- Packet loss: The percentage of data packets that are lost or corrupted during transmission. It is caused by network errors, interference, or congestion. Packet loss affects the reliability and quality of RTC.
- Quality of service (QoS): The ability of a network to provide different levels of priority and performance to different types of traffic. QoS can help improve the quality and efficiency of RTC by allocating more bandwidth, reducing latency, jitter, and packet loss for time-sensitive applications.
- Encryption: The process of transforming data into an unreadable form to protect it from unauthorized access or modification. Encryption can help enhance the security and privacy of RTC by preventing eavesdropping, tampering, or spoofing.
- Codec: The software or hardware that compresses and decompresses data for transmission or storage. Codec can help optimize the bandwidth and quality of RTC by reducing the size of data without compromising the fidelity.
- Protocol: The set of rules and standards that govern the format and exchange of data between devices or applications. Protocol can help facilitate the interoperability and compatibility of RTC by defining the syntax, semantics, and procedures of communication.



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities with strict timing constraints.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT) .
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- Hard real-time communication systems are deterministic in nature, meaning that they guarantee that the communication will be completed within a specified deadline .
- Soft real-time communication systems are probabilistic, meaning that they do not guarantee that the communication will be completed within a specified deadline, but they try to achieve it with a high probability .
- Examples of hard real-time communication systems are:
  - Air traffic control systems
  - Nuclear power plant control systems
  - Missile guidance systems
- Examples of soft real-time communication systems are:
  - Video conferencing systems
  - Online gaming systems
  - Multimedia streaming systems
- The design of real-time communication systems involves several challenges, such as:
  - Synchronizing the clocks of different entities
  - Managing the network resources and bandwidth
  - Handling the errors and faults in the communication
  - Ensuring the security and privacy of the communication
- Some of the techniques and protocols used for real-time communication systems are:
  - Time-division multiplexing (TDM)
  - Priority-based scheduling
  - Real-time transport protocol (RTP)
  - Real-time control protocol (RTCP)
  - Real-time publish-subscribe (RTPS) protocol
- Real-time communication systems are widely used in various domains, such as:
  - Industrial automation
  - Robotics
  - Healthcare
  - Smart grids
  - Internet of Things (IoT)



# Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination.
- Examples of real time communication include voice calls, video conferencing, instant messaging, and VoIP .
- Real time communication has many advantages, such as improving collaboration, productivity, customer service, and innovation.
- Real time communication also has some challenges, such as ensuring security, reliability, scalability, and interoperability.
- A model of real time communication consists of the following components:
  - Sources and destinations: the end users of the communication system, who generate and receive messages.
  - Hosts: the devices that host the sources and destinations, such as computers, smartphones, or servers.
  - Network interfaces: the hardware and software components that connect the hosts to the network, such as network cards, routers, or switches.
  - Input and output queues: the buffers that store the incoming and outgoing messages at the network interfaces, before and after transmission.
  - Network: the medium that carries the messages from one network interface to another, such as wired or wireless links, or the internet.
- A model of real time communication also involves the following parameters:
  - Traffic: the stream of messages that are generated by the sources and delivered to the destinations, which can be periodic, aperiodic, or sporadic.
  - Throughput: the rate at which the messages are successfully transmitted and received, measured in bits per second or messages per second.
  - Delay: the time elapsed between the generation of a message by the source and its delivery to the destination, measured in seconds or milliseconds.
  - Jitter: the variation in the delay of the messages, caused by factors such as network congestion, packet loss, or reordering, measured in seconds or milliseconds.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) is a simple and fair priority-based service discipline that assigns a weight to each queue and serves them in a circular order, proportional to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue.
- WRR can guarantee the minimum bandwidth for each queue, but it cannot guarantee the delay jitter bound or satisfy diverse delay requirements.
- To overcome the limitations of WRR, some variations have been proposed, such as weighted fair queuing (WFQ), probabilistic priority (PP), rate-controlled frame-based WRR (RFWRR), class-based WFQ (CBWFQ) and weighted fair priority queuing (WFPQ).
- WFQ assigns a weight and a finish time to each packet and serves them in the order of increasing finish times. WFQ can provide fairness and delay guarantees, but it requires complex computations and sorting.
- PP is a hybrid of SP and WFQ, where each queue is assigned a weight and a priority, and the server polls the queues according to their priority and serves them with a probability proportional to their weight. PP can achieve a trade-off between fairness and priority, but it may introduce additional delay and jitter.
- RFWRR is an extension of WRR that divides the scheduler into a rate controller and a frame-based WRR server. The rate controller adjusts the weights of the queues according to their delay requirements, and the frame-based WRR server serves the queues in a fixed frame size. RFWRR can guarantee the delay jitter bound and satisfy diverse delay requirements, but it may cause unfairness and underutilization.
- CBWFQ and WFPQ are class-based service disciplines that group the queues into different classes and apply WFQ or WRR within each class. CBWFQ and WFPQ can provide different levels of service for different classes, but they may suffer from the same drawbacks as WFQ or WRR.



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission from one node can reach all other nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but suffer from collisions and low efficiency.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as token passing or polling. These protocols are reliable and fair, but introduce overhead and delay.
- Reservation-based protocols use a separate control channel or a dedicated time slot to reserve the access to the data channel, such as TDMA or CDMA. These protocols can provide guaranteed performance and quality of service, but require synchronization and coordination among nodes.
- Some MAC protocols combine different access strategies to achieve a trade-off between performance and complexity, such as ABROAD, which incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay .
- MAC protocols for broadcast networks need to consider the characteristics and requirements of the network, such as the number of nodes, the traffic pattern, the channel quality, the network topology, the power consumption, and the real-time constraints.



# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different quality of service (QoS) requirements, such as bandwidth, delay, jitter, and reliability.
- Resource reservation protocols are network protocols that enable Internet applications to request and obtain specific QoS guarantees from the network for their data flows.
- Resource reservation protocols can be classified into two categories: integrated services (IntServ) and differentiated services (DiffServ).
- IntServ is a QoS model that provides end-to-end QoS guarantees by reserving resources along the path of a data flow using a signaling protocol such as RSVP (Resource Reservation Protocol).
- RSVP is a transport layer protocol that allows a receiver to initiate and maintain resource reservations for a multicast or unicast data flow. RSVP uses PATH and RESV messages to exchange QoS parameters and reserve resources between the sender and the receiver.
- DiffServ is a QoS model that provides QoS differentiation by marking packets with different priority levels using a field called DSCP (Differentiated Services Code Point) in the IP header. DiffServ does not require signaling or reservation, but relies on the network devices to apply different QoS policies based on the DSCP value of each packet.
- DiffServ can be combined with RSVP to provide end-to-end QoS guarantees for selected data flows, while providing QoS differentiation for the rest of the traffic. This is called RSVP over DiffServ or DiffServ-aware RSVP.



# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed to optimize the average performance and resource utilization, but not the worst-case performance or predictability.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to run multiple tasks or threads concurrently, each with its own priority and scheduling policy.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between threads, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, etc.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to protect the memory regions of different threads from each other.
  - Interrupt handling: The ability to respond to external events, such as hardware interrupts or software exceptions, in a timely and deterministic manner.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, network interfaces, etc., using standard or custom protocols.
  - System services: The ability to provide common functionalities, such as file systems, networking, timers, logging, etc., to the application threads.
- Some examples of RTOS are Azure RTOS, FreeRTOS, VxWorks, QNX, etc.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive.
- A RTDB is different from a conventional database, which is designed to store and process data that is persistent and changes much less frequently.
- A RTDB typically has the following attributes:
  - Live data: The data in a RTDB is continuously updated by external sources, such as sensors, devices, or users, and reflects the current state of the real world.
  - Time constraints: The data in a RTDB has associated deadlines or validity intervals, which specify how long the data is relevant or useful for the application.
  - Predictable performance: The RTDB is able to write and/or read data within a strict performance envelope, usually defined on the order of seconds to milliseconds.
  - High availability: The RTDB is able to tolerate failures and maintain data consistency and integrity across multiple nodes or replicas.
  - Scalability: The RTDB is able to handle increasing volumes and velocities of data without compromising the performance or availability.
- Some examples of RTDB are ScyllaDB, Raima, InfluxDB, MongoDB, etc.



# Features of RTOS

A real-time operating system (RTOS) is an operating system with two key features: **predictability** and **determinism**. This means that it will execute tasks quickly and efficiently, responding as expected every time within a tight time boundary. An RTOS is different from a general-purpose operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment. In an RTOS, processing time requirements need to be fully understood and bound rather than just kept as a minimum.

Some of the features of an RTOS are  :

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources, as it often runs on embedded systems with limited hardware capabilities.
- **Fast response**: An RTOS is able to handle interrupts and events with minimal latency and overhead, as it prioritizes the tasks that need to be executed in real time.
- **Preemptive scheduling**: An RTOS uses a preemptive scheduling algorithm, which means that each task has a unique priority value and the higher priority task can interrupt the lower priority task at any time. This ensures that the most urgent tasks are always executed first.
- **Cooperative scheduling**: An RTOS can also use a cooperative scheduling algorithm, which means that the task will run until the execution is completed or it voluntarily yields the control to another task. This reduces the context switching overhead and allows the tasks to cooperate with each other.
- **Main loop**: An RTOS can also use a main loop algorithm, which means that the tasks are executed in a sequential order in a loop, without any interruption or preemption. This is suitable for simple and periodic tasks that do not have strict timing constraints.
- **Inter-task communication**: An RTOS provides mechanisms for inter-task communication, such as message queues, semaphores, mutexes, events, signals, etc. These allow the tasks to exchange data, synchronize, and coordinate with each other.
- **Resource management**: An RTOS manages the allocation and deallocation of system resources, such as memory, CPU, I/O, etc. It ensures that the tasks have access to the resources they need and that the resources are not wasted or corrupted.
- **Error handling**: An RTOS handles the errors and exceptions that may occur during the execution of the tasks, such as memory faults, divide by zero, illegal instructions, etc. It provides mechanisms for error detection, recovery, and reporting.



# Time Services for Real Time Operating Systems

- A real time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS provides services for real time applications, such as industrial control, flight control, and telephone switching.
- A RTOS allows multiple tasks or programs to run simultaneously but based on their priorities.
- A RTOS uses a task scheduler to decide which thread to be executed, and can preempt the current task if a higher priority task arrives.
- A RTOS relies on clock interrupts to produce the interrupt service routine (ISR) that handles the incoming events.
- A RTOS also provides services for inter-thread communication and synchronization, such as message queues, semaphores, mutexes, and event flags.
- A RTOS also provides services for memory management, such as dynamic memory allocation, memory pools, and memory protection.
- A RTOS can be classified into two types: hard real time and soft real time.
  - A hard real time system guarantees that the deadlines of all tasks are met, and any failure to do so can result in a catastrophic consequence.
  - A soft real time system tries to meet the deadlines of most tasks, but some occasional delays are acceptable and do not cause a major impact.
- Some examples of RTOS are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, and LynxOS .



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS by default, but it can be modified or extended to provide some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one when an event occurs.
  - Priority inheritance: the mechanism to avoid priority inversion, which occurs when a low priority process holds a resource needed by a high priority process.
  - Real-time signals: the signals that are delivered to a process immediately, without being queued or blocked.
  - Memory locking: the function to prevent the memory pages of a process from being swapped out to disk.
  - High-resolution timers: the timers that can measure time intervals with nanosecond precision.
- Some examples of UNIX variants that have real-time capabilities are:
  - RTLinux: a hard real-time extension to the Linux kernel that runs the Linux OS as the lowest priority thread on a small real-time core.
  - QNX: a microkernel-based OS that supports preemptive scheduling, priority inheritance, real-time signals, memory locking, and high-resolution timers.
  - Solaris: a UNIX OS that supports real-time scheduling, real-time signals, memory locking, and high-resolution timers.
- The advantages of using UNIX as a RTOS are:
  - It can leverage the existing UNIX tools, libraries, and applications for development and debugging.
  - It can provide a familiar and user-friendly interface for the system administrators and users.
  - It can offer a high level of security, stability, and portability.
- The disadvantages of using UNIX as a RTOS are:
  - It may not meet the strict timing requirements of some hard real-time applications.
  - It may incur a higher overhead and complexity due to the additional layers of abstraction and functionality.
  - It may suffer from performance degradation due to the interference of non-real-time processes and interrupts.



# POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX-like systems, but it has been extended to cover real-time operating systems as well.
- Real-time operating systems are systems that have strict timing constraints and must respond to events within a specified deadline.
- POSIX real-time standards aim to provide application portability and interoperability for real-time systems, by defining common interfaces and services that are needed by real-time applications.
- Some of the POSIX real-time standards are:

  - POSIX.1b: Real-time extensions, which define features such as timers, clocks, semaphores, message queues, shared memory, and priority scheduling.
  - POSIX.1c: Threads extensions, which define features such as thread creation, synchronization, cancellation, and scheduling.
  - POSIX.4: Application programming interface for real-time signals and timers, which define features such as asynchronous I/O, memory locking, and memory mapping.
  - POSIX.13: Application environment profile for real-time systems, which define a minimal set of features that a POSIX-compliant real-time system must support.

- Some of the POSIX issues for real-time operating systems are:

  - POSIX does not specify the exact timing behavior or performance guarantees of the real-time features, leaving them to the implementation details of the operating system.
  - POSIX does not address some of the specific requirements of real-time systems, such as deadline scheduling, resource reservation, fault tolerance, and distributed processing.
  - POSIX does not provide a uniform way to access hardware devices or low-level system functions, which may be needed by some real-time applications.
  - POSIX may not be compatible with some of the existing real-time operating systems or applications, which may have different or proprietary interfaces and services.



# Characteristic of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, or events, and allow other data to be placed in a chronological sequence or to be analyzed chronologically.
- Temporal data can be used to analyze various phenomena that change over time, such as weather patterns, traffic conditions, demographic trends, etc.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time, depending on the context and purpose of the data.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be stored in different ways, such as using timestamps, temporal attributes, temporal tables, or temporal databases, depending on the data model and the query requirements.
- Temporal data can be manipulated and queried using different techniques, such as temporal algebra, temporal logic, temporal SQL, or temporal GIS, depending on the data type and the analysis goals.



# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. This can happen due to delays in data acquisition, transmission, processing, or storage.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with the data from other sources or the physical environment. This can happen due to errors in data acquisition, transmission, processing, or storage.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the occurrence of some events in the physical environment or the database. For example, a sensor can trigger an update when it detects a change in the physical environment, or a transaction can trigger an update when it commits or aborts.
  - Periodic updates, which are updates that are performed at regular intervals of time. For example, a sensor can update the database every second, or a transaction can update the database every 10 milliseconds.
  - Concurrency control, which is a mechanism that coordinates the access and modification of the data by multiple transactions. For example, a locking protocol can prevent two transactions from updating the same data at the same time, or a timestamp protocol can order the transactions based on their deadlines or arrival times.
  - Data replication, which is a technique that creates multiple copies of the data and distributes them across different nodes or locations. For example, a data object can be replicated on multiple sensors, servers, or clients, and the replicas can be synchronized using a consistency protocol.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon, of course. In the real world, at any given time, many things are happening simultaneously.
- When we design software to monitor and control real-world systems, we must deal with this natural concurrency.
- Real-time systems (RTS) respond to their environment within specified time constraints.
- RTS are inherently concurrent and typically manage shared data resources, so they require synchronization to ensure both logical and timing correctness.
- Much research in managing shared data has been carried out in the context of database systems.
- A database system is a collection of data and software that allows users to store, manipulate, and query data.
- A real-time database system (RTDBS) is a database system that supports applications with timing constraints.
- Transactions in RTDBS should be scheduled considering both data consistency and timing constraints.
- In addition, a RTDBS must adapt to changes in the operating environment and guarantee the completion of critical transactions.
- Concurrency control is the process of ensuring that concurrent transactions do not interfere with each other and preserve the consistency of the database.
- Concurrency control in RTDBS is more challenging than in conventional database systems, because it must also consider the deadlines and priorities of transactions.
- Concurrency control in RTDBS can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control prevents conflicts from occurring by locking the data items accessed by transactions.
- Optimistic concurrency control allows conflicts to occur and resolves them by aborting or restarting transactions.
- Pessimistic concurrency control has the advantage of avoiding unnecessary aborts, but it may cause blocking and deadlock problems.
- Optimistic concurrency control has the advantage of avoiding blocking and deadlock problems, but it may cause excessive aborts and restarts.
- The choice of concurrency control technique depends on the characteristics of the application and the workload.
- Some examples of concurrency control techniques for RTDBS are:
  - Priority-based locking: a pessimistic technique that assigns locks based on the priorities of transactions.
  - Two-phase locking with wait-die and wound-wait: a pessimistic technique that uses two rules to avoid deadlock and priority inversion.
  - Timestamp ordering: a pessimistic technique that orders transactions based on their timestamps and aborts or delays conflicting transactions.
  - Basic timestamp ordering: an optimistic technique that validates transactions based on their timestamps and aborts conflicting transactions.
  - Multiversion concurrency control: an optimistic technique that maintains multiple versions of data items and allows transactions to access the appropriate version based on their timestamps.
  - Epsilon serializability: an optimistic technique that relaxes the serializability criterion by allowing some degree of inconsistency within a predefined bound.
- Concurrency control in RTDBS is an active research area that aims to improve the performance and reliability of real-time applications.



# Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have to meet certain performance requirements, such as timeliness, consistency, concurrency, and reliability.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have to guarantee strict deadlines for every transaction, and any missed deadline is considered a failure.
  - Soft real-time databases have to meet most of the deadlines, but some occasional deadline misses are acceptable.
- Some examples of commercial real-time databases are:
  - Raima Database Manager (RDM): a cross-platform, embedded, in-memory, SQL database that supports hard and soft real-time applications.
  - Google Cloud Firestore: a scalable, serverless, NoSQL database that supports real-time data synchronization and offline access.
  - CoStar: a leading provider of commercial real estate information, analytics, and online marketplaces that offers real-time data on properties, transactions, and trends.
  - Altus Group: a global provider of software, data, and advisory services for the commercial real estate industry that offers historical and current data on deals, valuations, and market conditions.

