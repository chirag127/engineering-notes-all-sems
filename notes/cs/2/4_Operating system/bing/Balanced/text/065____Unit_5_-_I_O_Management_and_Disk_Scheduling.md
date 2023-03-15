## Unit 5 - I/O Management and Disk Scheduling

- I/O management is the process of controlling the input and output devices of a computer system, such as disks, keyboards, printers, terminals, etc.
- I/O management involves the following tasks:
  - Providing a uniform interface for different types of devices
  - Allocating and deallocating devices to processes
  - Buffering and caching data to improve performance
  - Handling errors and exceptions
  - Implementing security and protection mechanisms
- Disk scheduling is a specific aspect of I/O management that deals with the order in which disk requests are serviced by the disk controller.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller. Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - The access time of a disk request depends on the seek time, rotational latency, and transfer time. Seek time is the time required to move the disk head to the desired track. Rotational latency is the time required to wait for the desired sector to rotate under the disk head. Transfer time is the time required to read or write the data from or to the disk. Seek time and rotational latency are the major components of the access time and vary depending on the location of the data on the disk.
  - The objective of disk scheduling is to minimize the total access time and maximize the disk throughput (the amount of data transferred per unit time).
- Disk scheduling algorithms are the methods used to decide the order of servicing the disk requests in the waiting queue. Some common disk scheduling algorithms are:
  - First Come First Served (FCFS): The disk requests are serviced in the order they arrive in the queue. This algorithm is simple and fair, but does not take into account the location of the data on the disk and may result in long seek times and low disk throughput.
  - Shortest Seek Time First (SSTF): The disk request with the shortest seek time from the current head position is serviced next. This algorithm reduces the seek time and improves the disk throughput, but may cause starvation for some requests that are far away from the current head position.
  - SCAN: The disk head moves in one direction and services all the requests in that direction until it reaches the end of the disk. Then it reverses the direction and repeats the process. This algorithm is also known as the elevator algorithm, as it resembles the movement of an elevator in a building. This algorithm avoids starvation and provides a more uniform service than SSTF, but may cause long waiting times for requests at the ends of the disk.
  - C-SCAN: The disk head moves in one direction and services all the requests in that direction until it reaches the end of the disk. Then it jumps to the other end of the disk and repeats the process. This algorithm is a circular version of SCAN, and provides a more even distribution of service than SCAN, but may cause longer average waiting times than SCAN.
  - LOOK and C-LOOK: These algorithms are similar to SCAN and C-SCAN, except that they do not go to the end of the disk, but only to the last request in that direction. This reduces the unnecessary movement of the disk head and improves the performance of SCAN and C-SCAN.