

# Real Time System

A real time system is an information processing system that can respond to events within predictable and specific time constraints . The system must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization).

Some examples of real time systems are:

- Flight control systems: These systems control the flight parameters of an aircraft, such as altitude, speed, direction, etc. They must react to sensor inputs and user commands within milliseconds to ensure the safety and stability of the flight .
- Process control systems: These systems are used in industrial applications where production is continuous and requires precise monitoring and regulation of physical variables, such as temperature, pressure, flow, etc. They must adjust the output of the system according to the input and feedback signals within seconds or less .
- Machine vision: These systems are used to help machines rapidly interpret data so they can see their surroundings and perform tasks, such as object recognition, face detection, quality inspection, etc. They must process the images and videos captured by cameras and sensors within milliseconds or less .
- Robotics: These systems are used to control the movements and actions of robots, such as industrial robots, autonomous vehicles, surgical robots, etc. They must coordinate the sensors, actuators, and controllers of the robots within milliseconds or less to achieve the desired goals and avoid collisions and errors  .
- Medical imaging: These systems are used to capture, process, and display images of the human body for diagnosis and treatment, such as X-ray, MRI, ultrasound, etc. They must process the signals from the imaging devices and display the results within seconds or less to provide accurate and timely information to the medical staff.

Real time systems can be classified into two types based on the timing constraints:

- Hard real time systems: These systems have absolute deadlines, and if those allotted time spans are missed, a system failure will occur. For example, a flight control system must respond to a sudden change in the air pressure within a certain time limit, otherwise the aircraft may crash  .
- Soft real time systems: These systems have relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. For example, a video streaming system must deliver the frames within a certain time limit, otherwise the video quality will decrease but not stop  .

Real time systems face many challenges and requirements, such as:

- Concurrency: Real time systems must handle multiple tasks and events simultaneously and coordinate them efficiently and correctly .
- Schedulability: Real time systems must ensure that all the tasks and events can meet their deadlines and priorities, and allocate the available resources accordingly .
- Reliability: Real time systems must ensure that the system can function correctly and consistently under normal and abnormal conditions, and recover from faults and errors .
- Safety: Real time systems must ensure that the system can avoid or minimize the harm to the environment and the users in case of failures or errors .
- Security: Real time systems must ensure that the system can protect the data and the functionality from unauthorized access and malicious attacks .

Real time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare .



## Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization) .
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system .
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur. For example, flight control systems, airbag systems, etc.  .
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. For example, video streaming, online gaming, etc. .
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities .
- A real-time system can have different types of tasks: periodic, aperiodic, and sporadic. Periodic tasks have fixed intervals between successive executions. Aperiodic tasks have variable intervals between successive executions. Sporadic tasks have minimum intervals between successive executions .
- A real-time system can have different types of scheduling algorithms: static, dynamic, preemptive, and non-preemptive. Static scheduling algorithms assign priorities to tasks before execution. Dynamic scheduling algorithms assign priorities to tasks during execution. Preemptive scheduling algorithms can interrupt a task to execute a higher priority task. Non-preemptive scheduling algorithms can only execute a task until completion or blocking .
- A real-time system can have different types of challenges: concurrency, synchronization, communication, fault tolerance, security, etc. Concurrency refers to the ability of the system to execute multiple tasks simultaneously. Synchronization refers to the coordination of the tasks and resources to avoid conflicts and deadlocks. Communication refers to the exchange of data and messages between the tasks and components. Fault tolerance refers to the ability of the system to recover from errors and failures. Security refers to the protection of the system from unauthorized access and attacks .



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a computer system that **responds to input signals fast enough to keep an operation moving at its required speed**.
- A real-time system is also characterized by its ability to **produce the expected result within a defined deadline (timeliness)** and to **coordinate independent clocks and operate together in unison (time synchronization)**.
- A real-time system is one which **controls an environment by receiving data, processing them, and returning the results sufficiently quickly to affect the environment at that time**.
- A real-time system is subjected to **real-time, i.e., the response should be guaranteed within a specified timing constraint or the system should meet the specified deadline**.
- Examples of real-time systems are flight control systems, real-time monitors, gaming computers, videoconferencing systems, etc.



### Typical Real Time Applications

- A real-time application (RTA) is an application that requires a timely response from the underlying system or hardware to function correctly and meet user expectations.
- Real-time applications can be classified into two types: hard real-time and soft real-time.
- Hard real-time applications have strict deadlines and any missed deadline can result in catastrophic consequences, such as loss of life or damage to property .
- Soft real-time applications have more flexible deadlines and can tolerate some degree of delay or error without compromising the quality of service .
- Some examples of typical real-time applications are:

  - **Digital control**: This involves using sensors and actuators to monitor and control physical processes, such as temperature, pressure, speed, etc. Digital control systems are often hard real-time systems, as they need to react quickly and accurately to changes in the environment .
  - **Optimal control**: This involves using mathematical models and algorithms to optimize the performance of a system, such as minimizing the fuel consumption or maximizing the output of a plant. Optimal control systems are usually soft real-time systems, as they can tolerate some approximation or delay in the computation.
  - **Command and control**: This involves coordinating and directing the actions of multiple agents, such as military units, vehicles, robots, etc. Command and control systems are often hard real-time systems, as they need to ensure the safety and efficiency of the operations .
  - **Signal processing**: This involves processing and analyzing signals, such as audio, video, radar, etc. Signal processing systems are usually soft real-time systems, as they can trade off the quality or resolution of the output for the speed of the processing.
  - **Tracking**: This involves tracking the position and movement of objects, such as satellites, missiles, aircraft, etc. Tracking systems are often hard real-time systems, as they need to provide accurate and timely information for navigation or interception.
  - **Real-time databases**: This involves storing and retrieving data that are subject to temporal constraints, such as deadlines, freshness, validity, etc. Real-time databases are usually soft real-time systems, as they can adjust the consistency or completeness of the data for the timeliness of the access.
  - **Multimedia**: This involves delivering and presenting multimedia content, such as audio, video, graphics, etc. Multimedia systems are usually soft real-time systems, as they can adapt the quality or fidelity of the content for the bandwidth or latency of the network .

- These are some of the typical real-time applications that are used in various domains and scenarios. They require different levels of performance, reliability, and complexity from the underlying real-time systems.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must respond to events within a specified time interval.
- A real-time system can be classified into two types: hard real-time and soft real-time.
- A hard real-time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences.
- A soft real-time system is a system that can tolerate some deadline misses, but the quality of service may degrade.
- A real-time task is a unit of work that must be executed by a real-time system.
- A real-time task has three parameters: release time, execution time, and deadline.
- The release time of a task is the earliest time that the task can start execution.
- The execution time of a task is the amount of time that the task needs to complete its work.
- The deadline of a task is the latest time that the task must finish its execution.
- The release times of the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System are as follows:

  - Note 1: Introduction to Real-Time Systems - Release time: Wed, 15 Mar 2023 18:00:00 GMT
  - Note 2: Real-Time System Requirements and Specifications - Release time: Thu, 16 Mar 2023 18:00:00 GMT
  - Note 3: Real-Time System Design and Analysis - Release time: Fri, 17 Mar 2023 18:00:00 GMT
  - Note 4: Real-Time Scheduling Algorithms - Release time: Sat, 18 Mar 2023 18:00:00 GMT
  - Note 5: Real-Time Operating Systems - Release time: Sun, 19 Mar 2023 18:00:00 GMT
  - Note 6: Real-Time Communication and Synchronization - Release time: Mon, 20 Mar 2023 18:00:00 GMT
  - Note 7: Real-Time Fault Tolerance and Testing - Release time: Tue, 21 Mar 2023 18:00:00 GMT
  - Note 8: Real-Time System Applications and Case Studies - Release time: Wed, 22 Mar 2023 18:00:00 GMT

- The notes will be available on the course website and the students are expected to read them before the next class.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes for the Unit 1 - Introduction of Real Time System are due on **Friday, March 24, 2023** by **11:59 PM**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in **markdown format** and uploaded to the **course website** as a **single file** with the name **RTS_Unit1_Notes_YourName.md**.
- The notes should be **clear, concise, and comprehensive**, with proper use of **headings, lists, tables, code blocks, and diagrams** as needed.
- The notes should include **references** to the **textbook** and any other **relevant sources** used for the preparation of the notes.
- The notes will be **graded** based on the following criteria:
  - Completeness and accuracy of the content
  - Organization and presentation of the notes
  - Quality and originality of the notes
  - Adherence to the format and deadline requirements
- The notes will count for **10%** of the final grade for the subject of Real Time System.
- Late submissions will incur a **penalty** of **10%** per day, up to a maximum of **50%**.
- No submissions will be accepted after **Wednesday, March 29, 2023** by **11:59 PM**.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must produce the expected result by a specific deadline .
- The deadline is the maximum acceptable delay between an event and the system's response to that event.
- The correctness of the result in a real-time system depends not only on the logical correctness but also on the timeliness of the result.
- A timing constraint is a requirement or a restriction on the timing behavior of a real-time system.
- Timing constraints can be classified into two categories :
  - Performance constraints: The constraints enforced on the response of the system, such as the minimum and maximum response time, the average response time, the jitter, etc.
  - Scheduling constraints: The constraints enforced on the execution of the tasks in the system, such as the priority, the deadline, the period, the execution time, the precedence, etc.
- Timing constraints can be expressed using various constructs, such as temporal logic, interval algebra, event calculus, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual timing behavior of the system and compare it with the expected timing behavior.



### Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- Examples of hard real time systems are nuclear power plant control, air traffic control, missile guidance, pacemakers, etc. .
- A hard real time system requires a high degree of coordination, both within and across devices, and may use technologies such as Intel® Time Coordinated Computing (Intel® TCC) and Time-Sensitive Networking (TSN) to achieve this  .
- A hard real time system may have different levels of criticality, such as safety-critical, mission-critical, or business-critical, depending on the consequences of missing a deadline .
- A hard real time system may use a hard real time operating system (RTOS) that can guarantee a response within the deadline, and may have features such as preemptive scheduling, priority-based scheduling, interrupt handling, memory management, etc.  .
- A hard real time system may face challenges such as resource constraints, concurrency, synchronization, fault tolerance, security, etc. .



### Soft Real Time Systems

- A soft real time system is a system that can tolerate some degree of deadline misses or delays in response time without causing critical failures or unacceptable losses of quality.
- A soft real time system is typically used for applications that have flexible timing requirements and can adapt to changing situations or environments.
- A soft real time system can run on multiple cores and impose fewer restrictions on applications than a hard real time system, which requires strict adherence to deadlines and precise timing.
- Some examples of soft real time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications that can buffer or drop some frames if the network is congested.
  - Online gaming systems that can adjust the level of detail or resolution depending on the available resources.
- The main challenges of designing and implementing soft real time systems are:
  - Balancing the trade-off between performance and quality of service.
  - Managing the variability and unpredictability of the workload and the environment.
  - Handling the possible errors or exceptions that may occur due to deadline misses or delays.
  - Evaluating the impact of deadline misses or delays on the system and the user satisfaction.



### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .

- A workload model describes the applications supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, priority, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.)  .
- A resource model describes the resources available to the system, such as the CPU, memory, network, sensors, actuators, etc., their types (e.g., preemptive, non-preemptive, shared, dedicated, etc.), and their relations (e.g., contention, communication, etc.) .
- A system model describes the system behavior, such as the scheduling policy, the synchronization mechanism, the fault tolerance technique, the performance metric, etc., that determine how the workload is mapped to the resources .

- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .



### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job or a task. A job or a task must have one or more processors in order to execute and proceed towards completion.
- Examples of processors are computers, transmission links, disks, and database servers.
- Processors can be configured and optimized to meet the real-time requirements of the applications, such as bounded data access timings and precise time synchronization .
- Resources are also called passive resources. They are not essential for the execution of a job or a task, but they may be required by some jobs or tasks during their execution. A job or a task may or may not require a resource during its execution.
- Examples of resources are memory, files, printers, and sensors.
- Resources can be shared or exclusive among different jobs or tasks. Shared resources can be accessed by multiple jobs or tasks concurrently, while exclusive resources can be accessed by only one job or task at a time.
- Resources can cause contention or blocking among different jobs or tasks. Contention occurs when multiple jobs or tasks try to access the same resource at the same time, and blocking occurs when a job or a task has to wait for a resource that is occupied by another job or task.
- Resources can be managed by different policies or protocols, such as priority inheritance, priority ceiling, and deadlock avoidance. These policies or protocols aim to reduce the contention or blocking among different jobs or tasks, and to ensure the correctness and timeliness of the real-time system.



### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- The temporal parameters of a job are :
  - **Release time (r<sub>i</sub>)**: The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - **Relative deadline (D<sub>i</sub>)**: The maximum allowed time between the release time and the absolute deadline of a job. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The time interval in which a job can be feasibly executed. It is equal to the relative deadline minus the execution time of the job.
- Temporal parameters are important for the analysis and specification of real time systems, as they determine the schedulability and performance of the system.
- Temporal parameters can also be used to express real time constraints, which are the temporal properties that must be satisfied by the system. For example, a real time constraint may specify that a job must start within 10 ms after another job finishes.



### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline.
- Phase is the time at which the first job of the task is released.
- Period is the time interval between two consecutive job releases.
- Execution time is the worst-case time required to complete a job.
- Deadline is the time by which a job must finish.
- A periodic task model is a deterministic workload model that accurately represents many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a job may be at most jitter time units earlier or later than the exact start time of the period.
- A periodic task model can be analyzed using various scheduling algorithms, such as rate-monotonic, earliest deadline first, and fixed priority .



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal order of the jobs, while data dependency is caused by the communication or sharing of data among the jobs.
- Precedence constraints can be represented by a directed graph, called a precedence graph, where the vertices are the jobs and the edges indicate the precedence relation. A job J_i is a predecessor of another job J_k (and J_k a successor of J_i) if J_k cannot begin execution until the execution of J_i completes  .
- Data dependency cannot be captured by a precedence graph. In many real time systems, jobs communicate via shared data, such as buffers, queues, or global variables. A job J_i is data dependent on another job J_k if J_i needs to read or write some data that is produced or consumed by J_k .
- Precedence constraints and data dependency may affect the feasibility and optimality of the scheduling algorithms for real time systems. Some scheduling algorithms, such as rate monotonic or earliest deadline first, assume that the jobs are independent and do not have any precedence or data dependency. Other scheduling algorithms, such as deadline monotonic or least laxity first, can handle precedence constraints but not data dependency. Data dependency may require additional synchronization mechanisms, such as semaphores, locks, or monitors, to ensure the consistency and correctness of the shared data  .
- Precedence constraints and data dependency are important aspects of the design and analysis of real time systems. They may affect the performance, reliability, and predictability of the system. Therefore, they should be carefully considered and modeled in the specification and verification of the system requirements and behavior  .



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or design time, and does not change at run time. Static scheduling is suitable for systems that have fixed and known tasks and workloads .
  - Dynamic scheduling is done at run time, and can adapt to changes in the system state, workload, or environment. Dynamic scheduling is suitable for systems that have variable and unpredictable tasks and workloads .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently executing. Preemptive scheduling can reduce the response time and improve the schedulability of tasks .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently executing. Non-preemptive scheduling can avoid the overhead and complexity of context switching and synchronization .
- Real time scheduling algorithms are the rules and methods that determine how the scheduler selects and executes tasks in a real time system .
- Some examples of real time scheduling algorithms are:
  - Rate Monotonic Scheduling (RMS): a static and preemptive algorithm that assigns priorities to tasks based on their periods, such that the shorter the period, the higher the priority .
  - Earliest Deadline First (EDF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their deadlines, such that the earlier the deadline, the higher the priority .
  - Least Laxity First (LLF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their laxity, which is the difference between their deadline and their remaining execution time, such that the smaller the laxity, the higher the priority .
  - Fixed Priority Scheduling (FPS): a static and preemptive or non-preemptive algorithm that assigns fixed priorities to tasks based on some criteria, such as user preference, criticality, or importance .
  - Round Robin Scheduling (RR): a static and preemptive or non-preemptive algorithm that assigns equal priorities to tasks and executes them in a circular order for a fixed time slice or quantum .
- Real time scheduling analysis is the process of verifying and validating the correctness and feasibility of a real time scheduling algorithm and system .
- Real time scheduling analysis can be done using different methods, such as:
  - Utilization-based analysis: a method that uses the CPU utilization of tasks and the system to determine the schedulability and performance of a real time scheduling algorithm .
  - Response time analysis: a method that uses the worst-case response time of tasks and the system to determine the schedulability and performance of a real time scheduling algorithm .
  - Simulation: a method that uses a software or hardware model of the real time system and the scheduling algorithm to test and evaluate their behavior and performance under different scenarios and conditions .
  - Experimentation: a method that uses a real or prototype system and the scheduling algorithm to measure and observe their behavior and performance under real or simulated scenarios and conditions .



### Common Approaches to Real Time Scheduling

- Real time scheduling is the process of assigning execution time to tasks that have timing constraints, such as deadlines or periodicity.
- Real time scheduling aims to ensure that tasks meet their timing requirements, while maximizing system performance and resource utilization.
- There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the environment.
- Some of the common approaches are:

  - **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, and period, are known at design time. In this approach, a static schedule is computed offline, based on the worst-case execution time of the tasks, and stored in a table. The table specifies the start time and the duration of each task. A timer interrupts the system at predefined instants, and triggers the execution of the corresponding task from the table. This approach guarantees that all tasks will meet their deadlines, as long as the system behaves as expected. However, it is not flexible to handle dynamic changes, such as task arrivals, variations in execution time, or resource failures. It also may waste CPU time, if the tasks finish earlier than their worst-case execution time.   

  - **Priority-driven approach**: This approach is also known as event-driven or preemptive approach. It is mainly used for soft or firm real time systems, where the properties of the tasks may not be known at design time, or may vary at run time. In this approach, each task is assigned a priority, which may be static or dynamic, and the scheduler selects the highest priority task to run at each instant. The scheduler may preempt a lower priority task to run a higher priority task, if necessary. This approach is more flexible and adaptable to handle dynamic changes, such as task arrivals, variations in execution time, or resource failures. It also may improve CPU utilization, by allowing tasks to run as soon as they are ready. However, it is not easy to guarantee that all tasks will meet their deadlines, as the priority assignment and the scheduling algorithm may not be optimal.   

  - **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority, and the scheduler selects the next task to run in a circular order. This approach is commonly used for time-shared systems, where the goal is to provide fair and responsive service to multiple users or applications. In this approach, each task is allocated a fixed amount of time, called a time slice or a quantum, to run. If the task does not finish within its time slice, it is preempted and moved to the end of the ready queue. The scheduler then selects the next task from the head of the queue, and repeats the process. This approach ensures that no task will starve, as each task will get a chance to run periodically. However, it may not be suitable for real time systems, as it does not consider the timing requirements of the tasks, such as deadlines or periods. It also may introduce overhead, due to frequent context switches.  

  - **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different priorities, and the scheduler selects the next task to run in a circular order, but with a weighted time slice. The time slice of each task is proportional to its priority, such that higher priority tasks get more CPU time than lower priority tasks. This approach is commonly used for multimedia systems, where the goal is to provide differentiated and proportional service to multiple streams or applications. In this approach, each task is allocated a fraction of the CPU time, called a weight or a share, to run. If the task does not finish within its weight, it is preempted and moved to the end of the ready queue. The scheduler then selects the next task from the head of the queue, and repeats the process. This approach ensures that the tasks will get their desired CPU time, as long as the sum of the weights does not exceed 100%. However, it may not be suitable for real time systems, as it does not consider the timing requirements of the tasks, such as deadlines or periods. It also may introduce overhead, due to frequent context switches.



### Clock Driven Approach

- Clock driven scheduling is also called as time-driven scheduling.
- When scheduling is clock driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock driven scheduler computes a static schedule offline, before the system starts executing, and follows the schedule at runtime.
- A static schedule is a sequence of scheduling decisions that specifies which job executes on which processor at any given time.
- A periodic static schedule is a cyclic schedule that repeats itself after a fixed period of time.
- This approach to scheduling hard real-time jobs is called the clock driven or time driven approach because each scheduling decision is made at a specific time, independent of events, such as job releases and completions, in the system.
- It is easy to see why a clock driven system never exhibits the anomalous timing behavior of priority driven systems.
- Clock driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock driven scheduling has some drawbacks, such as:
  - It requires a priori knowledge of all the task parameters and system workload.
  - It may not be able to handle sporadic or aperiodic tasks efficiently.
  - It may not be able to adapt to dynamic changes in the system state or environment.
  - It may waste processor time if the schedule is not fully utilized.



### Weighted Round Robin Approach

- The weighted round robin approach is a generalization of the round robin approach for scheduling real-time tasks or traffic.
- In the round robin approach, each ready task is given an equal share of the processor for a fixed time quantum.
- In the weighted round robin approach, each ready task is given a fixed number of time quanta based on its weight, which reflects its priority or importance .
- The weight of a task can be determined by various factors, such as its deadline, its arrival rate, its resource requirements, or its quality of service.
- The weighted round robin approach can achieve a fair and efficient allocation of the processor among different tasks, while maintaining the responsiveness and predictability of real-time systems .
- The weighted round robin approach can also be applied to other resources, such as network bandwidth, memory, or disk space.
- The weighted round robin approach has some advantages and disadvantages compared to other real-time scheduling algorithms, such as:
  - It is simple and easy to implement .
  - It does not require preemption or context switching, which can reduce the overhead and complexity .
  - It can handle dynamic and heterogeneous tasks with different weights and time quanta .
  - It can avoid starvation and improve fairness among tasks .
  - It may not be optimal or feasible for some tasks with strict deadlines or resource constraints .
  - It may not be able to utilize the processor fully or efficiently if some tasks finish their time quanta early or have low weights .
  - It may not be able to adapt to changing task characteristics or system conditions .



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
- Priority-driven scheduling can be applied to both periodic and aperiodic tasks.
- Periodic tasks have a fixed inter-arrival time and a fixed deadline.
- Aperiodic tasks have a variable inter-arrival time and a variable deadline.
- Priority-driven scheduling can also handle mixed-criticality tasks, which have different levels of importance and different requirements for timeliness.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 uses a middleware layer that supports priority-driven scheduling and allows users to specify the priority of each task.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters (such as arrival time, execution time, deadline, priority, etc.) are known in advance and do not change during the system execution. A static system can be scheduled offline, meaning that the task allocation and ordering can be determined before the system runs. A static system can be validated for its correctness and timeliness, meaning that it can be proven that the system will meet all the task deadlines and functional requirements. A static system provides a predictable and deterministic behavior, which is desirable for hard real-time systems. However, a static system may not be able to handle dynamic changes in the workload or the environment, and may not be able to utilize the system resources efficiently. A static system may also be difficult to design and maintain, especially for complex and large-scale systems.   

- A **dynamic system** is one where the tasks and their parameters may vary or be unknown until the system execution. A dynamic system requires online scheduling, meaning that the task allocation and ordering must be determined at run time, based on the current system state and the available information. A dynamic system can adapt to dynamic changes in the workload or the environment, and can optimize the system performance and resource utilization. A dynamic system may also be easier to design and maintain, as it does not require a priori knowledge of the tasks and their parameters. However, a dynamic system cannot be validated for its correctness and timeliness, meaning that it cannot be guaranteed that the system will meet all the task deadlines and functional requirements. A dynamic system may also introduce unpredictability and non-determinism in the system behavior, which may be undesirable for hard real-time systems.   

- The choice between static and dynamic systems depends on the characteristics and requirements of the real-time system. For simple and small-scale real-time systems, that have a fixed and predictable workload, a static system may be sufficient and preferable. For complex and large-scale real-time systems, that have a variable and unpredictable workload, a dynamic system may be necessary and beneficial.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A task's deadline is the time by which it must finish its execution, and its slack is the difference between its deadline and its remaining execution time.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, that is, a schedule that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as well as for non-preemptive scheduling of periodic tasks with implicit deadlines (equal to their periods).
- LST is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines and constrained deadlines (less than or equal to their periods), as well as for non-preemptive scheduling of periodic tasks with implicit deadlines.
- EDF and LST may not be optimal for other types of tasks, such as aperiodic tasks, tasks with precedence constraints, tasks with resource sharing, or tasks with variable execution times.
- EDF and LST may also have some drawbacks, such as high overhead, low utilization, poor response time, and deadline misses in overload situations.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a static priority scheduling algorithm for periodic tasks in real-time systems.
- RMA assigns priorities to tasks based on their periods, with shorter periods having higher priorities.
- RMA is optimal for preemptive scheduling of periodic tasks with fixed deadlines, meaning that it can always find a feasible schedule if one exists.
- RMA has some advantages over other scheduling algorithms, such as simplicity, predictability, and low overhead.
- RMA also has some limitations, such as not being suitable for aperiodic or sporadic tasks, not being able to handle tasks with variable execution times or deadlines, and not being able to guarantee schedulability for all task sets.
- RMA can be analyzed using the Liu and Layland utilization bound, which states that a set of n periodic tasks with fixed deadlines is schedulable by RMA if and only if the total utilization of the tasks is less than or equal to n(2^(1/n) - 1).
- RMA can also be analyzed using the response time analysis, which computes the worst-case response time of each task and compares it with its deadline. If the response time of any task exceeds its deadline, the task set is not schedulable by RMA.



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way and avoid any deadline violations.
- Online scheduling has the advantage of being flexible and adaptive, as the scheduler can handle dynamic changes in the system such as task arrivals, task aborts, task migrations, etc.
- Offline scheduling requires a static and deterministic system, where the tasks are periodic or sporadic and their parameters are known in advance.
- Online scheduling requires a dynamic and stochastic system, where the tasks are aperiodic or irregular and their parameters are uncertain or variable.
- Offline scheduling is suitable for hard real-time systems that have strict timing constraints and high reliability requirements.
- Online scheduling is suitable for soft real-time systems that have relaxed timing constraints and low criticality levels.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, utilization, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a pre-defined schedule that is determined offline. The scheduler follows the schedule and switches jobs at fixed time instants. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven and clock driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the predictability of periodic jobs. Periodic jobs are jobs that have fixed arrival pattern and hard deadlines. They are the primary workload in real time systems and must be guaranteed to meet their deadlines.
- In priority driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: background scheduling and slack stealing.
  - Background scheduling is a simple and intuitive approach that assigns the lowest priority to aperiodic and sporadic jobs. This means that they can only execute when there is no periodic job ready to execute. This ensures that periodic jobs always meet their deadlines, but it may result in poor responsiveness and long response time for aperiodic and sporadic jobs.
  - Slack stealing is a more sophisticated approach that assigns higher priority to aperiodic and sporadic jobs when there is enough slack time in the system. Slack time is the amount of time that a job can be delayed without causing any deadline miss. Slack stealing algorithms use the available slack time of periodic and sporadic jobs to complete aperiodic jobs early. This improves the responsiveness and response time of aperiodic and sporadic jobs, but it may require more complex analysis and overhead to compute and track the slack time.
- In clock driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: spare capacity scheduling and dynamic scheduling.
  - Spare capacity scheduling is an approach that reserves some slots in the pre-defined schedule for aperiodic and sporadic jobs. These slots are allocated based on the expected arrival rate and execution time of aperiodic and sporadic jobs. This ensures that aperiodic and sporadic jobs can execute within a bounded delay, but it may result in underutilization and waste of resources if the slots are not fully used.
  - Dynamic scheduling is an approach that modifies the pre-defined schedule at run time to accommodate aperiodic and sporadic jobs. This means that the scheduler can insert, delete, or reorder jobs in the schedule based on the actual arrival and execution time of aperiodic and sporadic jobs. This improves the utilization and responsiveness of aperiodic and sporadic jobs, but it may require more complex analysis and overhead to ensure the feasibility and stability of the schedule.



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, or network bandwidth, available to multiple users or processes.
- Resource sharing can improve the efficiency, performance, reliability, and scalability of a computer system, as well as reduce the cost and complexity of managing it.
- Resource sharing can be achieved by various methods, such as:
  - Multiprogramming: running multiple programs or processes concurrently on a single processor, by switching between them in a time-sharing manner.
  - Multiprocessing: using multiple processors or cores to execute multiple programs or processes simultaneously or in parallel.
  - Distributed computing: using multiple computers or devices connected by a network to perform a common task or share a common resource.
  - Cloud computing: using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer.
  - Virtualization: creating a virtual version of a resource, such as a server, a storage device, a network, or an operating system, that can be accessed by multiple users or processes as if it were a real one.
- Resource sharing can also pose some challenges, such as:
  - Security: protecting the resources from unauthorized access, modification, or damage by malicious users or processes.
  - Privacy: preserving the confidentiality and anonymity of the users or processes that access or share the resources.
  - Availability: ensuring that the resources are accessible and functional at all times, without interruption or degradation.
  - Compatibility: ensuring that the resources can be used by different users or processes with different requirements and preferences.
  - Coordination: ensuring that the users or processes that access or share the resources can communicate and cooperate with each other effectively and efficiently.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of tasks .
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that a task that has acquired a resource cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task that holds a resource.
  - Preemptive RAC means that a task that has acquired a resource can be preempted by another task, but the resource is not released until the preempted task resumes and finishes its critical section. This may cause timing anomalies, where a higher-priority task may take longer to complete than a lower-priority task.
- Some examples of RAC protocols are:
  - Non-preemptive protocols: Priority Inheritance Protocol (PIP), Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), etc.
  - Preemptive protocols: Preemptive Priority Ceiling Protocol (PPCP), Preemptive Stack Resource Policy (PSRP), etc.



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or suspended by another job until it finishes the critical section .
- This protocol ensures that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of non-preemptive critical sections are:
  - Simplicity: no need for complex synchronization mechanisms or priority inheritance schemes .
  - Deadlock-freedom: no job can be blocked indefinitely by another job holding a resource  .
- The disadvantages of non-preemptive critical sections are:
  - Priority inversion: a high-priority job may have to wait for a low-priority job to finish its critical section before accessing the same resource .
  - Resource underutilization: a job holding a resource may not use it for the entire duration of its critical section, wasting processor time and delaying other jobs .
  - Response time unpredictability: the worst-case response time of a job depends on the length and number of critical sections of all other jobs, which may be hard to analyze or bound .



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed-priority scheduling.
- Both protocols aim to overcome the limitations of traditional semaphore-based synchronization, such as priority inversion, deadlock, and excessive blocking time.
- Priority inversion occurs when a high-priority job is blocked by a low-priority job that holds a shared resource. Deadlock occurs when two or more jobs form a circular wait for resources. Blocking time is the duration that a job has to wait for a resource to become available.
- PIP and PCP differ in their allocation rules, priority assignment rules, and deadlock prevention mechanisms.

#### Priority-Inheritance Protocol (PIP)

- PIP works as follows:
  - Each resource has a priority equal to the highest priority of any job that may access it. This is called the ceiling priority of the resource.
  - A job can lock a resource if the resource is free or if the job's priority is higher than the ceiling priority of the resource.
  - If a job is blocked by a lower-priority job that holds a resource, the blocking job inherits the priority of the blocked job until it releases the resource. This is called priority inheritance.
  - When a job releases a resource, its priority is restored to its original value, and the highest-priority blocked job that requests the resource is unblocked.
- PIP has the following properties:
  - It requires minimal support from the operating system, as it only needs to change the priority of a job dynamically.
  - It can reduce the blocking time of a high-priority job, as it can preempt a low-priority job that holds a resource.
  - It cannot prevent deadlock, as it does not check for circular waits among jobs.
  - It can cause chained blocking, as a job can be blocked by multiple lower-priority jobs that inherit higher priorities.

#### Priority-Ceiling Protocol (PCP)

- PCP works as follows:
  - Each resource has a priority equal to the highest priority of any job that may access it. This is called the ceiling priority of the resource.
  - A job can lock a resource if the resource is free and if the job's priority is higher than the ceiling priority of all the resources currently locked by other jobs. This is called the system ceiling.
  - If a job is blocked by a lower-priority job that holds a resource, the blocking job does not inherit the priority of the blocked job. Instead, it waits until the system ceiling is lower than its priority.
  - When a job releases a resource, the system ceiling is lowered to the ceiling priority of the highest-priority resource still locked by any job, and the highest-priority blocked job that requests the resource is unblocked.
- PCP has the following properties:
  - It requires more support from the operating system, as it needs to keep track of the system ceiling and the ceiling priority of each resource.
  - It can prevent deadlock, as it does not allow a circular wait among jobs to form.
  - It can also reduce the blocking time of a high-priority job, as it does not allow a low-priority job to lock a resource if it can block a higher-priority job.
  - It can avoid chained blocking, as a job can only be blocked by one lower-priority job that holds a resource.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered to the highest priority ceiling of the remaining locked resources.
- SBPCP has the following properties:
  - It prevents deadlocks, since a task can lock a resource only if it does not block any higher priority task.
  - It prevents unbounded priority inversion, since a task can be blocked by a lower priority task only for the duration of one critical section.
  - It is optimal, since it allows the highest priority task that does not cause a deadlock to execute at any time.
  - It reduces the number of context switches, since a task does not preempt another task that has locked a resource with a higher priority ceiling.



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
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

- Consider a system with two tasks Tasks T1 (2, 0.9), T2 (5, 2.3) executed in deadline driven system as below.

- Task T1 requires resource X for 0.3 time units and task T2 requires resource Y for 0.5 time units.

- The priority of T1 is higher than T2 from time 0 to 4 and lower than T2 from time 4 to 5.

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.

- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 6 and so on.

- The ceiling of the system is the maximum of the priority ceilings of X and Y.

- The execution of the tasks using the priority ceiling protocol is shown below:

| Time | T1 | T2 | X | Y | System Ceiling |
|------|----|----|---|---|----------------|
| 0    | 1  | 2  | 1 | 2 | 2              |
| 1    | 1  | 2  | 1 | 2 | 2              |
| 2    | 1  | 2  | 1 | 2 | 2              |
| 3    | 1  | 2  | 1 | 2 | 2              |
| 4    | 2  | 1  | 2 | 2 | 2              |
| 5    | 2  | 1  | 2 | 1 | 2              |
| 6    | 1  | 2  | 1 | 1 | 1              |
| 7    | 1  | 2  | 1 | 1 | 1              |

- At time 0, T1 starts executing and locks X. The system ceiling is 2, which is the priority ceiling of Y.

- At time 1, T2 starts executing and locks Y. The system ceiling remains 2.

- At time 2, T1 finishes using X and releases it. The system ceiling remains 2.

- At time 3, T1 finishes its execution and T2 continues.

- At time 4, the priorities of T1 and T2 change. T1 becomes lower priority and T2 becomes higher priority. The priority ceiling of X also changes to 2.

- At time 5, T2 finishes using Y and releases it. The system ceiling becomes 2, which is the priority ceiling of X. The priority ceiling of Y also changes to 1.

- At time 6, T2 finishes its execution and T1 resumes. The system ceiling becomes 1, which is the priority ceiling of Y.

- At time 7, T1 finishes its execution and the system is idle.



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for others in a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that mutual deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better schedulability than static preemption ceiling protocol, but it requires more storage space and dynamic priority systems.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed priority scheduling technique that allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can reduce the number of context switches, increase the schedulability, and decrease the memory requirements of real-time systems.
- PTS can also enable a scalable real-time system design, especially for object-oriented systems that require synchronization considerations to maintain consistent object states.
- PTS can be combined with preemption ceiling protocol by using the ceiling priority of a resource as the preemption threshold of the task that locks the resource.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable.
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section.
- The challenge of access control in multiple-unit resources is to prevent deadlock and priority inversion, while ensuring schedulability and resource utilization.
- There are different protocols for access control in multiple-unit resources, such as:
  - The Priority Inheritance Protocol (PIP): A job that locks a resource inherits the priority of the highest-priority job that is blocked on that resource. The priority is restored when the resource is unlocked.
  - The Priority Ceiling Protocol (PCP): Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource. A job can lock a resource only if its priority is higher than the priority ceiling of all locked resources. A job that locks a resource inherits the priority ceiling of that resource. The priority is restored when the resource is unlocked.
  - The Stack Resource Policy (SRP): Each job is assigned a preemption level, which is the highest priority of any resource that it can lock. A job can lock a resource only if its preemption level is higher than the preemption level of all locked resources. A job that locks a resource inherits the preemption level of that resource. The preemption level is restored when the resource is unlocked.
  - The Maximum Urgency First (MUF) Protocol: Each job is assigned an urgency, which is the inverse of its deadline. A job can lock a resource only if its urgency is higher than the urgency of all locked resources. A job that locks a resource inherits the urgency of that resource. The urgency is restored when the resource is unlocked.



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts by locking data objects before accessing them and releasing them after finishing the access. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and resolve them by aborting and restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the degree of data sharing, the number of processors, the workload, and the performance metrics.



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required by the participants.
- Synchronous RTC is when the participants communicate at the same time, such as in a phone call, a video conference, or a chat session.
- Asynchronous RTC is when the participants communicate at different times, such as in an email, a voice message, or a forum post.
- RTC can be one-to-one, one-to-many, or many-to-many, depending on the number and direction of the communication channels.
- One-to-one RTC is when two parties communicate directly with each other, such as in a private chat or a phone call.
- One-to-many RTC is when one party communicates with multiple parties, such as in a broadcast, a webinar, or a podcast.
- Many-to-many RTC is when multiple parties communicate with each other, such as in a group chat, a video conference, or a social network.
- RTC can be text-based, voice-based, video-based, or multimedia-based, depending on the type and format of the information exchanged.
- Text-based RTC is when the participants communicate using written words, such as in a chat, an email, or a tweet.
- Voice-based RTC is when the participants communicate using spoken words, such as in a phone call, a voice message, or a podcast.
- Video-based RTC is when the participants communicate using visual images, such as in a video call, a video message, or a video conference.
- Multimedia-based RTC is when the participants communicate using a combination of text, voice, video, and other media, such as in a multimedia message, a webinar, or a social network.
- RTC can be facilitated by various technologies, platforms, and protocols, depending on the requirements and preferences of the participants.
- Some of the common technologies for RTC are:
  - Internet Protocol (IP): a set of rules for transmitting data over the internet or other networks.
  - Voice over IP (VoIP): a technology that allows voice communication over IP networks, such as Skype, WhatsApp, or Zoom.
  - Web Real-Time Communication (WebRTC): a technology that enables RTC between web browsers, such as Google Meet, Facebook Messenger, or Discord.
  - Session Initiation Protocol (SIP): a protocol that establishes, modifies, and terminates RTC sessions, such as voice calls, video calls, or instant messages.
  - Real-time Transport Protocol (RTP): a protocol that delivers audio and video data over IP networks, such as VoIP or WebRTC.
  - Real-time Messaging Protocol (RTMP): a protocol that delivers multimedia data over IP networks, such as live streaming, video on demand, or online gaming.
- Some of the common platforms for RTC are:
  - Social media: platforms that allow users to create, share, and interact with content and other users, such as Facebook, Twitter, or Instagram.
  - Messaging apps: platforms that allow users to send and receive text, voice, video, and multimedia messages, such as WhatsApp, Telegram, or Signal.
  - Video conferencing apps: platforms that allow users to conduct video calls and meetings with multiple participants, such as Zoom, Google Meet, or Microsoft Teams.
  - Online gaming platforms: platforms that allow users to play games and communicate with other players, such as Steam, PlayStation Network, or Xbox Live.
  - Online learning platforms: platforms that allow users to access and deliver educational content and services, such as Coursera, Udemy, or Khan Academy.
- Some of the common protocols for RTC are:
  - Hypertext Transfer Protocol (HTTP): a protocol that defines how web browsers and servers communicate, such as for accessing web pages, images, or videos.
  - WebSocket: a protocol that enables bidirectional communication between web browsers and servers, such as for chat, gaming, or live updates.
  - Secure Sockets Layer (SSL) / Transport Layer Security (TLS): protocols that provide encryption and authentication for data transmission over networks, such as for secure web browsing, email, or online banking.
  - Datagram Transport Layer Security (DTLS): a protocol that provides encryption and authentication for data transmission over unreliable networks, such as for WebRTC or RTP.
  - Secure Real-time Transport Protocol (SRTP): a protocol that provides encryption and authentication for audio and video data transmission over IP networks, such as for VoIP or WebRTC.



### Basic Concepts in Real Time Communication

- Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays .
- In RTC, there is always a direct path between the source and the destination, and the data is not stored en route to the destination .
- RTC can be synchronous or asynchronous, depending on whether the communication is time-bound or not.
- Examples of synchronous RTC are voice calls, video calls, live streaming, online gaming, etc. Examples of asynchronous RTC are email, text messaging, social media, etc.
- RTC can be based on different protocols and standards, such as Session Initiation Protocol (SIP), Web Real-Time Communication (WebRTC), Real-Time Transport Protocol (RTP), etc .
- RTC can be used for various purposes, such as collaboration, entertainment, education, health care, emergency response, etc .
- RTC requires effective communication skills, such as listening, paying attention to nonverbal signals, managing stress, and asserting oneself.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- Hard real-time communication systems are deterministic in nature, meaning that they guarantee to meet the deadlines for all the tasks.
- Soft real-time communication systems are probabilistic, meaning that they may occasionally miss the deadlines for some tasks with very low probability.
- The deadlines for hard real-time communication systems are strict and cannot be violated, otherwise the system may fail or cause catastrophic damage .
- The deadlines for soft real-time communication systems are flexible and can be violated, but the system may suffer from reduced performance or quality of service .
- Examples of hard real-time communication systems are nuclear power plant control, air traffic control, missile guidance, pacemaker, etc  .
- Examples of soft real-time communication systems are multimedia streaming, video conferencing, online gaming, voice over IP, etc  .
- Hard real-time communication systems require specialized hardware and software that can handle the timing constraints and ensure the correctness and reliability of the system.
- Soft real-time communication systems can use general-purpose hardware and software that can adapt to the varying workload and network conditions and provide the best possible service.



### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without storing data en route to the destination  .
- Examples of real time communication include voice calls, video calls, instant messaging, live streaming, online gaming, etc.
- In the model of real time communication, end users of the message application systems are sources and destinations residing in different hosts.
- The network interface of each host contains input queue and output queue. Two buffer areas called input/output buffer are allocated to input and output queue to store queuing information.
- In real time traffic model, each message (Mi) can be characterized by tuples of inter-packet spacing (Pi), message length (ei), reception deadline (Di) as below:

  Mi = (pi, ei, Di)

- This traffic model is called peak rate model in real time communication.
- The performance of real time communication can be measured by throughput, delay and jitter .
- Throughput is the rate of successful message delivery over a communication channel.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in delay of received messages.
- The goal of real time communication is to achieve high throughput, low delay and low jitter.



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are scheduling algorithms that assign different priorities to different packets or flows in a network and transmit them according to their priority levels.
- Weighted round-robin (WRR) service discipline is a special case of priority-based service discipline, where each packet or flow is assigned a weight that determines the proportion of service it receives in each round.
- The advantages of priority-based service disciplines are that they can provide different levels of quality of service (QoS) to different packets or flows, such as delay, jitter, throughput, and loss rate, and they can also support real-time communication with strict deadlines and guarantees.
- The disadvantages of priority-based service disciplines are that they may cause starvation or unfairness to lower-priority packets or flows, and they may also be vulnerable to priority inversion or misclassification problems, where higher-priority packets or flows are delayed or blocked by lower-priority ones.
- Some examples of priority-based service disciplines are:
  - Strict priority (SP) service discipline, where the highest-priority queue is always served first, and the lower-priority queues are served only when the higher-priority queues are empty. This discipline can provide the lowest delay and jitter to the highest-priority packets or flows, but it may starve the lower-priority ones.
  - Weighted fair queuing (WFQ) service discipline, where each packet or flow is assigned a weight that determines its share of the bandwidth, and the packets or flows are served in order of their virtual finish times, which are calculated based on their arrival times, weights, and service rates. This discipline can provide fairness and proportional QoS to different packets or flows, but it may require complex computation and sorting of the virtual finish times.
  - Weighted fair priority queuing (WFPQ) service discipline, where each priority queue is assigned a weight that determines its share of the bandwidth, and the packets or flows within each priority queue are served in order of their virtual finish times, which are calculated based on their arrival times, weights, and service rates. This discipline can combine the advantages of SP and WFQ, but it may also inherit their disadvantages.
  - Probabilistic priority (PP) service discipline, where each priority queue is assigned a parameter that determines the probability with which it is served when it is polled by the server. This discipline can provide a trade-off between SP and WRR, where higher-priority queues have higher chances of being served, but lower-priority queues are not completely ignored.
  - Rate-controlled frame-based weighted round-robin (RFWRR) service discipline, where each packet or flow is assigned a weight that determines its share of the bandwidth, and the packets or flows are served in a frame-based manner, where each frame consists of a fixed number of slots, and each slot is allocated to a packet or flow based on its weight and rate. This discipline can provide delay jitter bound and diverse delay requirements to different packets or flows, but it may require complex rate control and frame allocation mechanisms.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols are mechanisms that allow several users or transmitters to access a common medium or channel, such as a wireless network or a shared bus.
- MAC protocols play an important role in the development and performance of both wired and wireless networks, as they determine how the channel capacity is allocated and utilized among the competing users .
- MAC protocols can be classified into two main categories: random access and scheduling .
  - Random access protocols allow users to transmit whenever they have data to send, without any coordination or reservation. However, this may result in collisions or interference among the concurrent transmissions, which reduces the channel efficiency and reliability. Examples of random access protocols are ALOHA, slotted ALOHA, and carrier-sense multiple access (CSMA) protocols .
  - Scheduling protocols require users to follow some rules or algorithms to determine when and how they can access the channel, based on some criteria such as priority, demand, or fairness. Scheduling protocols can avoid or minimize collisions and interference, but they may incur some overhead or delay in the channel allocation process. Examples of scheduling protocols are time-division multiple access (TDMA), frequency-division multiple access (FDMA), and code-division multiple access (CDMA) protocols .
- MAC protocols for broadcast networks are designed to handle the challenges and requirements of wireless communication, such as limited bandwidth, variable channel conditions, mobility, and scalability .
  - MAC protocols for broadcast networks can be centralized or distributed. Centralized protocols rely on a base station or a coordinator to control the channel access and schedule the transmissions of all the users. Distributed protocols allow users to communicate and coordinate with each other without any central authority .
  - MAC protocols for broadcast networks can be contention-based or reservation-based. Contention-based protocols use random access methods to compete for the channel, while reservation-based protocols use scheduling methods to reserve the channel in advance .
  - MAC protocols for broadcast networks can be adaptive or fixed. Adaptive protocols can adjust their parameters or behavior according to the network conditions or the user demands, while fixed protocols use predefined or static settings.



### Internet and Resource Reservation Protocols for Real Time Communication

- Internet protocols are the set of rules and standards that enable communication and data exchange over the Internet.
- Real time communication is the transmission and reception of data with minimal delay and high reliability, such as voice, video, or multimedia applications.
- Internet protocols for real time communication need to provide quality of service (QoS) guarantees, such as bandwidth, delay, jitter, and packet loss, to meet the requirements of real time applications.
- Some of the Internet protocols for real time communication are:

  - Real Time Protocol (RTP): A transport layer protocol that provides end-to-end delivery of real time data, such as audio and video, over IP networks. RTP supports real time applications that adapt to changing network situations to maintain the QoS.
  - Real Time Control Protocol (RTCP): A companion protocol to RTP that provides feedback on the quality and performance of the RTP data streams, such as packet loss, delay, jitter, and synchronization. RTCP also enables the participants of a real time session to exchange information, such as their identities, capabilities, and preferences.
  - Real Time Streaming Protocol (RTSP): An application layer protocol that controls the delivery of real time data streams from a media server to a client. RTSP enables the client to perform actions, such as play, pause, fast forward, and rewind, on the media stream.
  - Session Initiation Protocol (SIP): An application layer protocol that establishes, modifies, and terminates multimedia sessions, such as voice and video calls, over the Internet. SIP also enables the participants of a session to negotiate the media formats, codecs, and QoS parameters.
  - Resource Reservation Protocol (RSVP): A transport layer protocol that reserves resources across a network and can be used to deliver specific levels of QoS for application data streams. Resource reservation enables businesses to divide network resources by traffic of different types and origins, define limits, and prioritize the traffic according to their needs .

- Resource reservation protocols are the protocols that enable the reservation of network resources, such as bandwidth, buffer space, and CPU cycles, for specific data flows or sessions.
- Resource reservation protocols can be classified into two categories:

  - Integrated services (IntServ): A QoS model that provides end-to-end QoS guarantees by reserving resources along the entire path of a data flow. IntServ requires the support of RSVP or a similar protocol at every router along the path. IntServ can provide high QoS for individual flows, but it is not scalable for large networks with many flows .
  - Differentiated services (DiffServ): A QoS model that provides QoS differentiation by classifying and marking packets into different service classes at the edge of the network. DiffServ does not require per-flow reservation or state maintenance at the routers. DiffServ can provide QoS for aggregate flows, but it cannot guarantee QoS for individual flows .

- The impact of resource reservation for real time Internet services can be positive or negative, depending on the scenario and the QoS model used. Some of the possible impacts are:

  - Improved QoS for real time applications: Resource reservation can ensure that real time applications receive sufficient network resources to meet their QoS requirements, such as bandwidth, delay, jitter, and packet loss. This can improve the user experience and satisfaction, as well as the performance and efficiency of the applications.
  - Reduced QoS for best-effort applications: Resource reservation can reduce the network resources available for best-effort applications, such as web browsing, email, and file transfer. This can degrade the user experience and satisfaction, as well as the performance and efficiency of the applications.
  - Increased network complexity and overhead: Resource reservation can increase the network complexity and overhead, such as signaling, routing, and management, especially for the IntServ model. This can affect the scalability, reliability, and security of the network.
  - Increased network flexibility and adaptability: Resource reservation can increase the network flexibility and adaptability, such as dynamic allocation, reconfiguration, and optimization, especially for the DiffServ model. This can enhance the network performance, efficiency, and resilience.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations .
- An RTOS provides features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS can be classified into two types: hard real-time and soft real-time. A hard real-time system guarantees that tasks will be completed within their deadlines, while a soft real-time system allows some tasks to miss their deadlines occasionally .
- A real-time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, and online transactions.
- A real-time database provides features such as concurrency control, data consistency, data freshness, and data recovery.
- A real-time database can be based on SQL or NoSQL, depending on the data model and the query requirements.
- A real-time database can be distinguished from a time-series database, which is a database system that stores and analyzes data that changes over time, such as metrics, events, and logs.
- A time-series database provides features such as high ingestion rate, compression, aggregation, and visualization.
- A time-series database can also be distinguished from a real-time analytics system, which is a system that processes and analyzes data in real-time, such as streaming data, dashboards, and alerts.

