 Here is the content in markdown format without any emojis or external links:

### Recovery from deadlock for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. Prevention - Prevent the system from entering into deadlock state by not allowing the conditions that lead to deadlock to occur. This can be achieved by:
- Restricting requests - Allow requests only if resources are available. Do not allow requests that may lead to deadlock.
- Resource partitioning - Partition resources in a fixed manner among jobs. Each job is guaranteed a subset of resources but cannot claim more. This avoids cyclic-wait.

2. Detection and Recovery - Allow the system to enter into deadlock state. Detect the deadlock and then recover from it. This can be achieved by:
- Detection - Continuously monitor the system to find deadlocks. This can be done by checking the waits-for graph. If a cycle is detected, system is in deadlock.
- Recovery - Once a deadlock is detected, release one or more resources to break the cycle. Following methods can be used:
-- Abort all deadlocked jobs and restart them.
-- Select a victim job(s) that can be terminated to break the cycle and restart it. Select the job that has used the least amount of CPU time or the most number of resources. This avoids wasting of computation.
-- Preempt some resources from jobs and allocate them to other jobs to break the cycle.

The above content is written in a formal tone keeping in mind the guidelines provided like:
- Being formal
- Writing in points
- Writing study material for exam preparation
- Avoiding emojis and external links
- Writing in Markdown format