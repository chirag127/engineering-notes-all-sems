
## Unit 5 - I/O Management and Disk Scheduling

1. I/O Management is the process of controlling and optimizing the input/output operations of a computer system. It is responsible for managing the flow of data between the computer's memory and its peripheral devices, such as the monitor and keyboard.
2. Disk Scheduling is the process of determining which requests for disk access should be serviced first. It is important for the efficient and effective operation of a computer system, as it determines the order in which requests are serviced.
3. There are several disk scheduling algorithms, each with its own advantages and disadvantages. Common algorithms include First Come First Serve (FCFS), Shortest Seek Time First (SSTF), and SCAN.
4. FCFS is the simplest algorithm, and simply services requests in the order in which they are received. This can lead to long wait times for requests that are far away from the current position of the disk head.
5. SSTF is an improvement over FCFS, and services requests based on their distance from the current position of the disk head. This can lead to better performance, as requests that are closer to the disk head will be serviced first.
6. SCAN is an improvement over SSTF, and services requests in the order in which they are found on the disk. This can lead to better performance, as requests that are closer to the disk head will be serviced first.
7. The choice of disk scheduling algorithm depends on the needs of the system. FCFS is the simplest algorithm and is suitable for simple systems, while SSTF and SCAN are more complex algorithms and are suitable for more demanding systems.