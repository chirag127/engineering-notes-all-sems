### Disk Storage and Disk Scheduling

- Disk storage is a type of secondary storage that uses magnetic or optical disks to store data permanently or semi-permanently.
- Disk storage devices include hard disk drives (HDDs), solid state drives (SSDs), floppy disks, compact discs (CDs), digital versatile discs (DVDs), and Blu-ray discs (BDs).
- Disk storage devices have two main components: a disk surface that stores data in concentric tracks and sectors, and a disk head that reads and writes data to the disk surface.
- Disk storage devices have several characteristics that affect their performance, such as capacity, access time, transfer rate, rotational speed, and seek time.
- Disk scheduling is a technique used by the operating system to schedule multiple requests for accessing the disk.
- Disk scheduling is important because multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller.
- Disk scheduling aims to reduce the total seek time, which is the time taken by the disk head to move from one track to another.
- Disk scheduling also aims to improve the throughput, which is the amount of data transferred per unit time, and the fairness, which is the degree of satisfaction of different processes.
- Disk scheduling algorithms are the algorithms used for disk scheduling. They determine the order in which the disk requests are served by the disk controller.
- Some of the common disk scheduling algorithms are:
  - First in First Out (FIFO): This algorithm serves the disk requests in the order they arrive in the queue. It is simple and fair, but it does not minimize the seek time.
  - Shortest Seek Time First (SSTF): This algorithm serves the disk request that is closest to the current position of the disk head. It minimizes the seek time, but it may cause starvation for some requests that are far away from the disk head.
  - Scan: This algorithm moves the disk head from one end of the disk to the other, serving the disk requests that are in the direction of the disk head movement. It reduces the seek time and avoids starvation, but it may cause long waiting time for some requests at the ends of the disk.
  - Circular Scan (C-Scan): This algorithm is similar to Scan, but it moves the disk head back to the beginning of the disk after reaching the end, without serving any requests in the reverse direction. It provides a more uniform waiting time for the requests, but it may cause more seek time than Scan.
  - Look and C-Look: These algorithms are variations of Scan and C-Scan, but they do not move the disk head to the ends of the disk if there are no requests beyond the current position of the disk head. They reduce the seek time and the waiting time, but they are more complex than Scan and C-Scan.