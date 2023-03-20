 Here is the content in markdown format without any emojis or external links and in formal tone:

### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. Starvation: It is a scenario where a process is not getting enough CPU cycles as per its need for a very long time. This leads to a severe delay in the execution of the process.
To prevent starvation, scheduling algorithms must ensure that every process gets a fair share of CPU. Some ways to achieve this are:
- Guarantee each process a minimum CPU time quantum.
- Implement aging, which is increasing the priority of processes that wait for CPU the longest.

2. Deadlock: It is a state where a set of processes are blocked forever, waiting for each other to release a resource.
To prevent deadlock, we can:
- Avoid the conditions that lead to deadlock. This can be done using methods such as:
-- Not allowing processes to hold resources until they request all they need.
-- Ordering resource requests and always requesting resources in a specific order.
-- Not allowing processes to request resources that may lead to a circular wait.
- Use deadlock detection and recovery mechanisms. The scheduler can periodically check for deadlocks and take corrective actions if any are detected.

3. Thrashing: It is a phenomenon where the system spends more time in swapping processes in and out of main memory than in actual execution. This leads to severe performance degradation.
To prevent thrashing, we can:
- Ensure that the total memory demand does not exceed the actual physical memory available.
- Use swapping and paging more efficiently by modifying page replacement algorithms to consider the frequency of access of pages.
- Use memory caches to keep the most frequently used pages in memory.