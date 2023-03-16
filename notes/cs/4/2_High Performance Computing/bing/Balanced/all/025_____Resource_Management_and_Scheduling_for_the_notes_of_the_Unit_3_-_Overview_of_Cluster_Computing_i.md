# Resource Management and Scheduling for Cluster Computing

- Cluster computing is a form of parallel and distributed computing that consists of a collection of interconnected and independent computers (nodes) that work together as a single system.
- Resource management and scheduling (RMS) are critical tasks in cluster computing, as they determine how the cluster resources are allocated and utilized by the applications or jobs submitted by the users.
- The main objectives of RMS are to maximize resource utilization, minimize processing time, and ensure fairness and quality of service for the users.
- The main challenges of RMS are the heterogeneity of resources, the dynamicity of workloads, the scalability of the system, and the fault tolerance of the system.

## Resource Management

- Resource management is the process of controlling and maintaining the status information of the cluster resources, such as processors, memory, disk, network, etc.
- Resource management involves four main functionalities:
  - Resource discovery: the process of identifying and registering the available resources in the cluster.
  - Resource monitoring: the process of collecting and updating the information about the state and performance of the resources in the cluster.
  - Resource allocation: the process of assigning a certain quantity of resources to each user or application at runtime, guided by a global policy to share cluster resources among multiple users based on fairness and/or predefined priority.
  - Resource reservation: the process of reserving a certain quantity of resources for a specific user or application in advance, to guarantee the availability and quality of service for the user or application.

## Job Scheduling

- Job scheduling is the process of determining how the cluster resources are assigned to the jobs in the queue, and how the jobs are executed on the assigned resources.
- Job scheduling involves two main functionalities:
  - Job queuing: the process of placing the jobs submitted by the users into queues until there are available resources to execute the jobs. The queues can be organized based on different criteria, such as job priority, job size, job deadline, etc.
  - Job dispatching: the process of sending the jobs from the queues to the assigned resources and managing the job execution processes before returning the results to the users upon job completion.

## Types of Scheduling Algorithms

- Scheduling algorithms can be classified based on different criteria, such as the level of scheduling, the objective of scheduling, the knowledge of scheduling, and the strategy of scheduling.
- Based on the level of scheduling, scheduling algorithms can be divided into two categories:
  - Global scheduling: the scheduling is performed by a central entity that has a global view of the cluster resources and the jobs in the queue, and makes decisions for the whole cluster.
  - Local scheduling: the scheduling is performed by each node independently, based on the local view of the node resources and the jobs assigned to the node, and makes decisions for the node only.
- Based on the objective of scheduling, scheduling algorithms can be divided into two categories:
  - Performance-oriented scheduling: the scheduling aims to optimize the performance metrics of the system, such as throughput, response time, waiting time, turnaround time, etc.
  - Quality-of-service-oriented scheduling: the scheduling aims to satisfy the quality of service requirements of the users or applications, such as deadline, budget, reliability, security, etc.
- Based on the knowledge of scheduling, scheduling algorithms can be divided into two categories:
  - Static scheduling: the scheduling assumes that the information about the cluster resources and the jobs is known in advance and does not change during the execution, and makes decisions based on the static information.
  - Dynamic scheduling: the scheduling assumes that the information about the cluster resources and the jobs is unknown or changes dynamically during the execution, and makes decisions based on the current information.
- Based on the strategy of scheduling, scheduling algorithms can be divided into two categories:
  - Deterministic scheduling: the scheduling follows a fixed rule or formula to make decisions, and produces the same output for the same input.
  - Heuristic scheduling: the scheduling follows a general guideline or intuition to make decisions, and may produce different outputs for the same input.