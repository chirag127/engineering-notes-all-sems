

# Real Time System

A real time system is a system that can process and respond to events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to handle concurrent and unpredictable events and guarantee the correctness and timeliness of its outputs. 

Some examples of real time systems are:

- Flight control systems that monitor and adjust the position and speed of an aircraft
- Process control systems that regulate the temperature, pressure, and flow of fluids in industrial plants
- Machine vision systems that analyze images and guide robots or vehicles
- Medical imaging systems that capture and process images of internal organs or tissues
- Video wall systems that display and synchronize multiple video streams

There are two main types of real time systems based on the severity of the consequences of missing a deadline:

- Hard real time systems: These systems have absolute deadlines that must be met at all costs. A missed deadline can result in a catastrophic failure or a loss of life. For example, a flight control system must respond to a pilot's input or a sensor's reading within milliseconds, otherwise the aircraft may crash.
- Soft real time systems: These systems have relative deadlines that can be occasionally missed without causing a major damage. A missed deadline can result in a degraded performance or a lower quality of service. For example, a video wall system must display and synchronize video frames within a certain interval, otherwise the viewers may notice a delay or a glitch.

Real time systems are often deployed at the edge of a network, where they can interact with the physical world and process data locally. This reduces the latency and bandwidth requirements of sending data to a central server or a cloud. However, real time systems at the edge also face challenges such as limited resources, security threats, and environmental conditions. Therefore, real time systems require specialized hardware and software components that can meet the performance, reliability, and safety requirements of the application domain.



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- The correctness of a real time system depends not only on the logical results of the computations, but also on the time at which the results are produced.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences, such as loss of life, damage to property, or failure of mission-critical operations.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade.
- Examples of hard real time systems are air traffic control systems, nuclear power plant control systems, and pacemakers.
- Examples of soft real time systems are multimedia systems, online gaming systems, and web servers.
- A real time system typically consists of three components: sensors, processors, and actuators.
- Sensors are devices that monitor the physical environment and generate events or inputs for the system.
- Processors are devices that execute the software tasks or processes that handle the events or inputs and produce the outputs or commands for the system.
- Actuators are devices that perform the physical actions or outputs commanded by the system.
- A real time system must deal with various challenges, such as concurrency, synchronization, scheduling, resource management, fault tolerance, and security.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System:

### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A **real time system** is a system that must respond to events or stimuli within a specified time interval, called a **deadline**.
- A **real time system** can be classified into two types: **hard real time system** and **soft real time system**.
- A **hard real time system** is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A **soft real time system** is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A **real time system** consists of three main components: **sensors**, **processors**, and **actuators**.
- **Sensors** are devices that monitor the physical environment and generate events or stimuli for the system.
- **Processors** are devices that execute the tasks or programs that process the events or stimuli and generate the outputs or responses for the system.
- **Actuators** are devices that perform the actions or effects on the physical environment according to the outputs or responses of the system.
- A **real time system** can be designed using various approaches, such as **time-triggered**, **event-triggered**, or **hybrid**.
- A **time-triggered** approach is based on a predefined schedule that determines when each task or program is executed. The system is synchronized by a global clock and the events or stimuli are processed periodically.
- An **event-triggered** approach is based on the occurrence of events or stimuli that trigger the execution of tasks or programs. The system is asynchronous and the events or stimuli are processed as soon as possible.
- A **hybrid** approach is a combination of both time-triggered and event-triggered approaches, where some tasks or programs are executed according to a schedule and some are executed according to the events or stimuli. The system is partially synchronized and the events or stimuli are processed either periodically or as soon as possible.



### Typical Real Time Applications

- A real-time application (RTA) is an application that has strict time constraints on its performance and reliability. It must respond to events or inputs within a specified time frame, or else it may fail or cause undesirable consequences.
- Some examples of real-time applications are:

  - **Video conferencing**: This application allows users to communicate with each other through audio and video streams over the internet. It requires low latency and high bandwidth to ensure smooth and synchronized transmission of data. It also needs to handle packet loss, jitter, and network congestion gracefully. 
  - **Voice over Internet Protocol (VoIP)**: This application enables users to make phone calls over the internet using digital signals. It requires low latency and high quality of service (QoS) to ensure clear and uninterrupted voice communication. It also needs to deal with encryption, authentication, and security issues. 
  - **Online gaming**: This application allows users to play games with other players over the internet. It requires low latency and high responsiveness to ensure fair and enjoyable gameplay. It also needs to handle synchronization, consistency, and scalability issues. 
  - **Community storage applications**: This application allows users to share and access data stored on distributed devices over the internet. It requires high availability and reliability to ensure data integrity and accessibility. It also needs to deal with replication, consistency, and fault tolerance issues. 
  - **Some e-commerce applications**: This application allows users to buy and sell goods and services over the internet. It requires high performance and security to ensure fast and safe transactions. It also needs to deal with concurrency, consistency, and privacy issues. 
  - **Real-time operating system (RTOS)**: This application is a software platform that manages the hardware and software resources of a real-time system. It provides services such as scheduling, synchronization, communication, and memory management. It ensures that the real-time tasks meet their deadlines and priorities. 
  - **Instant messaging (IM) applications**: This application allows users to send and receive text, voice, and video messages over the internet. It requires low latency and high availability to ensure instant and continuous communication. It also needs to deal with encryption, authentication, and security issues. 
  - **Team collaboration applications**: This application allows users to work together on projects and tasks over the internet. It requires high performance and reliability to ensure effective and efficient collaboration. It also needs to deal with synchronization, consistency, and security issues. 
  - **Digital control systems**: This application controls the behavior of physical systems using digital signals. It requires high accuracy and stability to ensure correct and safe operation. It also needs to deal with sampling, quantization, and feedback issues.  
  - **Optimal control systems**: This application optimizes the performance of physical systems using mathematical models and algorithms. It requires high efficiency and robustness to ensure optimal and feasible solutions. It also needs to deal with uncertainty, complexity, and nonlinearity issues.  
  - **Command and control systems**: This application coordinates the actions of multiple agents or entities in complex and dynamic environments. It requires high reliability and adaptability to ensure effective and timely decision making. It also needs to deal with communication, coordination, and conflict issues.  
  - **Signal processing systems**: This application analyzes and transforms signals such as sound, image, and video using mathematical techniques and algorithms. It requires high speed and quality to ensure accurate and useful information extraction. It also needs to deal with noise, distortion, and compression issues.  
  - **Tracking systems**: This application monitors and predicts the location and movement of objects or targets using sensors and algorithms. It requires high precision and responsiveness to ensure accurate and timely tracking. It also needs to deal with occlusion, clutter, and uncertainty issues.  
  - **Real-time databases**: This application stores and retrieves data that have temporal constraints and dependencies. It requires high consistency and availability to ensure data validity and timeliness. It also needs to deal with concurrency, transaction, and scheduling issues.  
  - **Multimedia systems**: This application produces and consumes multimedia content such as audio, video, and graphics using hardware and software components. It requires high performance and quality to ensure smooth and realistic multimedia presentation. It also needs to deal



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System will be released on **Monday, 20 March 2023** at **10:00 AM GMT**.
- The notes will cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Challenges and requirements of real time systems
  - Real time system design and development process
  - Real time system standards and tools
- The notes will be available in PDF format on the course website and the learning management system (LMS).
- The notes will also be accompanied by a video lecture and a quiz to test your understanding of the concepts.
- You are expected to read the notes carefully and complete the quiz by **Friday, 24 March 2023** at **11:59 PM GMT**.
- You are encouraged to ask questions and participate in discussions on the course forum and the LMS.
- You can also contact the instructor or the teaching assistant via email or office hours if you have any doubts or queries regarding the unit.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by **Friday, 24 March 2023** before **5:00 PM**.
- The notes should be handwritten and scanned in PDF format.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be clear, concise, and accurate. They should include diagrams, tables, and examples wherever necessary.
- The notes should be uploaded on the online portal with the file name **RTS_Unit1_Name_RollNo.pdf**.
- The notes will be evaluated based on the completeness, correctness, and presentation of the content.
- Late submissions will not be accepted and will result in zero marks.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also on the result being obtained within the time constraint.
- Every real-time system has a set of timing constraints that it has been designed to meet. If a system does not have timing constraints, it is not real-time.
- Timing constraints can be broken down into two categories :
  - Performance constraints: The constraints enforced on the response of the system are known as performance constraints. They specify the maximum or minimum acceptable delay between an event and the system's reaction to it. For example, a car's airbag system must deploy within a few milliseconds of a collision.
  - Scheduling constraints: The constraints enforced on the execution of tasks are known as scheduling constraints. They specify the order, frequency, duration, and deadlines of tasks that must be performed by the system. For example, a video streaming system must process and transmit frames at a constant rate.
- Timing constraints can be expressed using various constructs in requirements languages, such as deadlines, periods, offsets, jitter, latency, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual response and execution times of the system and compare them with the expected values.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.



### Hard Real Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization).
- A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
- Examples of hard real-time systems are flight control systems, nuclear power plant control systems, missile guidance systems, etc .
- A hard real-time system requires a hard real-time operating system (RTOS) that can guarantee the timely execution of tasks and interrupt handlers.
- A hard real-time system must have predictable and deterministic behavior, meaning that the system state and output can be determined by the system input and initial state.
- A hard real-time system must have high reliability and availability, meaning that the system can perform its function correctly and continuously without failures or interruptions.



### Soft Real Time Systems

- A soft real time system is a system that can tolerate some degree of latency or jitter in meeting its deadlines .
- A deadline is the time limit within which a task or an event must be completed or occur.
- Latency is the delay between the initiation and completion of a task or an event.
- Jitter is the variation in latency over time.
- In a soft real time system, missing a deadline occasionally or by a small margin does not cause a catastrophic failure or a significant loss of quality  .
- A soft real time system can run on multiple cores and impose fewer restrictions on applications.
- A soft real time system is typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real time systems are: software that maintains and updates the flight plans for commercial airliners, streaming audio-video applications, online gaming, multimedia systems, etc. .



### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relationships of the functions needed in a real-time system.
- A reference model helps to reason about the timing behavior and performance of a real-time system, using consistent terminology and abstraction.
- A reference model consists of three elements:
  - A workload model that describes the applications supported by the system, such as tasks, events, deadlines, etc.
  - A resource model that describes the available system resources, such as processors, memory, devices, etc.
  - Algorithms that define how the system resources are used to execute the applications, such as scheduling, synchronization, communication, etc.
- A reference model can be used to analyze and compare different real-time systems, as well as to design and implement them.
- An example of a reference model is the Real-time Control System (RCS) architecture, which combines real-time motion planning and control with high-level task planning, problem solving, world modeling, state estimation, and sensory processing.



### Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource is typically shared by multiple jobs and can be accessed by only one job at a time. A job may need to wait for a resource to become available before using it. Example: printer, file, semaphore, memory.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors and resources can be interrupted and resumed by other jobs. They allow multitasking and concurrency. Example: CPU, RAM, disk.
- Non-preemptable processors and resources cannot be interrupted and resumed by other jobs. They require exclusive access and mutual exclusion. Example: printer, file, semaphore.
- Processors and resources can affect the timing and performance of real-time tasks. They can introduce delays, overheads, and uncertainties in the execution of tasks.
- Processors and resources need to be managed and allocated efficiently by the real-time operating system (RTOS) to meet the timing constraints and quality of service requirements of real-time applications .
- Processors and resources can be configured and optimized for real-time applications by using techniques such as workload-aware processor tuning, time synchronization, and communication protocols .



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are :
  - **Release time (r<sub>i</sub>)**: The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed with some penalty).
  - **Relative deadline (D<sub>i</sub>)**: The maximum time interval between the release time and the absolute deadline of a job. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The time interval in which a job can be feasibly executed by the system. It is equal to the relative deadline minus the execution time of the job.
- The temporal parameters of a job determine its urgency, priority, and schedulability in a real time system .



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks in the system.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that can meet all the deadlines of the task. A set of periodic tasks is said to be feasible if there exists a schedule that can meet all the deadlines of all the tasks in the set.
- A periodic task is said to be implicit-deadline if its relative deadline is equal to its period, i.e., Di = Pi. A periodic task is said to be constrained-deadline if its relative deadline is less than or equal to its period, i.e., Di ≤ Pi. A periodic task is said to be arbitrary-deadline if its relative deadline can be any value, i.e., Di can be greater than, equal to, or less than Pi.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a minimum inter-arrival time Mi for each task τi, to prevent the release of two consecutive jobs of the same task within Mi time units.



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the scheduling of jobs in real time systems.
- Precedence constraints are the restrictions on the order of execution of jobs that are imposed by the logic or functionality of the system. For example, a job that computes the average of some data must execute after the job that collects the data.
- Data dependency is the dependency of a job on the data produced or consumed by another job. For example, a job that displays the temperature on a screen must execute after the job that reads the temperature sensor.
- Precedence constraints and data dependency can be represented by a directed graph called the precedence graph, where the vertices are the jobs and the edges are the constraints or dependencies. A job can only start execution if all its predecessors have completed execution.
- Precedence constraints and data dependency can affect the feasibility and optimality of the scheduling algorithms for real time systems. Some algorithms may not be able to schedule a set of jobs with precedence constraints or data dependency, while others may require additional information or modifications to handle them.
- Precedence constraints and data dependency can also introduce additional challenges for the design and verification of real time systems, such as deadlock, livelock, race conditions, and data inconsistency. These challenges require careful analysis and testing to ensure the correctness and reliability of the system.



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their periods, execution times, deadlines, and priorities. Static scheduling is suitable for systems that have fixed and predictable workloads .
  - Dynamic scheduling is done at run time or during the system execution. It is based on the current state of the system, such as the availability of resources, the arrival of new tasks, the completion of existing tasks, and the occurrence of events. Dynamic scheduling is suitable for systems that have variable and unpredictable workloads .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and improve the schedulability of the system .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running. The higher priority task has to wait until the lower priority task finishes or is blocked. Non-preemptive scheduling can avoid the overhead and complexity of context switching and synchronization, but it can also increase the response time and reduce the schedulability of the system .
- Real time scheduling algorithms are the rules or methods that determine which task to execute next in a system. There are many real time scheduling algorithms, such as rate monotonic, earliest deadline first, least laxity first, etc. Each algorithm has its own advantages and disadvantages, and its own assumptions and conditions for ensuring the schedulability of the system .
- Real time scheduling analysis is the process of verifying and testing the performance and correctness of the system and the scheduling algorithm. It involves measuring and evaluating the parameters and metrics of the system, such as utilization, response time, deadline miss ratio, jitter, etc. Real time scheduling analysis can help to identify and resolve the problems and bottlenecks of the system, and to optimize and improve the system design and implementation .



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of allocating CPU time to tasks or processes that have timing constraints and deadlines. Real time scheduling aims to ensure that critical tasks are executed within their deadlines, and that the system meets its performance and quality of service requirements. 

Some of the common approaches to real time scheduling are:

- **Rate-monotonic scheduling (RMS)**: This is a static priority scheduling algorithm that assigns priorities to tasks based on their periods. The shorter the period, the higher the priority. RMS is optimal for periodic tasks with fixed deadlines and execution times. RMS guarantees that all tasks will meet their deadlines if the CPU utilization is less than or equal to 69.3%.  
- **Earliest deadline first (EDF)**: This is a dynamic priority scheduling algorithm that assigns priorities to tasks based on their absolute deadlines. The closer the deadline, the higher the priority. EDF is optimal for periodic and aperiodic tasks with arbitrary deadlines and execution times. EDF guarantees that all tasks will meet their deadlines if the CPU utilization is less than or equal to 100%.  
- **Least laxity first (LLF)**: This is a dynamic priority scheduling algorithm that assigns priorities to tasks based on their laxity. The laxity of a task is the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority. LLF is optimal for periodic and aperiodic tasks with arbitrary deadlines and execution times. LLF guarantees that all tasks will meet their deadlines if the CPU utilization is less than or equal to 100%.  
- **Deadline monotonic scheduling (DMS)**: This is a static priority scheduling algorithm that assigns priorities to tasks based on their relative deadlines. The shorter the deadline, the higher the priority. DMS is optimal for periodic tasks with fixed execution times and arbitrary deadlines. DMS guarantees that all tasks will meet their deadlines if the CPU utilization is less than or equal to 100%.  
- **Fixed priority scheduling (FPS)**: This is a static priority scheduling algorithm that assigns priorities to tasks based on some predefined criteria, such as task importance, criticality, or user preference. FPS is not optimal for any class of tasks, but it is simple and flexible. FPS can handle periodic, aperiodic, and sporadic tasks with arbitrary deadlines and execution times. FPS does not guarantee that all tasks will meet their deadlines, but it can provide some schedulability analysis techniques to check the feasibility of a given task set.  
- **Round robin scheduling (RR)**: This is a simple scheduling algorithm that assigns equal time slices to tasks in a circular order. RR is not optimal for any class of tasks, but it is fair and easy to implement. RR can handle periodic, aperiodic, and sporadic tasks with arbitrary deadlines and execution times. RR does not guarantee that all tasks will meet their deadlines, but it can provide some responsiveness and throughput for the system.



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- The system executes tasks according to a predetermined schedule.
- This can be useful for real-time systems that require predictable and deterministic behaviour.
- A periodic static schedule is called a cyclic schedule .
- This approach to scheduling hard real-time jobs is called the clock-driven or time-driven approach because each scheduling decision is made at a specific time, independent of events, such as job releases and completions, in the system .
- A clock-driven system never exhibits the anomalous timing behavior of priority-driven systems .
- A clock-driven scheduler can be implemented by using a table-driven approach or a cyclic executive approach.
- A table-driven approach uses a table that specifies the start time and the task to be executed for each scheduling point.
- A cyclic executive approach uses a loop that executes a sequence of tasks and waits for the next clock interrupt.
- A clock-driven scheduler can handle periodic tasks and aperiodic tasks with deadlines.
- A clock-driven scheduler can also handle sporadic tasks by using a slack stealing technique.
- A slack stealing technique allows a sporadic task to execute in the idle time or the slack time of the schedule.
- A clock-driven scheduler can handle overload situations by using a graceful degradation technique.
- A graceful degradation technique allows the system to drop some tasks or reduce the quality of service of some tasks when the workload exceeds the capacity.
- A clock-driven scheduler can handle mode changes by using a mode transition technique.
- A mode transition technique allows the system to switch from one schedule to another when the system mode changes.
- A clock-driven scheduler can handle resource sharing by using a resource reservation technique.
- A resource reservation technique allows the system to allocate a fixed amount of time for each resource in each schedule cycle.



### Weighted Round Robin Approach

- The weighted round robin (WRR) algorithm is a variation of the basic round robin (RR) algorithm that assigns different weights to different jobs based on their importance or priority .
- The WRR algorithm has been used for scheduling real-time traffic in high-speed switched networks, where different types of packets may have different quality of service (QoS) requirements .
- The WRR algorithm works as follows  :
  - Each job in the ready queue is assigned a weight that represents its share of the processor time. The weight can be a fixed value or a dynamic value that changes over time.
  - The algorithm maintains a pointer that points to the current job in the ready queue. Initially, the pointer points to the first job in the queue.
  - The algorithm allocates the processor to the current job for a time slice that is proportional to its weight. For example, if the weight of the current job is 3 and the time slice unit is 1, then the job gets 3 time slices of the processor.
  - After the time slice expires, the algorithm moves the pointer to the next job in the ready queue and repeats the process until all the jobs in the queue are served.
  - The algorithm then starts a new round and repeats the process until all the jobs are completed or preempted by a higher priority job.
- The advantages of the WRR algorithm are  :
  - It is simple and easy to implement.
  - It can handle different types of jobs with different QoS requirements by adjusting their weights.
  - It can provide fairness and balance among the jobs by giving them proportional shares of the processor time.
- The disadvantages of the WRR algorithm are  :
  - It may cause starvation or delay for some jobs if their weights are too low compared to other jobs.
  - It may not be suitable for hard real-time systems where the jobs have strict deadlines and need deterministic response times.
  - It may not be optimal for maximizing the system throughput or minimizing the average waiting time.



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two categories: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Examples of static priority-driven scheduling algorithms are rate-monotonic scheduling (RMS) and deadline-monotonic scheduling (DMS).
- Examples of dynamic priority-driven scheduling algorithms are earliest deadline first (EDF) and least laxity first (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to prioritize critical tasks and reduce the interference from non-critical tasks.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as the lack of priority inheritance, the heterogeneity of hardware platforms, and the complexity of the middleware.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters are known in advance and do not change during execution. A **dynamic system** is one where the tasks and their parameters may change unpredictably during execution.
- Static systems are easier to analyze and validate than dynamic systems, since they have fixed and deterministic behavior. Dynamic systems are more flexible and adaptable to changing workloads, but they require more complex scheduling algorithms and runtime overhead.
- Static systems are suitable for hard real-time systems, where missing a deadline can have catastrophic consequences. Dynamic systems are suitable for soft real-time systems, where missing a deadline can degrade the quality of service but not cause failure.
- Static systems use **static scheduling**, which assigns priorities to tasks before the system runs. Dynamic systems use **dynamic scheduling**, which assigns priorities to tasks as the system runs, based on their current parameters and state.
- Static scheduling has the advantages of simplicity, predictability, and low overhead. Dynamic scheduling has the advantages of responsiveness, adaptability, and optimality.
- Static scheduling can be done offline, using methods such as rate-monotonic scheduling or deadline-monotonic scheduling. Dynamic scheduling can be done online, using methods such as earliest deadline first scheduling or least laxity first scheduling.
- Static scheduling is more suitable for periodic tasks, which have fixed and regular arrival times and execution times. Dynamic scheduling is more suitable for aperiodic tasks, which have variable and irregular arrival times and execution times.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A task's deadline is the time by which it must finish its execution, and its slack is the difference between its deadline and its remaining execution time.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, that is, a schedule that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as well as for non-preemptive scheduling of periodic tasks with implicit deadlines (equal to their periods).
- LST is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines and constrained deadlines (less than or equal to their periods), as well as for non-preemptive scheduling of periodic tasks with implicit deadlines.
- EDF and LST may not be optimal for other types of tasks, such as aperiodic tasks, tasks with precedence constraints, tasks with resource sharing, or tasks with variable execution times.
- EDF and LST may also under-utilize the CPU, that is, leave some idle time when some tasks are ready to execute, especially in the overload scenario where the CPU load is greater than one.
- EDF and LST can be combined to enhance the performance of real-time task scheduling, by switching between them according to the CPU load or the slack distribution of the tasks.



### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- RMA is preemptive in nature, meaning that a higher priority task can interrupt a lower priority task at any time .
- RMA is optimal for periodic tasks with fixed deadlines, meaning that it can schedule any task set that is feasible under any other static-priority algorithm .
- RMA has a simple schedulability test that can determine if a task set is schedulable or not, based on the utilization factor of the tasks  .
- The utilization factor of a task is the ratio of its execution time to its period. The utilization factor of a task set is the sum of the utilization factors of all the tasks in the set  .
- The schedulability test for RMA is: U <= n(2^(1/n) - 1), where U is the utilization factor of the task set, and n is the number of tasks in the set  .
- If the schedulability test is satisfied, then the task set is guaranteed to be schedulable by RMA. If the test is not satisfied, then the task set may or may not be schedulable by RMA  .
- RMA has some advantages and disadvantages compared to other scheduling algorithms. Some of the advantages are:
  - It is simple and easy to implement .
  - It has low overhead and fast response time for high priority tasks .
  - It is optimal for periodic tasks with fixed deadlines .
- Some of the disadvantages are:
  - It does not consider the actual execution time of the tasks, only their worst-case execution time .
  - It does not handle aperiodic or sporadic tasks well .
  - It may waste CPU resources if the task set is not fully utilized .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, priority, and resource requirement of all tasks for all time . The scheduler follows the pre-defined table that contains the necessary scheduling decisions for use during the run-time . Offline scheduling is suitable for static and deterministic systems that have fixed and known task parameters.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system . The scheduler does not have the prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task . Online scheduling is suitable for dynamic and unpredictable systems that have variable and unknown task parameters. Online scheduling can be either static or dynamic, depending on whether the priority of a task is fixed or can change during the execution .
- The main difference between offline and online scheduling is the amount of information available to the scheduler and the time of making the scheduling decisions . Offline scheduling requires complete and accurate information about all tasks and makes scheduling decisions before the system starts, while online scheduling requires partial and uncertain information about the tasks and makes scheduling decisions as the system runs . Offline scheduling can guarantee the feasibility and optimality of the schedule, while online scheduling can only guarantee the feasibility and optimality of the current scheduling decision.
- The advantages of offline scheduling are that it can avoid the overhead and complexity of online scheduling, it can optimize the schedule based on global criteria, and it can handle complex constraints and dependencies among tasks. The disadvantages of offline scheduling are that it cannot handle dynamic and unpredictable events, it cannot adapt to changes in task parameters or system conditions, and it requires a lot of computation time and memory space to generate and store the schedule.
- The advantages of online scheduling are that it can handle dynamic and unpredictable events, it can adapt to changes in task parameters or system conditions, and it requires less computation time and memory space to make and store the scheduling decisions. The disadvantages of online scheduling are that it can incur the overhead and complexity of online scheduling, it can only optimize the schedule based on local criteria, and it can have difficulty handling complex constraints and dependencies among tasks.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, utilization, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a pre-defined schedule that is computed offline. The scheduler follows the schedule and switches jobs at fixed time instants. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven and clock driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the predictability of periodic jobs. Periodic jobs are jobs that have fixed arrival pattern and hard deadlines. They are the primary workload in real-time systems and must be guaranteed to meet their deadlines.
- In priority driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: background scheduling and slack stealing.
  - Background scheduling is a simple and efficient approach that assigns the lowest priority to aperiodic and sporadic jobs. This ensures that periodic jobs always have higher priority and meet their deadlines. However, this also means that aperiodic and sporadic jobs may suffer from long response times and poor quality of service.
  - Slack stealing is a more sophisticated and dynamic approach that assigns variable priorities to aperiodic and sporadic jobs based on the available slack times of periodic and sporadic jobs. Slack time is the amount of time that a job can be delayed without affecting its deadline. By stealing the slack time of other jobs, aperiodic and sporadic jobs can be executed earlier and improve their response times and quality of service. However, this also requires more computation and overhead to track the slack times and adjust the priorities.
- In clock driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: spare capacity scheduling and schedule modification.
  - Spare capacity scheduling is a simple and efficient approach that reserves some slots in the pre-defined schedule for aperiodic and sporadic jobs. This ensures that periodic jobs always follow the schedule and meet their deadlines. However, this also means that the schedule may not be fully utilized and some slots may be wasted if no aperiodic or sporadic jobs arrive.
  - Schedule modification is a more sophisticated and dynamic approach that modifies the pre-defined schedule online to accommodate aperiodic and sporadic jobs. This ensures that the schedule is fully utilized and no slots are wasted. However, this also requires more computation and overhead to modify the schedule and ensure the feasibility and correctness of the modified schedule.



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, and network bandwidth, available to multiple users or processes.
- Resource sharing can improve the efficiency, performance, scalability, and reliability of a computer system, as well as reduce the cost and complexity of managing it.
- Resource sharing can be achieved by various methods, such as:
  - Multiprogramming: running multiple programs or processes concurrently on a single processor, by switching between them in a time-sharing manner.
  - Multiprocessing: using multiple processors or cores to execute multiple programs or processes simultaneously or in parallel.
  - Distributed computing: using multiple computers or devices connected by a network to cooperate on a common task or problem, by dividing it into subtasks and exchanging data and results.
  - Cloud computing: using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer.
  - Virtualization: creating a virtual version of a resource, such as a server, a storage device, a network, or an operating system, that can be accessed and used by multiple users or processes, as if it were a real one.
- Resource sharing can also involve different levels of abstraction, such as:
  - Physical level: sharing the actual hardware components of a computer system, such as the CPU, the memory, the disk, the network interface, etc.
  - Logical level: sharing the software components of a computer system, such as the files, the databases, the applications, the services, etc.
  - Semantic level: sharing the meaning or the content of the data or the information stored or processed by a computer system, such as the keywords, the concepts, the categories, etc.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, a peripheral device, etc.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock  .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task holding a resource.
  - Preemptive RAC means that a task can be preempted by another task even if it holds a resource. This may cause timing anomalies, where a high-priority task is delayed by a low-priority task preempting a resource.
- RAC can also be classified into two types: priority-based and non-priority-based.
  - Priority-based RAC means that the priority of tasks determines the order of resource allocation and scheduling. This may cause deadlock, where two or more tasks are waiting for each other to release a resource.
  - Non-priority-based RAC means that the priority of tasks does not affect the resource allocation and scheduling. This may cause starvation, where a task is indefinitely denied access to a resource.
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP): a non-preemptive, priority-based protocol that eliminates unbounded priority inversion by temporarily raising the priority of a task holding a resource to the highest priority of the tasks waiting for the resource.
  - Priority ceiling protocol (PCP): a preemptive, priority-based protocol that eliminates priority inversion and deadlock by assigning a ceiling priority to each resource and preventing a task from acquiring a resource if its priority is lower than the ceiling priority of any resource currently in use.
  - Stack resource policy (SRP): a preemptive, non-priority-based protocol that eliminates priority inversion and deadlock by maintaining a stack of tasks that have acquired or are waiting for resources and allowing a task to preempt another task only if it is higher in the stack.
  - Immediate ceiling priority protocol (ICPP): a preemptive, non-priority-based protocol that eliminates priority inversion and deadlock by assigning a ceiling priority to each resource and raising the priority of a task to the ceiling priority of the resource as soon as it acquires the resource.



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or suspended by another job until it finishes the critical section .
- This implies that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand.
  - They prevent deadlock, since no job is ever blocked or preempted when it holds any resource.
- The disadvantages of non-preemptive critical sections are:
  - They may cause priority inversion, since a high-priority job may have to wait for a low-priority job to finish its critical section.
  - They may reduce the schedulability and utilization of the system, since a job may have to wait for a long time to enter a critical section, or may hold a resource for a long time, preventing other jobs from using it.
  - They may violate the timing constraints of the jobs, since a job may miss its deadline due to the delay caused by the critical sections.



### Basic Priority-Inheritance and Priority-Ceiling Protocols for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use preemptive scheduling and mutual exclusion.
- PIP and PCP aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources, and to prevent deadlocks and priority inversions.
- PIP works by temporarily raising the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it or that shares the same resource. This way, the low-priority task can finish using the resource and release it to the blocked high-priority task.
- PCP works by assigning a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource. A task can only lock a resource if its priority is higher than the ceiling priority of all the resources that are currently locked. This way, the high-priority tasks can preempt the low-priority tasks before they lock any resource that the high-priority tasks need.
- The main differences between PIP and PCP are  :
  - PIP is greedy while PCP is not. PIP lets a task lock a resource whenever the resource is free, while PCP may deny a task from locking a resource even if the resource is free, if the task's priority is lower than the ceiling priority of any locked resource.
  - PIP requires minimum support from the operating system, while PCP requires maximum support from the operating system. PIP only needs to change the priority of a task when it locks or unlocks a resource, while PCP needs to keep track of the ceiling priority of all the resources and the current system ceiling, which is the highest ceiling priority of any locked resource.
  - PIP cannot prevent deadlocks, while PCP can prevent deadlocks and priority inversions. PIP may cause a circular wait among tasks that share multiple resources, while PCP avoids this by enforcing a strict order of locking resources based on their ceiling priorities.
  - PIP may cause unbounded priority inversion, while PCP can bound the priority inversion. PIP may allow a low-priority task to lock a resource for a long time if it is preempted by other tasks that do not share the same resource, while PCP limits the blocking time of a high-priority task to the execution time of the critical section of the lowest-priority task that can preempt it.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered to the highest priority ceiling of the remaining locked resources.
- SBPCP guarantees that a task will not be blocked by a lower priority task, and that the maximum blocking time for a task is equal to the worst-case execution time of the critical section of the highest priority task that may lock the same resource .
- SBPCP also prevents deadlocks, priority inversion, and chain blocking .



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-Ceiling Protocol (PCP) is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- PCP works by temporarily raising the priorities of tasks that access shared resources and blocking tasks that have lower priorities than the ceiling of the system.
- The ceiling of the system is the highest priority among all the resources currently locked by any task.
- The ceiling of a resource is the highest priority among all the tasks that may request that resource.
- In a dynamic priority system, the priorities of the tasks change with time, but the resources required by each task remain constant.
- Hence, the ceilings of the resources and the system may change with time as well.
- For dynamic systems, PCP can be used to control resource accesses provided that the ceilings of each resource and the system are updated each time the task priorities change.
- PCP can be implemented in two variants: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP raises the priority of a task to the ceiling of the requested resource only when the task locks the resource.
- ICPP raises the priority of a task to the ceiling of the requested resource as soon as the task is ready to run.
- The worst-case behavior of the two variants is identical from a scheduling viewpoint.
- PCP has some advantages over other synchronization protocols, such as Priority Inheritance Protocol (PIP), such as:
  - PCP avoids chained blocking, which occurs when a low-priority task blocks a higher-priority task that in turn blocks another higher-priority task.
  - PCP bounds the blocking time of any task by the maximum execution time of a critical section of any lower-priority task.
  - PCP allows the schedulability analysis of the system to be performed without knowing the exact order of resource requests.
  - PCP can be combined with other techniques, such as slack stealing, to improve the system utilization.



### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its current priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower priority task, and that the blocking time is bounded by the worst-case execution time of the critical section of the lower priority task.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
  - Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the system design, and does not change it at run time.
  - Dynamic preemption ceiling protocol assigns a ceiling priority to each resource based on the current priority of the task that locks it, and updates it whenever the resource is locked or released.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed priority scheduling technique that allows a task to specify a preemption threshold, below which it cannot be preempted.
  - PTS can improve the schedulability, reduce the context switches, and decrease the memory requirements of real-time systems.
  - PTS can also enable a scalable real-time system design, especially for object-oriented systems that require synchronization considerations to maintain consistent object states.
  - PTS can be combined with preemption ceiling protocol to avoid long priority inversion and deadlock, while preserving the benefits of PTS.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to prevent deadlock and priority inversion, while ensuring schedulability and resource utilization.
- There are different protocols for access control in multiple-unit resources, such as:
  - The **Priority Inheritance Protocol (PIP)**: A job that locks a resource inherits the highest priority of any job blocked on that resource. When the job unlocks the resource, it reverts to its original priority  .
  - The **Priority Ceiling Protocol (PCP)**: Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource. A job can lock a resource only if its priority is higher than the priority ceiling of all locked resources. A job that locks a resource inherits the priority ceiling of that resource. When the job unlocks the resource, it reverts to its original priority  .
  - The **Stack Resource Policy (SRP)**: Each job is assigned a preemption level, which is fixed and independent of its priority. A job can lock a resource only if its preemption level is higher than the preemption level of all jobs that have locked any resource. A job that locks a resource inherits the preemption level of the highest-priority job blocked on that resource. When the job unlocks the resource, it reverts to its original preemption level .
  - The **Multiprocessor Priority Ceiling Protocol (MPCP)**: A variant of PCP for multiprocessor systems, where each resource is assigned to a processor and can be locked by jobs running on that processor. A job can lock a resource only if its priority is higher than the priority ceiling of all locked resources on the same processor. A job that locks a resource inherits the priority ceiling of that resource. When the job unlocks the resource, it reverts to its original priority .
  - The **Multiprocessor Stack Resource Policy (MSRP)**: A variant of SRP for multiprocessor systems, where each resource is shared among all processors and can be locked by jobs running on any processor. A job can lock a resource only if its preemption level is higher than the preemption level of all jobs that have locked any resource. A job that locks a resource inherits the preemption level of the highest-priority job blocked on that resource. When the job unlocks the resource, it reverts to its original preemption level .



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or violation of mutual exclusion.
- To ensure data consistency and mutual exclusion, concurrency control algorithms are needed to regulate the concurrent accesses to data objects.
- Concurrency control algorithms for real time systems should consider both data consistency and timing constraints of the jobs.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent data conflicts by locking the data objects before accessing them. They ensure serializability, but may cause blocking, deadlock, or priority inversion.
  - Optimistic algorithms allow data conflicts to occur, but detect and resolve them before committing the transactions. They avoid blocking, deadlock, and priority inversion, but may cause aborts and restarts.
- Some examples of pessimistic algorithms are:
  - Priority inheritance protocol (PIP): When a high priority job is blocked by a low priority job that holds a lock, the low priority job inherits the priority of the high priority job until it releases the lock.
  - Priority ceiling protocol (PCP): Each data object is assigned a priority ceiling, which is the highest priority of any job that can access it. A job can lock a data object only if its priority is higher than the current priority ceiling of the system, which is the highest priority ceiling of any locked data object.
  - Convex ceiling protocol (CCP): Each data object is assigned a convex ceiling, which is a set of priority levels that can access it. A job can lock a data object only if its priority level belongs to the convex ceiling of the data object and is higher than the current priority ceiling of the system.
- Some examples of optimistic algorithms are:
  - Wait-free algorithm: Each job has a private copy of the data objects it accesses, and updates them locally. At the end of the job, it validates its updates with the global data objects, and commits them if there is no conflict.
  - Timestamp ordering algorithm: Each job is assigned a timestamp based on its deadline or arrival time. A job can access a data object only if its timestamp is smaller than the timestamp of the last update to the data object.
  - Multiversion algorithm: Each data object has multiple versions, each with a timestamp and a validity interval. A job can read the latest version of a data object that is valid for its timestamp. A job can write a new version of a data object only if its timestamp is larger than the timestamp of the last version.



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information or data between two or more parties without any significant delay or latency.
- RTC can be synchronous or asynchronous, depending on whether the parties are communicating at the same time or not.
- RTC can be achieved through various technologies and protocols, such as voice over IP (VoIP), video conferencing, instant messaging, chatbots, websockets, etc.
- RTC can be used for various purposes and applications, such as online education, telemedicine, gaming, social networking, customer service, etc.
- RTC can also pose some challenges and risks, such as security, privacy, bandwidth, reliability, interoperability, etc.

Some key points to remember about RTC are:

- RTC requires low latency and high bandwidth to ensure smooth and clear communication.
- RTC can be affected by network congestion, packet loss, jitter, and other factors that degrade the quality of service (QoS).
- RTC can be encrypted and authenticated to protect the data and the identity of the parties involved.
- RTC can be integrated with other technologies and platforms, such as cloud computing, artificial intelligence, blockchain, etc. to enhance the functionality and efficiency of the communication.



### Basic Concepts in Real Time Communication

- Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays .
- In RTC, there is always a direct path between the source and the destination, and the data is not stored en route to the destination .
- RTC can be synchronous or asynchronous, depending on whether the communication is time-bound or not.
- Synchronous RTC requires both the sender and the receiver to be available at the same time, and the communication is bidirectional and interactive. Examples of synchronous RTC are voice calls, video calls, and instant messaging.
- Asynchronous RTC allows the sender and the receiver to communicate at different times, and the communication is unidirectional and non-interactive. Examples of asynchronous RTC are email, voicemail, and text messaging.
- RTC can be based on different protocols and technologies, such as Session Initiation Protocol (SIP), Real-time Transport Protocol (RTP), Web Real-Time Communication (WebRTC), and Real-Time Messaging Protocol (RTMP)  .
- RTC can be used for various purposes and applications, such as online collaboration, social networking, gaming, education, entertainment, and emergency services .
- RTC can also involve different types of media, such as audio, video, text, and data .
- RTC can pose some challenges and requirements, such as bandwidth, security, quality of service, interoperability, and scalability  .
- RTC can benefit from effective communication skills, such as listening, paying attention to nonverbal signals, managing stress, and asserting oneself.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- Hard real-time communication systems are deterministic in nature, meaning that they must guarantee that the communication is completed within a fixed deadline.
- If a hard real-time communication system fails to meet the deadline, it can result in catastrophic consequences, such as loss of life, property, or mission.
- Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and missile guidance.
- Soft real-time communication systems are probabilistic in nature, meaning that they can tolerate some degree of delay or error in the communication.
- If a soft real-time communication system misses the deadline, it can result in degraded performance, quality, or user satisfaction, but not in severe damage.
- Examples of soft real-time communication systems are video conferencing, online gaming, and multimedia streaming.
- Real-time communication systems can be classified based on other criteria as well, such as the communication topology, the communication protocol, the communication medium, and the communication quality of service.



### Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis, such as voice, video, or audio.
- Real time traffic can be further categorized into periodic, aperiodic, and sporadic messages, depending on the regularity and predictability of their generation and delivery.
- Real time control consists of commands or signals that are sent from a controller to a controlled device or system, such as a robot, a sensor, or a switch.
- Real time control can be further categorized into hard, firm, and soft real time control, depending on the criticality and tolerance of missing deadlines.
- A model of real time communication consists of the following components:
  - End users: the sources and destinations of the messages, such as applications, devices, or systems.
  - Hosts: the computers or processors that run the end users and provide network interfaces.
  - Network interface: the hardware or software that connects the hosts to the network and provides input and output queues for buffering messages.
  - Network: the physical or logical medium that carries the messages between the network interfaces, such as a LAN, a WAN, or a wireless network.
  - Protocol: the set of rules and procedures that govern the format, transmission, and reception of the messages, such as TCP, UDP, or RTP.
- A model of real time communication can be characterized by the following metrics:
  - Throughput: the amount of data that can be transmitted or received per unit time, such as bits per second or packets per second.
  - Delay: the amount of time that elapses from the moment a message is generated by the source to the moment it is received by the destination, such as milliseconds or seconds.
  - Jitter: the variation in delay among different messages of the same stream, such as microseconds or milliseconds.
- A model of real time communication can be evaluated by the following criteria:
  - Reliability: the probability that a message is delivered correctly and within its deadline, such as 0.99 or 0.9999.
  - Quality of service: the degree to which the communication meets the requirements and expectations of the end users, such as bandwidth, latency, or loss rate.
  - Scalability: the ability of the communication to handle increasing or decreasing numbers of end users, messages, or network resources, such as nodes, links, or routers.
  - Security: the protection of the communication from unauthorized access, modification, or disruption, such as encryption, authentication, or firewall.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) service discipline is a type of priority-based service discipline that assigns a weight to each queue and serves the queues in a circular order, giving each queue a number of service slots proportional to its weight .
- WRR service discipline has the advantages of simplicity, fairness and bandwidth guarantee, but it may not satisfy the diverse delay and jitter requirements of different types of packets.
- To overcome this limitation, some variants of WRR service discipline have been proposed, such as:
  - Rate-controlled frame-based weighted round-robin (RFWRR) service discipline, which divides the scheduler into a rate controller and a frame-based WRR server, and guarantees the delay jitter bound and satisfies a diverse set of delay requirements.
  - Probabilistic priority (PP) service discipline, which is based on the strict priority (SP) service discipline with the difference that each priority queue is assigned a parameter that determines the probability with which its corresponding queue is served when it is polled by the server.
  - Class-based weighted fair queuing (CBWFQ) service discipline, which extends the weighted fair queuing (WFQ) service discipline by allowing different classes of packets to have different weights and service rates.
  - Weighted fair priority queuing (WFPQ) service discipline, which combines the features of WFQ and SP service disciplines by giving higher priority to the packets with smaller weights and lower priority to the packets with larger weights.
- These variants of WRR service discipline aim to improve the performance of switched networks by providing different levels of quality of service (QoS) to different classes of packets, such as real-time, interactive and best-effort packets  .



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission from one node can reach all other nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols utilize direct, asynchronous competition between neighboring nodes to determine which node will transmit next. Examples include Aloha and CSMA. These protocols are simple, decentralized, and adaptive, but they suffer from collisions, low efficiency, and unbounded delay.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next. Examples include TDMA and token passing. These protocols are collision-free, efficient, and bounded in delay, but they require synchronization, coordination, and fixed allocation of resources.
- Reservation-based protocols combine the advantages of both probabilistic and deterministic contention protocols by allowing nodes to reserve slots for future transmissions. Examples include ABROAD and PRMA. These protocols are adaptive, collision-free, and bounded in delay, but they require some overhead for reservation and synchronization.



### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain differing qualities of service (QoS) for their data flows  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver.
- RSVP supports the following features :
  - Dynamic and soft state: RSVP can adapt to changing network conditions and user requirements by periodically refreshing the reservations and allowing them to time out if not refreshed.
  - Receiver-oriented: RSVP allows the receiver to specify the QoS parameters for the data flow, rather than the sender. This enables heterogeneous receivers to request different levels of QoS for the same data flow.
  - Scalability: RSVP can scale to large multicast groups by using local decision making and aggregation of reservation state. RSVP also supports shared reservations and wildcard filters to reduce the state information in routers.
  - Policy control: RSVP can enforce network policies based on the identity and credentials of the users and applications that request the reservations. RSVP can also communicate the admission decisions and the allocated resources to the users and applications.
  - Interoperability: RSVP can interoperate with different network layer protocols, such as IPv4, IPv6, and MPLS. RSVP can also interoperate with different QoS models, such as IntServ and DiffServ.



## Unit 5 - Real Time Operating Systems and Databases

- A **real-time operating system (RTOS)** is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations  .
- An RTOS is different from a general-purpose operating system, such as Windows or Linux, which are designed for multitasking and user interaction, and do not guarantee predictable response times.
- An RTOS typically has the following features  :
  - **Real-time multithreading**: The ability to run multiple tasks or threads concurrently, each with its own priority and scheduling policy.
  - **Inter-thread communication and synchronization**: The ability to exchange data and coordinate actions between threads using mechanisms such as message queues, semaphores, mutexes, and events.
  - **Memory management**: The ability to allocate and deallocate memory dynamically, and to protect the memory space of each thread from interference by other threads.
  - **Interrupt handling**: The ability to respond to external or internal signals that require immediate attention, such as hardware events, timers, or software exceptions.
  - **Input/output management**: The ability to access and control peripheral devices, such as sensors, actuators, displays, and network interfaces, using drivers and protocols.
  - **Power management**: The ability to conserve energy and extend battery life by adjusting the CPU frequency, voltage, and sleep modes according to the workload and system state.
- A **real-time database** is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, or online transactions .
- A real-time database is different from a traditional database, which contains data that is persistent and changes less frequently, such as customer records, product catalogs, or historical data.
- A real-time database typically has the following characteristics :
  - **High performance**: The ability to process a large number of transactions or queries per second, with low latency and high throughput.
  - **High availability**: The ability to maintain data consistency and reliability in the presence of failures, such as network partitions, node crashes, or disk errors.
  - **High scalability**: The ability to handle increasing data volumes and user demands by adding more nodes or resources to the system, without compromising performance or availability.
  - **High flexibility**: The ability to support different data models and query languages, such as SQL or NoSQL, and to adapt to changing data schemas and application requirements.
  - **High security**: The ability to protect data from unauthorized access, modification, or deletion, using encryption, authentication, and authorization mechanisms.



### Features of RTOS

- An RTOS is an operating system that provides **predictability** and **determinism**. This means that it can guarantee that tasks will be completed within a specified time limit, and that the system will respond consistently to events and inputs .
- An RTOS is **small**, **fast**, **responsive**, and **efficient**. It occupies very less memory and consumes fewer resources than a general-purpose operating system. It can execute tasks quickly and switch between them with minimal overhead .
- An RTOS supports **concurrent** and **parallel** processing of multiple tasks. It can handle multiple tasks that have different priorities, deadlines, and resource requirements. It can also use multiple processors or cores to improve performance and scalability .
- An RTOS provides **synchronization** and **communication** mechanisms for tasks. It allows tasks to share data and resources safely and efficiently, using semaphores, mutexes, message queues, pipes, etc. It also provides inter-task and inter-processor communication methods, such as signals, events, interrupts, etc .
- An RTOS supports **real-time** and **non-real-time** tasks. It can distinguish between tasks that have strict timing constraints and tasks that can tolerate some delays. It can also adjust the scheduling policy and the priority of tasks dynamically, depending on the system state and the workload .
- An RTOS is **configurable** and **adaptable**. It can be customized and optimized for different applications and platforms, depending on the system requirements and specifications. It can also support new features and capabilities as the market needs evolve, while maintaining compatibility and reliability.



### Time Services

Time services are essential components of real-time systems, as they provide the means to measure, control, and synchronize the temporal behavior of the system and its components. Time services can be classified into two categories: clock services and timer services.

- Clock services are responsible for providing a common notion of time to the system and its components, by maintaining and distributing a reference clock value. Clock services can be implemented by using hardware clocks, software clocks, or a combination of both. Hardware clocks are physical devices that generate periodic signals based on a stable oscillator. Software clocks are logical entities that derive their values from hardware clocks or other sources, such as network messages or external events. Clock services can also support different time domains, such as local time, universal time, or application-specific time.
- Timer services are responsible for providing mechanisms to schedule and execute actions based on time. Timer services can be implemented by using hardware timers, software timers, or a combination of both. Hardware timers are physical devices that generate interrupts or signals after a specified amount of time has elapsed. Software timers are logical entities that use clock services or other sources to trigger actions based on time. Timer services can also support different types of timers, such as one-shot timers, periodic timers, or deadline timers.

Time services are crucial for real-time systems, as they enable the following functions:

- Time measurement: Time services allow the system to measure the duration of events, tasks, or operations, and to compare them with the specified timing constraints or deadlines. Time measurement is essential for ensuring the timeliness and correctness of the system's behavior.
- Time control: Time services allow the system to control the execution order and priority of events, tasks, or operations, based on their timing requirements or deadlines. Time control is essential for ensuring the predictability and reliability of the system's behavior.
- Time synchronization: Time services allow the system to coordinate and align the clocks and timers of different components, devices, or nodes, and to ensure a consistent notion of time across the system. Time synchronization is essential for ensuring the consistency and accuracy of the system's behavior.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like Unix strives to provide good average performance, for a RTOS, correct timing is the key feature.
- Unix is not a RTOS by default, but it can be modified or extended to support real-time features, such as:
  - Adding a real-time kernel or patch, such as RTLinux, Xenomai, or PREEMPT_RT, to the Linux kernel .
  - Using real-time libraries or extensions, such as POSIX real-time extensions, to provide real-time APIs and services.
  - Configuring the system parameters, such as scheduling policies, priorities, interrupts, memory management, and device drivers, to reduce latency and jitter.
- Some advantages of using Unix as a RTOS are:
  - It is widely available, open source, and well supported by the developer community.
  - It offers a rich set of features, tools, and applications for general-purpose computing.
  - It can run on various hardware platforms, from embedded systems to supercomputers.
- Some challenges of using Unix as a RTOS are:
  - It may not meet the strict timing requirements of some hard real-time applications.
  - It may introduce unpredictability and overhead due to its complex and dynamic nature.
  - It may require significant modifications or customizations to achieve real-time performance.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a family of standards that define a common interface for operating systems, especially UNIX-like systems.
- POSIX aims to achieve application portability across different operating systems, by providing a consistent set of services and interfaces for the application programmers.
- However, POSIX does not address the specific needs of real-time applications, which require predictable and timely responses from the operating system and the hardware.
- Real-time applications are those that have strict deadlines and constraints on the execution time and the response time of the system. Examples of real-time applications are avionics, robotics, industrial control, multimedia, etc.
- To support real-time applications, POSIX needs to provide extensions and modifications to the existing standards, such as:
  - Real-time scheduling: POSIX needs to define a way to assign priorities and scheduling policies to the processes and threads, and to guarantee that the highest priority task will always run before any lower priority task.
  - Real-time synchronization: POSIX needs to define a way to synchronize the access to shared resources among the processes and threads, and to ensure that the synchronization mechanisms do not cause priority inversion or deadlock.
  - Real-time communication: POSIX needs to define a way to communicate data and events among the processes and threads, and to ensure that the communication mechanisms do not introduce excessive latency or jitter.
  - Real-time memory management: POSIX needs to define a way to allocate and deallocate memory for the processes and threads, and to ensure that the memory management does not cause fragmentation or memory exhaustion.
  - Real-time signals: POSIX needs to define a way to notify the processes and threads of the occurrence of events, and to ensure that the signals are queued, prioritized, and delivered in a timely manner.
- POSIX has developed several standards to address these issues, such as:
  - POSIX.1b: Real-time extensions, which defines the services and interfaces for real-time scheduling, synchronization, communication, memory management, and signals.
  - POSIX.1c: Threads extensions, which defines the services and interfaces for creating and managing multiple threads of execution within a process.
  - POSIX.4: Timers and clocks, which defines the services and interfaces for measuring and controlling the passage of time in the system.
  - POSIX.13: Application environment profile, which defines the minimum set of services and interfaces that a POSIX-compliant operating system must provide for real-time applications.
- POSIX standards are not mandatory, and the operating system vendors can choose to implement them partially or fully, or not at all. Therefore, the application programmers need to check the level of compliance and the availability of the POSIX services and interfaces in the target operating system, before developing and deploying their real-time applications.



### Characteristics of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, events, cycles, or sequences.
- Temporal data can be used to analyze weather patterns, traffic conditions, demographic trends, and other phenomena that change over time.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon.
- Temporal data can be stored in different ways, such as using timestamps, temporal attributes, temporal tables, or temporal databases.
  - Timestamps are values that indicate the time of creation, modification, or deletion of a data item.
  - Temporal attributes are attributes that store temporal values, such as dates, times, or intervals.
  - Temporal tables are tables that store temporal data, such as historical records, snapshots, or logs.
  - Temporal databases are databases that support temporal data and operations, such as querying, updating, or deleting temporal data.
- Temporal data can be manipulated using different operations, such as temporal selection, temporal projection, temporal join, temporal aggregation, or temporal analysis.
  - Temporal selection is the operation of selecting data items that satisfy a temporal condition.
  - Temporal projection is the operation of extracting temporal attributes from data items.
  - Temporal join is the operation of combining data items that have overlapping or matching temporal values.
  - Temporal aggregation is the operation of summarizing or grouping data items based on temporal values.
  - Temporal analysis is the operation of discovering patterns, trends, or anomalies in temporal data.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated if the data stored in the database becomes stale or outdated due to the delay in data acquisition, transmission, processing, or updating.
- Temporal consistency can be measured by the temporal error, which is the difference between the actual value of a data item and the value stored in the database at a given time.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the occurrence of some events, such as a change in the value of a data item, a deadline of a transaction, or a request from a transaction.
  - Periodic updates, which are updates that are performed at regular intervals, regardless of the events that occur in the system.
  - Eager updates, which are updates that are performed as soon as possible after a change in the value of a data item occurs.
  - Lazy updates, which are updates that are performed only when a transaction requests to read a data item.
  - Concurrency control algorithms, which are algorithms that coordinate the access and update of data items by multiple transactions, such as locking, timestamping, or optimistic methods.



### Concurrency Control

- Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the database.
- Concurrency control is especially important for real-time database systems, where transactions have timing constraints and must be completed before their deadlines.
- Concurrency control in real-time database systems should consider both data consistency and timing constraints, and also adapt to changes in the operating environment and guarantee the completion of critical transactions.

### Concurrency Control Methods

- There are two main methods of concurrency control: locking-based and timestamp-based.
- Locking-based methods use locks to prevent concurrent transactions from accessing the same data item in conflicting modes (read or write). A lock is a mechanism that grants exclusive access to a data item to a transaction that requests it. Locks can be shared (for read-only access) or exclusive (for read or write access). Locks can also be applied at different levels of granularity, such as records, pages, tables, or databases.
- Timestamp-based methods use timestamps to order the transactions and ensure serializability. A timestamp is a unique identifier that reflects the start time or the priority of a transaction. Timestamps can be assigned by the system or by the application. Timestamps can be used to determine the precedence of transactions and resolve conflicts by aborting or delaying the transactions with later timestamps.
- Locking-based and timestamp-based methods have different advantages and disadvantages. Locking-based methods can avoid unnecessary aborts and ensure deadlock-freedom, but they may incur high overhead and blocking. Timestamp-based methods can avoid blocking and reduce overhead, but they may cause unnecessary aborts and starvation.

### Concurrency Control Protocols

- A concurrency control protocol is a set of rules that govern how transactions access and manipulate data items in a database. A concurrency control protocol should ensure serializability, which means that the concurrent execution of a set of transactions is equivalent to some serial execution of these transactions.
- There are many concurrency control protocols that have been proposed for real-time database systems, such as:
  - Two-phase locking (2PL): a locking-based protocol that requires a transaction to acquire all the locks it needs before releasing any lock. 2PL ensures serializability, but it may cause deadlocks, blocking, and priority inversion.
  - Timestamp ordering (TO): a timestamp-based protocol that orders the transactions according to their timestamps and ensures that the transactions access the data items in the same order. TO ensures serializability, but it may cause aborts, starvation, and inconsistency.
  - Optimistic concurrency control (OCC): a timestamp-based protocol that allows transactions to execute without locking and validates them at the end using their timestamps. OCC avoids blocking and reduces overhead, but it may cause aborts and inconsistency.
  - Priority ceiling protocol (PCP): a locking-based protocol that assigns a priority ceiling to each data item and prevents a transaction from locking a data item if its priority is lower than the ceiling. PCP ensures serializability, deadlock-freedom, and priority inheritance, but it may cause blocking and overhead.
  - High priority two-phase locking (HP-2PL): a locking-based protocol that allows high priority transactions to preempt low priority transactions and abort them if they hold conflicting locks. HP-2PL ensures serializability and timeliness, but it may cause aborts, starvation, and inconsistency.
  - Earliest deadline first concurrency control (EDF-CC): a timestamp-based protocol that assigns deadlines to transactions and orders them according to their deadlines. EDF-CC ensures serializability and timeliness, but it may cause aborts, starvation, and inconsistency.
  - Real-time optimistic concurrency control (RT-OCC): a timestamp-based protocol that combines OCC with EDF-CC and validates transactions according to their deadlines. RT-OCC avoids blocking and reduces overhead, but it may cause aborts and inconsistency.



### Overview of Commercial Real Time databases for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have different requirements than traditional databases, such as timeliness, predictability, concurrency control, recovery, and data consistency.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases are those that must guarantee a response within a specified deadline, otherwise the system may fail or cause severe consequences.
  - Soft real-time databases are those that can tolerate some degree of deadline misses, but still aim to provide the best possible performance.
- Some examples of commercial real-time databases are:
  - Raima Database Manager (RDM): a cross-platform, embedded, in-memory, SQL, and NoSQL database that supports hard and soft real-time applications.
  - Altus Group: a data and software provider that offers historical and current commercial real estate data, analytics, and valuation tools.
  - CoStar: a leading provider of commercial real estate information, analytics, and online marketplaces that covers over 5.5 million properties and 18 million tenants.
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service that supports real-time data synchronization and offline access for web and mobile applications.

