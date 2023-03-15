### Disk Storage and Disk Scheduling

- Disk storage is a type of secondary storage that uses magnetic or optical disks to store data permanently or semi-permanently.
- Disk storage devices include hard disk drives (HDDs), floppy disks, compact discs (CDs), digital versatile discs (DVDs), Blu-ray discs, etc.
- Disk storage devices have two main components: a disk surface that stores data in concentric tracks and sectors, and a disk head that reads and writes data to and from the disk surface.
- Disk storage devices have several characteristics that affect their performance, such as capacity, access time, transfer rate, rotational speed, seek time, latency, etc.
- Disk scheduling is a technique used by the operating system to schedule multiple requests for accessing the disk.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive from different processes and only one I/O request can be served at a time by the disk controller.
  - Thus, other I/O requests need to wait in the waiting queue and need to be scheduled.
  - The order in which the I/O requests are served can affect the total seek time, which is the time taken by the disk head to move from one track to another.
  - The total seek time can affect the disk performance and the system throughput.
- Disk scheduling algorithms are the algorithms used for disk scheduling. The purpose of disk scheduling algorithms is to reduce the total seek time and improve the disk performance and the system throughput.
- Some disk scheduling algorithms are:
  - First Come First Serve (FCFS): It serves the I/O requests in the order they arrive in the waiting queue. It is the simplest disk scheduling algorithm, but it may not minimize the total seek time.
  - Shortest Seek Time First (SSTF): It serves the I/O request that is closest to the current position of the disk head. It reduces the total seek time, but it may cause starvation for some requests that are far away from the disk head.
  - SCAN: It moves the disk head from one end of the disk to the other, serving the I/O requests in one direction. Then, it reverses the direction and repeats the process. It is also known as the elevator algorithm. It reduces the total seek time and avoids starvation, but it may cause long waiting time for some requests at the ends of the disk.
  - C-SCAN: It is a variation of SCAN that moves the disk head from one end of the disk to the other, serving the I/O requests in one direction. Then, it jumps back to the other end of the disk and repeats the process. It is also known as the circular scan algorithm. It reduces the total seek time and avoids starvation, but it may cause long waiting time for some requests at the ends of the disk.
  - LOOK: It is a variation of SCAN that moves the disk head only as far as the last request in each direction, instead of going to the end of the disk. It reduces the total seek time and avoids starvation, but it may cause long waiting time for some requests at the ends of the disk.
  - C-LOOK: It is a variation of C-SCAN that moves the disk head only as far as the last request in each direction, instead of going to the end of the disk. Then, it jumps back to the other end of the disk and repeats the process. It reduces the total seek time and avoids starvation, but it may cause long waiting time for some requests at the ends of the disk.