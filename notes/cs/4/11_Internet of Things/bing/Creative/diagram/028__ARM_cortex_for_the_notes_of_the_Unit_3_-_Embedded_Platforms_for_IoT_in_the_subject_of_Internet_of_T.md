The following diagram illustrates the basic architecture of an ARM cortex processor:

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Instruction    |  |  Data           |  |  System         |
|  Bus Interface  |  |  Bus Interface  |  |  Bus Interface  |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         v                    v                    v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Instruction    |  |  Data           |  |  System         |
|  Cache          |  |  Cache          |  |  Control        |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         +--------------------+--------------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         v                    v                    v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Instruction    |  |  Data           |  |  System         |
|  Decode         |  |  Load/Store     |  |  Registers      |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         +--------------------+--------------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         v                    v                    v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Instruction    |  |  Data           |  |  System         |
|  Execute        |  |  Execute        |  |  Control        |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
```

The ARM cortex architecture consists of three main components: the instruction bus interface, the data bus interface, and the system bus interface. These interfaces connect the processor to the external memory and peripherals. Each interface has its own cache, which stores frequently accessed data and instructions. The instruction cache feeds the instruction decode unit, which decodes the instructions and sends them to the instruction execute unit. The data cache feeds the load/store unit, which performs memory operations and sends them to the data execute unit. The system control unit manages the system registers, which store the processor state and configuration. The system control unit also handles exceptions, interrupts, and debug events. The instruction execute unit and the data execute unit work in parallel, performing arithmetic, logical, and bit manipulation operations on the data and instructions. The system control unit coordinates the execution of the instructions and data, and ensures the correct operation of the processor.