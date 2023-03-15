# Unit 5 - I/O Management and Disk Scheduling

## I/O Management
- I/O management is the process of controlling the input and output devices of a computer system.
- I/O management involves the following tasks:
  - Allocating and deallocating I/O devices to processes or users.
  - Buffering and caching data to improve I/O performance and reduce CPU overhead.
  - Synchronizing and scheduling I/O requests to optimize device utilization and throughput.
  - Handling errors and exceptions that may occur during I/O operations.
  - Providing a uniform and abstract interface to the application programs and the operating system.

## Disk Scheduling
- Disk scheduling is the process of deciding the order in which disk I/O requests are serviced by the disk controller.
- Disk scheduling aims to minimize the seek time, rotational latency, and transfer time of disk I/O requests, and to maximize the disk bandwidth and throughput.
- Disk scheduling algorithms can be classified into two categories:
  - Non-preemptive algorithms: These algorithms service the disk I/O requests in a fixed order, without interruption. Examples are FCFS (First Come First Serve), SSTF (Shortest Seek Time First), SCAN, C-SCAN, LOOK, and C-LOOK.
  - Preemptive algorithms: These algorithms can interrupt the servicing of a disk I/O request if a higher priority request arrives. Examples are SPTF (Shortest Positioning Time First), EDF (Earliest Deadline First), and FD-SCAN.

## File Sharing
- File sharing is the process of allowing multiple users or processes to access the same file or files on a disk or a network.
- File sharing can be implemented in different ways, such as:
  - Shared access: Multiple users or processes can open and read or write the same file concurrently, with some form of locking or concurrency control to ensure data consistency and integrity.
  - Distributed file system: A file system that spans multiple disks or machines, and provides a transparent and uniform access to the files regardless of their physical location or network topology.
  - Peer-to-peer file system: A file system that allows users to share files directly with each other, without relying on a central server or authority.