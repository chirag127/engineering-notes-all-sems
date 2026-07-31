### Resource Management and Scheduling for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel and distributed computing that consists of a collection of interconnected computers (nodes) that work together as a single system.
- Resource management and scheduling (RMS) are critical tasks in cluster computing, as they determine how the cluster resources are allocated and utilized by the applications or jobs submitted by the users.
- The main objectives of RMS are to maximize resource utilization, minimize processing time, and ensure fairness and quality of service for the users.
- The main challenges of RMS are to deal with the heterogeneity, dynamism, and scalability of the cluster system, as well as the diversity and complexity of the applications or jobs.
- The RMS of clusters provides support for four main functionalities:
  - Management of resources: The RMS manages, controls, and maintains the status information of the resources such as processors, memory, disk, and network in the cluster system.
  - Job queuing: The RMS receives the jobs submitted by the users and places them into queues until there are available resources to execute them.
  - Job scheduling: The RMS invokes the cluster scheduler to determine how resources are assigned to various jobs, based on a global policy or a local heuristic.
  - Job execution: The RMS dispatches the jobs to the assigned nodes and manages the job execution processes before returning the results to the users upon job completion.
- Cluster resource scheduling includes two main functions:
  - Resource allocation: The process of assigning a certain quantity of computing resources to each user or application at runtime, guided by a global policy to share cluster resources among multiple users based on fairness and/or predefined priority.
  - Job scheduling: The process of mapping a set of jobs to a set of resources, taking into account the jobs' requirements, the resources' capabilities, and the system's objectives.
- Cluster resource scheduling can be classified into two categories:
  - Static scheduling: The scheduling decisions are made before the execution of the jobs, based on the prior knowledge of the jobs' characteristics and the resources' availability. Static scheduling is suitable for batch processing and predictable workloads, but it cannot adapt to dynamic changes in the system or the jobs.
  - Dynamic scheduling: The scheduling decisions are made during the execution of the jobs, based on the current status of the jobs and the resources. Dynamic scheduling is suitable for interactive and unpredictable workloads, but it requires more overhead and complexity to monitor and adjust the system.
- Cluster resource scheduling can also be classified into two levels:
  - Global scheduling: The scheduling decisions are made by a centralized entity that has a global view of the cluster system and the jobs. Global scheduling can achieve optimal or near-optimal solutions, but it may suffer from scalability and reliability issues due to the single point of failure and the communication bottleneck.
  - Local scheduling: The scheduling decisions are made by distributed entities that have a local view of the cluster system and the jobs. Local scheduling can achieve scalability and reliability, but it may result in suboptimal or inconsistent solutions due to the lack of coordination and information sharing.