# Unit 5 - I/O Management and Disk Scheduling

- I/O management is the process of coordinating and controlling the communication between the CPU and the external devices, such as disks, printers, keyboards, mice, etc.
- I/O devices vary widely in their characteristics, such as data transfer rate, access method, capacity, and functionality.
- I/O management involves several components, such as device drivers, interrupt handlers, device controllers, buffers, and I/O scheduling algorithms.
- Device drivers are software modules that interact with specific devices and provide a uniform interface to the operating system.
- Interrupt handlers are routines that are executed when an I/O device signals the CPU that it needs attention or has completed an operation.
- Device controllers are hardware components that manage the data transfer between the device and the main memory, and generate interrupts when necessary.
- Buffers are memory areas that temporarily store data during I/O operations, to improve performance and reduce CPU involvement.
- I/O scheduling algorithms are methods that determine the order and priority of I/O requests, to optimize the utilization of the I/O devices and the CPU.

- Disk scheduling is a specific type of I/O scheduling that deals with the requests for data transfer to and from the disk drives.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller. Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - Disk drives have long access times for requests placed far away from the current position of the disk head (this operation is called a seek). Thus the order of servicing the requests can affect the total seek time and the disk performance.
  - Disk drives are used to store files and virtual memory pages, which have different characteristics and requirements. For example, file access may be sequential or random, while virtual memory access may be more predictable and require faster response time. Thus the disk scheduling algorithm may need to consider the type and purpose of the requests.
- Disk scheduling algorithms can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive algorithms are those that do not interrupt the current request once it is started, and wait until it is completed before moving to the next one. Examples of non-preemptive algorithms are First Come First Served (FCFS), Shortest Seek Time First (SSTF), and Scan (or Elevator).
  - Preemptive algorithms are those that can interrupt the current request if a higher priority request arrives, and resume the interrupted request later. Examples of preemptive algorithms are Circular Scan (C-Scan), Look, and C-Look.