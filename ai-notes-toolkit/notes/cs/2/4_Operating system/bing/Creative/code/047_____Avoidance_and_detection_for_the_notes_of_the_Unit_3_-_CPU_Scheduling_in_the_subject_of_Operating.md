### Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- The main function of the CPU scheduling is to ensure that whenever the CPU remains idle, the OS has at least selected one of the processes available in the ready-to-use line.
- The objectives of CPU scheduling are to maximize the utilization of the CPU, to keep the CPU as busy as possible, to minimize the waiting time and turnaround time of the processes, and to provide fairness and balance among the processes.
- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock can be prevented or avoided by using some techniques that ensure that at least one of the necessary conditions for deadlock does not occur.
- Deadlock prevention is a method that denies the request of processes for resources if the allocation leaves the system in an unsafe state.
- Deadlock avoidance is a method that checks whether the system is in a safe state or in an unsafe state and in order to avoid the deadlocks, the process must need to tell the operating system about the maximum number of resources a process can request in order to complete its execution.
- Deadlock avoidance can be done with Banker’s Algorithm, which tests all the requests made by processes for resources, and checks for the safe state, if after granting request system remains in the safe state it allows the request otherwise it delays the request.
- Deadlock detection is a method that allows the system to enter a deadlock state and then tries to recover from it by aborting one or more processes and releasing their resources.
- Deadlock detection can be done with a wait-for graph, which is a directed graph that represents the waiting relationship between processes and resources.
- Deadlock recovery is a method that involves either preempting some resources from the processes or terminating some processes to break the deadlock cycle.