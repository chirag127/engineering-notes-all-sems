## Unit 5 - I/O Management and Disk Scheduling

1. **I/O Management:** Input/Output (I/O) management is responsible for controlling the flow of data between the computer's main memory and its peripheral devices, such as printers, keyboards, and disk drives. It involves buffering, caching, and spooling data to improve the performance of the system.

2. **Disk Scheduling:** Disk scheduling is the process of determining the order in which disk I/O requests are processed. The goal of disk scheduling is to minimize the total seek time, which is the time it takes for the disk read/write head to move to the location of the requested data. Common disk scheduling algorithms include First-Come-First-Serve (FCFS), Shortest Seek Time First (SSTF), and SCAN.

3. **Buffering:** Buffering is the process of temporarily storing data in memory while it is being transferred between two devices. This can help to smooth out variations in the data transfer rate and improve the overall performance of the system.

4. **Caching:** Caching is the process of storing frequently accessed data in a high-speed memory, such as the CPU cache or a disk cache, to reduce the time it takes to access the data. This can significantly improve the performance of the system.

5. **Spooling:** Spooling is the process of temporarily storing data on a disk or in memory while it is waiting to be processed. This can be used to manage the flow of data between devices with different data transfer rates, such as a printer and a computer.

6. **First-Come-First-Serve (FCFS):** FCFS is a simple disk scheduling algorithm that processes disk I/O requests in the order in which they are received. While this algorithm is easy to implement, it can result in long wait times for some requests.

7. **Shortest Seek Time First (SSTF):** SSTF is a disk scheduling algorithm that processes disk I/O requests in the order of their proximity to the current position of the disk read/write head. This can reduce the total seek time, but can also result in starvation for some requests.

8. **SCAN:** SCAN is a disk scheduling algorithm that moves the disk read/write head back and forth across the disk, processing requests in the order of their position on the disk. This can result in a more even distribution of wait times for requests, but can also result in longer seek times for some requests.