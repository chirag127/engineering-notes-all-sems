## Unit 5 - I/O Management and Disk Scheduling

### I/O Management
- I/O devices allow the computer system to interact with the outside world.
- I/O management handles the communication between the CPU and I/O devices.
- The goal of I/O management is to maximize the performance of the I/O devices and minimize the CPU idle time.
- The most common I/O devices are keyboards, mice, printers, scanners, and disk drives.
- I/O requests are placed in a queue and are handled by the device driver.
- I/O devices can be either blocking or non-blocking.
- Blocking devices halt the CPU until the I/O operation is complete, while non-blocking devices allow the CPU to continue processing.

### Disk Scheduling
- Disk scheduling is the process of deciding which disk I/O request to handle next.
- The goal of disk scheduling is to minimize the seek time and rotational latency.
- The most common disk scheduling algorithms are First-Come-First-Serve (FCFS), Shortest-Seek-Time-First (SSTF), SCAN, and C-SCAN.
- FCFS schedules the requests in the order they arrive.
- SSTF schedules the request with the shortest seek time from the current head position.
- SCAN schedules the requests in one direction, servicing all requests in that direction, and then reversing direction.
- C-SCAN is similar to SCAN, but it only services requests in one direction, and when it reaches the end of the disk, it immediately returns to the beginning.

### Disk Caching
- Disk caching is the process of storing frequently accessed data in memory to reduce the number of disk accesses.
- The most common disk caching algorithms are Least Recently Used (LRU) and First-In-First-Out (FIFO).
- LRU replaces the least recently used block in the cache when a new block needs to be added.
- FIFO replaces the oldest block in the cache when a new block needs to be added.
- Disk caching can significantly improve performance, but it can also lead to data inconsistency if the cache is not properly managed.

### RAID
- RAID (Redundant Array of Independent Disks) is a technique for combining multiple disk drives into a single logical unit.
- RAID provides improved performance, fault tolerance, and data protection.
- The most common RAID levels are RAID 0, RAID 1, RAID 5, and RAID 6.
- RAID 0 uses striping to improve performance but does not provide fault tolerance.
- RAID 1 uses mirroring to provide fault tolerance but does not improve performance.
- RAID 5 uses striping with parity to provide both performance and fault tolerance.
- RAID 6 is similar to RAID 5 but uses two parity blocks for greater fault tolerance.