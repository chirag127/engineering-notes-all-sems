### Bus Arbitration

- Bus arbitration is the process by which the next device becomes the bus controller by transferring bus mastership to another device   .
- A bus master is a device that initiates data transfers on the bus at any given time, such as a processor or a DMA controller  .
- Bus arbitration is necessary to avoid conflicts and ensure proper communication among multiple devices that share the same bus.
- There are two types of bus arbitration: centralized and distributed .

#### Centralized Arbitration
- In centralized arbitration, there is a single bus arbiter that performs the required arbitration and grants the bus to the requesting device .
- The bus arbiter can be either a processor or a separate hardware unit.
- The advantages of centralized arbitration are simplicity, low cost, and easy implementation.
- The disadvantages of centralized arbitration are single point of failure, bottleneck, and limited scalability.

#### Distributed Arbitration
- In distributed arbitration, there is no single bus arbiter, but each device on the bus can participate in the arbitration process .
- The devices on the bus communicate with each other using a predefined protocol and agree on who gets the bus next .
- The advantages of distributed arbitration are fault tolerance, high performance, and scalability.
- The disadvantages of distributed arbitration are complexity, high cost, and difficult implementation.