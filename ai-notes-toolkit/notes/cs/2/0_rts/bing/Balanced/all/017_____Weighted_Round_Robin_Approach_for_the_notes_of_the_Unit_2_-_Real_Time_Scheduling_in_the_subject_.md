# Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the service opportunities will be allocated as follows: 1/6, 2/6, and 3/6.
- Weighted round robin can achieve a fair and efficient allocation of resources among different classes of jobs.
- It can also handle variable-length jobs and bursty traffic.
- However, it may not be suitable for hard real-time systems where strict deadlines and priorities are required.
- It may also suffer from starvation if the weights are not properly configured.