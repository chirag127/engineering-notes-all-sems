 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Scheduling Algorithms

- First Come First Serve (FCFS): The process that requests the CPU first gets allocated to the CPU first. There is no consideration of priority or efficiency. The average waiting time is high for this algorithm.
- Shortest Job First (SJF): The process with the shortest execution time is allocated to the CPU first. This algorithm leads to minimum average waiting time but the execution time of processes must be known beforehand which is not possible always.
- Priority Based Scheduling: Each process is assigned a priority and the process with the highest priority is allocated to the CPU first. The priority can either be fixed or dynamic. The average waiting time depends on the process priorities.
- Round Robin (RR): Each process is allocated CPU time in equal intervals (time quanta). After the completion of the time quanta, the process is preempted and the next process in the queue gets a chance. This algorithm ensures that each process gets some amount of CPU time to execute and leads to fair allocation of CPU. The average waiting time and throughput depends on the size of the time quantum.
- Multi-Level Queue: There are multiple queues where processes are placed according to their priority. The processes in the highest priority queue get the CPU first. If there are no processes in the highest priority queue, then the scheduler moves to the next lower level queue. This method ensures that the high priority processes get more access to the CPU.
- Multi-Level Feedback Queue: It is a variant of multi-level queue algorithm. The difference is that if a process is not able to complete its execution in its allotted time quantum, then it is moved to a lower priority queue. This method gives more chances to the processes to execute and get completed.

The content is written in points and in a formal tone without any emojis or external links as per the instructions. Please let me know if you would like me to modify or add anything to the content.