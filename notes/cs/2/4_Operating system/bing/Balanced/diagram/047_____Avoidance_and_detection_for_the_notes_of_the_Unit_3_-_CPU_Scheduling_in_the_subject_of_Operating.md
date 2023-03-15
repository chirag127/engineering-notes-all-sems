### Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of allocating CPU time to different processes based on their priority, resource requirements, and execution state.
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock avoidance and detection are two methods to prevent or resolve deadlocks in an operating system.
- Deadlock avoidance is a proactive approach that ensures that the system will never enter an unsafe state that may lead to deadlock. 
  - The operating system uses the deadlock avoidance method to determine whether the system is in a safe or unsafe state .
  - The process must inform the operating system of the maximum number of resources, and a process may request to complete its execution .
  - The operating system maintains a data structure called a resource allocation graph that shows the current allocation and request of resources by processes.
  - The operating system uses an algorithm called the banker's algorithm to simulate the allocation and request of resources and check if the system will remain in a safe state.
  - The operating system grants a request only if it leaves the system in a safe state, otherwise it denies or postpones the request.
- Deadlock detection is a reactive approach that allows the system to enter a deadlock state and then tries to recover from it.
  - The operating system uses the deadlock detection method to periodically check if the system is in a deadlock state using an algorithm.
  - There are several algorithms for detecting deadlocks in an operating system, including:
    - Wait-For Graph: A graphical representation of the system’s processes and resources. A directed edge is created from a process to a resource if the process is waiting for that resource. A cycle in the graph indicates a deadlock.
    - Resource Allocation Matrix: A matrix that shows the current allocation and request of resources by processes. The matrix is divided into four submatrices: allocation, request, available, and need. A deadlock exists if there is no safe sequence of processes that can finish their execution.
  - The operating system recovers from a deadlock by either aborting or preempting some of the processes involved in the deadlock and releasing their resources.
  - The operating system uses some criteria to select which processes to abort or preempt, such as priority, execution time, resource utilization, etc.