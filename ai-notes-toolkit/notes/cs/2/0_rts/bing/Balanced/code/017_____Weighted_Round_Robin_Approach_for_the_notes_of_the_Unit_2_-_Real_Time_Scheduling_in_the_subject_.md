### Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the job with weight 3 will receive twice as many service opportunities as the job with weight 2, and three times as many as the job with weight 1.
- Weighted round robin can achieve a fair and efficient allocation of resources among different jobs.
- It can also handle different types of traffic with different quality of service requirements.
- However, weighted round robin may not be suitable for hard real-time systems where all properties of all jobs are known at design time, and where offline scheduling techniques can be used.
- Weighted round robin may also suffer from long waiting times and poor response times for some jobs, especially if the weights are not well balanced.