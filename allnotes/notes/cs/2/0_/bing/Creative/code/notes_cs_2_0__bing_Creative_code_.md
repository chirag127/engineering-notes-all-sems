

# Real Time System

A real time system is a system that can process and respond to events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to handle concurrent and unpredictable events and guarantee the correctness and timeliness of its outputs. A real time system can be classified into two types based on the consequences of missing the deadlines:

- **Hard real time system**: A system that must meet all the deadlines, otherwise it will cause a catastrophic failure or unacceptable loss. For example, a flight control system, a nuclear reactor control system, or a pacemaker.
- **Soft real time system**: A system that can tolerate some deadline misses, but the quality of service or performance will degrade. For example, a video streaming system, a voice recognition system, or a web server.

Some of the characteristics of a real time system are:

- **Determinism**: The system must produce the same output for the same input and initial state, regardless of the timing of events or the execution order of tasks.
- **Responsiveness**: The system must react to events as soon as they occur and complete the required actions within the deadlines.
- **Predictability**: The system must be able to estimate the worst-case execution time and resource usage of each task and ensure that they are feasible and schedulable.
- **Reliability**: The system must be able to handle faults and errors and recover from them without compromising the safety or functionality of the system.
- **Time synchronization**: The system must be able to coordinate the actions of different components or devices that have independent clocks and operate in parallel.

Some of the applications of real time systems are:

- **Process control systems**: These systems are used to monitor and control physical processes such as temperature, pressure, flow, level, etc. in industrial plants, power plants, chemical plants, etc. They use sensors, actuators, controllers, and communication networks to achieve the desired output.
- **Machine vision systems**: These systems are used to help machines interpret visual data such as images, videos, or 3D models and perform tasks such as object recognition, face detection, gesture recognition, etc. They use cameras, processors, algorithms, and display devices to process the data and provide feedback or commands to the machines.
- **Robotics systems**: These systems are used to create machines that can perform tasks that are difficult, dangerous, or repetitive for humans, such as manufacturing, assembly, exploration, surgery, etc. They use sensors, motors, controllers, and communication networks to perceive the environment, plan the actions, and execute the movements.
- **Medical imaging systems**: These systems are used to capture, process, and display images of the internal structures or functions of the human body, such as X-rays, MRI, ultrasound, etc. They use scanners, processors, algorithms, and display devices to provide diagnosis or treatment to the patients.
- **Video wall systems**: These systems are used to create large-scale displays that consist of multiple screens or projectors that show synchronized images or videos. They use processors, communication networks, and display devices to provide entertainment or information to the viewers.



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failures or losses. For example, a nuclear reactor control system, an air traffic control system, or a pacemaker.
  - Soft real time systems are systems that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- Real time systems can also be classified into two types based on the predictability of their inputs or events: periodic systems and aperiodic systems.
  - Periodic systems are systems that have inputs or events that occur at regular intervals, such as sensor readings, clock ticks, or data packets. Periodic systems can be analyzed using techniques such as rate monotonic scheduling, earliest deadline first scheduling, or cyclic executive.
  - Aperiodic systems are systems that have inputs or events that occur at irregular or unpredictable intervals, such as user commands, interrupts, or faults. Aperiodic systems can be analyzed using techniques such as sporadic server, polling server, or deferrable server.
- Real time systems face many challenges and trade-offs, such as limited resources, concurrency, synchronization, fault tolerance, security, testing, verification, etc. Real time systems require careful design, implementation, and evaluation to ensure their correctness, efficiency, and robustness.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition for the notes of the unit 1 - introduction of real time system in the subject of real time system.

### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types: periodic and aperiodic.
- A periodic system is a system that has a set of tasks that must be executed repeatedly at regular intervals, called periods. For example, a sensor sampling task, a data processing task, or a display update task.
- An aperiodic system is a system that has a set of tasks that are triggered by unpredictable events or inputs, called arrivals. For example, a user request, a network packet, or an interrupt.
- A real time system can also be classified into two types: preemptive and non-preemptive.
- A preemptive system is a system that allows a higher priority task to interrupt and suspend a lower priority task that is currently executing, and resume it later when the higher priority task is completed. For example, a real time operating system, a real time scheduler, or a real time kernel.
- A non-preemptive system is a system that does not allow a higher priority task to interrupt a lower priority task that is currently executing, and waits until the lower priority task is completed before executing the higher priority task. For example, a batch processing system, a sequential system, or a cooperative system.



### Typical Real Time Applications

A real-time application (RTA) is an application that requires a timely response from the underlying system or hardware. The response time can vary depending on the nature and complexity of the application, but it is usually within milliseconds or microseconds. Real-time applications are often used in scenarios where human lives, safety, or quality of service depend on the system's performance.

Some examples of typical real-time applications are:

- **Digital control**: This is the use of digital devices, such as microprocessors, microcontrollers, or field-programmable gate arrays (FPGAs), to control physical processes or systems, such as motors, valves, pumps, or robots. Digital control systems can be classified into two types: hard real-time and soft real-time. Hard real-time systems have strict deadlines and cannot tolerate any delay or error in the control output. Soft real-time systems have more relaxed deadlines and can tolerate some delay or error in the control output, but still aim to optimize the system performance.  

- **Optimal control**: This is the use of mathematical techniques, such as optimization, dynamic programming, or calculus of variations, to find the best control strategy for a system or process, such as a rocket, a car, or a chemical plant. Optimal control systems can be classified into two types: open-loop and closed-loop. Open-loop systems do not use feedback from the system output to adjust the control input. Closed-loop systems use feedback from the system output to adjust the control input, and can adapt to changes or uncertainties in the system or environment. Optimal control systems are usually hard real-time systems, as they need to compute and apply the optimal control input within a given time frame. 

- **Command and control**: This is the use of computer systems to monitor, coordinate, and direct the actions of human or machine agents, such as soldiers, vehicles, or weapons, in a military, civil, or emergency situation. Command and control systems can be classified into two types: centralized and decentralized. Centralized systems have a single authority or decision maker that issues commands and receives feedback from the agents. Decentralized systems have multiple authorities or decision makers that communicate and cooperate with each other and the agents. Command and control systems are usually hard real-time systems, as they need to respond quickly and accurately to changing situations and threats.  

- **Signal processing**: This is the use of mathematical or computational methods to analyze, modify, or synthesize signals, such as sound, image, video, or radar. Signal processing systems can be classified into two types: offline and online. Offline systems process signals that are already recorded or stored, and do not have any time constraints. Online systems process signals that are generated or received in real time, and have to meet certain deadlines or quality requirements. Online signal processing systems are usually soft real-time systems, as they can tolerate some delay or error in the signal output, but still aim to enhance or extract useful information from the signal. 

- **Tracking**: This is the use of sensors, such as cameras, radars, or GPS, to measure and estimate the position, velocity, or orientation of a moving object, such as a person, a vehicle, or a missile. Tracking systems can be classified into two types: passive and active. Passive systems only observe the object and do not affect its motion. Active systems also interact with the object and can influence its motion, such as by guiding or intercepting it. Tracking systems are usually hard real-time systems, as they need to provide accurate and timely information about the object's state and motion. 

- **Real-time databases**: These are databases that store and manipulate data that have temporal constraints or deadlines, such as sensor data, stock prices, or reservation records. Real-time databases can be classified into two types: snapshot and transactional. Snapshot databases only store the most recent or relevant data, and discard or archive the old or irrelevant data. Transactional databases store and update the data using transactions, which are sequences of operations that have to be executed atomically, consistently, isolatedly, and durably (ACID properties). Real-time databases are usually soft real-time systems, as they can tolerate some delay or error in the data access or update, but still aim to maintain the data consistency and integrity. 

- **Multimedia**: These are applications that involve the generation, processing, or presentation of multiple types of media, such as audio, video, text, or graphics. Multimedia applications can be classified into two



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of release times for the notes of the unit 1 - introduction of real time system in the subject of real time system. Here is the content I have written:

### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the unit 1 - introduction of real time system in the subject of real time system will be released on the following dates:
  - Lecture 1: Introduction to Real Time Systems - 20th March 2023
  - Lecture 2: Characteristics and Challenges of Real Time Systems - 22nd March 2023
  - Lecture 3: Classification and Examples of Real Time Systems - 24th March 2023
  - Lecture 4: Real Time Scheduling - 26th March 2023
  - Lecture 5: Real Time Operating Systems - 28th March 2023
- The notes will be available on the online learning platform of the university and can be accessed by the registered students of the subject.
- The notes will contain the following information:
  - The objectives and learning outcomes of each lecture
  - The main concepts and definitions of real time systems
  - The diagrams and examples of real time systems and their applications
  - The exercises and questions for self-assessment and revision
  - The references and further readings for each lecture
- The notes will be prepared by the subject coordinator and the lecturers of the subject and will be reviewed by the quality assurance team of the university.
- The notes will be updated and revised periodically based on the feedback and suggestions from the students and the lecturers.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Real Time System. Here is the content for the topic of Deadlines for the notes of the Unit 1 - Introduction of Real Time System:

```markdown
### Deadlines for the notes of the Unit 1 - Introduction of Real Time System

- A deadline is a time limit or a constraint that specifies when a task or an activity must be completed or terminated.
- Deadlines are important for real time systems because they ensure the timeliness and predictability of the system's behavior and performance.
- There are different types of deadlines for real time systems, such as:
  - Hard deadline: A hard deadline is a deadline that must be met without any exception or tolerance. Missing a hard deadline can result in a catastrophic failure or a severe degradation of the system's functionality or quality of service. For example, a hard deadline for an airbag deployment system is the time before the collision occurs.
  - Soft deadline: A soft deadline is a deadline that can be missed occasionally or with some acceptable degree of deviation. Missing a soft deadline can result in a reduced performance or a lower quality of service, but not a failure of the system. For example, a soft deadline for a video streaming system is the time before the buffer underflows or overflows.
  - Firm deadline: A firm deadline is a deadline that can be missed occasionally, but with no benefit or penalty for the system. Missing a firm deadline means that the task or the activity is no longer useful or relevant for the system. For example, a firm deadline for a weather forecasting system is the time before the forecast becomes obsolete or inaccurate.
- Deadlines can also be classified as:
  - Static deadline: A static deadline is a deadline that is fixed and known in advance. A static deadline does not change during the execution of the system. For example, a static deadline for a periodic task is the period of the task.
  - Dynamic deadline: A dynamic deadline is a deadline that is variable and determined at run time. A dynamic deadline can change during the execution of the system depending on the system's state, environment, or input. For example, a dynamic deadline for an aperiodic task is the time before the next request arrives.
- Deadlines can be specified as:
  - Absolute deadline: An absolute deadline is a deadline that is expressed as a fixed point in time. An absolute deadline is independent of the start time or the completion time of the task or the activity. For example, an absolute deadline for a flight reservation system is the time before the flight departs.
  - Relative deadline: A relative deadline is a deadline that is expressed as an offset or a duration from the start time or the completion time of the task or the activity. A relative deadline is dependent on the start time or the completion time of the task or the activity. For example, a relative deadline for a sensor data processing system is the time after the data is received or processed.
```



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must produce the expected result by a specific deadline .
- The deadline is the maximum acceptable delay between the occurrence of an event and the completion of the system's response to that event.
- The correctness of the result in a real-time system depends not only on the logical correctness but also on the timeliness of the result.
- A timing constraint is a restriction or requirement on the timing behavior of a real-time system.
- Timing constraints can be classified into two categories :
  - Performance constraints: The constraints enforced on the response of the system, such as the minimum and maximum response time, the average response time, the throughput, etc.
  - Scheduling constraints: The constraints enforced on the execution of the tasks in the system, such as the deadlines, the priorities, the periods, the execution time, etc.
- Timing constraints can be further classified into three types based on the severity of the consequences of missing the deadline:
  - Hard constraints: The constraints that must be met for the system to function correctly. Missing a hard constraint can cause catastrophic failure or unacceptable loss.
  - Soft constraints: The constraints that should be met for the system to perform optimally. Missing a soft constraint can cause degraded performance or reduced quality of service.
  - Firm constraints: The constraints that have a benefit only if met, but no benefit if missed. Missing a firm constraint can cause wasted resources or missed opportunities.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval algebra, event calculus, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual timing behavior of the system and compare it with the expected timing behavior.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of hard real time systems for the unit 1 - introduction of real time system in the subject of real time system.

### Hard Real Time Systems

- A hard real time system is a system that must meet its deadlines, otherwise it may cause a system failure or a catastrophic consequence .
- A deadline is the maximum time allowed for a task to complete its execution.
- A hard real time system is also known as an immediate real time system.
- Examples of hard real time systems are nuclear power plant control, air traffic control, missile guidance, pacemaker, etc .
- A hard real time system has the following characteristics  :
  - The size of data and the number of tasks are fixed and known in advance.
  - The response time is in milliseconds or microseconds.
  - The peak load performance should be predictable and consistent.
  - The system should be able to handle faults and errors gracefully and recover quickly.
  - The system should be able to synchronize and coordinate with other devices and clocks.
  - The system should be able to handle high concurrency and parallelism.
  - The system should be able to prioritize tasks based on their urgency and importance.
  - The system should be able to guarantee the quality of service and the correctness of the results.
- A hard real time system requires a real time operating system (RTOS) that can support the above characteristics  .
- A RTOS is an operating system that can schedule tasks based on their deadlines and priorities, and can provide low latency and high throughput .
- Examples of RTOS are VxWorks, QNX, FreeRTOS, etc .
- A hard real time system also requires a real time hardware that can provide fast and reliable processing, communication, and memory .
- Examples of real time hardware are Intel® TCC, Intel® TSN, etc .



### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a catastrophic failure or a significant degradation of performance .
- A soft real-time system has a **soft deadline**, which is a desired time limit for completing a task, but not a strict requirement. Missing a soft deadline may result in lower quality of service, reduced user satisfaction, or increased costs, but not in a fatal error or a system crash .
- A soft real-time system can be run on multiple cores and impose fewer restrictions on applications, such as memory management, scheduling, and synchronization. A soft real-time system can also handle more complex and dynamic tasks than a hard real-time system, which has a rigid deadline and a deterministic behavior.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications, such as video conferencing, online gaming, and multimedia playback.
  - Process control systems, such as industrial automation, smart grid, and traffic management.
  - User interface systems, such as virtual reality, augmented reality, and gesture recognition.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of reference models for real time systems:

### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system, not a system design specification .
- A reference model helps us to reason about the timing behavior and performance of a real time system, using consistent terminology and focusing on the important aspects while ignoring the irrelevant details .
- A reference model consists of three elements :
  - A workload model: It specifies the applications supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, resource dependencies, etc.), their arrival patterns (e.g., periodic, sporadic, aperiodic, etc.), and their precedence relations (e.g., task graph, data flow, etc.).
  - A resource model: It describes the resources available to the system, such as the CPU, memory, network, sensors, actuators, etc., their types (e.g., preemptive, non-preemptive, shared, exclusive, etc.), and their relations (e.g., hierarchy, topology, contention, etc.).
  - A system model: It defines the policies and mechanisms used by the system to manage the workload and the resources, such as the scheduling algorithm, the synchronization protocol, the communication protocol, the fault tolerance technique, etc.
- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- A reference model can be used to analyze, compare, and evaluate different real time systems, as well as to guide the design and implementation of new real time systems .



### Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. A resource can be preemptable or non-preemptable. Example: printer, memory, file, semaphore.
- A real-time system must manage the allocation and scheduling of processors and resources to meet the timing constraints of the tasks. A real-time operating system (RTOS) is an operating system that serves real-time applications that process data without any buffering delay .
- A real-time system must also ensure the correctness and consistency of the data that is accessed by the tasks. Data can be classified into three types: static, dynamic, and temporal. Static data is data that does not change during the execution of the system. Dynamic data is data that changes during the execution of the system. Temporal data is data that has a validity period and must be accessed within that period.
- A real-time system must also deal with the uncertainties and unpredictabilities that may arise during the execution of the system. These include faults, failures, errors, exceptions, and disturbances. A real-time system must be able to detect, isolate, and recover from these situations and maintain the desired level of performance and reliability.



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - Release time (r<sub>i</sub>): The time instant when the job becomes available for execution.
  - Absolute deadline (d<sub>i</sub>): The time instant by which the job must finish its execution.
  - Relative deadline (D<sub>i</sub>): The time interval between the release time and the absolute deadline of the job.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval during which the job can be executed by the system.
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from other parameters such as periodicity, jitter, or precedence constraints .
- The temporal parameters of a job can be used to analyze the schedulability and performance of the real time system, and to design appropriate scheduling algorithms and policies .



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task generates an infinite sequence of jobs (or called task instances) that are released at regular intervals. A periodic task repeats itself after a fixed time interval  .
- A periodic task is denoted by four or five tuples: Ti = < Φi, Pi, ei, Di > or Ti = < Φi, Pi, ei, Di, Ri >  where:
  - Φi is the phase of the task, which is the time of the first job release.
  - Pi is the period of the task, which is the time interval between two consecutive job releases.
  - ei is the worst-case execution time of the task, which is the maximum time required to execute a job on a given processor.
  - Di is the relative deadline of the task, which is the maximum time allowed for a job to complete after its release.
  - Ri is the resource requirement of the task, which is the amount of a shared resource (such as memory or bandwidth) needed by a job during its execution.
- A periodic task is said to be feasible if there exists a schedule that can meet all the deadlines of its jobs. A set of periodic tasks is said to be feasible if there exists a schedule that can meet all the deadlines of all the jobs of all the tasks.
- A periodic task is said to be implicit-deadline if Di = Pi, constrained-deadline if Di ≤ Pi, and arbitrary-deadline if Di can be any value.
- A periodic task is said to be harmonic if its period is an integer multiple of the periods of all the other tasks in the system.
- A periodic task is said to be sporadic if its period is the minimum separation time between two consecutive job releases, and aperiodic if its period is the maximum separation time between two consecutive job releases.



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal dependencies among jobs, such as control flow or synchronization. For example, a job J1 may need to finish before another job J2 can start, or a job J3 may need to wait for a signal from another job J4.
- Data dependency is imposed by the communication or sharing of data among jobs, such as input/output or shared memory. For example, a job J5 may need to read the data produced by another job J6, or a job J7 may need to write the data to a shared buffer that is accessed by another job J8.
- Precedence constraints and data dependency may affect the feasibility and optimality of scheduling algorithms for real time systems, as they may limit the parallelism or flexibility of job execution.
- An efficient way to represent precedence constraints is by using a directed graph G = (J, <) where J is the set of jobs. This graph is known as the precedence graph. Jobs are represented by vertices of the graph and precedence constraints are represented using directed edges. For example, the following graph shows the precedence constraints among four jobs J1, J2, J3 and J4:

```
J1 -> J2
J1 -> J3
J2 -> J4
J3 -> J4
```

- Data dependency cannot be captured by a precedence graph, as it may depend on the runtime values or states of the data. For example, a job J9 may need to read the data from a sensor only if the data is above a certain threshold, or a job J10 may need to write the data to a file only if the file is not locked by another job. Data dependency may require additional mechanisms to ensure the consistency and correctness of the data, such as locks, semaphores, monitors, or message passing.



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or design time, and does not change at run time. Static scheduling is suitable for systems that have fixed and known tasks and workloads .
  - Dynamic scheduling is done at run time, and can adapt to changes in the system state, workload, or environment. Dynamic scheduling is suitable for systems that have variable and unpredictable tasks and workloads .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently executing. Preemptive scheduling can reduce the response time and improve the schedulability of tasks .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently executing. Non-preemptive scheduling can avoid the overhead and complexity of context switching and synchronization .
- Real time scheduling algorithms are the rules and methods that determine how to select and order tasks for execution in a real time system .
- Some examples of real time scheduling algorithms are:
  - Rate monotonic scheduling (RMS): a static and preemptive algorithm that assigns priorities to tasks based on their periods, with shorter periods having higher priorities .
  - Earliest deadline first (EDF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their deadlines, with earlier deadlines having higher priorities .
  - Least laxity first (LLF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their laxity, which is the difference between their deadline and their remaining execution time, with smaller laxity having higher priorities .
  - Fixed priority scheduling (FPS): a static and preemptive algorithm that assigns fixed priorities to tasks based on some criteria, such as user preference, criticality, or importance .
  - Round robin scheduling (RR): a static and non-preemptive algorithm that assigns equal priorities to tasks and executes them in a circular order for a fixed time slice .
- Real time scheduling analysis is the process of verifying and validating the correctness and feasibility of a real time scheduling algorithm and system .
- Real time scheduling analysis can be done using different methods, such as:
  - Utilization bound test: a sufficient but not necessary condition for schedulability that checks if the total utilization of the tasks is less than or equal to a certain bound, depending on the algorithm and the number of tasks .
  - Response time analysis: a method that computes the worst-case response time of each task and compares it with its deadline, to check if the task can meet its deadline under the given algorithm and system .
  - Simulation: a method that models the behavior and performance of the system and the algorithm using software or hardware tools, and tests the system under different scenarios and workloads .
- Real time scheduling applications are the domains and systems that require real time scheduling, such as:
  - Embedded systems: systems that are integrated with physical devices and sensors, and perform specific functions, such as automotive, aerospace, medical, or industrial systems .
  - Multimedia systems: systems that process and deliver audio, video, or graphics data, such as streaming, gaming, or virtual reality systems .
  - Online scheduling systems: systems that allow users to book and manage appointments, meetings, or events, such as Calendly, Google Calendar, or Outlook .



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning tasks to processors or resources in a way that meets the timing constraints and performance requirements of a real time system. A real time system is a system that must respond to events or stimuli within a specified time bound, otherwise it may fail or cause undesirable consequences.

There are different types of real time tasks, such as periodic, aperiodic, and sporadic, which have different characteristics and requirements. Periodic tasks are tasks that repeat at fixed intervals and have a known execution time and deadline. Aperiodic tasks are tasks that occur irregularly and have a variable execution time and deadline. Sporadic tasks are tasks that occur randomly and have a minimum inter-arrival time and a deadline.

There are also different types of real time systems, such as hard, soft, and firm, which have different levels of tolerance for missing deadlines. Hard real time systems are systems that must meet all deadlines, otherwise they may cause catastrophic failures or losses. Soft real time systems are systems that can tolerate some deadline misses, but the quality of service or performance may degrade. Firm real time systems are systems that can tolerate some deadline misses, but the missed tasks have no value and can be discarded.

Some of the common approaches to real time scheduling are:

- **Rate Monotonic Scheduling (RMS)**: This is a static priority scheduling algorithm that assigns priorities to tasks based on their periods. The shorter the period, the higher the priority. This algorithm is optimal for preemptive scheduling of periodic tasks on a single processor, meaning that it can schedule any set of tasks that is feasible on a single processor .
- **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm that assigns priorities to tasks based on their deadlines. The closer the deadline, the higher the priority. This algorithm is optimal for preemptive scheduling of periodic and aperiodic tasks on a single processor, meaning that it can schedule any set of tasks that is feasible on a single processor .
- **Least Laxity First (LLF)**: This is a dynamic priority scheduling algorithm that assigns priorities to tasks based on their laxity. The laxity of a task is the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority. This algorithm is optimal for preemptive scheduling of periodic and aperiodic tasks on a single processor, meaning that it can schedule any set of tasks that is feasible on a single processor .
- **Deadline Monotonic Scheduling (DMS)**: This is a static priority scheduling algorithm that assigns priorities to tasks based on their relative deadlines. The shorter the relative deadline, the higher the priority. The relative deadline of a task is the difference between its period and its deadline. This algorithm is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines on a single processor, meaning that it can schedule any set of tasks that is feasible on a single processor .
- **Fixed Priority Scheduling (FPS)**: This is a static priority scheduling algorithm that assigns priorities to tasks based on some predefined criteria, such as importance, urgency, or user preference. The higher the priority, the higher the priority. This algorithm is not optimal for preemptive scheduling of periodic or aperiodic tasks on a single processor, meaning that it may not be able to schedule some sets of tasks that are feasible on a single processor .
- **Round Robin Scheduling (RR)**: This is a static priority scheduling algorithm that assigns equal priorities to all tasks and schedules them in a circular order. Each task gets a fixed amount of time, called a time quantum, to execute before it is preempted by the next task in the queue. This algorithm is fair and simple, but it may not meet the deadlines or performance requirements of real time tasks .

There are also other approaches to real time scheduling, such as:

- **Multiprocessor Scheduling**: This is the process of scheduling tasks on multiple processors or cores in a parallel or distributed system. There are different challenges and trade-offs involved in multiprocessor scheduling, such as load balancing, inter-processor communication, synchronization, and resource contention. There are different types of multiprocessor scheduling algorithms, such as partitioned, global, and hybrid, which have different advantages and disadvantages .
- **Resource Reservation**:



# Clock Driven Approach

- Clock driven approach is a scheduling method for hard real-time systems that require predictable and deterministic behaviour.
- In clock driven approach, the system executes tasks according to a predetermined schedule, which is computed offline based on the task parameters and system constraints .
- The schedule is usually periodic and cyclic, meaning that it repeats itself after a fixed interval of time, called the major cycle .
- The schedule specifies the exact time instants when each task should start and finish execution, independent of events such as job releases and completions .
- The schedule is stored in a table or a program, and is invoked by a clock interrupt at regular intervals .
- Clock driven approach has several advantages, such as:
  - It guarantees that all tasks will meet their deadlines, as long as the schedule is feasible and the system is stable .
  - It avoids the overhead of dynamic scheduling decisions and priority assignments at runtime .
  - It simplifies the analysis and verification of the system's timing behaviour .
- Clock driven approach also has some limitations, such as:
  - It requires that all task parameters and system constraints are known and fixed in advance .
  - It cannot handle aperiodic or sporadic tasks, or tasks with variable execution times or deadlines .
  - It may waste processor time if some tasks finish earlier than expected or do not arrive at all .
  - It may not be able to adapt to changes in the system's workload or environment .
- Clock driven approach is suitable for applications that have periodic and deterministic tasks, such as industrial control, avionics, and multimedia.
- Clock driven approach is not suitable for applications that have aperiodic or sporadic tasks, or tasks with variable execution times or deadlines, such as interactive systems, network servers, and mobile computing.



### Weighted Round Robin Approach

- The weighted round robin approach is a generalization of the round robin approach for scheduling real-time tasks or traffic.
- In the round robin approach, each ready task is given an equal share of the processor for a fixed time quantum, and the tasks are served in a circular order.
- In the weighted round robin approach, each ready task is given a fixed number of time quanta according to its weight, which represents its priority or importance .
- The tasks are still served in a circular order, but the number of service opportunities for each task may vary depending on its weight .
- The weighted round robin approach can be used for scheduling real-time traffic in high-speed switched networks, where different types of traffic may have different quality of service requirements .
- The advantages of the weighted round robin approach are:
  - It is simple and easy to implement .
  - It can handle variable-length tasks or packets without preemption .
  - It can achieve a fair allocation of the processor or bandwidth among the tasks or traffic according to their weights .
- The disadvantages of the weighted round robin approach are:
  - It may not be optimal for meeting the deadlines of real-time tasks or traffic, especially if the weights are not proportional to the task periods or packet sizes .
  - It may introduce a large delay or jitter for some tasks or traffic, especially if the weights are large or the time quanta are small .
  - It may not be suitable for heterogeneous systems or networks, where the tasks or traffic may have different processing or transmission rates .



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally. A resource becomes idles only when job does not require the resource for execution .
- It is a event driven approach for job scheduling and scheduling decision are made only when release and completion of job occur.
- In a priority-driven approach, tasks are executed based on their priority level. Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static priority and dynamic priority.
- Static priority means that the priority of each task is fixed and does not change during the execution. Examples of static priority algorithms are Rate Monotonic (RM) and Deadline Monotonic (DM).
- Dynamic priority means that the priority of each task can vary depending on the current state of the system. Examples of dynamic priority algorithms are Earliest Deadline First (EDF) and Least Laxity First (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to handle different types of real-time tasks, such as sensor data processing, control, and communication.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as priority inversion, resource contention, and interference from non-real-time tasks.



# Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters are known in advance and do not change during execution. A **dynamic system** is one where the tasks and their parameters may vary unpredictably during execution.
- Static systems are easier to analyze and validate than dynamic systems, since they have fixed and deterministic behavior. Dynamic systems are more flexible and adaptable to changing workloads and environments, but they require more complex and efficient scheduling algorithms.
- Static systems are suitable for hard real-time systems, where missing a deadline can have catastrophic consequences. Dynamic systems are suitable for soft real-time systems, where missing a deadline can have acceptable or negligible effects.
- Static systems use **static scheduling**, which assigns priorities to tasks before the system runs. Dynamic systems use **dynamic scheduling**, which assigns priorities to tasks as the system runs.
- Static scheduling has the advantages of simplicity, predictability, and low overhead. Dynamic scheduling has the advantages of responsiveness, adaptability, and optimality.
- Static scheduling has the disadvantages of inflexibility, inefficiency, and waste of resources. Dynamic scheduling has the disadvantages of complexity, uncertainty, and high overhead.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively .
- A task's deadline is the time by which it must finish its execution, and its slack is the difference between its deadline and its remaining execution time .
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack  .
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, that is, a schedule that meets all the deadlines of the tasks .
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as long as the total utilization of the tasks is less than or equal to one  .
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints, as long as the tasks are independent and the total utilization of the tasks is less than or equal to one  .
- EDF and LST may not be optimal for non-preemptive scheduling, aperiodic tasks, tasks with shared resources, tasks with variable execution times, or tasks with utilization greater than one    .
- EDF and LST may have different advantages and disadvantages depending on the characteristics of the tasks and the system, such as the number of tasks, the deadline distribution, the slack distribution, the context switch overhead, the deadline miss penalty, etc   .
- EDF and LST can be combined to enhance the performance of real-time task scheduling by switching between them according to some criteria, such as the load factor, the slack factor, the deadline factor, etc.



### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- It is a preemptive scheduling algorithm, which means that a higher priority task can preempt a lower priority task at any time .
- It is optimal for periodic tasks, which means that it can schedule any set of periodic tasks that is feasible, i.e., that can be scheduled by any other algorithm  .
- It has a simple schedulability test, which is based on the utilization factor of the task set, i.e., the sum of the ratios of execution time to period for each task  .
- The schedulability test is sufficient and necessary for task sets with harmonic periods, i.e., periods that are integer multiples of each other, and sufficient but not necessary for task sets with arbitrary periods  .
- The schedulability test is given by the following formula, where n is the number of tasks, C_i is the execution time of task i, and T_i is the period of task i  :

formula

- The schedulability test can be improved by using the exact response time analysis, which computes the worst-case response time of each task and compares it with its deadline  .
- The advantages of RMA are its simplicity, optimality, and low overhead .
- The disadvantages of RMA are its inability to handle aperiodic or sporadic tasks, its sensitivity to task parameters, and its pessimism for task sets with arbitrary periods .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, priority, and resource requirement of all tasks for all time. The schedule is stored in a table and followed by the system at run-time. Offline scheduling is suitable for static and deterministic systems where the task parameters are known in advance and do not change during execution. Offline scheduling has the advantage of reducing the run-time overhead and complexity, but the disadvantage of being inflexible and unable to handle dynamic events or uncertainties.

- Online scheduling is a technique that makes scheduling decisions during the run-time of the system. The scheduler does not have the complete knowledge of the task parameters or the future events, and only knows the information of the tasks that are released or active at the current time. Online scheduling can be either static or dynamic, depending on whether the task parameters are fixed or variable after the release. Online scheduling is suitable for dynamic and unpredictable systems where the task parameters or the system state may change during execution. Online scheduling has the advantage of being flexible and adaptive, but the disadvantage of increasing the run-time overhead and complexity.

- Examples of offline scheduling algorithms are table-driven scheduling, time-triggered scheduling, and cyclic executive scheduling. Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and earliest deadline first scheduling.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the topic you requested:

### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or deadline, such as user inputs, interrupts, or network packets.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive instances, such as sensor readings, alarms, or events.
- Priority driven systems are systems that assign a fixed priority to each job and schedule the highest priority job at any time, such as rate monotonic or deadline monotonic algorithms.
- Clock driven systems are systems that schedule jobs based on a predefined table that is computed offline, such as cyclic executive or time triggered algorithms.

- The main challenge of scheduling aperiodic and sporadic jobs in real time systems is to balance the responsiveness of these jobs with the predictability of periodic jobs, which have fixed arrival times and deadlines.
- There are different approaches to schedule aperiodic and sporadic jobs in priority driven and clock driven systems, such as:

  - Polling servers: A periodic task that polls the aperiodic or sporadic job queue and executes them if they are present. The server has a fixed priority and a fixed budget of execution time per period. The advantage of this approach is that it guarantees a bounded response time for aperiodic or sporadic jobs, but the disadvantage is that it may waste the server budget if there are no jobs in the queue .
  - Deferrable servers: A periodic task that executes aperiodic or sporadic jobs only if they are present and defers its execution otherwise. The server has a fixed priority and a fixed budget of execution time per period, but it can replenish its budget if it does not use it. The advantage of this approach is that it avoids wasting the server budget, but the disadvantage is that it may increase the response time of aperiodic or sporadic jobs if the server is deferred too often .
  - Sporadic servers: A periodic task that executes sporadic jobs only if they are present and replenishes its budget based on the minimum inter-arrival time of the sporadic jobs. The server has a fixed priority and a variable budget of execution time per period, which is determined by the arrival time of the sporadic jobs. The advantage of this approach is that it adapts to the sporadic job arrival pattern, but the disadvantage is that it may not be able to handle aperiodic jobs or sporadic jobs with variable inter-arrival times .
  - Slack stealing: An algorithm that uses the available slack times of periodic and sporadic jobs to complete aperiodic jobs early. The slack time of a job is the difference between its deadline and its worst-case execution time. The algorithm assigns a low priority to aperiodic jobs and executes them only when there is enough slack time in the system. The advantage of this approach is that it improves the responsiveness of aperiodic jobs without affecting the predictability of periodic and sporadic jobs, but the disadvantage is that it requires online computation of the slack times and may not be feasible for complex systems .
  - Reservation based: An algorithm that reserves a fraction of the processor time for aperiodic or sporadic jobs and schedules them using a priority driven or a clock driven algorithm within the reserved time. The reservation can be static or dynamic, depending on whether the fraction of the processor time is fixed or variable. The advantage of this approach is that it isolates the aperiodic or sporadic jobs from the periodic jobs and guarantees a minimum service level for them, but the disadvantage is that it may underutilize or overutilize the processor time depending on the arrival pattern of the aperiodic or sporadic jobs .

- The choice of the best approach depends on the characteristics of the system, such as the number and type of jobs, the processor utilization, the deadline constraints, and the performance metrics.



## Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, and network bandwidth, available to multiple users or processes.

Resource sharing can have several benefits, such as:

- Improving the efficiency and utilization of the system resources
- Reducing the cost and redundancy of the system resources
- Enhancing the performance and scalability of the system
- Enabling the collaboration and communication among the users or processes

Resource sharing can also have some challenges, such as:

- Managing the access and allocation of the shared resources
- Ensuring the security and privacy of the shared resources
- Handling the conflicts and contention of the shared resources
- Dealing with the heterogeneity and compatibility of the shared resources

Resource sharing can be implemented at different levels of a computer system, such as:

- Hardware level: sharing the physical components of the system, such as CPU, memory, disk, printer, etc.
- Operating system level: sharing the system services and functions, such as file system, process management, device drivers, etc.
- Application level: sharing the user programs and data, such as databases, web servers, email clients, etc.
- Network level: sharing the communication channels and protocols, such as TCP/IP, Ethernet, Wi-Fi, etc.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, a peripheral device, etc.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, deadlock, and reduced schedulability.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, while a medium-priority task preempts the low-priority task.
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, resulting in a circular dependency.
- Reduced schedulability means that some tasks may miss their deadlines due to resource contention and blocking time.

## RAC Protocols

- There are different RAC protocols that aim to prevent or limit the effects of resource contention, such as:
  - Non-preemptive critical sections (NPCS): A task cannot be preempted while executing a critical section, but it can be preempted before or after it. This prevents priority inversion, but may cause long blocking time and reduced schedulability.
  - Priority inheritance protocol (PIP): A task that holds a resource inherits the highest priority of the tasks that are blocked by it. This limits the priority inversion to one level, but may cause deadlock and timing anomalies.
  - Priority ceiling protocol (PCP): A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks. The ceiling priority of a resource is the highest priority of any task that may lock it. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.
  - Stack resource policy (SRP): A task can lock a resource only if its preemption level is higher than the system ceiling, which is the highest preemption level of all the resources currently locked by other tasks. The preemption level of a task is determined by the order of its arrival. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.
  - Multiprocessor priority ceiling protocol (MPCP): A generalization of PCP for multiprocessor systems, where each processor has its own ceiling priority and a task can migrate to another processor if it is blocked by a lower priority task. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.
  - Multiprocessor stack resource policy (MSRP): A generalization of SRP for multiprocessor systems, where each processor has its own system ceiling and a task can migrate to another processor if it is blocked by a lower priority task. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.



# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section.
- This protocol ensures that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - Simplicity: The protocol is easy to implement and understand, and does not require any complex data structures or algorithms.
  - Deadlock-freedom: The protocol guarantees that no deadlock can occur, since no job is ever blocked or waiting for a resource held by another job.
- The disadvantages of non-preemptive critical sections are:
  - Priority inversion: The protocol may cause a high-priority job to be delayed by a low-priority job that holds a resource, which violates the real-time scheduling principle.
  - Resource underutilization: The protocol may waste processor time by preventing other jobs from executing while a job holds a resource, even if the resource is not needed by the job at that moment.
  - Unbounded blocking: The protocol may cause a job to be blocked for an indefinite amount of time by a job that holds a resource, depending on the length of the critical section and the arrival pattern of other jobs.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed-priority scheduling.
- Both protocols aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources, and to prevent priority inversion and deadlock situations.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task, and the low-priority task is preempted by a medium-priority task, thus delaying the execution of the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed.

#### Priority-Inheritance Protocol (PIP)

- PIP works by temporarily raising the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it or that may block it in the future.
- This way, the low-priority task can finish using the resource and release it to the high-priority task, thus avoiding priority inversion and reducing blocking time.
- PIP has the following rules :
  - A task can lock a resource only if it is not locked by another task, or if it is locked by a task with lower or equal priority.
  - A task that locks a resource inherits the highest priority of any task that is blocked by it or that may block it in the future, until it releases the resource.
  - A task that releases a resource reverts to its original priority.
- PIP has the following advantages :
  - It overcomes the limitations of traditional priority-based scheduling, such as unbounded priority inversion and deadlock.
  - It requires minimum support from the operating system, such as priority manipulation and resource status tracking.
  - It preserves the optimality of fixed-priority scheduling, such as the rate-monotonic algorithm.
- PIP has the following disadvantages :
  - It can still cause long blocking times, especially for tasks with intermediate priorities, as they may be blocked by multiple lower-priority tasks.
  - It can cause chained blocking, where a high-priority task is blocked by a low-priority task that is blocked by another low-priority task, and so on.
  - It can not prevent deadlock, as two or more tasks may lock different resources and wait for each other to release them.

#### Priority-Ceiling Protocol (PCP)

- PCP works by assigning a priority ceiling to each shared resource, which is the highest priority of any task that can lock that resource, and by preventing a task from locking a resource if its priority is lower than the priority ceiling of any locked resource.
- This way, PCP ensures that a high-priority task can always access a resource if it is free, and that a low-priority task can not lock a resource if it may block a high-priority task, thus avoiding priority inversion and deadlock.
- PCP has the following rules  :
  - A task can lock a resource only if it is not locked by another task, or if it is locked by a task with lower or equal priority, and if its priority is higher than the priority ceiling of any locked resource.
  - A task that locks a resource inherits the priority ceiling of that resource, until it releases the resource.
  - A task that releases a resource reverts to its original priority.
- PCP has the following advantages  :
  - It overcomes the limitations of PIP and traditional priority-based scheduling, such as unbounded priority inversion, chained blocking, and deadlock.
  - It reduces the blocking time of high-priority tasks to at most one critical section of the lowest-priority task that can lock the same resource.
  - It prevents tasks from going into an unbounded wait state, as they can always access a resource if it is free and they have higher priority than any locked resource.
- PCP has the following disadvantages  :
  - It requires maximum support from the operating system, such as priority ceiling assignment, resource status tracking, and priority ceiling checking.
  - It may deny a task from locking a resource even if it is free, if its priority is lower than the priority ceiling of any locked resource, thus causing unnecessary blocking.
  - It may cause priority inversion, if a



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



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- A dynamic priority system is a system where the priorities of the periodic tasks change with time, while the resources required by each task remain constant .
- A priority-ceiling protocol is a job task synchronization protocol that prevents deadlock and unbounded priority inversion in a real-time system .
- There are two variants of the priority-ceiling protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- Both variants work by temporarily raising the priorities of tasks that access shared resources to the highest priority of any task that may access the same resource .
- The difference between OCPP and ICPP is that OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to execute .
- The priority ceiling of a resource is the highest priority of any task that may access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- In a dynamic priority system, the priority ceilings of the resources may change with time, depending on the changing priorities of the tasks .
- For dynamic systems, we can use the priority-ceiling protocol to control resource accesses, provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- The priority-ceiling protocol ensures that a task will not be blocked by a lower priority task for more than one critical section, and that the blocking time is bounded by the worst-case execution time of the highest priority task that may access the same resource .
- The priority-ceiling protocol also prevents circular wait and hence deadlock, by ensuring that a task can lock a resource only if it does not violate the priority order of the resources .
- The priority-ceiling protocol improves the schedulability and predictability of real-time systems, by reducing the blocking time and the number of preemptions .



# Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access the resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of the resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the worst-case scenario, and does not change it during execution.
- Dynamic preemption ceiling protocol assigns a variable ceiling priority to each resource based on the current situation, and updates it whenever a resource is locked or released.
- Dynamic preemption ceiling protocol has less blocking time and higher schedulability than static preemption ceiling protocol, but it requires more storage and computation overhead.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed-priority scheduling technique that allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can improve the performance of real-time systems by reducing context switches, memory requirements, and response times.
- However, PTS may cause long priority inversion if not combined with a synchronization protocol, since a low-priority task holding a resource may not be preempted by a high-priority task that needs the resource.
- Preemption ceiling protocol can solve this problem by raising the priority of the low-priority task to the ceiling priority of the resource, and allowing the high-priority task to preempt it.
- Preemption ceiling protocol can also prevent deadlock in PTS systems, since a task cannot lock a resource if its priority is lower than the ceiling priority of any resource locked by another task.
- Preemption ceiling protocol and PTS can work together to provide a scalable and efficient real-time system design.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of access control in multiple-unit resources for real time systems:

### Access Control in Multiple-Unit Resources

- A multiple-unit resource is a resource that can be used by more than one job at a time, but each unit of the resource is used in a non-preemptive and mutually exclusive manner. For example, a printer with multiple paper trays or a disk with multiple heads are multiple-unit resources .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards. The time the resource is locked is the critical section .
- The priority-ceiling protocol and the preemption-ceiling protocol that were discussed for single-unit resources can be extended to handle multiple-unit resources. The main idea is to assign a ceiling to each unit of the resource, and to allow a job to lock a unit only if its priority is higher than the ceiling of all the locked units.
- The ceiling of a unit can be defined as the highest priority of any job that may lock that unit. Alternatively, the ceiling of a unit can be defined as the highest priority of any job that may lock any unit of the same resource. The former is called the unit ceiling, and the latter is called the resource ceiling.
- The advantage of using the unit ceiling is that it allows more concurrency, as jobs can lock different units of the same resource without blocking each other. The advantage of using the resource ceiling is that it simplifies the implementation, as there is only one ceiling per resource.
- The priority-ceiling protocol with unit ceiling (PCP-UC) and the preemption-ceiling protocol with unit ceiling (PCP-UC) are similar to the original protocols, except that they use the unit ceiling instead of the resource ceiling. The priority-ceiling protocol with resource ceiling (PCP-RC) and the preemption-ceiling protocol with resource ceiling (PCP-RC) are identical to the original protocols.
- The PCP-UC and the PCP-UC guarantee freedom from deadlock, mutual exclusion, and bounded blocking. The PCP-RC and the PCP-RC guarantee freedom from deadlock, mutual exclusion, and bounded priority inversion.
- The PCP-UC and the PCP-UC have better schedulability than the PCP-RC and the PCP-RC, as they allow more parallelism and less blocking. However, they require more overhead to maintain the ceilings of each unit and to check the locking conditions.




### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts by locking data objects before accessing them and releasing them after finishing the access. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- Pessimistic algorithms have the advantage of avoiding unnecessary aborts and restarts, but they may incur blocking overhead and deadlock risk. Optimistic algorithms have the advantage of avoiding blocking and deadlock, but they may incur abort and restart overhead and waste system resources.
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, the predictability of workload, and the performance requirements.



# Unit 4 - Real Time Communication

Real time communication (RTC) is the exchange of information between two or more parties without significant delay. RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required. RTC can involve different types of media, such as text, audio, video, or data.

Some examples of RTC applications are:

- Instant messaging (IM): A form of text-based communication that allows users to send and receive messages in real time, usually over the internet or a local network. IM can also support file transfer, voice chat, video chat, or group chat.
- Voice over Internet Protocol (VoIP): A technology that enables voice communication over the internet or other IP networks. VoIP can use various protocols, such as Session Initiation Protocol (SIP), H.323, or Skype, to establish and manage calls. VoIP can also support video calls, conferencing, or faxing.
- Video conferencing: A form of RTC that allows two or more parties to see and hear each other using video and audio devices, such as webcams, microphones, and speakers. Video conferencing can use different platforms, such as Zoom, Google Meet, or Microsoft Teams, to facilitate collaboration, education, or entertainment.
- Streaming: A form of RTC that involves transmitting or receiving continuous media, such as audio or video, over the internet or other networks. Streaming can use various formats, such as MP3, AAC, or MPEG-4, to compress and encode the media. Streaming can also support live or on-demand content, such as radio, podcasts, or movies.
- Online gaming: A form of RTC that involves playing games over the internet or other networks, either individually or with other players. Online gaming can use various genres, such as action, strategy, or role-playing, to create immersive and interactive experiences. Online gaming can also support chat, voice, or video communication among players.

Some benefits of RTC are:

- It can enhance communication and collaboration among individuals or groups, regardless of their physical location or time zone.
- It can reduce costs and increase efficiency by eliminating the need for travel, phone calls, or postal services.
- It can provide more flexibility and convenience by allowing users to access RTC services anytime and anywhere, using various devices and platforms.
- It can improve user satisfaction and engagement by offering more interactive and personalized experiences.

Some challenges of RTC are:

- It can require high bandwidth and low latency to ensure good quality and performance of the RTC services.
- It can pose security and privacy risks by exposing the users' data and activities to potential threats, such as hackers, malware, or eavesdroppers.
- It can create social and ethical issues by affecting the users' behavior, relationships, or values, such as addiction, isolation, or cyberbullying.



### Basic Concepts in Real Time Communication

Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Live streaming and broadcasting

Some basic concepts in real time communication are:

- **Bandwidth**: The amount of data that can be transmitted or received per unit of time. Bandwidth is measured in bits per second (bps) and affects the quality and speed of RTC.
- **Latency**: The time it takes for a signal to travel from the sender to the receiver. Latency is measured in milliseconds (ms) and affects the responsiveness and synchronicity of RTC.
- **Jitter**: The variation in latency over time. Jitter is caused by network congestion, packet loss, or routing changes. Jitter can cause glitches, delays, or distortions in RTC.
- **Packet loss**: The percentage of data packets that are lost or corrupted during transmission. Packet loss can occur due to network congestion, errors, or interference. Packet loss can degrade the quality and reliability of RTC.
- **Codec**: A software or hardware device that compresses and decompresses data for transmission or storage. Codec stands for coder-decoder. Codec affects the bandwidth, quality, and compatibility of RTC.
- **Encryption**: A process of transforming data into an unreadable form to protect it from unauthorized access or modification. Encryption is used to ensure the security and privacy of RTC.
- **Protocol**: A set of rules and standards that define how data is formatted, transmitted, and interpreted. Protocol enables different devices and applications to communicate with each other. Some common protocols for RTC are SIP, RTP, RTCP, WebRTC, and VoIP .
- **Quality of service (QoS)**: A measure of the performance and reliability of a network or service. QoS is determined by factors such as bandwidth, latency, jitter, packet loss, and availability. QoS can be improved by using techniques such as prioritization, reservation, or optimization .



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- Hard real-time communication systems are deterministic in nature, meaning that they must guarantee that the communication is completed within a fixed deadline.
- Soft real-time communication systems are probabilistic, meaning that they can tolerate some degree of delay or error in the communication, as long as the probability of missing the deadline is very low.
- Examples of hard real-time communication systems are:
  - Control systems for nuclear reactors, aircraft, or medical devices.
  - Military or emergency communication systems.
  - Audio or video streaming systems that require synchronization.
- Examples of soft real-time communication systems are:
  - Online gaming or chat applications.
  - E-commerce or banking transactions.
  - Web browsing or email services.
- The design of real-time communication systems depends on various factors, such as:
  - The communication medium (wired or wireless).
  - The communication protocol (TCP, UDP, etc.).
  - The communication topology (point-to-point, broadcast, multicast, etc.).
  - The communication quality of service (QoS) parameters (bandwidth, latency, jitter, reliability, etc.).
  - The communication security and privacy requirements.
- The challenges of real-time communication systems include:
  - Dealing with unpredictable network conditions (congestion, interference, failures, etc.).
  - Ensuring timely and accurate delivery of data.
  - Balancing the trade-offs between performance and resource consumption.
  - Adapting to dynamic changes in the system or the environment.
  - Verifying and validating the correctness and safety of the system.

: Real-time communication - Wikipedia
: Difference Between Hard and Soft Real-Time Systems



# Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis, such as voice, video, or audio.
- Real time control consists of commands or signals that are sent from a controller to a controlled device or system, such as a robot, a sensor, or a switch.
- Real time communication requires certain quality of service (QoS) parameters to be met, such as throughput, delay, and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time .
- Delay is the time elapsed between the generation of a message at the source and its reception at the destination .
- Jitter is the variation in delay among different messages in the same stream .
- A model of real time communication can be used to analyze and design the communication system and network that support real time applications .
- A model of real time communication consists of the following components :
  - Sources and destinations: the end users of the real time applications that generate and consume messages, such as speakers, cameras, or displays.
  - Hosts: the devices that host the sources and destinations, such as computers, smartphones, or tablets.
  - Network interfaces: the hardware and software components that connect the hosts to the network, such as network cards, drivers, or protocols.
  - Input and output queues: the buffers that store the incoming and outgoing messages at the network interfaces, such as FIFOs, priority queues, or leaky buckets.
  - Network: the physical and logical infrastructure that connects the network interfaces, such as cables, routers, switches, or protocols.
  - Links: the transmission media that carry the messages between the network interfaces, such as copper wires, optical fibers, or wireless channels.
- A model of real time communication can be characterized by the following parameters :
  - Message characteristics: the attributes of each message, such as inter-packet spacing, message length, or reception deadline.
  - Traffic characteristics: the aggregate behavior of the message streams, such as arrival rate, burstiness, or variability.
  - Network characteristics: the properties of the network and links, such as bandwidth, latency, or reliability.
  - QoS requirements: the desired or acceptable values of the QoS parameters, such as minimum throughput, maximum delay, or maximum jitter.
- A model of real time communication can be used to perform the following tasks :
  - Traffic shaping: the process of modifying the message characteristics to meet the QoS requirements or to match the network characteristics, such as using leaky buckets, token buckets, or rate controllers.
  - Traffic scheduling: the process of determining the order and timing of transmitting or receiving the messages to meet the QoS requirements or to optimize the network performance, such as using earliest deadline first, weighted fair queueing, or round robin algorithms.
  - Traffic analysis: the process of evaluating the QoS parameters or the network performance based on the model of real time communication, such as using queuing theory, network calculus, or simulation tools.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) service discipline is a type of priority-based service discipline that assigns a weight to each priority queue and serves the queues in a circular order according to their weights .
- WRR does not require a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of the scheduler.
- WRR can guarantee both bandwidth and fairness among different priority queues, but it cannot guarantee the delay jitter bound or satisfy diverse delay requirements.
- To overcome the limitations of WRR, some variations have been proposed, such as:
  - Weighted fair queuing (WFQ), which assigns a virtual finish time to each packet based on its weight and serves the packets in increasing order of their virtual finish times.
  - Probabilistic priority (PP), which assigns a probability parameter to each priority queue and serves the queue with the highest probability when it is polled by the server.
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server, and adjusts the frame size and the weights of the queues according to the delay and jitter requirements of the packets.
  - Class-based weighted fair queuing (CBWFQ) and weighted fair priority queuing (WFPQ), which combine the features of WFQ and priority queuing to provide different service classes for different types of traffic.
- Priority-based service disciplines and WRR service discipline are suitable for real-time communication in switched networks, as they can provide quality of service (QoS) guarantees, such as bandwidth, delay, jitter and fairness, for different types of applications and users.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless broadcast network.
- Broadcast networks are networks where a single transmission from one node can be received by all other nodes in the network.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols utilize direct, asynchronous competition between neighboring nodes to determine which node will transmit next. Examples include Aloha and CSMA.
- Deterministic contention protocols use a predefined order or priority to decide which node will transmit next. Examples include token passing and polling.
- Reservation-based protocols use a separate control channel or a dedicated time slot to reserve the access to the broadcast channel. Examples include TDMA and CDMA.
- The design of MAC protocols for broadcast networks should consider the following factors: reliability, fairness, efficiency, scalability, and adaptability.
- Reliability refers to the ability of the MAC protocol to deliver packets without errors or collisions.
- Fairness refers to the ability of the MAC protocol to provide equal or proportional access opportunities to all nodes in the network.
- Efficiency refers to the ability of the MAC protocol to utilize the channel capacity and minimize the overhead and delay.
- Scalability refers to the ability of the MAC protocol to accommodate more nodes or traffic without degrading the performance.
- Adaptability refers to the ability of the MAC protocol to adjust to the changes in the network conditions, such as node mobility, topology, or traffic load.



### Internet and Resource Reservation Protocols for Real Time Communication

- Internet protocols are the set of rules and standards that enable communication and data exchange over the Internet.
- Real time communication is the transmission and reception of data with minimal delay and high reliability, such as voice, video, or multimedia applications.
- Internet protocols for real time communication need to provide quality of service (QoS) guarantees, such as bandwidth, delay, jitter, and packet loss, to meet the requirements of real time applications.
- Some of the Internet protocols for real time communication are:

  - Real-time Transport Protocol (RTP): A protocol that provides end-to-end delivery of real time data, such as audio and video, over IP networks. RTP supports features such as payload type identification, sequence numbering, timestamping, and synchronization.
  - Real-time Transport Control Protocol (RTCP): A protocol that works in conjunction with RTP to provide feedback and control information, such as sender and receiver reports, source description, and bye messages.
  - Real-time Streaming Protocol (RTSP): A protocol that enables the establishment and control of media sessions between a client and a server, such as play, pause, fast forward, and rewind.
  - Session Initiation Protocol (SIP): A protocol that enables the initiation, modification, and termination of multimedia sessions, such as voice and video calls, over IP networks. SIP supports features such as user location, user availability, session negotiation, and session management.
  - Session Description Protocol (SDP): A protocol that describes the characteristics and parameters of a multimedia session, such as media type, codec, format, and transport protocol.

- Resource reservation protocols are the protocols that enable the reservation of network resources, such as bandwidth and buffer space, along the path of a data flow, to provide QoS guarantees for real time communication.
- Resource reservation protocols can be classified into two categories:

  - Integrated services (IntServ): A model that provides QoS guarantees by reserving resources for each individual flow at each router along the path. IntServ requires the use of the Resource Reservation Protocol (RSVP) to signal and maintain the reservations .
  - Differentiated services (DiffServ): A model that provides QoS guarantees by classifying and marking packets into different service classes at the edge routers, and applying different forwarding policies based on the service classes at the core routers. DiffServ does not require per-flow reservation or signaling, but relies on traffic engineering and network provisioning to allocate resources.

- Resource Reservation Protocol (RSVP) is a protocol that enables the reservation of network resources for real time communication. RSVP has the following features :

  - Receiver-oriented: The reservation requests are initiated by the receivers, based on the QoS requirements of the application and the network conditions.
  - Soft state: The reservations are maintained by periodic refresh messages, and are automatically removed if the refresh messages stop or the network topology changes.
  - Scalable: The reservations are aggregated at the routers, and only the routers along the path of the data flow need to maintain the reservation state.
  - Flexible: The reservations can be made for unicast or multicast flows, and can be modified or canceled at any time.
  - QoS-aware: The reservations can specify the QoS parameters, such as bandwidth, delay, and packet loss, using the IntServ service models, such as guaranteed service or controlled load service.



# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and user interaction, but do not guarantee a timely response to external stimuli.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to run multiple tasks concurrently, each with its own priority and scheduling policy, and to switch between them with minimal overhead.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between tasks, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to protect the memory space of each task from corruption or interference by other tasks.
  - Interrupt handling: The ability to respond to hardware or software interrupts quickly and deterministically, and to resume the interrupted task without losing its state or timing.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, or network interfaces, using standard or custom protocols and APIs.
- An RTOS is suitable for applications that require high reliability, predictability, and performance, such as industrial control, embedded systems, robotics, aerospace, medical devices, and real-time simulations.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive.
- A RTDB is different from a conventional database, such as Oracle or MySQL, which are designed for persistent and consistent data storage, but do not guarantee a timely response to data queries or updates.
- A RTDB typically has the following features :
  - Data freshness: The ability to maintain the validity and accuracy of data, despite frequent changes and updates, and to provide the most recent data to the users or applications.
  - Data timeliness: The ability to process data queries or updates within a predefined deadline, and to notify the users or applications of any delays or failures.
  - Data concurrency: The ability to support multiple users or applications accessing or modifying the same data simultaneously, and to resolve any conflicts or inconsistencies using mechanisms such as locking, versioning, or timestamping.
  - Data availability: The ability to ensure the accessibility and durability of data, despite any failures or disruptions in the system, and to recover from any data loss or corruption using mechanisms such as replication, backup, or checkpointing.
- A RTDB is suitable for applications that require real-time analysis, decision making, or action, such as online gaming, stock trading, e-commerce, social media, or IoT.



### Features of RTOS

- A real-time operating system (RTOS) is an operating system with two key features: **predictability** and **determinism**. This means that it will execute tasks quickly and efficiently, responding as expected every time within a tight time boundary.
- An RTOS is **small**, **fast**, **responsive**, and **deterministic**. It occupies very less memory and consumes fewer resources.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment. Processing time requirements need to be fully understood and bound rather than just kept as a minimum.
- An RTOS can use different scheduling algorithms, such as **co-operative scheduling**, **pre-emptive scheduling**, or **rate-monotonic scheduling**. Co-operative scheduling allows a task to run until it is completed or it voluntarily yields the processor. Pre-emptive scheduling assigns a unique priority value to each task and the faster the task, the higher the priority. Rate-monotonic scheduling assigns a fixed priority to each task based on its period or frequency.
- An RTOS can provide various features and advantages, such as **real-time communication**, **real-time data processing**, **real-time control**, **real-time monitoring**, **real-time feedback**, **real-time security**, **real-time reliability**, and **real-time performance** . These features can help in differentiating product offerings, leveraging the growth opportunity of IoT, and adding new features to products as market needs evolve.



# Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.
- A real-time system can be classified into hard real-time and soft real-time based on the timing constraints  .
  - A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
  - A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- Time services are the mechanisms that provide the system with the notion of time and enable the system to measure, compare, and synchronize time.
- Time services are essential for real-time systems because they allow the system to:
  - Schedule tasks and events according to their deadlines and priorities.
  - Monitor the execution time of tasks and events and detect any timing violations.
  - Communicate and coordinate with other real-time systems and devices using a common time reference.
- Time services can be implemented using hardware and software components, such as:
  - Synchronous programming languages, which support the specification and verification of timing constraints and properties.
  - Real-time operating systems (RTOSes), which provide the system with a scheduler, a timer, and a clock.
  - Real-time networks, which enable the system to exchange time-sensitive data and synchronize clocks with other systems and devices.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like Unix strives to provide good average performance, for a RTOS, correct timing is the key feature.
- Unix is not a RTOS by default, but it can be modified or extended to support real-time features, such as:
  - Using a real-time kernel patch, such as RTLinux or RTAI, that provides a hard real-time layer below the standard Linux kernel .
  - Using a real-time extension library, such as POSIX.1b or Xenomai, that provides real-time APIs and services to user applications .
  - Using a real-time scheduler, such as SCHED_FIFO or SCHED_RR, that allows user processes to run with higher priority and preemption over non-real-time processes .
- Some advantages of using Unix as a RTOS are:
  - It is widely available, stable, and mature.
  - It supports a large variety of hardware platforms and devices.
  - It offers a rich set of development tools and libraries.
  - It can run both real-time and non-real-time applications on the same system.
- Some disadvantages of using Unix as a RTOS are:
  - It may not provide the required level of determinism and responsiveness for some hard real-time applications.
  - It may introduce additional overhead and complexity due to the interaction between the real-time and non-real-time layers.
  - It may require extensive testing and validation to ensure the correctness and reliability of the real-time behavior.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX-like systems, but it does not address the specific needs of real-time applications, such as predictable timing, priority scheduling, and inter-process communication.
- To address these needs, a real-time working group was established in POSIX, and it developed several extensions to the standard, such as POSIX.1b (real-time extensions), POSIX.1c (threads), and POSIX.4 (timers and clocks).
- Some of the issues that POSIX real-time extensions address are:

  - Scheduling: POSIX.1b defines two scheduling policies for real-time applications: FIFO (first-in first-out) and RR (round-robin). These policies allow the application to assign priorities to threads or processes, and the operating system to schedule them according to their priorities. FIFO policy gives the highest priority thread or process the CPU until it blocks or yields, while RR policy gives each thread or process a fixed time slice of the CPU.
  - Timers and clocks: POSIX.4 defines two types of timers: interval timers and absolute timers. Interval timers expire after a specified amount of time, while absolute timers expire at a specified point in time. POSIX.4 also defines two types of clocks: system clock and monotonic clock. System clock reflects the wall clock time, while monotonic clock reflects the elapsed time since some unspecified point in the past. Both timers and clocks can be used to measure the execution time of real-time tasks, or to trigger events or signals at specific times.
  - Signals: POSIX.1b defines a new type of signal called real-time signal, which is different from the standard signal defined in POSIX.1. Real-time signals are queued, so that no signal is lost due to overwriting. Real-time signals are also prioritized, so that the highest priority signal is delivered first. Real-time signals can also carry additional information, such as the value of a timer or the identity of a sender.
  - Semaphores: POSIX.1b defines a new type of synchronization primitive called semaphore, which is different from the standard mutex and condition variable defined in POSIX.1c. A semaphore is a counter that can be incremented or decremented by threads or processes, and can be used to control the access to a shared resource or to synchronize the execution of multiple tasks. A semaphore can also be initialized with a priority ceiling, which is the highest priority that a thread or process can have while holding the semaphore. This can prevent priority inversion, which is a situation where a low priority thread or process blocks a high priority one from accessing a shared resource.



### Characteristics of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, or events, and allow other data to be placed in a chronological sequence or to be analyzed chronologically.
- Temporal data can be used to analyze weather patterns, traffic conditions, demographic trends, and other phenomena that change over time.
- Temporal data can be stored in the form of a tuple that contains the data value, the validity time, and the generation time of the data instance.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time, depending on the context and purpose of the data.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be classified into different types, such as historical, current, or future data, depending on the relationship between the valid time and the current time.
  - Historical data is the data that has a valid time before the current time.
  - Current data is the data that has a valid time that includes the current time.
  - Future data is the data that has a valid time after the current time.
- Temporal data can be managed by using temporal databases, which are databases that support the storage and manipulation of temporal data.
  - Temporal databases can provide temporal consistency, which is the property that ensures that the temporal data in the database reflects the temporal data in the real world.
  - Temporal databases can also provide temporal query languages, which are languages that allow the users to query and manipulate temporal data using temporal operators and predicates.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. This can happen due to the delay in data acquisition, data transmission, or data processing.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other. This can happen due to the concurrency of transactions, the replication of data, or the failure of data sources.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the data sources when they detect a change in the physical environment. This reduces the data staleness by minimizing the delay in data acquisition and data transmission.
  - Deadline-driven updates, which are updates that are initiated by the database system when the data stored in the database is about to expire. This reduces the data staleness by minimizing the delay in data processing.
  - Concurrency control algorithms, which are algorithms that coordinate the access and modification of data by multiple transactions. This reduces the data inconsistency by enforcing the serializability or the temporal order of transactions.
  - Data replication protocols, which are protocols that synchronize the copies of data stored in different locations. This reduces the data inconsistency by ensuring the consistency or the freshness of data replicas.
  - Data validation mechanisms, which are mechanisms that check the validity and accuracy of data before using it. This reduces the data inconsistency by detecting and correcting the errors or anomalies in data.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, where many events occur simultaneously and interact with each other.
- Real-time systems (RTS) are systems that respond to their environment within specified time constraints.
- RTS are inherently concurrent and typically manage shared data resources, such as sensors, actuators, files, databases, etc.
- Concurrency control is the process of ensuring both logical and timing correctness of concurrent accesses to shared data resources in RTS.
- Logical correctness means that the concurrent accesses do not violate the integrity and consistency of the data.
- Timing correctness means that the concurrent accesses do not cause any deadline misses or timing anomalies in the system.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by using locks, timestamps, or serialization protocols to coordinate concurrent accesses.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them by using validation, compensation, or restart mechanisms.
- Concurrency control techniques can also be classified into two levels: transaction level and data item level.
- Transaction level concurrency control techniques deal with the atomicity, consistency, isolation, and durability (ACID) properties of transactions, which are logical units of work that access or update shared data resources.
- Data item level concurrency control techniques deal with the granularity, freshness, and validity of data items, which are the smallest units of data that can be accessed or updated by transactions.
- Concurrency control techniques for RTS must consider not only the logical and timing correctness, but also the performance and predictability of the system.
- Performance measures the throughput, response time, and resource utilization of the system.
- Predictability measures the degree of certainty and stability of the system behavior under different workloads and scenarios.
- Concurrency control techniques for RTS must balance the trade-offs among these criteria and adapt to the dynamic and uncertain nature of the real-time environment.



### Overview of Commercial Real Time databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the attributes of live real-time databases are:
  - Concurrency control: the ability to handle multiple transactions accessing the same data without compromising the consistency and integrity of the database.
  - Data freshness: the degree to which the data reflects the current state of the real world.
  - Data distribution: the ability to store and access data across multiple nodes or locations for scalability and availability.
  - Data replication: the ability to create and maintain copies of data for fault tolerance and load balancing.
  - Data security: the ability to protect data from unauthorized access, modification, or deletion.
  - Data recovery: the ability to restore data in case of failures or disasters.
  - Data analysis: the ability to perform queries and analytics on the data to derive insights and support decision making.
  - Data visualization: the ability to present data in a graphical or interactive way to enhance understanding and communication.
- Some of the examples of commercial real-time databases are :
  - Dealpath: a cloud-based platform that provides data and tools for commercial real estate investment and development.
  - Altus Group: a data and software provider that offers historical and current market information for commercial real estate valuation and analysis.
  - CoStar: a leading provider of commercial real estate information, analytics, and online marketplaces.
  - Google Cloud Firestore: a highly performant, fully managed NoSQL database service for large analytical and operational workloads.

