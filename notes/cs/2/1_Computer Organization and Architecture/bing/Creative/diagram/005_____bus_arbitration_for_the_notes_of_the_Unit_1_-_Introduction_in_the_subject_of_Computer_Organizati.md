### Bus Arbitration

- Bus arbitration is the process of deciding which device or processor can access the shared bus at a given time  .
- The device or processor that has the control of the bus is called the bus master  .
- The bus master can initiate data transfers on the bus and communicate with other devices or processors  .
- Bus arbitration is necessary to avoid conflicts and ensure correct data transfer on the bus  .
- There are two main types of bus arbitration: centralized and distributed.
  - Centralized arbitration: A single device, usually a bus controller or arbiter, decides which device or processor can become the bus master based on a fixed priority or a rotating scheme.
  - Distributed arbitration: Each device or processor on the bus can contend for the bus mastership by sending signals or messages on the bus, following a predefined protocol or algorithm.
- Bus arbitration can affect the performance, efficiency and fairness of the bus system.
  - Performance: The bus arbitration scheme should minimize the delay and overhead of granting the bus mastership to a device or processor.
  - Efficiency: The bus arbitration scheme should maximize the utilization and throughput of the bus.
  - Fairness: The bus arbitration scheme should avoid starvation and ensure equal opportunity for all devices or processors to access the bus.