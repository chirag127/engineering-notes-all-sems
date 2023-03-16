### Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which gives equal shares of the processor to ready jobs in a circular order.
- Rather than giving all the ready jobs equal shares of the processor, weighted round robin assigns different weights to different jobs  .
- The weight of a job represents the fixed number of service opportunities or the fixed fraction of the processor time that the job receives in each cycle .
- The higher the weight of a job, the more service opportunities or processor time it gets.
- Weighted round robin can improve the performance and fairness of real-time scheduling by giving higher priority to more urgent or important jobs .
- However, weighted round robin may also introduce more overhead and complexity in the scheduling algorithm and the weight assignment .
- Weighted round robin may also delay the completion of every job, especially if there are precedence constraints among the jobs .
- Therefore, weighted round robin should be carefully designed and configured to balance the trade-offs between performance, fairness, overhead, and complexity .