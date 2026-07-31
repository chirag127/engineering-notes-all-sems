

# Real Time System

A real time system is a system that can process data and events within a specified and predictable time frame. A real time system must meet the deadlines imposed by the environment, otherwise it may cause a system failure or undesirable consequences. A real time system is often used for applications that require high reliability, safety, and performance, such as flight control systems, industrial automation, robotics, and medical devices.

Some characteristics of a real time system are:

- Timeliness: The system must produce the correct output within the required time limit.
- Time synchronization: The system must coordinate the activities of different components that operate with independent clocks.
- Concurrency: The system must handle multiple tasks or events that occur simultaneously or overlap in time.
- Determinism: The system must behave in a predictable and consistent manner under all circumstances.
- Fault tolerance: The system must be able to recover from errors or failures without compromising the functionality or safety of the system.

There are two types of real time systems based on the severity of the deadlines:

- Hard real time system: A system that must meet the deadlines without any exception. A missed deadline can result in a catastrophic failure or loss of life. For example, a missile guidance system, a pacemaker, or an airbag system.
- Soft real time system: A system that can tolerate some degree of deadline violation. A missed deadline can result in a degraded performance or quality of service, but not a fatal outcome. For example, a video streaming system, a voice recognition system, or a web server.

A real time system requires a special type of operating system, called a real time operating system (RTOS), that can support the features and requirements of the system. An RTOS is different from a general purpose operating system, such as Windows or Linux, that is designed for time-sharing or multitasking applications. An RTOS provides the following functions:

- Task scheduling: The RTOS assigns priorities to the tasks and allocates the CPU time according to the deadlines and importance of the tasks.
- Interrupt handling: The RTOS responds to the external or internal events that trigger the execution of the tasks or interrupt the current task.
- Memory management: The RTOS allocates and deallocates the memory space for the tasks and data structures.
- Inter-task communication: The RTOS provides mechanisms for the tasks to exchange information or synchronize their activities, such as message queues, semaphores, or mutexes.
- Device drivers: The RTOS interfaces with the hardware devices and peripherals that are used by the system, such as sensors, actuators, or network cards.

Some examples of RTOS are:

- FreeRTOS: An open source RTOS that supports various microcontrollers and platforms.
- VxWorks: A commercial RTOS that is widely used for aerospace, defense, and industrial applications.
- QNX: A commercial RTOS that is based on a microkernel architecture and is used for automotive, medical, and telecommunications applications.
- RTLinux: An extension of the Linux kernel that provides hard real time capabilities.



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failures or unacceptable losses. For example, a nuclear reactor control system, an air traffic control system, or a pacemaker.
  - Soft real time systems are systems that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- Real time systems can also be classified into two types based on the predictability of their workload: periodic systems and aperiodic systems.
  - Periodic systems are systems that have a regular and predictable pattern of events or inputs, such as sensor readings, control signals, or alarms. Periodic systems can be analyzed using techniques such as rate monotonic scheduling, earliest deadline first scheduling, or cyclic executive.
  - Aperiodic systems are systems that have an irregular and unpredictable pattern of events or inputs, such as user requests, network packets, or interrupts. Aperiodic systems can be analyzed using techniques such as sporadic server, polling server, or deferrable server.
- Real time systems face many challenges and trade-offs in their design and implementation, such as:
  - Timing constraints: real time systems must ensure that their tasks meet their deadlines, which may require careful analysis, scheduling, and synchronization of the system components.
  - Resource constraints: real time systems may have limited resources, such as memory, CPU, or power, which may require efficient allocation, management, and optimization of the system resources.
  - Dependability: real time systems must ensure that they function correctly and reliably, even in the presence of faults, errors, or uncertainties, which may require techniques such as fault tolerance, error detection and recovery, or redundancy.
  - Adaptability: real time systems may have to cope with changing requirements, environments, or workloads, which may require techniques such as reconfiguration, self-adaptation, or learning.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System.

# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences, such as loss of life, damage to property, or failure of mission.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade.
- Examples of hard real time systems are air traffic control systems, nuclear power plant control systems, and pacemakers.
- Examples of soft real time systems are multimedia systems, online gaming systems, and web servers.
- A real time system consists of three main components: sensors, processors, and actuators.
- Sensors are devices that monitor the physical environment and generate events or inputs for the system.
- Processors are devices that execute the software or logic of the system and produce outputs or commands for the system.
- Actuators are devices that perform actions or control the physical environment according to the outputs or commands of the system.
- A real time system must satisfy two main requirements: functional correctness and temporal correctness.
- Functional correctness means that the system must produce the correct outputs or commands for the given inputs or events.
- Temporal correctness means that the system must produce the outputs or commands within the specified deadlines.
- A real time system must also consider other factors, such as reliability, availability, safety, security, and cost.



# Typical Real Time Applications

- A real-time application, or RTA, is an application that functions within a time frame that the user senses as immediate or current. The latency must be less than a defined value, usually measured in seconds.
- Real-time applications are applications that operate within an immediate time frame; sensing, analyzing, and acting on streaming data as it happens.
- Real-time applications are used in various domains, such as industrial, medical, multimedia, and peripheral equipment. Some examples are:

  - **Process Control Systems**: Process control systems are used in industrial applications where production is continuous and interruptions cannot happen. For example, chemical plants, power plants, steel mills, etc. These systems monitor and control the physical processes and ensure safety, efficiency, and quality .
  - **Machine Vision**: Machine vision is used to help machines rapidly interpret data so they can see their surroundings and make decisions quickly based on that visual input. For example, face recognition, autonomous vehicles, quality inspection, etc. These systems require high-speed image processing and low-latency response .
  - **Robotics**: Robotics is the field of engineering that deals with the design, construction, operation, and application of robots. Robots are machines that can perform tasks that are difficult, dangerous, or repetitive for humans. For example, industrial robots, surgical robots, service robots, etc. These systems require real-time sensing, computation, and actuation .
  - **Manufacturing**: Manufacturing is the process of transforming raw materials into finished products. Manufacturing systems use real-time applications to coordinate and optimize the production process. For example, computer-aided design (CAD), computer-aided manufacturing (CAM), computer numerical control (CNC), etc. These systems require real-time scheduling, communication, and control .
  - **Healthcare and Patient Monitoring**: Healthcare and patient monitoring systems use real-time applications to provide medical services and care to patients. For example, electrocardiogram (ECG), electroencephalogram (EEG), pacemakers, ventilators, etc. These systems require real-time data acquisition, analysis, and feedback .
  - **Multimedia**: Multimedia is the use of multiple media types, such as text, audio, video, graphics, etc., to convey information or entertainment. Multimedia applications use real-time systems to provide interactive and immersive experiences to users. For example, video games, virtual reality, augmented reality, video conferencing, etc. These systems require real-time synchronization, compression, and transmission .
  - **Peripheral Equipment**: Peripheral equipment is any device that is connected to a computer system and provides input or output functions. Peripheral equipment uses real-time systems to communicate with the computer and perform the required tasks. For example, keyboards, mice, printers, scanners, etc. These systems require real-time drivers, protocols, and interfaces.



# Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System will be released on **Friday, 17 March 2023** by 5:00 PM GMT.
- The notes will cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Challenges and requirements of real time systems
  - Real time system design and development process
  - Real time system modeling and analysis techniques
- The notes will be available in PDF format on the course website and the learning management system (LMS).
- The notes will be accompanied by a set of self-assessment questions and exercises to test your understanding of the concepts and applications of real time systems.
- The notes are expected to take approximately **two hours** to read and comprehend.
- You are advised to read the notes carefully and thoroughly before the next lecture session, which will be held on **Monday, 20 March 2023** at 10:00 AM GMT.
- You are also encouraged to participate in the online discussion forum and ask any questions or doubts you may have regarding the notes or the subject matter.
- The instructor will provide feedback and clarification on the forum and during the lecture session.
- The notes are an essential part of the course and will help you prepare for the upcoming assignments and exams. Please make sure you download and study the notes as soon as they are released.



# Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System are due on **Friday, March 24, 2023** by **11:59 PM**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in a clear, concise, and accurate manner, using proper grammar, spelling, and punctuation.
- The notes should follow the formatting guidelines given by the instructor, such as font size, margins, headings, etc.
- The notes should include relevant diagrams, tables, graphs, or code snippets to illustrate the concepts and algorithms.
- The notes should cite the sources of information using the APA style of referencing.
- The notes should be submitted as a single PDF file through the online learning platform.
- The notes will be graded based on the following criteria:
  - Completeness and correctness of the content
  - Organization and clarity of the presentation
  - Quality and relevance of the illustrations
  - Adherence to the formatting and citation guidelines
- The notes will account for **10%** of the final grade for the subject of Real Time System.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of timing constraints for the unit 1 - introduction of real time system in the subject of real time system.

# Timing Constraints

- A real time system is a system that must respond to events within certain time bounds, called timing constraints.
- Timing constraints can be classified into two types: hard and soft.
- Hard timing constraints are those that must be met for the system to function correctly. If a hard timing constraint is violated, the system may fail or cause severe consequences.
- Soft timing constraints are those that can be violated occasionally without compromising the system functionality, but may degrade the system performance or quality of service.
- Examples of hard timing constraints are:
  - The deadline for a control system to send a command to a physical device, such as a brake or a valve.
  - The maximum latency for a communication system to deliver a message, such as a voice or video call.
  - The minimum frequency for a sensor system to sample and process data, such as a radar or a camera.
- Examples of soft timing constraints are:
  - The desired frame rate for a video game or a simulation system.
  - The preferred response time for a user interface or a web service.
  - The average throughput for a data processing or a streaming system.
- Timing constraints can be specified in different ways, such as:
  - Absolute deadlines: the time by which a task or a message must be completed or delivered, relative to a fixed reference point, such as the system start time or the wall clock time.
  - Relative deadlines: the time by which a task or a message must be completed or delivered, relative to the occurrence of an event, such as the arrival of a request or a trigger signal.
  - Periodic deadlines: the time by which a task or a message must be completed or delivered, relative to the previous completion or delivery of the same task or message, such as every 10 milliseconds or every 100 frames.
  - Sporadic deadlines: the time by which a task or a message must be completed or delivered, relative to the minimum separation between two consecutive occurrences of the same task or message, such as at least 5 seconds apart or at most 20 times per hour.
- Timing constraints can also be expressed in terms of the worst-case execution time (WCET) or the best-case execution time (BCET) of a task or a message, which are the maximum and minimum possible time required to complete or deliver it, respectively, under any possible scenario.
- The design and analysis of a real time system must take into account the timing constraints of its tasks and messages, and ensure that they are met under all possible conditions, such as varying workload, resource availability, and environmental factors.



# Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- Examples of hard real time systems are nuclear power plant control systems, air traffic control systems, missile guidance systems, medical devices, etc.  .
- A hard real time system requires a high degree of coordination, both within and across devices, and may use technologies such as Intel® Time Coordinated Computing (Intel® TCC) and Time-Sensitive Networking (TSN) to achieve this  .
- A hard real time system must have predictable and deterministic behavior, which means that the system must always produce the same output for the same input and execute the same sequence of instructions in the same amount of time  .
- A hard real time system must have low latency and high throughput, which means that the system must respond quickly to events and process a large amount of data efficiently  .
- A hard real time system must have fault tolerance and reliability, which means that the system must be able to handle errors and failures gracefully and continue to operate correctly  .
- A hard real time system must have security and safety, which means that the system must protect itself and its environment from unauthorized access and malicious attacks, and prevent harm to people and property  .



# Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a catastrophic failure or a significant degradation of performance  .
- A soft real-time system has a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system.
- A soft real-time system can be run on multiple cores and impose fewer restrictions on applications.
- A soft real-time system is typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications.
  - Online gaming and virtual reality systems.
  - Multimedia systems and interactive user interfaces.
- A soft real-time system is different from a hard real-time system, which is a system that must meet its deadlines precisely and consistently, otherwise it may cause a critical failure or unacceptable consequences .
- Some examples of hard real-time systems are:
  - Air traffic control systems.
  - Nuclear power plant control systems.
  - Medical devices and surgical robots.
  - Automotive and avionics systems.



# Reference Models for Real Time Systems

A reference model is a conceptual framework that defines the essential features and characteristics of a real time system. It helps to understand, analyze, design, and evaluate real time systems in a consistent and systematic way. A reference model is not a specific system design, but rather a general template that can be instantiated for different applications and domains.

There are different reference models for real time systems, depending on the level of abstraction, the scope, and the purpose of the model. Some examples of reference models are:

- **Real-time Control System (RCS)**: This is a reference model architecture that combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis . It is suitable for many software-intensive, real-time computing control problem domains, such as robotics, manufacturing, and aerospace. It defines the types of functions needed in a real-time intelligent control system, and how these functions relate to each other.
- **Reference Model of Real-Time Systems**: This is a reference model that focuses on the timing behavior of the systems, and allows us to reason about the schedulability and performance of real time systems . It is characterized by three elements: a workload model, a resource model, and a system model. The workload model specifies the applications supported by the system, such as the set of tasks, their parameters, and their dependencies. The resource model describes the resources available in the system, such as the CPU, memory, network, and their types and relations. The system model defines the policies and mechanisms used by the system to manage the resources and the workload, such as the scheduling algorithm, the synchronization protocol, and the fault tolerance scheme.
- **Model of a Real-Time System**: This is a reference model that provides a general description of the components and interactions of a real time system, without specifying the details of the implementation. It comprises of the following parts: the workload model, the resource model, the system model, and the environment model. The workload model and the resource model are similar to the previous reference model, but the system model also includes the communication model, which describes the communication channels and protocols among the tasks and the resources. The environment model captures the external factors that affect the system, such as the physical environment, the user input, and the disturbances.



# Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. A job may need to acquire and release a resource multiple times during its execution. Example: memory, file, printer, semaphore.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job without affecting their functionality or state. Example: CPU, memory.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job without affecting their functionality or state. Example: disk, printer, network.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. Example: private memory, dedicated CPU core.
- Shared processors or resources can be used by multiple jobs, but only one job can use them at a time. Example: public memory, shared CPU core.
- Processors and resources can affect the performance and schedulability of real-time tasks. Therefore, they need to be managed and allocated efficiently by the real-time operating system (RTOS).
- A RTOS is an operating system that serves real-time applications that process data without any buffering delay. It has to meet the timing constraints and deadlines of the real-time tasks.
- A RTOS typically consists of the following components:
  - Task scheduler: It decides which task to execute next based on the priority, deadline, and resource requirements of the tasks.
  - Task dispatcher: It switches the context between the tasks and assigns the processor to the selected task.
  - Resource manager: It manages the allocation and deallocation of the resources to the tasks and handles the resource conflicts and contention.
  - Interrupt handler: It handles the external and internal interrupts that may occur during the execution of the tasks and invokes the appropriate routines.
  - Clock and timer: It provides the time reference and the timing services for the tasks and the RTOS.
  - Communication and synchronization: It provides the mechanisms for the tasks to communicate and synchronize with each other and with the external devices.



# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub>-, r<sub>i</sub>+], where r<sub>i</sub>- is the minimum release time and r<sub>i</sub>+ is the maximum release time. The difference between r<sub>i</sub>+ and r<sub>i</sub>- is called the **jitter** of the job.
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which a job must finish execution. It may be fixed or variable depending on the system and the job. A job that misses its absolute deadline is considered to have failed.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time interval between the release time and the absolute deadline of a job. It is usually fixed and known in advance. A job that finishes within its relative deadline is considered to have succeeded.
  - **Feasible interval [(r<sub>i</sub>), (d<sub>i</sub>)]**: The time interval in which a job can be feasibly executed by the system. It is bounded by the release time and the absolute deadline of the job. A job that starts before its release time or finishes after its absolute deadline is considered to have violated its feasible interval.
- The temporal parameters of a job are important for the analysis and design of real time systems, as they determine the schedulability, performance, and correctness of the system .



# Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that meets all the deadlines of the task. A set of periodic tasks is said to be feasible if there exists a schedule that meets all the deadlines of all the tasks.
- A periodic task is said to be implicit-deadline if its relative deadline is equal to its period, i.e., Di = Pi. A periodic task is said to be constrained-deadline if its relative deadline is less than or equal to its period, i.e., Di ≤ Pi. A periodic task is said to be arbitrary-deadline if its relative deadline can be any value, i.e., Di can be greater than, equal to, or less than Pi.
- A periodic task is said to be synchronous if its phase is zero, i.e., Φi = 0. A periodic task is said to be asynchronous if its phase is non-zero, i.e., Φi > 0.
- A periodic task is said to be independent if it does not share any resources or communicate with any other tasks. A periodic task is said to be dependent if it shares some resources or communicates with some other tasks.
- A periodic task is said to be preemptive if it can be interrupted by a higher priority task and resume later. A periodic task is said to be non-preemptive if it cannot be interrupted once it starts execution.
- A periodic task is said to be sporadic if it has a minimum inter-arrival time between two consecutive jobs, which is equal to or greater than its period. A periodic task is said to be jittered if it has a maximum deviation from its ideal release time, which is called the jitter.



# Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the scheduling of jobs in real-time systems.
- Precedence constraints specify the order in which jobs must execute, while data dependency specifies the data flow between jobs that communicate via shared data.
- Precedence constraints and data dependency can be represented by directed graphs, where vertices are jobs and edges are constraints or dependencies.

## Precedence Constraints

- Precedence constraints are imposed by the logical or temporal relationships among jobs, such as control flow, synchronization, or resource sharing.
- A job J_i is a predecessor of another job J_k (and J_k a successor of J_i) if J_k cannot begin execution until the execution of J_i completes.
- A precedence graph G = (J, <) is a directed graph where J is the set of jobs and < is the precedence relation. An edge (J_i, J_k) in G means that J_i is a predecessor of J_k.
- A precedence graph is acyclic if there is no cycle in the graph, meaning that there is no job that is a predecessor of itself or of its predecessors. A cyclic precedence graph implies a deadlock situation, where no job can execute.
- A precedence graph is transitive if for any three jobs J_i, J_j, and J_k, if (J_i, J_j) and (J_j, J_k) are edges in the graph, then (J_i, J_k) is also an edge in the graph. A transitive precedence graph can be simplified by removing redundant edges.
- A precedence graph is consistent if for any two jobs J_i and J_k, if (J_i, J_k) is an edge in the graph, then the deadline of J_i is earlier than or equal to the deadline of J_k. A consistent precedence graph ensures that no job misses its deadline because of its predecessors.

## Data Dependency

- Data dependency arises when jobs communicate via shared data, such as variables, buffers, or messages.
- A job J_i is a producer of another job J_k (and J_k a consumer of J_i) if J_i writes data that J_k reads.
- A data dependency graph G = (J, D) is a directed graph where J is the set of jobs and D is the data dependency relation. An edge (J_i, J_k) in G means that J_i is a producer of J_k.
- A data dependency graph is acyclic if there is no cycle in the graph, meaning that there is no job that is a producer of itself or of its producers. A cyclic data dependency graph implies a livelock situation, where no job can access the data it needs.
- A data dependency graph is transitive if for any three jobs J_i, J_j, and J_k, if (J_i, J_j) and (J_j, J_k) are edges in the graph, then (J_i, J_k) is also an edge in the graph. A transitive data dependency graph can be simplified by removing redundant edges.
- A data dependency graph is consistent if for any two jobs J_i and J_k, if (J_i, J_k) is an edge in the graph, then the release time of J_i is earlier than or equal to the release time of J_k. A consistent data dependency graph ensures that no job reads stale data because of its producers.



# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: **hard real time** and **soft real time** .
  - Hard real time scheduling requires that every task must meet its deadline, otherwise the system may fail or cause severe consequences .
  - Soft real time scheduling allows some tasks to miss their deadlines occasionally, without causing significant harm to the system or the user .
- Real time scheduling can also be classified into two types: **static** and **dynamic** .
  - Static real time scheduling assigns priorities and schedules to tasks before the system starts running, and does not change them during the execution .
  - Dynamic real time scheduling assigns priorities and schedules to tasks at run time, based on the current state and behavior of the system .
- Real time scheduling algorithms can be divided into two groups: **preemptive** and **non-preemptive** .
  - Preemptive real time scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running, and resume it later when the higher priority task finishes or is blocked .
  - Non-preemptive real time scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running, and waits until the lower priority task completes or yields .
- Some examples of real time scheduling algorithms are: **Rate Monotonic Scheduling (RMS)**, **Earliest Deadline First (EDF)**, **Least Laxity First (LLF)**, **Fixed Priority Scheduling (FPS)**, **Round Robin Scheduling (RRS)**, **Deadline Monotonic Scheduling (DMS)**, etc .
- Real time scheduling can be applied to various domains and applications, such as: **embedded systems**, **robotics**, **multimedia**, **industrial control**, **aerospace**, **medical devices**, **telecommunications**, etc  .
- Real time scheduling can be supported by various tools and platforms, such as: **real time operating systems (RTOS)**, **real time schedulers**, **real time programming languages**, **real time middleware**, **real time simulators**, **real time analyzers**, etc   .
- Real time scheduling can also be integrated with other techniques and methods, such as: **resource management**, **fault tolerance**, **quality of service (QoS)**, **energy efficiency**, **security**, **adaptation**, etc  .
- Real time scheduling is a challenging and active research area, with many open problems and opportunities for improvement and innovation  .



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of allocating CPU time to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that tasks meet their timing requirements and that the system is predictable and responsive. There are different approaches to real time scheduling, depending on the characteristics of the tasks and the system. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival times, execution times, deadlines, and periods, are known at design time. In this approach, a static schedule is computed offline, based on the worst-case execution times of the tasks, and stored in a table. The table specifies the start and end times of each task in each cycle. A timer interrupts the CPU at regular intervals and triggers the execution of the next task in the table. The advantages of this approach are that it is simple, deterministic, and avoids overheads of dynamic scheduling. The disadvantages are that it is inflexible, wasteful of CPU time, and cannot handle aperiodic or sporadic tasks.

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft or firm real time systems, where the properties of the tasks may vary at run time or may not be known in advance. In this approach, each task is assigned a priority, which may be static or dynamic, and the scheduler selects the highest priority task that is ready to run at any given time. The priority of a task may depend on various factors, such as its deadline, its period, its importance, or its resource requirements. The advantages of this approach are that it is flexible, adaptable, and can handle different types of tasks. The disadvantages are that it may incur higher overheads, may suffer from priority inversion, and may not guarantee schedulability.

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority and are scheduled in a circular order. Each task is given a fixed time slice, also known as quantum, to execute, and then preempted by the next task in the queue. The scheduler maintains a ready queue of tasks that are waiting to run, and rotates the queue after each quantum. The advantages of this approach are that it is simple, fair, and easy to implement. The disadvantages are that it may not meet the timing requirements of the tasks, may cause frequent context switches, and may not utilize the CPU efficiently.

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where each task is assigned a weight, which reflects its relative importance or resource demand. The scheduler allocates a time slice to each task that is proportional to its weight, and then preempts it by the next task in the queue. The scheduler maintains a ready queue of tasks that are waiting to run, and rotates the queue after each time slice. The advantages of this approach are that it is fair, easy to implement, and can handle different types of tasks. The disadvantages are that it may not meet the timing requirements of the tasks, may cause frequent context switches, and may not utilize the CPU efficiently.



# Clock Driven Approach

- Clock driven approach is also known as time driven approach or cyclic scheduling .
- In this approach, the system executes tasks according to a predetermined schedule .
- The schedule is computed offline before the system starts running  .
- The schedule is based on the known parameters of the tasks, such as period, deadline, execution time, and precedence constraints .
- The schedule is usually periodic and cyclic, meaning that it repeats itself after a fixed interval of time  .
- The schedule specifies the exact time instants when each task should start and finish execution .
- The scheduling decisions are made at specific time points, independent of events, such as job releases and completions, in the system  .
- The advantages of clock driven approach are:
  - It guarantees the feasibility and timeliness of hard real-time tasks .
  - It avoids the overhead of dynamic scheduling, such as priority assignment, context switching, and preemption .
  - It simplifies the analysis and verification of the system .
  - It eliminates the possibility of anomalous timing behavior, such as priority inversion and deadline misses, that may occur in priority driven systems  .
- The disadvantages of clock driven approach are:
  - It requires the complete knowledge of the task parameters and system configuration .
  - It cannot handle unpredictable or aperiodic tasks, such as interrupts, faults, or user inputs .
  - It may waste CPU resources if the tasks are not fully utilized or if the schedule is not optimal .
  - It may be difficult to update or modify the schedule if the task parameters or system configuration change .



# Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the service opportunities will be allocated as follows:

| Job | Weight | Service opportunities |
| --- | ------ | --------------------- |
| A   | 1      | 1                     |
| B   | 2      | 2                     |
| C   | 3      | 3                     |

- The total number of service opportunities in a cycle is equal to the sum of the weights of the jobs.
- In this example, the total number of service opportunities is 6, and the portion of service time allocated to each job is:

| Job | Weight | Portion of service time |
| --- | ------ | ----------------------- |
| A   | 1      | 1/6                     |
| B   | 2      | 2/6                     |
| C   | 3      | 3/6                     |

- The advantage of weighted round robin is that it can provide different levels of service to different jobs based on their weights.
- It can also handle jobs with different arrival rates and service times.
- The disadvantage of weighted round robin is that it may not be optimal for some real-time systems that require strict deadlines or priorities.
- It may also introduce more overhead and complexity than the basic round-robin scheme.



# Priority Driven Approach

- The priority driven approach is a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur.
- In a priority driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- The priority driven approach is primarily used for more dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events.
- The priority driven approach can improve the real-time performance and predictability of real-time systems by reducing the response time and deadline misses of high-priority tasks.
- The priority driven approach can also support different types of tasks, such as periodic, sporadic, aperiodic, and mixed tasks, by assigning them appropriate priority levels.
- The priority driven approach can be implemented using different priority assignment schemes, such as fixed priority, dynamic priority, or hybrid priority.
- The priority driven approach can also be combined with other techniques, such as resource reservation, admission control, or overload handling, to enhance the quality of service and robustness of real-time systems.



# Dynamic Versus Static Systems

- A **static system** is a system that has a fixed set of tasks and a predefined schedule for executing them. A static system does not change its behavior or structure in response to external events or inputs. A static system can be validated before execution and can guarantee the timing constraints of the tasks. A static system is suitable for hard real-time systems that require deterministic and predictable behavior. A static system provides poor performance in comparison with a dynamic system in terms of overall response time of the job.
- A **dynamic system** is a system that has a variable set of tasks and a flexible schedule for executing them. A dynamic system can adapt its behavior or structure in response to external events or inputs. A dynamic system cannot be validated before execution and may not guarantee the timing constraints of the tasks. A dynamic system is suitable for soft real-time systems that require adaptive and flexible behavior. A dynamic system provides better performance in comparison with a static system in terms of overall response time of the job.
- A **real-time scheduling** algorithm is an algorithm that assigns priorities and execution times to the tasks in a real-time system. A real-time scheduling algorithm can be classified as static or dynamic. For a static scheduler, task priorities are determined before the system runs. For a dynamic scheduler, task priorities are determined as the system runs. Tasks are accepted by the hardware elements in a real-time scheduling system from the computing environment and processed in real-time.
- A **static scheduling** algorithm is an algorithm that assigns fixed priorities and execution times to the tasks in a static system. A static scheduling algorithm does not change the schedule of the tasks during the system execution. A static scheduling algorithm can guarantee the timing constraints of the tasks if the system is feasible. A static scheduling algorithm is simpler and faster than a dynamic scheduling algorithm. A static scheduling algorithm is suitable for simple real-time systems that have a small and fixed number of tasks that do not function in a pipeline.
- A **dynamic scheduling** algorithm is an algorithm that assigns variable priorities and execution times to the tasks in a dynamic system. A dynamic scheduling algorithm can change the schedule of the tasks during the system execution. A dynamic scheduling algorithm may not guarantee the timing constraints of the tasks if the system is not feasible. A dynamic scheduling algorithm is more complex and slower than a static scheduling algorithm. A dynamic scheduling algorithm is suitable for complex real-time systems that have a large and variable number of tasks that function in a pipeline.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms for Real Time Scheduling:

# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms for Real Time Scheduling

## Effective-Deadline-First (EDF) Algorithm

- EDF is a dynamic priority-driven scheduling algorithm used in real-time systems.
- EDF assigns priorities to tasks based on their deadlines, such that the task with the earliest deadline has the highest priority.
- EDF is optimal for preemptive scheduling on a single processor, meaning that it can schedule any feasible set of tasks without missing any deadlines.
- EDF can also be extended to multiprocessor systems, but it may not be optimal in some cases.
- EDF may suffer from high context-switching overhead and priority inversion problems.

## Least-Slack-Time-First (LST) Algorithm

- LST is another dynamic priority-driven scheduling algorithm used in real-time systems.
- LST assigns priorities to tasks based on their slack time, which is the difference between their deadline and their remaining execution time.
- LST is also optimal for preemptive scheduling on a single processor, under the same conditions as EDF.
- LST can also be extended to multiprocessor systems, but it may not be optimal in some cases.
- LST may have better performance than EDF in terms of reducing the number of missed deadlines, minimizing the maximum lateness, and balancing the processor utilization.
- LST may be impractical to implement in some real-time systems, because it requires accurate estimation of the execution time of the tasks.

## Comparison of EDF and LST Algorithms

- Both EDF and LST are optimal dynamic priority-driven scheduling algorithms for real-time systems on a single processor, under the assumption that the tasks are preemptable and the processor is not overloaded.
- Both EDF and LST can be applied to multiprocessor systems, but they may not be optimal in some cases, and they may require additional mechanisms to handle inter-processor communication and synchronization.
- EDF and LST may have different performance characteristics depending on the workload and the system parameters, such as the number of tasks, the deadline distribution, the execution time variation, the context-switching cost, and the priority inversion effect.
- EDF and LST can be combined to form hybrid algorithms that may enhance the performance of real-time task scheduling, by exploiting the advantages of both algorithms and mitigating their drawbacks.



# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for a set of periodic and independent jobs, meaning that it can always meet the deadlines of all the jobs if there exists a feasible schedule  .
- RMA has a simple and efficient implementation, as it only requires the knowledge of the cycle duration of each job and the current time .
- RMA has some limitations, such as:
  - It does not consider the actual execution time of the jobs, only the worst-case scenario .
  - It does not handle aperiodic or sporadic jobs well, as they may have unpredictable arrival times and deadlines .
  - It does not account for resource sharing or synchronization among the jobs, which may cause blocking or deadlock .
  - It does not guarantee the schedulability of all the jobs, even if the total utilization of the system is less than 100% .
- RMA has some schedulability tests, such as:
  - The necessary condition: The total utilization of the system must be less than or equal to the number of jobs .
  - The sufficient condition: The total utilization of the system must be less than or equal to a certain bound that depends on the number of jobs .
  - The exact condition: The system is schedulable if and only if there exists a feasible schedule that meets all the deadlines .



# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler makes each scheduling decision without knowledge about the tasks that will be released in future and parameter of each task known to scheduler only after release of task.
- Offline scheduling can be either static or dynamic, depending on whether the schedule is fixed or can be modified during the run-time.
- Online scheduling can be either static or dynamic, depending on whether the priority of the tasks is fixed or can be changed during the run-time.
- Offline scheduling has the advantage of being optimal, since it can exploit the complete information about the tasks and their requirements.
- Online scheduling has the advantage of being flexible, since it can adapt to the unpredictable changes in the system state and workload.
- Offline scheduling has the disadvantage of being inflexible, since it cannot handle the uncertainties and variations in the system behavior and environment.
- Online scheduling has the disadvantage of being suboptimal, since it has to make decisions based on limited and incomplete information about the tasks and their requirements.
- Offline scheduling is suitable for systems that have predictable and deterministic task sets, such as embedded systems and control systems.
- Online scheduling is suitable for systems that have unpredictable and dynamic task sets, such as interactive systems and multimedia systems.
- An example of offline scheduling is table-driven scheduling, where a table is generated that contains the necessary scheduling decisions for use during the run-time.
- An example of online scheduling is priority-driven scheduling, where the scheduler assigns a priority to each task and selects the highest priority task for execution at each scheduling point.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a pre-defined schedule that is determined offline. The scheduler follows the schedule and switches jobs at fixed time instants. Examples are cyclic executive, time triggered, etc.

## Scheduling Aperiodic and Sporadic jobs in Priority Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs. If aperiodic jobs are given high priority, they may interfere with the deadlines of periodic and sporadic jobs. If aperiodic jobs are given low priority, they may suffer from long response times.
- There are two main approaches to scheduling aperiodic and sporadic jobs in priority driven systems: background scheduling and server-based scheduling.
- Background scheduling is a simple approach that assigns the lowest priority to aperiodic jobs and executes them only when no periodic or sporadic jobs are ready. This ensures that aperiodic jobs do not affect the schedulability of periodic and sporadic jobs, but it also results in poor responsiveness of aperiodic jobs. Background scheduling is suitable for systems that have low aperiodic workload and do not require timely service for aperiodic jobs.
- Server-based scheduling is a more sophisticated approach that allocates a portion of the processor time to aperiodic jobs using a server task. A server task is a periodic or sporadic task that has a budget of execution time and a replenishment policy. The server task can execute aperiodic jobs using its budget, and replenish its budget according to its policy. The server task can have different priority levels, depending on the desired responsiveness of aperiodic jobs and the impact on periodic and sporadic jobs. There are different types of server-based scheduling algorithms, such as polling server, deferrable server, sporadic server, etc.

## Scheduling Aperiodic and Sporadic jobs in Clock Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to handle the unpredictability of aperiodic and sporadic jobs. Since the schedule is fixed and determined offline, it may not be able to accommodate the arrival of aperiodic and sporadic jobs at any time. If aperiodic and sporadic jobs are ignored, they may miss their deadlines or service requirements. If aperiodic and sporadic jobs are inserted into the schedule, they may disrupt the execution of periodic jobs and cause deadline misses or overruns.
- There are two main approaches to scheduling aperiodic and sporadic jobs in clock driven systems: slack stealing and event-driven scheduling.
- Slack stealing is an approach that utilizes the unused processor time or slack in the schedule to execute aperiodic and sporadic jobs. Slack is the difference between the worst-case execution time and the actual execution time of a periodic job. Slack can be either static or dynamic. Static slack is the slack that is known at the beginning of the schedule cycle and can be allocated to aperiodic and sporadic jobs offline. Dynamic slack is the slack that is generated during the execution of the schedule cycle and can be allocated to aperiodic and sporadic jobs online. Slack stealing algorithms can be either offline or online, depending on how they allocate slack to aperiodic and sporadic jobs. Examples of slack stealing algorithms are offline slack stealing, online slack stealing, total slack stealing, etc.
- Event-driven scheduling is an approach that modifies the schedule dynamically to accommodate the arrival of aperiodic and sporadic jobs. Event-driven scheduling algorithms can be either preemptive or non-preemptive, depending on whether they allow aperiodic and sporadic jobs to preempt periodic jobs or not. Event-driven scheduling algorithms can also be either conservative or optimistic, depending on whether they assume the worst-case or the best



# Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of one computer system available to other computer systems on a network. Resource sharing can improve the efficiency, performance, and reliability of distributed systems by allowing multiple users and applications to access and utilize the same resources.

Some examples of resources that can be shared are:

- Files and directories: Users can store, retrieve, and modify data on remote file systems as if they were local.
- Printers and scanners: Users can send documents to print or scan on remote devices without having to physically connect them to their own computers.
- CPU and memory: Users can run programs or processes on remote computers that have more processing power or memory than their own computers.
- Software and applications: Users can access and use software and applications that are installed on remote computers without having to install them on their own computers.
- Databases and web servers: Users can query and update data on remote databases or access web pages and services hosted on remote web servers.

Resource sharing can be implemented in different ways depending on the network architecture, the type of resources, and the level of abstraction. Some common methods of resource sharing are:

- File transfer: Users can copy files from one computer to another using protocols such as FTP, SCP, or HTTP.
- Remote login: Users can log in to a remote computer and execute commands or run programs using protocols such as SSH, Telnet, or RDP.
- Remote procedure call: Users can invoke procedures or functions on a remote computer and receive the results using protocols such as RPC, SOAP, or REST.
- Distributed file system: Users can access and manipulate files and directories on a remote computer as if they were part of their own file system using protocols such as NFS, SMB, or HDFS.
- Distributed computing: Users can run programs or processes on a remote computer and share the CPU and memory resources using frameworks such as MPI, MapReduce, or Spark.
- Cloud computing: Users can access and use software and applications that are hosted on remote servers and pay only for the resources they consume using platforms such as AWS, Azure, or Google Cloud.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a processor, a memory, a disk, a network, or a peripheral device .
- Resource contention affects the execution behavior and schedulability of jobs or tasks, especially in priority-driven systems, where higher-priority jobs or tasks may be blocked or delayed by lower-priority ones that hold the resource  .
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how jobs or tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock  .
- Priority inversion occurs when a higher-priority job or task is preempted by a lower-priority one that holds the resource, or when a lower-priority job or task inherits the priority of a higher-priority one that is waiting for the resource  .
- Timing anomalies occur when a change in the execution time of a job or task affects the schedulability of other jobs or tasks in an unpredictable or counter-intuitive way  .
- Deadlock occurs when a set of jobs or tasks are waiting for each other to release the resources they hold, resulting in a circular dependency that prevents any of them from making progress  .
- Some examples of RAC protocols are priority inheritance protocol (PIP), priority ceiling protocol (PCP), stack resource policy (SRP), and multiprocessor priority ceiling protocol (MPCP) .
- These protocols aim to prevent or limit priority inversion, timing anomalies, and deadlock by enforcing certain rules on the locking and unlocking of resources, such as giving the resource to the highest-priority job or task, raising the priority of the job or task that holds the resource, or blocking the job or task that requests the resource .
- The effectiveness and performance of RAC protocols depend on various factors, such as the number and type of resources, the number and priority of jobs or tasks, the length and frequency of critical sections, the degree of concurrency and parallelism, and the overhead of locking and unlocking operations .



# Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies a shared resource, such as a variable, a file, a device, etc. .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of NPCS are:
  - It is simple to implement and understand.
  - It prevents deadlock, since no job is ever preempted when it holds any resource.
  - It preserves the temporal correctness of the system, since no job can be blocked by a lower-priority job.
- The disadvantages of NPCS are:
  - It may cause priority inversion, since a higher-priority job may have to wait for a lower-priority job to finish its critical section.
  - It may reduce the processor utilization, since a job holding a resource may not be able to use the processor effectively.
  - It may increase the response time and jitter of the jobs, since they may have to wait for an unpredictable amount of time to enter their critical sections.



# Basic Priority-Inheritance and Priority-Ceiling Protocols

## Priority-Inheritance Protocol (PIP)

- It is a critical resource sharing protocol for real-time systems that allows a low-priority job to inherit the priority of a higher-priority job that is blocked by it.
- It overcomes the limitations of traditional priority-based scheduling, such as unbounded priority inversion and chain blocking.
- It requires minimum support from the operating system or the hardware, and can be implemented easily.
- It cannot prevent the deadlock, and may still suffer from long blocking times and high overheads.
- The basic rules of PIP are:

  1. A job can lock a resource only if it is not locked by another job, or if it has inherited the priority of the job that locked the resource.
  2. A job that locks a resource inherits the priority of the highest-priority job that is blocked by it, or by any other job that transitively depends on it.
  3. A job that releases a resource reverts to its original priority, unless it still holds another resource that requires a higher priority.

- An example of PIP is shown below:

  PIP example

  - In this example, there are three jobs J1, J2, and J3, with priorities 1, 2, and 3 respectively (higher number means higher priority).
  - There are two resources R1 and R2, both initially free.
  - At time 0, J1 locks R1 and starts executing.
  - At time 1, J2 arrives and preempts J1, since it has a higher priority.
  - At time 2, J2 tries to lock R2, but it is blocked by J1, which holds R1.
  - At time 3, J3 arrives and preempts J1, since it has the highest priority.
  - At time 4, J3 tries to lock R1, but it is blocked by J1, which holds R1.
  - At this point, J1 inherits the priority of J3, since it blocks J3 directly, and J2 indirectly.
  - J1 resumes execution and releases R1 at time 5.
  - J3 then locks R1 and starts executing.
  - J1 reverts to its original priority and is blocked by J2, which holds R2.
  - J3 releases R1 at time 6 and completes.
  - J2 then locks R1 and starts executing.
  - J2 releases R1 and R2 at time 7 and completes.
  - J1 then resumes execution and completes at time 8.

## Priority-Ceiling Protocol (PCP)

- It is a critical resource sharing protocol for real-time systems that prevents a low-priority job from locking a resource if a higher-priority job may need it in the future.
- It overcomes the limitations of PIP and traditional priority-based scheduling, such as unbounded priority inversion, chain blocking, and deadlock.
- It requires maximum support from the operating system or the hardware, and can be implemented with some complexity.
- It guarantees the shortest blocking time and the lowest overhead among all resource sharing protocols.
- The basic rules of PCP are:

  1. Each resource is assigned a priority ceiling, which is the highest priority of any job that may lock the resource.
  2. A job can lock a resource only if its priority is higher than the priority ceilings of all the resources that are currently locked by other jobs.
  3. A job that locks a resource inherits the priority ceiling of the resource, and keeps it until it releases the resource.
  4. A job that releases a resource reverts to its original priority, unless it still holds another resource that requires a higher priority.

- An example of PCP is shown below:

  PCP example

  - In this example, there are three jobs J1, J2, and J3, with priorities 1, 2, and 3 respectively (higher number means higher priority).
  - There are two resources R1 and R2, both initially free, with priority ceilings 3 and 2 respectively.
  - At time 0, J1 locks R1 and starts executing.
  - At time 1, J2 arrives and preempts J1, since it has a higher



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- SBPCP has the following rules:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its current priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its current priority is restored to its original priority, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its current priority is higher than the current priority of the other task.
- SBPCP has the following properties:
  - SBPCP prevents deadlock, as a circular wait among tasks is impossible.
  - SBPCP prevents unbounded priority inversion, as a task can be blocked by a lower priority task for at most one critical section.
  - SBPCP is optimal, as it allows any feasible set of tasks to be scheduled without missing any deadlines.
  - SBPCP is stack optimal, as it minimizes the total stack space required by the tasks.



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that may access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no circular wait is possible .
- An example of using priority ceiling protocol in a dynamic priority system is given below :

example

- In this example, there are two tasks T1 and T2 with dynamic priorities and two resources X and Y with priority ceilings .
- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 6 and so on .
- The system ceiling is the maximum of the priority ceilings of the locked resources at any time .
- The table below shows the priority ceilings and the system ceiling at different time intervals :

| Time | Priority ceiling of X | Priority ceiling of Y | System ceiling |
|------|-----------------------|-----------------------|----------------|
| 0-1  | 1                     | 2                     | 0              |
| 1-2  | 1                     | 2                     | 1              |
| 2-3  | 1                     | 2                     | 2              |
| 3-4  | 1                     | 2                     | 1              |
| 4-5  | 2                     | 2                     | 2              |
| 5-6  | 2                     | 1                     | 2              |
| 6-7  | 2                     | 1                     | 1              |
| 7-8  | 2                     | 1                     | 0              |

- The priority ceiling protocol ensures that T1 and T2 can access the resources without deadlock or unbounded priority inversion .
- However, the protocol may cause some blocking of higher priority tasks by lower priority tasks when the priority ceilings change .
- For example, T1 is blocked by T2 from time 4 to 5 when the priority ceiling of X becomes 2 .
- This blocking can be reduced by using the Immediate Ceiling Priority Protocol (ICPP), which assigns the priority ceiling of a resource to a task as soon as it requests the resource, rather than when it locks it.
- This way, T1 would inherit the priority ceiling of X as soon as it requests it at time 4 and would not be blocked by T2.
- The table below shows the priority ceilings and the system ceiling at different time intervals using ICPP:

| Time | Priority ceiling of X | Priority ceiling of Y | System ceiling |
|------|-----------------------|-----------------------|----------------|
| 0-1  | 1                     | 2                     | 0              |
| 1-2  | 1



# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a shared resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the actual priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better schedulability than static preemption ceiling protocol, but it requires more memory and synchronization primitives.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can reduce the number of context switches and improve the performance of real-time systems, but it may also cause long priority inversion and deadlock.
- Preemption ceiling protocol can solve these problems by enforcing the ceiling priority of the resources as the preemption threshold of the tasks that lock them.
- Preemption ceiling protocol is suitable for object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Preemption ceiling protocol can avoid the inheritance anomaly, which is a situation where a task inherits multiple priorities from different objects and causes unpredictable behavior.



# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section .
- The challenge of access control in multiple-unit resources is to avoid deadlock and unbounded blocking, while ensuring schedulability and resource utilization.
- Some of the protocols for access control in multiple-unit resources are:
  - **Priority Inheritance Protocol (PIP)**: A job that locks a resource inherits the highest priority of all the jobs waiting for any unit of that resource. When the job unlocks the resource, it reverts to its original priority.
  - **Priority Ceiling Protocol (PCP)**: Each resource is assigned a priority ceiling, which is the highest priority of any job that may lock that resource. A job can lock a resource only if its priority is higher than the priority ceilings of all the locked resources. A job that locks a resource inherits the priority ceiling of that resource until it unlocks it.
  - **Stack Resource Policy (SRP)**: Each job is assigned a preemption level, which is fixed and unique. A job can lock a resource only if its preemption level is higher than the preemption levels of all the jobs that have locked any resource. A job that locks a resource cannot be preempted by any other job until it unlocks the resource.
  - **Multiprocessor Priority Ceiling Protocol (MPCP)**: A variant of PCP for multiprocessor systems, where each resource is assigned to a processor and a priority ceiling. A job can lock a resource only if it is executing on the same processor as the resource, and its priority is higher than the priority ceilings of all the locked resources on that processor. A job that locks a resource inherits the priority ceiling of that resource until it unlocks it.
  - **Multiprocessor Stack Resource Policy (MSRP)**: A variant of SRP for multiprocessor systems, where each resource is assigned to a processor and a preemption level. A job can lock a resource only if its preemption level is higher than the preemption levels of all the jobs that have locked any resource on any processor. A job that locks a resource cannot be preempted by any other job until it unlocks the resource.



# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or violation of mutual exclusion.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and mutual exclusion.
- Concurrency control algorithms for real time systems should also consider the timing constraints of the jobs and avoid unnecessary blocking or priority inversion.
- Some of the common concurrency control algorithms for real time systems are:

  - **Priority-ceiling protocol**: This protocol assigns a priority ceiling to each data object, which is the highest priority of any job that can access that object. A job can lock a data object only if its priority is higher than the current system ceiling, which is the highest priority ceiling of all the locked objects. This protocol prevents deadlock and bounds the blocking time of any job by the execution time of one critical section of a lower priority job.
  - **Immediate-ceiling protocol**: This protocol is a variation of the priority-ceiling protocol, where the priority of a job is raised to the priority ceiling of the object it locks as soon as it requests the lock. This protocol prevents deadlock and reduces the blocking time of any job by the execution time of at most one critical section of a lower priority job.
  - **Priority-inheritance protocol**: This protocol allows a job that is blocked by a lower priority job to inherit the priority of the blocked job until it releases the lock. This protocol prevents unbounded priority inversion and reduces the blocking time of any job by the execution time of all the critical sections of the lower priority jobs that access the same object.
  - **Convex-ceiling protocol**: This protocol assigns a convex ceiling to each data object, which is the lowest priority of any job that can access that object. A job can lock a data object only if its priority is higher than the current system floor, which is the lowest priority of all the active jobs. This protocol prevents deadlock and bounds the blocking time of any job by the execution time of one critical section of a higher priority job.
  - **Timestamp-based protocol**: This protocol assigns a timestamp to each job based on its deadline or arrival time, and uses the timestamp to order the requests for data objects. A job can lock a data object only if its timestamp is smaller than the timestamp of any other job that has requested the same object. This protocol ensures serializability and preserves the temporal order of the jobs.
  - **Wait-free protocol**: This protocol allows a job to access a data object without waiting for any other job, by using a versioning scheme or a replication scheme. A versioning scheme maintains multiple versions of a data object, each with a timestamp, and allows a job to read the latest version that is consistent with its timestamp. A replication scheme maintains multiple copies of a data object, each with a timestamp, and allows a job to write to the copy that is consistent with its timestamp. This protocol ensures wait-freedom and avoids blocking, but may incur high overhead and storage costs.



## Unit 4 - Real Time Communication

Real time communication (RTC) is the exchange of information between two or more parties without significant delay. RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required. RTC can involve different types of media, such as text, audio, video, or data.

Some examples of RTC applications are:

- Instant messaging (IM): A form of text-based communication that allows users to send and receive messages in real time, usually over the internet or a local network. IM can also support file transfer, voice chat, video chat, or group chat.
- Voice over Internet Protocol (VoIP): A technology that enables voice communication over the internet or other IP networks. VoIP can use various protocols, such as Session Initiation Protocol (SIP), H.323, or Skype, to establish and manage calls. VoIP can also support video calls, conferencing, or faxing.
- Video conferencing: A form of RTC that allows two or more parties to see and hear each other using video and audio devices, such as webcams, microphones, and speakers. Video conferencing can use different platforms, such as Zoom, Google Meet, or Microsoft Teams, to facilitate collaboration, education, or entertainment.
- Streaming: A form of RTC that involves transmitting or receiving continuous media, such as audio or video, over the internet or a network. Streaming can be live or on-demand, depending on the availability and delivery of the content. Streaming can use different formats, such as MPEG, MP3, or MP4, to encode and compress the media.
- Online gaming: A form of RTC that involves playing games over the internet or a network, either individually or with other players. Online gaming can use different genres, such as action, strategy, or role-playing, to create immersive and interactive experiences. Online gaming can also support voice chat, text chat, or video chat among players.

Some benefits of RTC are:

- It can enhance communication and collaboration among individuals or groups, regardless of their physical location or time zone.
- It can reduce costs and increase efficiency by eliminating the need for travel, phone calls, or physical meetings.
- It can provide more flexibility and convenience by allowing users to access RTC services from any device, anywhere, and anytime.
- It can improve customer service and satisfaction by enabling faster and more personalized interactions with clients or customers.
- It can create new opportunities and markets by enabling new forms of entertainment, education, or commerce.

Some challenges of RTC are:

- It can require high bandwidth and low latency to ensure good quality and performance of the RTC services.
- It can pose security and privacy risks by exposing sensitive or personal information to unauthorized parties or malicious attacks.
- It can create compatibility and interoperability issues by using different standards, protocols, or platforms for RTC services.
- It can cause social and ethical problems by affecting human relationships, behaviors, or values.



# Basic Concepts in Real Time Communication

Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Remote control and teleoperation

Some of the basic concepts in real time communication are:

- **Bandwidth**: The amount of data that can be transmitted or received per unit of time. Bandwidth is measured in bits per second (bps) or multiples of it, such as kilobits per second (kbps), megabits per second (Mbps), or gigabits per second (Gbps). Bandwidth affects the quality and speed of real time communication.
- **Latency**: The time it takes for a signal to travel from the source to the destination and back. Latency is measured in milliseconds (ms) or microseconds (µs). Latency affects the responsiveness and interactivity of real time communication.
- **Jitter**: The variation in latency over time. Jitter is caused by network congestion, packet loss, or other factors that disrupt the smooth flow of data. Jitter affects the consistency and reliability of real time communication.
- **Packet loss**: The percentage of data packets that are lost or corrupted during transmission. Packet loss is caused by network congestion, errors, or interference. Packet loss affects the quality and completeness of real time communication.
- **Codec**: A software or hardware device that compresses and decompresses data for transmission or storage. Codec stands for coder-decoder. Codec affects the quality and efficiency of real time communication.
- **Protocol**: A set of rules and standards that govern how data is formatted, transmitted, and received. Protocol affects the compatibility and interoperability of real time communication.
- **Encryption**: A process of transforming data into an unreadable form to protect it from unauthorized access or modification. Encryption affects the security and privacy of real time communication.
- **Feedback**: A process of sending and receiving information about the performance or quality of real time communication. Feedback affects the improvement and adjustment of real time communication.



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic damage or loss of life  .
- A soft real-time communication system is one that can tolerate some deadline misses, without causing severe harm or degradation of service  .
- Examples of hard real-time communication systems are:
  - Air traffic control systems 
  - Nuclear power plant control systems 
  - Missile guidance systems 
- Examples of soft real-time communication systems are:
  - Multimedia streaming systems 
  - Online gaming systems 
  - Voice over IP systems 
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic.
- Hard real-time communication systems require strict guarantees on the timing and reliability of the communication, while soft real-time communication systems can accept some variations and errors.
- Hard real-time communication systems often use dedicated hardware and software, while soft real-time communication systems can use general-purpose hardware and software.
- Hard real-time communication systems are more complex and costly to design, implement, and maintain, while soft real-time communication systems are more flexible and adaptable.
- Hard real-time communication systems are more suitable for safety-critical and mission-critical applications, while soft real-time communication systems are more suitable for performance-critical and quality-critical applications.



# Model of Real Time Communication

- Real time communication (RTC) is any live telecommunications method in which all users can interact in a live capacity, with negligible latency  .
- RTC can involve different types of data, such as voice, video, text, images, etc.
- RTC can be implemented using various technologies, such as landlines, mobile phones, VoIP, WebRTC, etc.
- RTC can be used for various applications, such as online gaming, video conferencing, telemedicine, remote education, etc.
- RTC can be modeled using different parameters, such as traffic, throughput, delay, jitter, etc.

## Real Time Traffic Model

- The real time traffic means isochronous or synchronous traffic, consisting stream of message that are generated by their sources and delivered to their respective destination on continuous basis.
- The traffic includes the periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals and have fixed deadlines.
- Aperiodic messages are generated at irregular intervals and have variable deadlines.
- Sporadic messages are generated at random intervals and have unpredictable deadlines.
- In real time traffic model, each message (Mi) can be characterized by tuples of inter-packet spacing (Pi), message length (ei), reception deadline (Di) as below:

  Mi = (pi, ei, Di)

- This traffic model is called peak rate model in real time communication.

## Throughput, Delay and Jitter

- Throughput is the amount of data that can be transmitted or received per unit time.
- Throughput can be affected by various factors, such as bandwidth, congestion, errors, etc.
- Delay is the time taken for a message to travel from the source to the destination.
- Delay can be composed of various components, such as propagation delay, transmission delay, queuing delay, processing delay, etc.
- Jitter is the variation in delay for different messages in the same stream.
- Jitter can be caused by various factors, such as network congestion, routing changes, packet loss, etc.
- Jitter can affect the quality of service (QoS) of real time communication, especially for voice and video applications.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- In real-time communication networks, packets need to be transmitted with certain quality of service (QoS) guarantees, such as delay, jitter, throughput, and loss rate.
- Priority-based service disciplines are a class of scheduling algorithms that assign different priorities to different packets or flows, and serve them according to their priority levels.
- Weighted round-robin (WRR) service disciplines are a class of scheduling algorithms that assign different weights to different packets or flows, and serve them in a circular order with a proportion of the server capacity proportional to their weights.
- Both priority-based and WRR service disciplines can be used to achieve QoS differentiation and fairness among different packets or flows in switched networks, such as routers, switches, and multiplexers.

## Priority-Based Service Disciplines

- According to a priority-based service discipline, the transmission of ready packets are scheduled in a priority-driven manner. The packets or flows with higher priority are served before the packets or flows with lower priority.
- Priority-based service disciplines can be classified into two types: strict priority (SP) and weighted fair queuing (WFQ).
- SP discipline serves the packets or flows in the order of their priority levels, without any regard to their arrival times or sizes. SP discipline can achieve the highest QoS for the highest priority packets or flows, but it may starve the lower priority packets or flows if the higher priority traffic is heavy or bursty.
- WFQ discipline serves the packets or flows in a weighted order of their virtual finish times, which are calculated based on their arrival times, sizes, and weights. WFQ discipline can achieve both QoS differentiation and fairness among different packets or flows, by giving more service to the higher priority packets or flows, but also guaranteeing a minimum service to the lower priority packets or flows.

## Weighted Round-Robin Service Disciplines

- According to a WRR service discipline, the transmission of ready packets are scheduled in a circular order, with each packet or flow getting a share of the server capacity proportional to its weight. The packets or flows with higher weights are served more frequently and for longer durations than the packets or flows with lower weights.
- WRR service disciplines can be classified into two types: simple WRR (SWRR) and frame-based WRR (FWRR).
- SWRR discipline serves the packets or flows in a circular order, with each packet or flow getting a fixed number of bytes or slots per round. SWRR discipline can achieve QoS differentiation among different packets or flows, by giving more service to the higher weight packets or flows, but it may cause large delay jitter and unfairness if the packet or flow sizes are variable or bursty.
- FWRR discipline serves the packets or flows in a circular order, with each packet or flow getting a fixed amount of time or rate per round. FWRR discipline can achieve both QoS differentiation and fairness among different packets or flows, by giving more service to the higher weight packets or flows, but also guaranteeing a maximum delay jitter and a minimum service rate to the lower weight packets or flows.



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless broadcast network.
- Broadcast networks allow multiple nodes to transmit data to all other nodes in the network, which can be useful for real-time communication applications such as video conferencing, sensor networks, or vehicular networks.
- However, broadcast networks also face the challenge of avoiding or resolving collisions, which occur when two or more nodes transmit data at the same time, resulting in interference and data loss.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic scheduling, or hybrid protocols.
- Probabilistic contention protocols utilize direct, asynchronous competition between neighboring nodes to determine which node will transmit next. Examples include Aloha, CSMA, and IEEE 802.11.
- Deterministic scheduling protocols assign fixed or dynamic time slots to each node, ensuring collision-free transmission. Examples include TDMA, FDMA, and CDMA.
- Hybrid protocols combine elements of both contention and scheduling protocols, aiming to achieve high throughput, low delay, and adaptability. Examples include ABROAD, PRMA, and MACAW.
- The design and performance of MAC protocols depend on various factors, such as the network topology, the traffic pattern, the channel characteristics, the node capabilities, and the quality of service requirements.



# Internet and Resource Reservation Protocols

- Internet applications have different network performance requirements, such as reliability, timeliness, and quality of service (QoS)  .
- Resource Reservation Protocol (RSVP) is a transport layer protocol that enables Internet applications to obtain specific QoS for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows .
- RSVP is receiver-initiated, meaning that the receiver of a data flow requests a certain QoS from the network and the sender adapts to the available resources  .
- RSVP uses soft state, meaning that the reservations are periodically refreshed and can be easily modified or deleted  .
- RSVP uses two types of messages: PATH and RESV. PATH messages are sent by the sender to inform the receivers and intermediate routers about the characteristics of the data flow. RESV messages are sent by the receiver to request a certain QoS and reserve resources along the path  .
- RSVP can work with two service models: integrated services (IntServ) and differentiated services (DiffServ). IntServ provides end-to-end QoS guarantees by reserving resources for each data flow. DiffServ provides aggregate QoS by classifying and marking data packets into different service classes .



# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can handle data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and resource sharing, but do not guarantee any timing requirements.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to run multiple tasks or threads concurrently, each with its own priority and scheduling policy.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between threads, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, etc.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to protect the memory space of each thread from corruption or interference by other threads.
  - Interrupt handling: The ability to respond to external or internal events that require immediate attention, such as hardware inputs, timers, or exceptions.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, or network interfaces, using standard or custom protocols.
- An RTOS is suitable for applications that have real-time requirements, such as industrial control, embedded systems, robotics, avionics, or multimedia.

## Real Time Databases

- A real time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive.
- A real time database is different from a traditional database, which contains data that is persistent and changes much less frequently.
- A real time database typically has the following characteristics :
  - High performance: The ability to write and read data within a strict time bound, usually on the order of seconds to milliseconds.
  - High availability: The ability to maintain data consistency and integrity even in the presence of failures, such as network partitions, power outages, or hardware malfunctions.
  - High scalability: The ability to handle increasing data volumes and concurrent users without compromising performance or availability.
  - High flexibility: The ability to support various data types and structures, such as structured, semi-structured, or unstructured data, and to adapt to changing data schemas and queries.
- A real time database is suitable for applications that need to process and analyze data in real time, such as online transactions, streaming analytics, IoT, or gaming .

## Operational Database

- An operational database is a type of real time database that is oriented toward real-time, transactional operations.
- An operational database is different from a data warehouse, which is a type of traditional database that is oriented toward historical, analytical operations.
- An operational database typically has the following attributes:
  - Low latency: The ability to execute transactions and queries with minimal delay, usually on the order of microseconds to milliseconds.
  - High throughput: The ability to process a large number of transactions and queries per second, usually on the order of thousands to millions.
  - ACID compliance: The ability to ensure that transactions are atomic, consistent, isolated, and durable, meaning that they are executed as a whole, without errors, without interference, and without loss.
  - Data freshness: The ability to reflect the most recent state of the data, without stale or outdated information.
- An operational database is suitable for applications that need to perform real-time, transactional operations on the data, such as e-commerce, banking, or social media.



# Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks in a system that has strict timing constraints. An RTOS is different from a general-purpose operating system, which may not be able to meet the deadlines or respond as quickly as required by the system.

Some of the features of an RTOS are:

- **Small and fast**: An RTOS is designed to be compact and efficient, occupying less memory and consuming fewer resources than a general-purpose operating system. An RTOS can also perform tasks quickly and with low overhead, minimizing the latency and jitter in the system.
- **Responsive and deterministic**: An RTOS can respond to events or interrupts in a timely and consistent manner, ensuring that the system behaves as expected every time. An RTOS can also guarantee that tasks will be completed within a specified time bound, regardless of the system load or other factors.
- **Preemptive and prioritized**: An RTOS can support preemptive scheduling, which means that a higher-priority task can interrupt a lower-priority task and resume it later. This allows the RTOS to allocate the CPU time to the most urgent or critical tasks in the system. An RTOS can also assign different priority levels to tasks based on their importance or urgency, and schedule them accordingly.
- **Cooperative and multitasking**: An RTOS can support cooperative scheduling, which means that a task can voluntarily yield the CPU to another task when it is done or waiting for an event. This allows the RTOS to optimize the CPU utilization and avoid wasting resources. An RTOS can also support multitasking, which means that multiple tasks can run concurrently on the same CPU or on different CPUs in a multicore or distributed system.
- **Real-time and embedded**: An RTOS is designed to run on real-time systems, which are systems that have strict timing constraints and need to interact with the physical world in a timely and reliable manner. Examples of real-time systems are industrial control systems, robotics, avionics, medical devices, etc. An RTOS is also designed to run on embedded systems, which are systems that have limited hardware resources and are dedicated to a specific function or application. Examples of embedded systems are smart watches, sensors, cameras, etc.



# Time Services

- Time services are the functions provided by a real-time operating system (RTOS) to manage the temporal aspects of a real-time system.
- Time services include:
  - Clock interrupt processing: The RTOS handles the periodic clock interrupts generated by the hardware timer and updates the system time and the ready queue of tasks.
  - Providing high clock resolution: The RTOS can use a high-frequency hardware timer to provide a fine-grained measurement of time, which is useful for tasks with tight deadlines and high precision requirements.
  - Timers: The RTOS can create and manage software timers that can trigger events or actions after a specified amount of time or at a specific point in time.
  - Time synchronization: The RTOS can coordinate the clocks of different devices or nodes in a distributed real-time system to ensure a consistent notion of time across the system.
- Time services are essential for real-time systems because they enable the system to:
  - Meet the timeliness requirements of the tasks and the application.
  - Schedule the tasks according to their priorities and deadlines.
  - Monitor and control the physical devices and the environment.
  - Communicate and cooperate with other real-time systems.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like Unix strives to provide good average performance, for a RTOS, correct timing is the key feature.
- Unix is not a RTOS by default, but it can be modified or extended to support real-time features, such as:
  - Adding a real-time kernel or patch, such as RTLinux, Xenomai, or PREEMPT_RT, to the Linux kernel .
  - Using real-time libraries or frameworks, such as POSIX real-time extensions, RTAI, or ROS, to provide real-time APIs and services .
  - Configuring the system parameters, such as scheduling policies, priorities, interrupts, memory management, and device drivers, to reduce latency and jitter .
- Some advantages of using Unix as a RTOS are:
  - It is open source, widely available, and well supported by the community .
  - It offers a rich set of features, tools, and applications for general-purpose computing .
  - It can run on various hardware platforms, from embedded systems to supercomputers .
  - It can integrate with other systems and networks using standard protocols and interfaces .
- Some challenges of using Unix as a RTOS are:
  - It is not designed for hard real-time applications, where missing a deadline can have catastrophic consequences .
  - It may introduce unpredictable delays or overheads due to its complex and dynamic nature .
  - It may require extensive testing, tuning, and verification to ensure its real-time performance and reliability .
  - It may not comply with some industry standards or certifications for safety-critical systems .



# POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interface with an operating system.
- POSIX was originally designed for UNIX systems, but it has been extended to cover real-time operating systems as well.
- Real-time operating systems are systems that have strict timing constraints and need to respond to events in a predictable and timely manner.
- POSIX real-time standards aim to provide application portability and interoperability for real-time systems, by defining common interfaces for operating system services such as scheduling, synchronization, memory management, timers, signals, and message passing.
- Some of the POSIX real-time standards are:

  - POSIX.1b: Real-time extensions, which defines priority-based preemptive scheduling, high-resolution timers, asynchronous I/O, memory locking, and interprocess communication.
  - POSIX.1c: Threads extensions, which defines the creation, management, and synchronization of multiple threads of execution within a process.
  - POSIX.4: Timers and clocks, which defines various types of timers and clocks that can be used for measuring time and triggering events.
  - POSIX.13: Real-time streams, which defines a framework for processing streams of data in real-time, such as audio and video.
  - POSIX.22: Real-time controller system application program interface, which defines a standard interface for controlling real-time systems, such as robots and industrial machines.

- Some of the POSIX issues for real-time systems are:

  - POSIX does not define the semantics of real-time behavior, such as deadlines, jitter, and latency. It only defines the interfaces for real-time services, but not how they are implemented or guaranteed by the operating system.
  - POSIX does not address the issues of distributed real-time systems, such as communication protocols, fault tolerance, and synchronization across multiple nodes.
  - POSIX does not specify the performance or quality of service of the real-time services, such as the resolution, accuracy, and overhead of the timers and clocks, or the throughput and latency of the message passing and I/O operations.
  - POSIX does not cover all the aspects of real-time systems, such as power management, security, and resource allocation. It also does not define any standard libraries or tools for developing and testing real-time applications.
  - POSIX may not be compatible with some existing real-time operating systems, which may have different or proprietary interfaces and features. It may also not be sufficient for some specific or specialized real-time applications, which may require more functionality or flexibility than POSIX can provide.



# Characteristic of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, events, cycles, etc.
- Temporal data can be used to analyze weather patterns, traffic conditions, demographic trends, and other phenomena that change over time.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon.
- Temporal data can be stored in different ways, such as using timestamps, temporal attributes, temporal tables, temporal databases, etc.
- Temporal data can be queried and manipulated using different techniques, such as temporal SQL, temporal algebra, temporal logic, temporal constraints, etc.
- Temporal data can be visualized using different methods, such as temporal charts, maps, animations, etc.
- Temporal data can be validated and verified using different criteria, such as temporal consistency, temporal accuracy, temporal completeness, etc.



# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. Data staleness can be caused by delays in data acquisition, data transmission, data processing, or data storage.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other or with the physical environment. Data inconsistency can be caused by concurrent updates, data replication, data partitioning, or data corruption.
- Temporal consistency can be maintained by using various techniques, such as:
  - Data freshness, which is a measure of how recent the data stored in the database is. Data freshness can be improved by using periodic updates, triggered updates, or on-demand updates .
  - Data validity, which is a measure of how accurate the data stored in the database is. Data validity can be improved by using data verification, data correction, or data approximation.
  - Data coherence, which is a measure of how consistent the data stored in the database is. Data coherence can be improved by using concurrency control, data synchronization, or data reconciliation .
- Temporal consistency can be evaluated by using various metrics, such as:
  - Temporal error, which is the difference between the data stored in the database and the data in the physical environment.
  - Temporal precision, which is the maximum temporal error allowed for the data stored in the database.
  - Temporal accuracy, which is the probability that the data stored in the database has a temporal error less than or equal to the temporal precision.
  - Temporal reliability, which is the probability that the data stored in the database is temporally consistent.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency control is a procedure of managing simultaneous operations on a shared database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the respective database.
- Concurrency control is important for real-time database systems, which have to deal with both data consistency and timing constraints.
- A real-time database system must adapt to changes in the operating environment and guarantee the completion of critical transactions.
- Concurrency control in real-time database systems can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control prevents conflicts from occurring by locking data items before accessing them. Examples of pessimistic concurrency control are timestamp-based protocols and lock-based protocols.
- Optimistic concurrency control allows conflicts to occur and resolves them later by validating transactions before committing them. Examples of optimistic concurrency control are validation-based protocols and multiversion protocols.
- Concurrency control in real-time database systems can also be classified into two categories: centralized and distributed.
- Centralized concurrency control assumes that there is a single site that coordinates all the transactions and maintains the database. Centralized concurrency control is simpler and more efficient, but it has a single point of failure and a high communication overhead.
- Distributed concurrency control assumes that there are multiple sites that cooperate to execute transactions and maintain the database. Distributed concurrency control is more robust and scalable, but it has a higher complexity and a lower consistency.
- Concurrency control in real-time database systems should consider the following factors: transaction priority, deadline, data freshness, data availability, and system workload.
- Concurrency control in real-time database systems should balance the trade-off between performance and correctness. Performance refers to the ability to meet the timing constraints of transactions, while correctness refers to the ability to maintain the data consistency of the database.



# Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have to meet certain requirements, such as timeliness, consistency, concurrency, reliability, and availability.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have to guarantee strict deadlines for every transaction, and any missed deadline is considered a failure.
  - Soft real-time databases have to meet most of the deadlines, but some occasional deadline misses are acceptable.
- Some examples of commercial real-time databases are:
  - Raima Database Manager (RDM): a cross-platform, embedded, in-memory, SQL database that supports hard and soft real-time applications.
  - Oracle TimesTen: an in-memory, relational database that provides low-latency and high-throughput data access for real-time applications.
  - Google Cloud Firestore: a scalable, serverless, NoSQL database that provides real-time synchronization and offline support for web and mobile applications.
  - IBM Informix: a hybrid database that combines SQL, NoSQL, and time-series data for real-time analytics and IoT applications.
  - Microsoft SQL Server: a relational database that supports in-memory OLTP, temporal tables, and real-time operational analytics.

