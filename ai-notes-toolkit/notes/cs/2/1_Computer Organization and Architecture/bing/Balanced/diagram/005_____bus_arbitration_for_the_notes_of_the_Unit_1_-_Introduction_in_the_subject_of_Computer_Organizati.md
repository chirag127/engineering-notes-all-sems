### Bus Arbitration

- Bus arbitration is the process by which the current bus master accesses and then leaves the control of the bus and passes it to another bus requesting processor unit    .
- A bus master is a controller that can access the bus for a given instance.
- Bus arbitration is necessary to avoid conflicts and ensure proper communication among the devices connected to the bus.
- There are two types of bus arbitration: centralized and distributed.

#### Centralized Arbitration

- In centralized arbitration, there is a single bus arbiter that decides which device gets the bus access.
- The bus arbiter can be a part of the processor, the memory controller, or a separate device.
- The devices that want to access the bus send their requests to the bus arbiter, which grants the bus access to one of them based on some priority scheme.
- The advantages of centralized arbitration are simplicity, low cost, and easy implementation.
- The disadvantages of centralized arbitration are single point of failure, bottleneck, and limited scalability.

#### Distributed Arbitration

- In distributed arbitration, there is no central bus arbiter, and the devices communicate with each other to decide which one gets the bus access.
- The devices that want to access the bus send their requests to the bus using some protocol, such as daisy chaining, polling, or token passing.
- The advantages of distributed arbitration are fault tolerance, high performance, and high scalability.
- The disadvantages of distributed arbitration are complexity, high cost, and difficult implementation.