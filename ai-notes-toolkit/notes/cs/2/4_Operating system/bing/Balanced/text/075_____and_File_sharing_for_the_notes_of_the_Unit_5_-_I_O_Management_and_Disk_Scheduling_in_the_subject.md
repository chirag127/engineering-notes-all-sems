# I/O Management and Disk Scheduling

## I/O Management
- I/O management is the process of coordinating and controlling the communication between the CPU and the external devices, such as disks, terminals, printers, etc.
- I/O devices vary in their characteristics, such as data transfer rate, access method, capacity, etc. Therefore, different I/O devices may require different I/O techniques and strategies.
- I/O management involves several components, such as:
  - I/O hardware: the physical devices and controllers that perform I/O operations.
  - I/O software: the software layers that provide interfaces and services for I/O operations, such as device drivers, interrupt handlers, device-independent I/O, user-level I/O, etc.
  - I/O performance: the metrics and methods to measure and improve the efficiency and effectiveness of I/O operations.

## Disk Scheduling
- Disk scheduling is the process of deciding the order and timing of I/O requests to a disk drive, in order to optimize the disk performance and reduce the disk access time.
- Disk scheduling is necessary because disk access time consists of two components: seek time and rotational latency. Seek time is the time required to move the disk head to the desired track, and rotational latency is the time required to wait for the desired sector to rotate under the disk head. Both seek time and rotational latency depend on the physical location of the data on the disk, and can be minimized by choosing an appropriate order of I/O requests.
- Disk scheduling algorithms are the methods to determine the order of I/O requests to a disk drive, based on different criteria and objectives, such as:
  - FCFS (First Come First Served): the simplest algorithm that processes the I/O requests in the order they arrive, without any reordering or optimization.
  - SSTF (Shortest Seek Time First): the algorithm that processes the I/O request that requires the shortest seek time from the current position of the disk head, thus minimizing the total seek time.
  - SCAN (Elevator): the algorithm that processes the I/O requests in one direction until there are no more requests in that direction, then reverses the direction and repeats the process, thus avoiding the starvation of requests at the ends of the disk.
  - C-SCAN (Circular SCAN): the algorithm that processes the I/O requests in one direction until there are no more requests in that direction, then jumps to the other end of the disk and repeats the process, thus providing a more uniform service time for all requests.
  - LOOK and C-LOOK: the variants of SCAN and C-SCAN that only change the direction or jump to the other end of the disk when there are requests in that direction, thus avoiding unnecessary movements of the disk head.