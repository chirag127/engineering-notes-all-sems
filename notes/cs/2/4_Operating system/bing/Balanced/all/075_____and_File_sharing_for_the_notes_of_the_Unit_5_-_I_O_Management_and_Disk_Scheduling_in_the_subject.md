# Unit 5 - I/O Management and Disk Scheduling

## I/O Management
- I/O management is the process of controlling the input and output devices of a computer system.
- I/O devices can be classified into three categories:
  - Human I/O devices: suitable for communicating with the computer user, such as printers, terminals, video display, keyboard, mouse, etc.
  - Machine I/O devices: suitable for communicating with electronic equipment, such as sensors, actuators, controllers, etc.
  - Storage I/O devices: suitable for storing data, such as disk drives, tape drives, CD-ROMs, etc.
- I/O management involves the following tasks:
  - Buffering: storing data temporarily in memory to cope with the speed and size differences between the I/O device and the CPU or memory.
  - Caching: storing frequently used data in a faster storage device (such as RAM) to reduce the access time and improve the performance.
  - Spooling: transferring data between two devices or processes that have different speeds or availability, such as printing a file while editing another file.
  - Device reservation: allocating a device to a process for exclusive use, such as a printer or a tape drive.
  - Error handling: detecting and correcting errors that occur during I/O operations, such as parity errors, device failures, etc.
  - Device drivers: software modules that provide a uniform interface between the operating system and the device, hiding the device-specific details and commands.

## Disk Scheduling
- Disk scheduling is the process of deciding the order and manner of servicing the requests for data transfer to or from the disk.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller. Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - The disk access time depends on the seek time (the time to move the disk head to the desired track), the rotational latency (the time to wait for the desired sector to rotate under the disk head), and the transfer time (the time to read or write the data). The seek time is usually the dominant factor and can be reduced by scheduling the requests that are close to the current position of the disk head.
  - The disk performance can be measured by the throughput (the amount of data transferred per unit time) and the response time (the average time for a request to be completed).
- Disk scheduling algorithms can be classified into two categories:
  - Non-preemptive algorithms: the disk head services a request until it is completed, then moves to the next request. Examples are First Come First Serve (FCFS), Shortest Seek Time First (SSTF), SCAN, C-SCAN, LOOK, C-LOOK, etc.
  - Preemptive algorithms: the disk head can be interrupted by a higher priority request while servicing a request, then resumes the interrupted request later. Examples are Shortest Remaining Time First (SRTF), Earliest Deadline First (EDF), etc.