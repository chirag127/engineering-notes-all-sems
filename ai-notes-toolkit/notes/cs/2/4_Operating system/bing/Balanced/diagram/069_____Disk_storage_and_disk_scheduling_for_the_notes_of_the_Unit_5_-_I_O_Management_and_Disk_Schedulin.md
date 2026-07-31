### Disk Storage and Disk Scheduling

- Disk storage is a type of secondary storage that uses magnetic or optical disks to store data permanently or semi-permanently.
- Disk storage devices include hard disk drives (HDDs), floppy disks, compact discs (CDs), digital versatile discs (DVDs), Blu-ray discs, etc.
- Disk storage devices have two main components: a disk surface that stores data in concentric tracks and sectors, and a disk head that reads and writes data to and from the disk surface.
- Disk storage devices have several characteristics that affect their performance, such as capacity, access time, transfer rate, rotational speed, seek time, latency, etc.
- Disk scheduling is a technique used by the operating system to schedule multiple requests for accessing the disk.
- Disk scheduling aims to reduce the total seek time, which is the time taken by the disk head to move from one track to another.
- Disk scheduling also aims to improve the throughput, which is the amount of data transferred per unit time, and the fairness, which is the degree of satisfaction of different processes or users.
- Disk scheduling algorithms are the algorithms used for disk scheduling. They determine the order in which the disk requests are serviced by the disk head.
- Some common disk scheduling algorithms are:
  - First Come First Serve (FCFS): It services the disk requests in the order they arrive. It is simple but may result in long seek time and low throughput.
  - Shortest Seek Time First (SSTF): It services the disk request that is closest to the current position of the disk head. It reduces the seek time but may cause starvation of some requests.
  - SCAN: It services the disk requests in one direction until there are no more requests in that direction, then reverses the direction and repeats the process. It is also known as the elevator algorithm. It reduces the seek time and provides fairness but may cause long waiting time for some requests.
  - C-SCAN: It is a variation of SCAN that services the disk requests in one direction only, then jumps to the other end of the disk and repeats the process. It is also known as the circular scan algorithm. It provides more uniform waiting time than SCAN but may cause more seek time.
  - LOOK and C-LOOK: They are variations of SCAN and C-SCAN that only move the disk head as far as the last request in each direction, rather than to the end of the disk. They reduce the seek time and the waiting time.