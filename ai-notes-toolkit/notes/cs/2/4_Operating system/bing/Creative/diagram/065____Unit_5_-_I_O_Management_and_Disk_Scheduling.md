## Unit 5 - I/O Management and Disk Scheduling

- I/O management is the process of controlling the input and output devices of a computer system, such as keyboards, mice, printers, disks, etc.
- I/O management involves the following tasks:
  - Allocating and deallocating I/O devices to processes or users.
  - Buffering and caching data to improve I/O performance and reduce latency.
  - Error handling and recovery from I/O failures.
  - Providing a uniform and abstract interface to different types of I/O devices.
  - Synchronizing and scheduling I/O requests to optimize throughput and fairness.
- Disk scheduling is a specific type of I/O scheduling that deals with the order in which disk read and write requests are serviced by the disk controller.
- Disk scheduling aims to minimize the seek time, rotational latency, and transfer time of disk operations, as well as to maximize the disk utilization and bandwidth.
- Disk scheduling algorithms include:
  - First Come First Serve (FCFS): The simplest algorithm that services requests in the order they arrive. It is fair but not efficient, as it does not take into account the location of the disk head or the requests.
  - Shortest Seek Time First (SSTF): The algorithm that services the request that is closest to the current position of the disk head. It is efficient but not fair, as it may cause starvation of distant requests.
  - SCAN: The algorithm that moves the disk head in one direction, servicing all the requests in that direction, until it reaches the end of the disk, then reverses the direction and repeats. It is also known as the elevator algorithm. It is more fair than SSTF, but may cause long waiting times for requests at the ends of the disk.
  - C-SCAN: The algorithm that is similar to SCAN, but instead of reversing the direction at the ends of the disk, it jumps to the other end and continues in the same direction. It is also known as the circular scan algorithm. It is more uniform than SCAN, as it provides equal waiting time for all requests, but may cause longer average waiting time.
  - LOOK and C-LOOK: The algorithms that are variations of SCAN and C-SCAN, but instead of going to the ends of the disk, they change direction or jump to the other end when there are no more requests in that direction. They are more efficient than SCAN and C-SCAN, as they avoid unnecessary disk head movements.