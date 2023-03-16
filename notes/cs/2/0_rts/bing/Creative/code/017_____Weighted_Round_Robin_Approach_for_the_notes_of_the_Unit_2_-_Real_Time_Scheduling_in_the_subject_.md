### Weighted Round Robin Approach

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

- The weighted round robin algorithm can be implemented using a circular queue of jobs, where each job is enqueued as many times as its weight.
- The algorithm then dequeues and serves one job at a time, until the queue is empty.
- The queue is then refilled with the same jobs and weights, and the process repeats.
- The advantage of weighted round robin is that it can provide differentiated service to different jobs, based on their relative importance or urgency  .
- The disadvantage of weighted round robin is that it may not be fair or optimal for some jobs, especially if their weights are not proportional to their service demands .
- For example, if a job has a high weight but a low service demand, it may receive more service than it needs, while another job with a low weight but a high service demand may receive less service than it needs .
- This may result in poor performance or missed deadlines for some jobs .
- Another disadvantage of weighted round robin is that it may not be suitable for dynamic real-time systems, where the properties of the jobs may change over time or new jobs may arrive unpredictably.
- In such cases, priority-driven scheduling algorithms may be more effective.