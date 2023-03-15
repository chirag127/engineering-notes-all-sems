## Unit 5 - I/O Management and Disk Scheduling

- I/O management is the process of coordinating and controlling the communication between the CPU and the external devices, such as disks, terminals, printers, etc.
- I/O devices vary widely in their characteristics, such as data transfer rate, access method, capacity, etc. Therefore, I/O management requires different strategies and techniques for different devices.
- I/O management involves several components, such as device drivers, interrupt handlers, device controllers, I/O buffers, and I/O scheduling algorithms.
- Device drivers are software modules that interact with specific devices and provide a uniform interface to the operating system.
- Interrupt handlers are routines that are invoked when an I/O device signals the CPU that it needs attention, such as completing an I/O operation or reporting an error.
- Device controllers are hardware components that manage the data transfer between the device and the main memory, using direct memory access (DMA) or programmed I/O (PIO).
- I/O buffers are memory locations that temporarily store data during I/O operations, to improve the performance and reduce the CPU involvement.
- I/O scheduling algorithms are methods that determine the order and priority of I/O requests, to optimize the utilization and performance of the I/O devices and the system as a whole.

- Disk scheduling is a specific type of I/O scheduling that deals with the requests for data transfer to and from the disk drives.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller. Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - Disk drives have long access times for requests placed far away from the current position of the disk head (this operation is called a seek). Therefore, the order of servicing the requests can affect the total seek time and the disk throughput.
  - Disk drives are used for different purposes, such as file storage, virtual memory, database, etc. Therefore, the disk scheduling algorithm may need to consider the application-specific requirements and constraints.
- Disk scheduling algorithms can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive algorithms are those that do not interrupt the current I/O request once it is started, even if a higher-priority request arrives. Examples of non-preemptive algorithms are First Come First Served (FCFS), Shortest Seek Time First (SSTF), SCAN, C-SCAN, LOOK, and C-LOOK.
  - Preemptive algorithms are those that can interrupt the current I/O request if a higher-priority request arrives, and resume the interrupted request later. Examples of preemptive algorithms are Shortest Remaining Time First (SRTF), Earliest Deadline First (EDF), and Least Slack Time First (LSTF).
- Disk scheduling algorithms can be evaluated based on several criteria, such as average seek time, average response time, average waiting time, throughput, fairness, and starvation.