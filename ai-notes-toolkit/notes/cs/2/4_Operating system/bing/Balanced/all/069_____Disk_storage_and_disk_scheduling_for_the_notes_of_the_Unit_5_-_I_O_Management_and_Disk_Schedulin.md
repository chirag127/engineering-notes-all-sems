# Disk Storage and Disk Scheduling

## Disk Storage

- Disk storage is a type of non-volatile storage that uses rotating magnetic disks to store and retrieve data.
- Disk storage consists of one or more platters, each with a thin coating of magnetic material, that are mounted on a common spindle and rotated at high speed.
- A read/write head, attached to an arm that can move across the surface of the platters, is used to read or write data on the disk.
- The position of the head and the platter is specified by two parameters: the cylinder number and the sector number.
- The cylinder number is the vertical alignment of tracks on different platters. A track is a circular path on a platter where data is stored.
- The sector number is the angular position of the data on a track. A sector is a fixed-size unit of data on a track, typically 512 bytes.
- The time required to access data on a disk depends on three factors: the seek time, the rotational latency, and the transfer time.
- The seek time is the time required to move the head to the desired cylinder. It depends on the current and the target position of the head, and the speed of the arm.
- The rotational latency is the time required to rotate the platter to the desired sector. It depends on the current and the target position of the sector, and the speed of the spindle.
- The transfer time is the time required to read or write data from or to the disk. It depends on the amount of data, the sector size, and the rotational speed of the disk.

## Disk Scheduling

- Disk scheduling is a technique used by the operating system to schedule multiple requests for accessing the disk.
- Disk scheduling aims to reduce the total seek time, which is the sum of the seek times for all the requests in the queue.
- Disk scheduling also aims to improve the throughput, which is the number of requests serviced per unit time, and the fairness, which is the degree of satisfaction of the processes that issued the requests.
- Disk scheduling algorithms are the methods used by the operating system to decide the order in which the requests in the queue are serviced.
- Some of the common disk scheduling algorithms are:

  - First In First Out (FIFO): This algorithm services the requests in the order they arrive in the queue. It is simple and fair, but it does not minimize the seek time or the head movement.
  - Shortest Seek Time First (SSTF): This algorithm services the request that is closest to the current position of the head. It minimizes the seek time and the head movement, but it may cause starvation for the requests that are far from the head.
  - SCAN: This algorithm moves the head in one direction, servicing all the requests in that direction, until it reaches the end of the disk. Then it reverses the direction and repeats the process. It reduces the seek time and the head movement, but it may cause long waiting time for the requests at the ends of the disk.
  - C-SCAN: This algorithm is similar to SCAN, but instead of reversing the direction at the end of the disk, it jumps to the other end and continues in the same direction. It provides more uniform waiting time for the requests, but it may cause more head movement than SCAN.
  - LOOK: This algorithm is similar to SCAN, but instead of going to the end of the disk, it reverses the direction when there are no more requests in that direction. It reduces the head movement and the seek time, but it may cause long waiting time for the requests at the ends of the disk.
  - C-LOOK: This algorithm is similar to C-SCAN, but instead of jumping to the other end of the disk, it reverses the direction when there are no more requests in that direction. It provides more uniform waiting time for the requests, but it may cause more head movement than LOOK.