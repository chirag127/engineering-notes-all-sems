

# Real Time System

A real time system is a system that can process and respond to inputs or events within a specified time limit, called a deadline. The system must meet the deadline, otherwise it may cause a failure or a loss of performance. Real time systems are often used to control or monitor physical processes, such as industrial machines, robots, aircraft, or medical devices. 

Some key characteristics of real time systems are:

- Timeliness: The system must produce the correct output within the deadline, regardless of the workload or the complexity of the input.
- Time synchronization: The system must coordinate its actions with other systems or devices that have independent clocks and operate in parallel.
- Predictability: The system must behave consistently and reliably under all possible scenarios and conditions.
- Fault tolerance: The system must be able to handle errors or failures gracefully and recover quickly.

There are two main types of real time systems based on the severity of the deadline:

- Hard real time systems: These systems have absolute deadlines that must be met at all costs. A missed deadline can result in a catastrophic failure or a severe damage. For example, a flight control system, a nuclear reactor, or a pacemaker are hard real time systems.
- Soft real time systems: These systems have relative deadlines that can be occasionally missed without causing a major harm. However, a missed deadline can still degrade the quality or the performance of the system. For example, a video streaming, a voice recognition, or a gaming system are soft real time systems.

Some examples of real time systems are:

- Process control systems: These systems are used to control or regulate physical or chemical processes, such as temperature, pressure, flow, or level. They use sensors to measure the process variables and actuators to manipulate the process parameters. For example, a thermostat, a boiler, or a chemical plant are process control systems.
- Machine vision systems: These systems are used to help machines or robots to perceive and interpret visual data, such as images, videos, or patterns. They use cameras to capture the data and algorithms to process and analyze them. For example, a face recognition, a barcode scanner, or a self-driving car are machine vision systems.
- Robotics systems: These systems are used to create machines or devices that can perform tasks autonomously or semi-autonomously, such as movement, manipulation, or communication. They use sensors to detect the environment and actuators to execute the actions. For example, a robot arm, a drone, or a chatbot are robotics systems.



## Unit 1 - Introduction of Real Time System

A real-time system is a system that can process data and events within predictable and specific time constraints. Real-time systems are often used for applications that require high reliability, safety, and performance, such as flight control systems, industrial automation, robotics, and medical devices.

There are two main types of real-time systems based on their timing constraints:

- **Hard real-time systems**: These systems have absolute deadlines that must be met, otherwise a system failure or a catastrophic consequence will occur. For example, a missile guidance system must compute the correct trajectory and fire the missile within a certain time limit, otherwise the target may be missed or the missile may explode.
- **Soft real-time systems**: These systems have relative deadlines that can be occasionally missed, but the quality of service or the performance of the system will degrade. For example, a video streaming system must deliver the frames to the display device within a certain time limit, otherwise the video quality will be affected or the frames will be dropped.

A real-time system consists of hardware and software components that interact with each other and with the environment. A real-time system typically has the following components:

- **Real-time operating system (RTOS)**: This is a special type of operating system that can handle real-time tasks and events with minimal latency and overhead. An RTOS provides features such as preemptive scheduling, priority-based dispatching, inter-task communication, synchronization, and memory management.
- **Real-time application**: This is the software program that implements the real-time functionality and logic of the system. A real-time application consists of one or more real-time tasks or processes that execute on the RTOS. A real-time task or process has a priority, a deadline, and a set of input and output parameters.
- **Real-time hardware**: This is the physical device or platform that runs the RTOS and the real-time application. A real-time hardware can be a microcontroller, a microprocessor, a field-programmable gate array (FPGA), or a system-on-chip (SoC). A real-time hardware must have sufficient processing power, memory, and input/output (I/O) capabilities to meet the real-time requirements of the system.
- **Real-time environment**: This is the external context or situation that influences the behavior and performance of the real-time system. A real-time environment can be dynamic, unpredictable, noisy, or hostile. A real-time system must be able to sense, adapt, and respond to the changes and events in the real-time environment.



# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that performs information processing and responds to events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization).
- A real-time system can be classified into two types based on the severity of the consequences of missing the deadlines: hard real-time system and soft real-time system.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur. Examples are flight control systems, nuclear power plant control systems, etc .
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. Examples are videoconferencing systems, gaming computers, etc  .
- A real-time system can also be classified into two types based on the predictability of the events: periodic real-time system and aperiodic real-time system.
- A periodic real-time system has events that occur at regular intervals and have known deadlines. Examples are sensor data acquisition, audio/video processing, etc.
- An aperiodic real-time system has events that occur at irregular intervals and have unknown deadlines. Examples are keyboard inputs, mouse clicks, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the topic of typical real time applications for the notes of the unit 1 - introduction of real time system in the subject of real time system.

### Typical Real Time Applications

- A real time application is an application that provides services or performs tasks within a specified time constraint, usually in response to external events or stimuli.
- Real time applications are often used in domains where timeliness, reliability, and accuracy are critical, such as industrial control, aerospace, defense, telecommunications, multimedia, and e-commerce.
- Some examples of typical real time applications are:

  - **Digital control**: A digital control system uses sensors and actuators to monitor and manipulate physical processes, such as temperature, pressure, speed, or position. The system must react to the sensor inputs and generate appropriate actuator outputs within a fixed time interval, called the sampling period. Examples of digital control systems are thermostats, cruise control, autopilot, and robotics.
  - **Optimal control**: An optimal control system is a special type of digital control system that optimizes some performance criterion, such as minimizing energy consumption, maximizing profit, or minimizing error. The system must solve a complex mathematical problem within a given time limit, using the current and past sensor inputs and actuator outputs. Examples of optimal control systems are power management, inventory control, and trajectory planning.
  - **Command and control**: A command and control system is a system that coordinates the actions of multiple agents, such as humans, machines, or software, to achieve a common goal. The system must communicate with the agents, process the information, and generate commands or decisions within a specified time frame, depending on the urgency and importance of the situation. Examples of command and control systems are air traffic control, military operations, and emergency response.
  - **Signal processing**: A signal processing system is a system that transforms, analyzes, or enhances signals, such as sound, image, or video. The system must process the incoming signals and produce the desired output signals within a certain time interval, depending on the quality and latency requirements. Examples of signal processing systems are speech recognition, image processing, and video compression.
  - **Tracking**: A tracking system is a system that estimates the state or location of a moving object, such as a vehicle, a person, or a missile, based on noisy and incomplete measurements from sensors, such as radar, GPS, or camera. The system must update the state estimate and predict the future state within a fixed time interval, called the update period. Examples of tracking systems are navigation, surveillance, and missile guidance.
  - **Real time databases**: A real time database is a database that supports transactions with timing constraints, such as deadlines or priorities. The database must ensure that the transactions are executed and committed within their specified time limits, while maintaining the consistency and integrity of the data. Examples of real time databases are reservation systems, online auctions, and stock trading.
  - **Multimedia**: A multimedia system is a system that handles multiple types of media, such as text, audio, video, or graphics. The system must deliver the media content to the users or devices within a certain time interval, called the playback time, while ensuring the quality and synchronization of the media. Examples of multimedia systems are video conferencing, online gaming, and streaming services.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must respond to events within a certain time frame, otherwise it may fail to meet its requirements or cause undesirable consequences.
- A real-time system can be classified into two types: hard real-time and soft real-time.
- A hard real-time system is a system that must meet all its deadlines, otherwise it may cause catastrophic failure or severe damage. For example, a nuclear reactor control system, a pacemaker, or an air traffic control system are hard real-time systems.
- A soft real-time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server are soft real-time systems.
- A real-time system consists of a set of tasks that must be executed periodically or sporadically. Each task has a release time, an execution time, and a deadline.
- The release time of a task is the time when the task becomes ready to execute. The release time can be fixed or variable, depending on the type of the task.
- A periodic task is a task that has a fixed release time and a fixed period. The period is the time interval between two consecutive releases of the same task. For example, a task that reads a sensor every 10 milliseconds is a periodic task with a period of 10 milliseconds and a release time of 0, 10, 20, ... milliseconds.
- A sporadic task is a task that has a variable release time and a minimum inter-arrival time. The minimum inter-arrival time is the minimum time interval between two consecutive releases of the same task. For example, a task that handles a user input is a sporadic task with a minimum inter-arrival time of 1 second and a release time of 0, 1.5, 3.2, ... seconds.
- The execution time of a task is the time required for the task to complete its computation. The execution time can be fixed or variable, depending on the complexity of the task and the system load.
- The deadline of a task is the time by which the task must finish its execution. The deadline can be fixed or variable, depending on the requirements of the task and the system.
- A task can have different types of deadlines, such as implicit, explicit, or constrained.
- An implicit deadline is a deadline that is equal to the period or the minimum inter-arrival time of the task. For example, a periodic task with a period of 10 milliseconds has an implicit deadline of 10 milliseconds.
- An explicit deadline is a deadline that is specified separately from the period or the minimum inter-arrival time of the task. For example, a sporadic task with a minimum inter-arrival time of 1 second and an explicit deadline of 0.5 second has a deadline of 0.5 second after each release.
- A constrained deadline is a deadline that is less than or equal to the period or the minimum inter-arrival time of the task. For example, a periodic task with a period of 10 milliseconds and a constrained deadline of 8 milliseconds has a deadline of 8 milliseconds after each release.
- The release times of the tasks in a real-time system are important for the scheduling and analysis of the system. The scheduling of a real-time system is the process of assigning tasks to processors and determining the order of execution. The analysis of a real-time system is the process of verifying that the system can meet all its deadlines under certain assumptions and conditions.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes for the Unit 1 - Introduction of Real Time System are due on **Friday, March 24, 2023** by **11:59 PM**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in **Markdown** format and uploaded to the **course website** as a **single file** with the name **RTS_Unit1_Notes_YourName.md**.
- The notes should be **clear, concise, and comprehensive**, with proper use of **headings, lists, tables, code blocks, and equations**.
- The notes should include **references** to the **textbook** and any other **relevant sources** used for the preparation of the notes.
- The notes will be **graded** based on the following criteria:
  - Completeness and accuracy of the content
  - Organization and presentation of the notes
  - Quality and originality of the notes
  - Adherence to the format and deadline requirements
- The notes will count for **10%** of the final grade for the course.
- Late submissions will be **penalized** by **10%** per day of delay.
- No submissions will be accepted after **Monday, March 27, 2023** by **11:59 PM**.
- If you have any questions or concerns regarding the notes, please contact the **instructor** or the **teaching assistant** as soon as possible.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must produce the correct results within a specific time frame, otherwise it may cause undesirable consequences or failures .
- Timing constraints are the requirements that specify the deadlines or the acceptable ranges of response times for the real-time system .
- Timing constraints are essential for ensuring the timeliness and the correctness of the real-time system, as well as for designing, testing, and verifying the system .
- Timing constraints can be classified into two categories: performance constraints and behavioral constraints.
  - Performance constraints are the constraints that define the desired or acceptable response times of the system, such as the maximum, minimum, average, or probabilistic response times.
  - Behavioral constraints are the constraints that define the temporal relationships or dependencies among the events, tasks, or data in the system, such as the precedence, periodicity, synchronicity, or freshness constraints.
- Timing constraints can be expressed using various constructs, such as temporal logic, interval algebra, or graphical notations.
  - Temporal logic is a formal language that can specify the logical and temporal properties of the system using operators such as always, eventually, until, or next.
  - Interval algebra is a mathematical framework that can specify the temporal relations between intervals using symbols such as before, after, meets, overlaps, or contains.
  - Graphical notations are visual representations that can specify the timing constraints using diagrams, charts, or graphs, such as state transition diagrams, Gantt charts, or timing diagrams.
- Timing constraints can be validated using various methods, such as simulation, testing, or verification.
  - Simulation is a technique that can model the behavior of the system under different scenarios and observe the response times and the temporal relations of the system.
  - Testing is a technique that can execute the system under different inputs and measure the actual response times and the temporal relations of the system.
  - Verification is a technique that can prove the correctness of the system with respect to the timing constraints using formal methods, such as model checking, theorem proving, or static analysis.



### Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- Examples of hard real time systems are nuclear power plant control, air traffic control, missile guidance, pacemakers, etc.
- A hard real time system requires a high degree of coordination, both within and across devices, and may use technologies such as Time Sensitive Networking (TSN) and Time Coordinated Computing (TCC)  .
- A hard real time system may have different levels of criticality, depending on the consequences of missing a deadline. For example, a level A system is the most critical and must never miss a deadline, while a level E system is the least critical and can tolerate occasional deadline misses .
- A hard real time system may use different scheduling algorithms to allocate resources and tasks, such as rate monotonic, earliest deadline first, least laxity first, etc. .
- A hard real time system may face different challenges, such as unpredictability, concurrency, resource contention, fault tolerance, security, etc. .



### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a failure or a significant degradation of the system performance  .
- A soft real-time system has a **small window of time** for program completion rather than a precise moment due to a bit of jitter from the operating system.
- A soft real-time system can be run on **multiple cores** and impose fewer restrictions on applications.
- A soft real-time system can continue to function even if it has missed its deadline, though with undesirable lower quality of output.
- A soft real-time system is typically used to solve issues of **concurrent access** and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications.
  - Online gaming platforms.
  - Multimedia systems.



### Reference Models for Real Time Systems

A reference model is a canonical form that describes the essential features and properties of a system, without specifying the implementation details. A reference model can help us to reason about the system, to compare different systems, and to design new systems.

A reference model for real time systems consists of three main elements:

- A workload model that describes the applications supported by the system, such as the tasks, the events, the deadlines, the data, and the quality of service requirements.
- A resource model that describes the available system resources, such as the processors, the memory, the communication channels, the sensors, and the actuators.
- A set of algorithms that define how the system resources are used to execute the applications, such as the scheduling, the synchronization, the communication, the fault tolerance, and the adaptation.

A reference model can be used to analyze the performance, the correctness, the reliability, and the adaptability of a real time system. It can also be used to compare different real time systems or to design new ones.

One example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which is suitable for many software-intensive, real-time computing control problem domains. It defines the types of functions needed in a real-time intelligent control system, and how these functions relate to each other. The RCS architecture combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .

Another example of a reference model for real time systems is the Real-Time CORBA (RT-CORBA) specification, which is an extension of the Common Object Request Broker Architecture (CORBA) standard for distributed object computing. It defines the interfaces and services that enable the development of distributed real time systems using the object-oriented paradigm. The RT-CORBA specification supports the specification and enforcement of quality of service parameters, such as the priority, the deadline, the latency, and the bandwidth, for the communication between the distributed objects.



### Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. A resource can be preemptable or non-preemptable. Example: memory, file, printer, semaphore.
- A real-time system must manage the allocation and scheduling of processors and resources to meet the timing constraints of the tasks. A real-time operating system (RTOS) is an operating system that serves real-time applications that process data without any buffering delay. An RTOS provides mechanisms for task creation, synchronization, communication, and scheduling .
- A real-time system can be classified into two types based on the criticality of the timing constraints: hard real-time system and soft real-time system. A hard real-time system is one that must meet all the deadlines, otherwise it may cause catastrophic consequences. A soft real-time system is one that can tolerate some deadline misses, but the quality of service may degrade .
- A real-time system can also be classified into two types based on the predictability of the task arrival: periodic and aperiodic. A periodic task is one that arrives at regular intervals and has a fixed execution time and deadline. An aperiodic task is one that arrives at irregular intervals and may have a variable execution time and deadline.
- A real-time system can use different scheduling algorithms to assign processors and resources to the tasks. Some of the common scheduling algorithms are: rate-monotonic scheduling, earliest deadline first scheduling, least laxity first scheduling, priority ceiling protocol, and resource reservation protocol.
- A real-time system can also use different techniques to improve the performance and reliability of the system. Some of the common techniques are: fault tolerance, redundancy, replication, checkpointing, and recovery.
- A real-time system can also use different technologies to enable precise time synchronization and communication among the system components. Some of the common technologies are: time-sensitive networking (TSN), time-coordinated computing (TCC), and real-time configuration and optimization (RCO) .



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The earliest time at which the job can start execution.
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which the job must finish execution.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for the job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval ([r<sub>i</sub>, d<sub>i</sub>])**: The time interval in which the job can be feasibly executed. It is equal to [r<sub>i</sub>, r<sub>i</sub> + D<sub>i</sub>].
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from the system model or the environment .
- The temporal parameters of a job can be fixed or variable, depending on the nature of the real time system and the workload.
- The temporal parameters of a job can affect the schedulability, performance, and correctness of the real time system .



### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline .
- Phase is the time at which the first instance of the task is released.
- Period is the time interval between two consecutive releases of the task.
- Execution time is the worst-case time required by the task to complete its execution.
- Deadline is the time by which the task must finish its execution.
- The periodic task model is a deterministic workload model that accurately represents many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- The periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a task may vary within a certain range from the exact start time of the period.




Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of precedence constraints and data dependency in real time systems.

### Precedence Constraints and Data Dependency

- Precedence constraints are the restrictions on the order of execution of jobs in a real time system. They are usually represented by a directed graph called a precedence graph, where the vertices are the jobs and the edges indicate the precedence relations.  
- Data dependency is the situation where the output of one job is used as the input of another job in a real time system. Data dependency cannot be captured by a precedence graph, as it does not imply a fixed order of execution. Data dependency may cause synchronization and communication issues among jobs.  
- Some examples of precedence constraints and data dependency are:
  - A job that controls the brakes of a car must execute before a job that displays the speed on the dashboard. This is a precedence constraint, as the order of execution is fixed and crucial for safety. 
  - A job that reads the temperature from a sensor must execute before a job that adjusts the thermostat based on the temperature. This is a data dependency, as the output of the first job is the input of the second job. However, the order of execution is not fixed, as long as the data is available when needed. 




## Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints. Real time scheduling aims to ensure that tasks meet their deadlines, avoid interference, and optimize system performance. Real time scheduling is used in applications such as embedded systems, robotics, multimedia, and industrial control.

Some of the topics covered in this unit are:

- Real time system components: A real time system consists of the scheduler, clock, and the processing hardware elements. The scheduler is responsible for selecting the next task to run based on the scheduling algorithm and the task parameters. The clock provides the time reference for the system and the tasks. The processing hardware elements include the CPU, memory, and I/O devices that execute the tasks and handle the interrupts. 
- Real time task models: A real time task is characterized by its arrival time, execution time, deadline, period, priority, and resource requirements. A real time task can be periodic, aperiodic, or sporadic depending on its arrival pattern. A real time task can also be hard, firm, or soft depending on its deadline requirement. A hard real time task must meet its deadline, otherwise the system fails. A firm real time task can miss its deadline, but the result is useless. A soft real time task can miss its deadline, but the result is still acceptable with some degradation. 
- Real time scheduling algorithms: A real time scheduling algorithm is a rule that determines which task to execute at any given time. There are two types of real time scheduling algorithms: static and dynamic. Static scheduling algorithms assign priorities to tasks before the system starts and do not change them during the system execution. Dynamic scheduling algorithms assign priorities to tasks at run time based on their current parameters and system state. Some examples of real time scheduling algorithms are rate monotonic, earliest deadline first, least laxity first, and round robin. 
- Real time scheduling analysis: Real time scheduling analysis is the process of verifying and evaluating the schedulability and performance of a real time system under a given scheduling algorithm and task set. Real time scheduling analysis can be done by using mathematical methods, simulation tools, or empirical testing. Real time scheduling analysis can help to determine the feasibility, utilization, response time, deadline miss ratio, and throughput of a real time system.



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution time to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that the tasks meet their timing requirements and that the system is predictable and correct. There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the performance criteria. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, and period, are known at design time. In this approach, a static schedule is computed offline, based on the worst-case execution time of the tasks, and stored in a table. The table specifies the start time and the end time of each task in each cycle. A timer interrupts the system at regular intervals and triggers the execution of the tasks according to the table. The advantage of this approach is that it is simple, predictable, and avoids overheads of dynamic scheduling. The disadvantage is that it is inflexible, wasteful of resources, and cannot handle aperiodic or sporadic tasks.

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft or firm real time systems, where the properties of the tasks may vary at run time or may not be known in advance. In this approach, each task is assigned a priority, which may be static or dynamic, and the scheduler selects the highest priority task to run at each scheduling point. The scheduling points are usually the arrival or completion of a task, or a preemption by a higher priority task. The advantage of this approach is that it is flexible, adaptive, and can handle different types of tasks. The disadvantage is that it may incur higher overheads, complexity, and unpredictability.

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority and are scheduled in a circular order. Each task is allocated a fixed time slice, called quantum, to run. If a task finishes before its quantum expires, it relinquishes the processor to the next task in the queue. If a task does not finish within its quantum, it is preempted and moved to the end of the queue. The advantage of this approach is that it is simple, fair, and easy to implement. The disadvantage is that it does not consider the timing requirements of the tasks and may cause deadline misses or poor response time.

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different weights and are allocated proportional time slices based on their weights. For example, a task with weight 2 will get twice as much time as a task with weight 1. The advantage of this approach is that it can differentiate the tasks based on their importance or resource demand. The disadvantage is that it still does not consider the timing requirements of the tasks and may cause deadline misses or poor response time.

- **Earliest deadline first (EDF) approach**: This approach is a dynamic priority-driven approach, where the priority of a task is inversely proportional to its absolute deadline. The task with the earliest deadline has the highest priority and is scheduled first. The priority of a task may change over time, as new tasks arrive or existing tasks complete. The advantage of this approach is that it is optimal for preemptive scheduling, meaning that it can schedule any set of tasks that is feasible, i.e., that can meet all their deadlines. The disadvantage is that it may cause high preemption overhead, priority inversion, and deadline misses in overload situations.

- **Least slack time (LST) approach**: This approach is another dynamic priority-driven approach, where the priority of a task is inversely proportional to its slack time. The slack time of a task is the difference between its deadline and its remaining execution time. The task with the least slack time has the highest priority and is scheduled first. The priority of a task may change over time, as new tasks arrive or existing tasks execute. The advantage of this approach is that it is optimal for non-preemptive scheduling, meaning that it can schedule any set of tasks that is feasible without preemption. The disadvantage is that it may cause high blocking time, priority inversion, and deadline misses in overload situations.



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a static schedule offline, before the system starts to execute, and follows the schedule at runtime.
- A static schedule is a sequence of scheduling decisions that specifies which job executes on which processor at any given time.
- A periodic static schedule is a cyclic schedule that repeats itself after a fixed period of time .
- This approach to scheduling hard real-time jobs is called the clock-driven or time-driven approach because each scheduling decision is made at a specific time, independent of events, such as job releases and completions, in the system.
- It is easy to see why a clock-driven system never exhibits the anomalous timing behavior of priority-driven systems.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling has some drawbacks, such as:
  - It may not be able to handle aperiodic or sporadic jobs well.
  - It may not be able to adapt to dynamic changes in the system, such as faults, overloads, or resource variations.
  - It may incur high overhead due to frequent context switches and clock interrupts.
  - It may waste processor time due to idle slots or fragmentation.



### Weighted Round Robin Approach

- The weighted round robin (WRR) algorithm is a variant of the basic round robin (RR) algorithm that assigns different weights to different jobs based on their importance or priority.
- The WRR algorithm has been used for scheduling real-time traffic in high-speed switched networks, where different types of packets may have different quality of service (QoS) requirements .
- The WRR algorithm works as follows:
  - Each job in the ready queue is assigned a weight that represents its share of the processor time. The weight can be a fixed value or a dynamic value that changes over time.
  - The algorithm maintains a pointer that points to the current job in the queue. The pointer is initialized to point to the first job in the queue.
  - The algorithm allocates the processor to the current job for a time slice that is proportional to its weight. For example, if the weight of the current job is 3 and the time slice unit is 1 millisecond, then the job gets 3 milliseconds of processor time.
  - After the time slice expires, the algorithm moves the pointer to the next job in the queue and repeats the process. If the pointer reaches the end of the queue, it wraps around to the beginning of the queue.
  - The algorithm continues this cycle until all the jobs in the queue are completed or preempted by a higher priority job.
- The advantages of the WRR algorithm are:
  - It is simple and easy to implement.
  - It can handle different types of jobs with different QoS requirements by adjusting their weights.
  - It can provide fairness and balance among the jobs by giving them proportional shares of the processor time.
- The disadvantages of the WRR algorithm are:
  - It may cause starvation or delay for some jobs if their weights are too low compared to other jobs.
  - It may not be optimal for some real-time systems where the deadlines of the jobs are more important than their weights.
  - It may not be suitable for some real-time systems where the jobs have variable execution times or arrival rates, as the weights may not reflect the actual workload of the jobs.



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state and events.
- Priority-driven scheduling can be applied to both periodic and aperiodic tasks.
- Periodic tasks are tasks that have a fixed period and deadline and are activated at regular intervals.
- Aperiodic tasks are tasks that have a variable period and deadline and are activated by unpredictable events.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 can benefit from priority-driven scheduling by using a middleware layer that supports different quality of service (QoS) policies for different topics and nodes.
- QoS policies can specify the priority, reliability, durability, and deadline of the messages exchanged between nodes.
- Priority-driven scheduling can also be implemented by using a real-time operating system (RTOS) that supports priority inheritance and priority ceiling protocols.
- Priority inheritance is a mechanism that allows a lower-priority task to temporarily inherit the priority of a higher-priority task that is blocked by a shared resource.
- Priority ceiling is a mechanism that assigns a ceiling priority to each shared resource and prevents a lower-priority task from accessing the resource if a higher-priority task is ready.
- These mechanisms can prevent priority inversion, which is a situation where a higher-priority task is delayed by a lower-priority task that holds a shared resource.



### Dynamic Versus Static Systems

- A **static system** is one that has a fixed set of tasks and a predefined schedule for executing them. A static system does not change its behavior or structure in response to external events or inputs. A static system can be validated before execution and can guarantee the timing constraints of the tasks. However, a static system may not be able to handle unpredictable or variable workloads, and may have poor performance in terms of resource utilization and overall response time. Static systems are suitable for hard real-time systems that require strict predictability and reliability .
- A **dynamic system** is one that can adapt its behavior or structure in response to external events or inputs. A dynamic system does not have a fixed set of tasks or a predefined schedule for executing them. A dynamic system can handle unpredictable or variable workloads, and may have better performance in terms of resource utilization and overall response time. However, a dynamic system may not be able to guarantee the timing constraints of the tasks, and may be difficult to validate or verify. Dynamic systems are suitable for soft real-time systems that can tolerate some degree of uncertainty and flexibility .
- **Real-time scheduling** is the process of assigning tasks to processors or resources in a real-time system, such that the timing constraints of the tasks are met. Real-time scheduling can be classified into two types: **static scheduling** and **dynamic scheduling** .
- **Static scheduling** is a type of real-time scheduling that assigns priorities to tasks before the system runs, based on their characteristics and requirements. Static scheduling does not change the priorities of tasks during execution, and follows a predetermined order of execution. Static scheduling can guarantee the timing constraints of the tasks, if the system is feasible and schedulable. Static scheduling is suitable for real-time systems that have a fixed and known set of tasks, and do not need to react to external events or inputs. Examples of static scheduling algorithms are **rate-monotonic scheduling** and **deadline-monotonic scheduling** .
- **Dynamic scheduling** is a type of real-time scheduling that assigns priorities to tasks as the system runs, based on their current state and the system conditions. Dynamic scheduling can change the priorities of tasks during execution, and adapts to the changing workload and environment. Dynamic scheduling can handle unpredictable or variable workloads, and may improve the performance of the system. However, dynamic scheduling may not guarantee the timing constraints of the tasks, and may be complex and costly to implement. Dynamic scheduling is suitable for real-time systems that have a variable and unknown set of tasks, and need to react to external events or inputs. Examples of dynamic scheduling algorithms are **earliest deadline first scheduling** and **least laxity first scheduling** .



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems.
- EDF assigns priorities to tasks based on their absolute deadlines. The earlier the deadline, the higher the priority.
- LST assigns priorities to tasks based on their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The smaller the slack, the higher the priority.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. This means that EDF can schedule any set of tasks that is schedulable by any other algorithm.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. This means that LST can schedule any set of tasks that is schedulable by any other algorithm that respects the precedence constraints.
- However, EDF and LST are not optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements. In these cases, EDF and LST may miss some deadlines or under-utilize the CPU.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a static priority scheduling algorithm for periodic tasks in real-time systems.
- RMA assigns priorities to tasks based on their periods, with shorter periods having higher priorities.
- RMA is optimal for preemptive scheduling of periodic tasks with fixed deadlines, meaning that it can always find a feasible schedule if one exists.
- RMA has some advantages over other scheduling algorithms, such as simplicity, predictability, and low overhead.
- RMA also has some limitations, such as not being suitable for tasks with variable periods, deadlines, or execution times, or for tasks with shared resources or dependencies.
- RMA can be analyzed using the utilization bound test and the response time analysis to determine the schedulability of a set of tasks.
- The utilization bound test is a sufficient but not necessary condition for schedulability, meaning that it can reject some feasible schedules.
- The utilization bound test states that a set of n periodic tasks with utilization U is schedulable by RMA if U <= n(2^(1/n) - 1), where U = sum(Ci/Ti) for all tasks i, Ci is the worst-case execution time of task i, and Ti is the period of task i.
- The response time analysis is a necessary and sufficient condition for schedulability, meaning that it can accept all feasible schedules and reject all infeasible ones.
- The response time analysis computes the worst-case response time of each task by considering the interference from higher priority tasks and the execution time of the task itself.
- The response time analysis states that a task i is schedulable by RMA if Ri <= Di, where Ri is the worst-case response time of task i, and Di is the deadline of task i.
- The worst-case response time of task i can be calculated iteratively using the formula Ri = Ci + sum(ceil(Ri/Tj) * Cj) for all tasks j with higher priority than i, where ceil(x) is the smallest integer greater than or equal to x. The iteration stops when Ri converges or exceeds Di.



### Offline Versus Online Scheduling

- Offline scheduling is a technique where the scheduling decisions are made before the system starts to execute. It requires the prior knowledge of the task parameters, such as arrival times, execution times, deadlines, resource requirements, etc. It generates a static schedule that is followed by the system at run-time. It is suitable for periodic and predictable tasks that have fixed deadlines and resource demands. It is also called clock-driven or table-driven scheduling .
- Online scheduling is a technique where the scheduling decisions are made during the system execution. It does not require the complete knowledge of the task parameters, but it can adapt to the dynamic changes in the system, such as task arrivals, preemptions, resource availability, etc. It generates a dynamic schedule that is updated by the system at run-time. It is suitable for aperiodic and unpredictable tasks that have variable deadlines and resource demands. It is also called event-driven or priority-driven scheduling .
- The advantages of offline scheduling are that it can guarantee the schedulability of all the tasks, it can optimize the system performance, and it can reduce the scheduling overhead. The disadvantages of offline scheduling are that it cannot handle the uncertainties and variations in the system, it cannot accommodate new tasks or changes in the task parameters, and it requires a lot of computation and memory to generate and store the schedule.
- The advantages of online scheduling are that it can handle the uncertainties and variations in the system, it can accommodate new tasks or changes in the task parameters, and it requires less computation and memory to generate and update the schedule. The disadvantages of online scheduling are that it cannot guarantee the schedulability of all the tasks, it cannot optimize the system performance, and it can increase the scheduling overhead.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the highest priority job to execute at any time. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign fixed time slots to jobs based on their arrival patterns and execution times. The scheduler follows a pre-computed schedule that is periodically repeated. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven and clock driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs.
- In priority driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: background scheduling and slack stealing.
  - Background scheduling assigns the lowest priority to aperiodic and sporadic jobs, and executes them only when no periodic job is ready. This ensures that periodic jobs always meet their deadlines, but may result in poor response time for aperiodic and sporadic jobs.
  - Slack stealing assigns higher priority to aperiodic and sporadic jobs, and executes them by using the available slack time of periodic and sporadic jobs. Slack time is the amount of time that a job can be delayed without affecting the schedulability of other jobs. This improves the response time of aperiodic and sporadic jobs, but may require complex algorithms to compute and track the slack time.
- In clock driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: spare capacity scheduling and overloading.
  - Spare capacity scheduling reserves some time slots in the schedule for aperiodic and sporadic jobs, and executes them in a first-come first-served or priority based order. This guarantees some responsiveness for aperiodic and sporadic jobs, but may result in underutilization of the processor if the reserved slots are not used.
  - Overloading allows aperiodic and sporadic jobs to preempt periodic jobs in some time slots, and executes them in a priority based order. This improves the responsiveness of aperiodic and sporadic jobs, but may require online feasibility analysis to ensure that periodic jobs can still meet their deadlines.



## Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, and network bandwidth, available to multiple users or processes.

Some of the benefits of resource sharing are:

- It can improve the efficiency and performance of the system by reducing duplication and waste of resources.
- It can enhance the functionality and usability of the system by providing access to a wider range of resources and services.
- It can promote collaboration and communication among users by enabling them to share information and work together.

Some of the challenges of resource sharing are:

- It can increase the complexity and cost of the system by requiring additional hardware, software, and network infrastructure to support resource sharing.
- It can introduce security and privacy risks by exposing the resources and data of the system to unauthorized or malicious users or processes.
- It can create conflicts and competition among users or processes by requiring coordination and allocation of the shared resources.

Some of the methods of resource sharing are:

- Centralized resource sharing: In this method, the resources of a single computer system are shared among multiple users or processes. For example, a mainframe computer can provide access to its CPU, memory, disk, and printer to multiple terminals connected to it.
- Distributed resource sharing: In this method, the resources of multiple computer systems are shared among multiple users or processes. For example, a peer-to-peer network can allow users to share files, music, and videos among their computers.
- Virtualized resource sharing: In this method, the resources of a computer system are abstracted and presented as virtual resources that can be shared among multiple users or processes. For example, a cloud computing platform can provide virtual machines, storage, and network services to multiple applications running on different devices.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a processor, a memory, a device, or a communication channel .
- Resource contention affects the execution behavior and schedulability of jobs or tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock  .
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for a resource is granted and how jobs or tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the real-time system  .
- RAC can be classified into two categories: non-preemptive and preemptive .
  - Non-preemptive RAC means that once a job or task acquires a resource, it cannot be preempted by another job or task until it releases the resource .
  - Preemptive RAC means that a job or task can be preempted by another job or task with higher priority while holding a resource, and resume the resource when it resumes execution .
- Some examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive RAC: Multiprocessor Priority Ceiling Protocol (MPCP), Multiprocessor Stack Resource Policy (MSRP), Multiprocessor Priority Inheritance Protocol (MPIP), etc .
- The choice of RAC protocol depends on the characteristics of the real-time system, such as the number and type of resources, the number and type of jobs or tasks, the priority assignment, the scheduling algorithm, the system architecture, etc .
- The performance of RAC protocols can be evaluated by metrics such as blocking time, response time, schedulability, utilization, overhead, etc .



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- This implies that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand.
  - They prevent deadlock, since no job is ever preempted when it holds any resource.
- The disadvantages of non-preemptive critical sections are:
  - They may cause priority inversion, since a high-priority job may have to wait for a low-priority job to finish its critical section.
  - They may cause blocking, since a job may have to wait for a resource that is held by another job.
  - They may reduce the schedulability and utilization of the system, since the critical sections are executed at the highest priority and may delay other jobs.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for resolving the problem of priority inversion in real-time systems.
- Priority inversion occurs when a higher-priority task is blocked by a lower-priority task that holds a shared resource, and the lower-priority task is preempted by a medium-priority task that does not need the resource.
- Priority-inheritance protocol works by temporarily raising the priority of the lower-priority task that holds the resource to the priority of the highest-priority task that is waiting for the resource. This way, the lower-priority task can finish its critical section and release the resource, allowing the higher-priority task to resume.
- Priority-ceiling protocol works by assigning a ceiling priority to each resource, which is the highest priority of any task that can access the resource. A task can only lock a resource if its priority is higher than the ceiling priority of all the resources that are currently locked by other tasks. This way, the priority-ceiling protocol prevents a lower-priority task from locking a resource that is needed by a higher-priority task, and avoids blocking by a free resource.
- The differences between the priority-inheritance and priority-ceiling protocols are:
  - Priority-inheritance is greedy, while priority-ceiling is not. The priority-inheritance protocol lets the requesting task have a resource whenever the resource is free, but the priority-ceiling protocol may deny the requesting task the resource even when the resource is free, if the task's priority is lower than the ceiling priority of another locked resource.
  - Priority-inheritance may cause chained blocking, while priority-ceiling does not. Chained blocking occurs when a task is blocked by another task that is blocked by another task, and so on. The priority-inheritance protocol may cause chained blocking if multiple resources are locked by different tasks with different priorities, but the priority-ceiling protocol prevents chained blocking by ensuring that a task can only lock one resource at a time, and that the resource has the highest ceiling priority among all the resources.
  - Priority-inheritance may cause deadlock, while priority-ceiling does not. Deadlock occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed. The priority-inheritance protocol may cause deadlock if there is a circular dependency among the tasks and the resources, but the priority-ceiling protocol prevents deadlock by ensuring that a task can only lock a resource if its priority is higher than the ceiling priority of all the resources that are currently locked by other tasks.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its current priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its current priority is restored to its original priority, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its current priority is higher than the current priority of the other task.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock.
  - It bounds the blocking time of each task by the worst-case execution time of the critical sections of the tasks with lower priority ceilings.
  - It allows tasks to share a run-time stack, which reduces the memory requirement and the context switch overhead.
  - It reduces the number of preemptions and migrations compared to OCPP.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP works by temporarily raising the priority of a task that accesses a shared resource to the highest priority of any task that may access the same resource.
- ICPP works by raising the priority of a task that accesses a shared resource to the ceiling priority of the resource, which is the highest priority of any task that may access the resource.
- In a dynamic priority system, the priorities of the tasks may change over time, but the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may also change over time, depending on the current priorities of the tasks that may access them .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses, provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- An example of a dynamic priority system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline-driven system is shown below :

```
|<--T1-->|<--T2-->|<--T1-->|<--T2-->|<--T1-->|<--T2-->|
0        2        4        5        7        9        11
```

- Suppose the tasks share a resource X, and T1 accesses X from time 1 to 2, and T2 accesses X from time 6 to 7 .
- The priority ceiling of X is 1 from time 0 to 4, and becomes 2 from time 4 to 5, and so on .
- Using OCPP, T1 will raise its priority to 1 when it accesses X, and T2 will raise its priority to 2 when it accesses X .
- Using ICPP, T1 will raise its priority to the ceiling priority of X, which is 1 from time 0 to 4, and 2 from time 4 to 5, and so on .
- In both cases, no deadlock or priority inversion will occur, as the tasks will always access the resource in priority order .



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a resource access control protocol for real-time systems that use fixed priority scheduling.
- The protocol assigns a preemption ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the preemption ceiling of all the resources currently locked by other tasks.
- This ensures that a task is never blocked by a lower priority task, and prevents deadlock and chained blocking.
- The protocol also raises the priority of a task that locks a resource to the preemption ceiling of that resource, to prevent preemption by unrelated higher priority tasks.
- The protocol guarantees that the blocking time of a task is at most the execution time of the critical section of the highest priority task that shares a resource with it.
- The protocol can be implemented statically or dynamically, depending on whether the preemption ceilings are assigned at design time or run time.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that have more than one unit of the same type, such as printers, disks, or CPUs.
- Access control in multiple-unit resources is the problem of ensuring that jobs that request a unit of a resource are granted one in a timely and fair manner, without causing deadlocks or priority inversions.
- Access control in multiple-unit resources can be classified into two categories: static and dynamic.
  - Static access control assigns a fixed number of units of a resource to each job or task, based on its worst-case resource demand. Static access control is simple and predictable, but may waste resources or fail to meet the demand of some jobs.
  - Dynamic access control allows jobs to request and release units of a resource at run-time, based on their actual resource demand. Dynamic access control is more flexible and efficient, but may introduce complexity and unpredictability in the system.
- Some of the protocols for dynamic access control in multiple-unit resources are:
  - The Priority Inheritance Protocol (PIP): This protocol allows a job that is blocked by a lower-priority job that holds a unit of a resource to inherit the priority of the blocked job, until it releases the resource. This protocol prevents priority inversion, but may cause deadlock or chain blocking.
  - The Priority Ceiling Protocol (PCP): This protocol assigns a priority ceiling to each resource, which is the highest priority of any job that may request that resource. A job can lock a resource only if its priority is higher than the priority ceiling of all the resources currently locked by other jobs. This protocol prevents deadlock and bounds the blocking time of each job, but may cause unnecessary blocking or resource underutilization.
  - The Stack Resource Policy (SRP): This protocol maintains a stack of the jobs that have locked or requested a resource, ordered by their original priority. A job can lock a resource only if its original priority is higher than the original priority of the job at the top of the stack. This protocol prevents deadlock and bounds the blocking time of each job, and also allows resource nesting and preemption.



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in inconsistent or incorrect data values.
- To ensure data consistency and correctness, concurrent accesses to data objects must be controlled by some synchronization mechanisms.
- The synchronization mechanisms must also consider the timing constraints of the jobs, as blocking or delaying a job may cause it to miss its deadline.
- There are different types of synchronization mechanisms for controlling concurrent accesses to data objects, such as:
  - Lock-based protocols: A job must acquire a lock on a data object before accessing it, and release the lock after finishing the access. The lock can be exclusive (for write access) or shared (for read access). There are different lock-based protocols that vary in how they handle lock conflicts, such as priority inheritance, priority ceiling, and convex ceiling protocols.
  - Timestamp-based protocols: A job is assigned a timestamp when it is released, and the timestamp determines the order of access to data objects. A job can access a data object only if its timestamp is smaller than the timestamp of the last writer of the data object. There are different timestamp-based protocols that vary in how they handle timestamp conflicts, such as wait-die, wound-wait, and optimistic protocols.
  - Validation-based protocols: A job can access data objects without any synchronization, but it must validate its read set and write set before committing the changes. The validation ensures that the data values are consistent and no conflicts have occurred. There are different validation-based protocols that vary in how they perform the validation, such as two-phase locking, two-phase commit, and multiversion protocols.
- The choice of synchronization mechanism depends on the characteristics of the real time system, such as the number and type of data objects, the frequency and duration of accesses, the priority and deadline of jobs, and the performance and overhead requirements.
- The synchronization mechanism should aim to achieve the following objectives:
  - Data consistency: The data values should reflect the correct and logical state of the system, and no data corruption or inconsistency should occur due to concurrent accesses.
  - Timing correctness: The jobs should meet their deadlines, and no unnecessary blocking or aborting should occur due to synchronization.
  - Concurrency: The jobs should be able to access data objects concurrently as much as possible, and no unnecessary serialization or waiting should occur due to synchronization.
  - Adaptability: The synchronization mechanism should be able to adapt to changes in the system state, such as workload, resource availability, and failure conditions.
  - Efficiency: The synchronization mechanism should have low overhead in terms of time, space, and communication, and should not degrade the system performance or throughput.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real-Time Database Systems
: Controlling Concurrent Access to Data Objects - Bench Partner
: Concurrency Control in Real-Time Database Systems



## Unit 4 - Real Time Communication

- Real-time communication (RTC) is a category of software protocols and communication hardware media that gives real-time guarantees, which is necessary to support real-time guarantees of real-time computing.
- Real-time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.
- Real-time communication is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays.
- In real-time communication, there is always a direct path between the source and the destination.
- Some examples of real-time communication are voice calls, video calls, instant messaging, online gaming, live streaming, and telepresence.
- Real-time communication can be achieved using various technologies, such as WebRTC, SIP, RTP, RTCP, RTSP, WebSocket, and MQTT.
- Real-time communication can offer benefits such as improved collaboration, productivity, customer service, and user experience.
- Real-time communication can also pose challenges such as security, privacy, scalability, interoperability, and quality of service.



### Basic Concepts in Real Time Communication

Real time communication (RTC) is a mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Streaming media and live broadcasting

Some of the basic concepts in real time communication are:

- Bandwidth: The amount of data that can be transmitted or received per unit of time. Bandwidth is measured in bits per second (bps) and affects the quality and speed of RTC.
- Latency: The time it takes for a data packet to travel from the source to the destination. Latency is measured in milliseconds (ms) and affects the responsiveness and synchronicity of RTC.
- Jitter: The variation in latency of data packets. Jitter is caused by network congestion, routing changes, or other factors. Jitter can cause glitches, delays, or loss of data in RTC.
- Packet loss: The percentage of data packets that are lost or corrupted during transmission. Packet loss can occur due to network errors, congestion, or interference. Packet loss can degrade the quality and reliability of RTC.
- Encoding and decoding: The process of converting analog signals (such as sound or video) into digital data (such as bits or bytes) and vice versa. Encoding and decoding are done by codecs, which are software or hardware components that compress and decompress data. Codecs affect the bandwidth, quality, and compatibility of RTC.
- Protocols: The rules and standards that govern how data is transmitted and received over a network. Protocols define the format, structure, and sequence of data packets, as well as the methods for error detection and correction. Some common protocols for RTC are RTP, RTCP, SIP, and WebRTC.
- Security: The protection of data and communication from unauthorized access, modification, or disclosure. Security is achieved by using encryption, authentication, and authorization techniques. Security is important for RTC to ensure privacy, confidentiality, and integrity of data and communication.



### Soft and Hard Real-Time Communication Systems

Real-time communication systems are systems that exchange information between two or more entities within a specified time bound. These systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT). The difference between a hard and soft real-time communication system is the consequences of incorrect operation.

- Hard Real-Time Communication Systems
  - A hard real-time communication system is a system that must meet its deadlines for every message or task, otherwise it may cause catastrophic failure or unacceptable loss. For example, a communication system for a nuclear power plant or a flight control system must be hard real-time, as any delay or error could result in severe damage or loss of life.
  - A hard real-time communication system is deterministic, meaning that it can guarantee the worst-case execution time and response time for every message or task. It also has strict priority and scheduling policies to ensure that the most critical messages or tasks are always executed first and without interference from lower priority ones.
  - A hard real-time communication system requires high reliability, fault tolerance, and security, as any malfunction or attack could compromise its functionality and safety. It also requires low latency, high bandwidth, and low jitter, as any variation in the communication performance could affect the timeliness and accuracy of the messages or tasks.
- Soft Real-Time Communication Systems
  - A soft real-time communication system is a system that can tolerate some degree of deadline misses or errors, without causing severe consequences or loss. For example, a communication system for a video streaming service or a voice over IP service can be soft real-time, as some delay or distortion may not affect the user experience or satisfaction significantly.
  - A soft real-time communication system is probabilistic, meaning that it can estimate the average or expected execution time and response time for every message or task, but it cannot guarantee the worst-case scenario. It also has flexible priority and scheduling policies to balance the trade-off between timeliness and resource utilization.
  - A soft real-time communication system requires moderate reliability, fault tolerance, and security, as some malfunction or attack could degrade its functionality and quality, but not endanger its users or environment. It also requires moderate latency, bandwidth, and jitter, as some variation in the communication performance could affect the smoothness and clarity of the messages or tasks.



### Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- Examples of real time communication include voice calls, video calls, instant messaging, live streaming, online gaming, etc.
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic can be further divided into three categories: periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals and have fixed deadlines and lengths.
- Aperiodic messages are generated at irregular intervals and have variable deadlines and lengths.
- Sporadic messages are generated randomly and have unpredictable deadlines and lengths.
- Real time control consists of commands and feedbacks that are exchanged between controllers and controlled devices in real time systems.
- Real time control can be further divided into two categories: hard and soft control.
- Hard control requires that the commands and feedbacks are delivered within strict deadlines and with high reliability.
- Soft control allows some flexibility in the delivery of commands and feedbacks, as long as the performance of the system is not degraded.
- In the model of real time communication, the end users of the message application systems are sources and destinations residing in different hosts .
- The network interface of each host contains input queue and output queue .
- Two buffer areas called input/output buffer are allocated to input and output queue to store queuing information .
- The input buffer stores the incoming messages from the network and the output buffer stores the outgoing messages to the network .
- The input and output queues are managed by the network interface controller (NIC) and the host processor, respectively .
- The NIC is responsible for transmitting and receiving messages over the network, while the host processor is responsible for processing and scheduling messages for the application .
- The network is composed of routers and links that connect the hosts and provide the communication service .
- The routers are responsible for routing and forwarding messages along the network, while the links are responsible for transferring messages between routers .
- The network can be characterized by its bandwidth, delay, jitter and reliability .
- Bandwidth is the maximum amount of data that can be transferred over the network per unit time .
- Delay is the time taken for a message to travel from the source to the destination over the network .
- Jitter is the variation in the delay of messages over the network .
- Reliability is the probability that a message is delivered correctly and without errors over the network .
- In real time communication, the performance of the system depends on the throughput, delay and jitter of the messages .
- Throughput is the number of messages that are delivered successfully over the network per unit time .
- Delay and jitter affect the timeliness and quality of the messages, which are critical for real time applications .
- The goal of real time communication is to maximize the throughput and minimize the delay and jitter of the messages, while satisfying the deadlines and reliability requirements of the applications .
- To achieve this goal, various techniques and protocols are used at different layers of the network, such as reservation, prioritization, scheduling, congestion control, error control, etc .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels. Higher priority packets are served before lower priority packets, and packets with the same priority are served in a first-come first-served (FCFS) order.
- Weighted round-robin (WRR) service disciplines are used to allocate bandwidth to different classes of packets in a fair and proportional way. Each class of packets is assigned a weight, which determines the number of packets that can be served from that class in each round. A round is a cycle of serving one packet from each non-empty class in a circular order.
- Priority-based service disciplines can provide strict guarantees on the delay and jitter of high priority packets, but they may starve low priority packets if the network is congested. Weighted round-robin service disciplines can provide fairness and bandwidth guarantees to all classes of packets, but they may not meet the diverse delay and jitter requirements of different applications.
- A hybrid approach that combines priority-based and weighted round-robin service disciplines can achieve a better trade-off between performance and fairness. For example, the probabilistic priority (PP) discipline assigns a parameter to each priority queue, which determines the probability of serving that queue when it is polled by the server. The rate-controlled frame-based weighted round-robin (RFWRR) discipline divides the scheduler into a rate controller and a frame-based WRR server, which can control the delay jitter and satisfy different delay requirements. The class-based weighted fair queuing (CBWFQ) and the weighted fair priority queuing (WFPQ) techniques use a weighted fair queuing algorithm to schedule packets within each priority class.     
- The choice of the service discipline depends on the characteristics of the network, the traffic, and the application requirements. Priority-based service disciplines are suitable for networks with low congestion and applications with strict delay and jitter constraints. Weighted round-robin service disciplines are suitable for networks with high congestion and applications with flexible delay and jitter constraints. Hybrid approaches are suitable for networks with moderate congestion and applications with diverse delay and jitter constraints.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Medium Access Control Protocols for Broadcast Networks for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System.

```markdown
### Medium Access Control Protocols for Broadcast Networks

- Broadcast networks are networks where multiple nodes share a common communication channel, such as a wireless network or a bus network.
- Medium access control (MAC) protocols are protocols that coordinate the access of multiple nodes to the shared channel, avoiding collisions and ensuring fair and efficient use of the channel.
- MAC protocols can be classified into two main categories: contention-based and reservation-based.

#### Contention-based MAC protocols

- Contention-based MAC protocols are protocols where nodes compete for the channel access, without any prior reservation or coordination.
- Examples of contention-based MAC protocols are ALOHA, slotted ALOHA, carrier sense multiple access (CSMA), and CSMA with collision detection (CSMA/CD).
- Contention-based MAC protocols are simple and decentralized, but they suffer from low channel utilization, high collision probability, and unpredictable delay.

#### Reservation-based MAC protocols

- Reservation-based MAC protocols are protocols where nodes reserve the channel access in advance, using some form of coordination or negotiation.
- Examples of reservation-based MAC protocols are time division multiple access (TDMA), frequency division multiple access (FDMA), code division multiple access (CDMA), and polling.
- Reservation-based MAC protocols are more complex and centralized, but they offer higher channel utilization, lower collision probability, and predictable delay.

#### MAC protocols for real-time communication

- Real-time communication requires MAC protocols that can provide bounded and predictable delay, as well as guarantee a certain quality of service (QoS) for the real-time traffic.
- Contention-based MAC protocols are not suitable for real-time communication, as they cannot guarantee the channel access and the delay bound for the real-time nodes.
- Reservation-based MAC protocols are more suitable for real-time communication, as they can allocate the channel resources according to the QoS requirements of the real-time nodes.
- However, reservation-based MAC protocols also face some challenges for real-time communication, such as how to handle dynamic and heterogeneous traffic, how to cope with channel errors and node failures, and how to achieve scalability and flexibility.
```



### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain different qualities of service (QoS) for their data flows    .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is used in real-time systems for efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP supports the following features     :
  - Application-adaptive QoS: RSVP enables applications to specify their QoS requirements and adapt to the network conditions.
  - Dynamic resource allocation: RSVP allows the network to allocate and deallocate resources according to the changing traffic demands and network conditions.
  - Policy control: RSVP enables the network to enforce policies for resource allocation and admission control based on the identity and priority of the users and applications.
  - Scalability: RSVP uses soft state and aggregation techniques to reduce the overhead and complexity of maintaining resource reservations in large and dynamic networks.
  - Heterogeneity: RSVP supports different types of QoS models, such as the integrated services model and the differentiated services model, and can interoperate with various routing protocols and network technologies.
- RSVP uses the following messages to establish and maintain resource reservations     :
  - PATH: Sent by the sender to inform the intermediate nodes and the receiver about the characteristics and requirements of the data flow.
  - RESV: Sent by the receiver to request a specific QoS from the intermediate nodes and the sender for the data flow.
  - PATH TEAR: Sent by the sender to tear down the PATH state in the intermediate nodes and the receiver when the data flow is terminated or modified.
  - RESV TEAR: Sent by the receiver to tear down the RESV state in the intermediate nodes and the sender when the data flow is terminated or modified.
  - PATH ERROR: Sent by an intermediate node or the receiver to report an error in processing a PATH message or receiving a data flow.
  - RESV ERROR: Sent by an intermediate node or the sender to report an error in processing a RESV message or providing a QoS for a data flow.
  - RESV CONF: Sent by an intermediate node or the sender to confirm the successful processing of a RESV message and the provision of a QoS for a data flow.



# Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations .
- An RTOS provides features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS is different from a time-sharing operating system, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- A real-time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, and online transactions.
- A real-time database provides features such as concurrency control, data consistency, data freshness, and data recovery.
- A real-time database can be based on SQL or NoSQL, and can be the source for data warehouses and business analytics operations.
- A real-time database is different from a time-series database, which stores and analyzes data that changes over time, such as metrics, events, and logs.
- A time-series database provides features such as high ingestion rate, data compression, and query optimization.
- A time-series database can be used for applications such as monitoring, forecasting, and anomaly detection.



### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has two key features: predictability and determinism.

Some of the features of an RTOS are:

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources than a general-purpose operating system. This makes it suitable for embedded systems and devices with limited resources.
- **Fast response**: An RTOS is able to respond quickly and efficiently to events and interrupts, without significant delays or overheads. This is important for applications that require real-time feedback and control.
- **Deterministic behavior**: An RTOS ensures that tasks are executed as expected every time, without any variations or uncertainties. This is achieved by using strict scheduling algorithms, data buffers, or fixed task prioritization.
- **Co-operative or pre-emptive scheduling**: An RTOS can use either co-operative or pre-emptive scheduling to manage the execution of tasks. In co-operative scheduling, a task runs until it is completed or it voluntarily yields the processor to another task. In pre-emptive scheduling, a task can be interrupted by a higher-priority task at any time, and resumed later when the processor is available.
- **Main and background loops**: An RTOS can use a main and background loop structure to handle tasks. The main loop is responsible for executing the most critical and time-sensitive tasks, while the background loop handles the less urgent and non-real-time tasks. The main loop has higher priority than the background loop, and can pre-empt it if necessary.



### Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.
- A real-time system can be classified into hard real-time and soft real-time based on the timing constraints  .
  - A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
  - A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- Time services are the mechanisms that provide the system with the notion of time and enable the system to measure, compare, and synchronize time.
- Time services can be divided into two categories: clock services and timer services.
  - Clock services are the functions that provide the system with the current time value, which can be absolute (based on a reference point) or relative (based on an elapsed interval).
  - Timer services are the functions that allow the system to schedule events or actions to occur at a specified future time, which can be absolute (based on a clock value) or relative (based on a duration).
- Time services are essential for real-time systems, as they enable the system to:
  - Monitor and enforce the timing constraints of the system tasks and activities.
  - Coordinate and synchronize the system components and devices that operate with different clocks.
  - Perform time-dependent computations and operations, such as signal processing, control, and encryption.
  - Record and analyze the system behavior and performance over time.
- Time services can be implemented by using hardware and software components, such as:
  - Synchronous programming languages, which provide constructs and primitives for expressing and manipulating time.
  - Real-time operating systems (RTOSes), which provide system calls and APIs for accessing and managing clock and timer services.
  - Real-time networks, which provide protocols and mechanisms for transmitting and synchronizing time information among distributed nodes.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS is different from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing.
- However, some variants of UNIX, such as Linux, have been modified to support real-time features, such as preemptive scheduling, priority inheritance, and real-time signals .
- Linux is used as a RTOS for some applications, such as human-in-the-loop simulation, launch vehicles, and spacecraft .
- Some advantages of using Linux as a RTOS are its open source nature, its large user community, its compatibility with various hardware platforms, and its rich set of software tools .
- Some challenges of using Linux as a RTOS are its complexity, its lack of certification, its unpredictability, and its vulnerability to security threats .
- Some alternatives to UNIX or Linux as a RTOS are VxWorks, QNX, FreeRTOS, and RTX. These RTOSs are designed specifically for real-time applications and have different features, such as memory footprint, scalability, reliability, and compatibility.



# POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interface with an operating system.
- POSIX was originally designed for UNIX-like systems, but it has been extended to cover real-time operating systems as well.
- Real-time operating systems are systems that have strict timing constraints and need to respond to events in a predictable and timely manner.
- POSIX real-time extensions aim to provide the operating system services that are needed by real-time applications, such as scheduling, synchronization, timers, memory management, and inter-process communication.
- Some of the POSIX real-time standards are:

  - POSIX.1b: Real-time extensions, which defines the basic real-time features such as priority-based scheduling, timers, semaphores, message queues, shared memory, and asynchronous I/O.
  - POSIX.1c: Threads extensions, which defines the interface for creating and managing multiple threads of execution within a process.
  - POSIX.4: Timers and clocks, which defines the interface for accessing high-resolution timers and clocks.
  - POSIX.13: Application environment profile, which defines the minimum set of features that a POSIX-compliant system must support.

- Some of the POSIX issues that arise in real-time operating systems are:

  - The compatibility and portability of POSIX applications across different real-time operating systems, which may have different implementations and extensions of the POSIX standards.
  - The performance and predictability of POSIX services, which may depend on the underlying hardware, kernel, and system configuration.
  - The trade-off between functionality and simplicity of POSIX services, which may affect the ease of use and the overhead of the POSIX interface.
  - The completeness and adequacy of POSIX services, which may not cover all the needs and requirements of real-time applications.



### Characteristics of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, or events, and allow other data to be placed in a chronological sequence or to be analyzed chronologically.
- Temporal data can be used to analyze various phenomena that change over time, such as weather patterns, traffic conditions, demographic trends, etc.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time, depending on the context and purpose of the data.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be stored in different ways, such as using timestamps, temporal attributes, temporal tables, or temporal databases, depending on the data model and the query requirements.
- Temporal data can be manipulated and queried using different techniques, such as temporal algebra, temporal logic, temporal SQL, or temporal GIS, depending on the data type and the analysis goals.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the application logic.
- Temporal consistency is important for real-time systems because they need to make timely and accurate decisions based on the data they read from the database.
- Temporal consistency can be violated if the data in the database becomes outdated or stale due to the dynamic nature of the physical environment or the delays in the data acquisition and update processes.
- Temporal consistency can be measured by the temporal error, which is the difference between the actual value of the physical entity and the value of the data object that represents it in the database.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the data sources whenever there is a significant change in the physical environment.
  - Periodic updates, which are updates that are performed at regular intervals regardless of the changes in the physical environment.
  - Temporal validity, which is a property of data objects that specifies the maximum duration for which they can be considered valid.
  - Absolute validity, which is a property of data objects that specifies the maximum temporal error that can be tolerated.
  - Relative validity, which is a property of data objects that specifies the maximum temporal error that can be tolerated relative to the temporal error of other data objects.
  - Temporal constraints, which are constraints that specify the deadlines or the temporal requirements for the transactions that access or update the data objects.
  - Concurrency control, which is a mechanism that coordinates the access and update of data objects by multiple transactions to prevent conflicts and ensure consistency.



### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency control is the process of managing the access and modification of shared data resources by multiple concurrent processes or transactions in a system.
- Concurrency control is essential for ensuring both logical and timing correctness of real-time systems (RTS), which are systems that respond to their environment within specified time constraints.
- Concurrency control can be classified into two main categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking or reserving the data resources before accessing or modifying them. Examples of pessimistic concurrency control methods are two-phase locking, timestamp ordering, and priority inheritance.
  - Optimistic concurrency control allows conflicts to occur and then resolves them by aborting or restarting the conflicting processes or transactions. Examples of optimistic concurrency control methods are optimistic locking, multiversion concurrency control, and validation.
- Concurrency control methods for RTS must consider both the data consistency and the timing constraints of the processes or transactions. Data consistency means that the shared data resources must reflect a correct and coherent state of the system. Timing constraints mean that the processes or transactions must meet their deadlines and avoid blocking or starvation.
- Concurrency control methods for RTS must also be compatible with the scheduling policies and the resource allocation strategies of the system. Scheduling policies determine the order and priority of the processes or transactions to be executed. Resource allocation strategies determine how the system resources, such as CPU, memory, and disk, are assigned to the processes or transactions.
- Concurrency control methods for RTS can be evaluated based on several criteria, such as correctness, performance, complexity, and robustness.
  - Correctness refers to the ability of the concurrency control method to ensure both data consistency and timing constraints of the processes or transactions.
  - Performance refers to the efficiency and effectiveness of the concurrency control method in terms of throughput, response time, utilization, and overhead.
  - Complexity refers to the difficulty and cost of implementing and maintaining the concurrency control method in terms of algorithm, data structure, and communication.
  - Robustness refers to the adaptability and reliability of the concurrency control method in terms of handling failures, errors, and uncertainties.



### Overview of Commercial Real Time databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the attributes of live real-time databases are:
  - Concurrency control: the ability to handle multiple transactions accessing the same data without compromising the consistency and integrity of the data.
  - Data freshness: the degree to which the data reflects the current state of the real world.
  - Data distribution: the ability to store and access data across multiple nodes or locations for scalability and availability.
  - Data replication: the ability to create and maintain copies of data for backup, load balancing, or fault tolerance.
  - Data security: the ability to protect data from unauthorized access, modification, or deletion.
  - Data recovery: the ability to restore data to a consistent state after a failure or error.
  - Data analysis: the ability to perform queries, reports, or analytics on the data to derive insights or support decision making.
- Some of the examples of commercial real-time databases are :
  - Dealpath: a cloud-based platform that provides data and tools for commercial real estate investment and development.
  - Altus Group: a data and software provider that offers historical and current market information, valuation, and advisory services for commercial real estate.
  - CoStar: a leading provider of commercial real estate information, analytics, and online marketplaces.
  - Google Cloud Firestore: a highly performant, fully managed NoSQL database service for large analytical and operational workloads.

