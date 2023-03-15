# Weighted Round Robin Approach

- The weighted round robin (WRR) algorithm is a variation of the basic round robin (RR) algorithm that assigns different weights to different jobs based on their importance or priority .
- The WRR algorithm has been used for scheduling real-time traffic in high-speed switched networks, where different types of packets may have different quality of service (QoS) requirements .
- The WRR algorithm works as follows:
  - Each job in the ready queue is assigned a weight that represents its share of the processor time. The weight can be a fixed value or a dynamic value that changes over time.
  - The algorithm maintains a pointer that points to the current job in the queue. The pointer is initialized to point to the first job in the queue.
  - The algorithm allocates the processor to the current job for a time slice that is proportional to its weight. For example, if the weight of the current job is 3 and the time slice unit is 1, then the job gets 3 time slices of the processor.
  - After the current job finishes its time slice, the pointer moves to the next job in the queue. If the end of the queue is reached, the pointer wraps around to the first job in the queue.
  - The algorithm repeats the above steps until all the jobs in the queue are completed or preempted by a higher priority job.
- The advantages of the WRR algorithm are:
  - It is simple and easy to implement.
  - It can handle different types of jobs with different QoS requirements by adjusting their weights.
  - It can achieve a fair allocation of the processor among the jobs, as each job gets a share of the processor that is proportional to its weight.
- The disadvantages of the WRR algorithm are:
  - It may cause starvation of low-weight jobs if the high-weight jobs dominate the queue.
  - It may not be suitable for hard real-time systems, as it does not guarantee the deadlines of the jobs.
  - It may not be optimal for minimizing the average response time or the average waiting time of the jobs, as it does not consider the job lengths or arrival times.