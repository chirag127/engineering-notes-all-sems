# Bus Arbitration in Computer Organization

- Bus arbitration is the process by which the next device becomes the bus controller by transferring bus mastership to another bus   .
- A bus master is a device that initiates data transfers on the bus at any given time, such as a processor or a DMA controller  .
- Bus arbitration is necessary to avoid conflicts and ensure proper communication among multiple bus masters that may want to access the bus simultaneously .
- There are two types of bus arbitration: centralized and distributed   .
- In centralized arbitration, there is a single bus arbiter that performs the required arbitration and grants the bus access to one of the requesting devices. The bus arbiter can be either a processor or a separate hardware unit   .
- In distributed arbitration, there is no central arbiter, but each device has its own arbitration logic and communicates with other devices to decide the bus access. This can be done using daisy chaining or independent request lines   .
- Centralized arbitration is simpler and faster, but it creates a single point of failure and a bottleneck for the bus access. Distributed arbitration is more reliable and scalable, but it requires more hardware and communication overhead .