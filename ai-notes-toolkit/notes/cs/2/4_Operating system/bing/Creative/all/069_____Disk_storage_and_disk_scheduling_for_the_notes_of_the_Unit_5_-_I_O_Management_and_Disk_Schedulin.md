# Disk Storage and Disk Scheduling

## Disk Storage

- Disks are the mainly used secondary storage devices. They provide the bulk of secondary storage in operating systems today.
- Disks are composed of one or more circular platters, each divided into concentric tracks and sectors. A disk drive has a read/write head that can move to any track and sector on the disk.
- Disks can be classified into two types: hard disks and floppy disks. Hard disks have higher capacity, speed, and reliability than floppy disks. Floppy disks are removable and portable, but have lower performance and durability.
- Disks can also be classified into two modes: sequential access and random access. Sequential access means that the data is accessed in a fixed order, such as in a tape drive. Random access means that the data can be accessed in any order, such as in a disk drive.

## Disk Scheduling

- Disk scheduling is a technique used by the operating system to schedule multiple requests for accessing the disk.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller. Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - The disk head movement is the major factor that affects the disk performance. The disk head has to move from one track to another to access the requested data. This movement is called seek. The time taken by the disk head to move from one track to another is called seek time. The seek time is proportional to the distance between the tracks. The disk scheduling algorithms aim to reduce the total seek time and improve the disk efficiency .
- Disk Scheduling Algorithms
  - The algorithms used for disk scheduling are called as disk scheduling algorithms. The purpose of disk scheduling algorithms is to reduce the total seek time.
  - Some disk head scheduling algorithms include  :
    - First Come First Serve (FCFS): It serves the requests in the order they arrive. It is the simplest disk scheduling algorithm, but it does not optimize the disk head movement.
    - Shortest Seek Time First (SSTF): It serves the request that is closest to the current position of the disk head. It minimizes the seek time for each request, but it may cause starvation for some requests that are far away from the disk head.
    - SCAN: It moves the disk head from one end of the disk to the other, serving the requests along the way. It is also known as the elevator algorithm. It reduces the variance of the seek time, but it may cause long waiting time for the requests at the ends of the disk.
    - C-SCAN: It is a circular version of SCAN. It moves the disk head from one end of the disk to the other, serving the requests along the way, and then jumps back to the first end without serving any request. It provides a more uniform waiting time for the requests, but it may cause more seek time than SCAN.
    - LOOK and C-LOOK: They are variations of SCAN and C-SCAN, respectively. They do not move the disk head to the ends of the disk, but only to the last request in each direction. They reduce the unnecessary disk head movement and improve the performance of SCAN and C-SCAN.