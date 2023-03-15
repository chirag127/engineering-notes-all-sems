# Bus Arbitration

- Bus arbitration is the process by which the current bus master accesses and then leaves the control of the bus and passes it to another bus requesting processor unit    .
- A bus master is a controller that can access the bus for a given instance.
- Bus arbitration is necessary to avoid conflicts and ensure proper communication among the devices connected to the bus.
- There are two types of bus arbitration: centralized arbitration and distributed arbitration.

## Centralized Arbitration

- In centralized arbitration, there is a single bus arbiter that decides which device gets the bus access.
- The bus arbiter can be a part of the processor, the memory controller, or a separate chip.
- The devices send their bus requests to the bus arbiter, which grants the bus access to one of them based on some priority scheme.
- The advantages of centralized arbitration are simplicity and efficiency.
- The disadvantages of centralized arbitration are single point of failure, bottleneck, and scalability issues.

## Distributed Arbitration

- In distributed arbitration, there is no central bus arbiter, and the devices communicate with each other to decide which device gets the bus access.
- The devices use a common bus line or a set of bus lines to send and receive signals indicating their bus requests and grants.
- The devices follow some protocol or algorithm to resolve conflicts and determine the bus access order.
- The advantages of distributed arbitration are fault tolerance, parallelism, and scalability.
- The disadvantages of distributed arbitration are complexity and overhead.