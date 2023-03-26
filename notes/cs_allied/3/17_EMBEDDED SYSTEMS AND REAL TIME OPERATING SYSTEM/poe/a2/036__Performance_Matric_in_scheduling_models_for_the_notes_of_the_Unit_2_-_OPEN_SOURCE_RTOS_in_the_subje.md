 Here is the content in Markdown format without any emojis or external links:

### Performance Matric in scheduling models for the notes of the Unit 2 - OPEN SOURCE RTOS

- Scheduling is a key concept in any multi-tasking operating system. It refers to the way tasks (processes, threads, etc.) are allocated to run on the CPU.
- There are several scheduling algorithms, each with different performance characteristics and use cases:
- First In First Out (FIFO): Simplest algorithm. Tasks are executed in the order they arrive in the queue. Poor response times for high priority tasks.
- Round Robin (RR): Each task gets a time slice in a circular order. Prevents starvation but can cause high latency for tasks with high CPU requirements.
- Priority Based: Higher priority tasks get preference. Can cause starvation for lower priority tasks.
- Multi-level queue: Separate queues for different priority levels. Higher priority queues get serviced first.
- The choice of a scheduling algorithm depends on the requirements and characteristics of the application:
- Response time requirements: For real-time systems, deadlines must be met so priority based / multi-level queue needed.
- Throughput requirements: For maximum CPU utilization, round robin needed.
- Fairness: To prevent starvation, round robin or multi-level queue needed.
- The performance of a scheduling algorithm can be evaluated based on:
- Average waiting time: The average time a task has to wait from the time it arrives to the time it starts execution. Should be low.
- Average turnaround time: The time from when a task arrives to the time it completes execution. Should be low.
- CPU utilization: The percentage of CPU time spent on actual execution of tasks. Should be high.
- Context switch overheads: The time and resources required to stop one task and start another. Should be low.