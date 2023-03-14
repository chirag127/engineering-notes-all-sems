## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue operating without interruption when one or more of its components fail. Fault-tolerant systems use backup components that automatically take the place of failed components, ensuring no loss of service. Fault tolerance can be achieved by using redundancy, which is the availability of multiple paths or components that can perform the same function.

The following diagram illustrates the basic architecture of a fault-tolerant system. It consists of four main components:

- A controller, which is responsible for managing the system and sending commands to the actuators.
- A set of actuators, which are devices that perform actions on the system, such as motors, valves, etc.
- A set of sensors, which are devices that measure the state of the system, such as temperature, pressure, etc.
- A fault-detection and isolation (FDI) module, which monitors the system and detects and isolates faults in the components.

The controller sends commands to the actuators based on the desired system behavior. The sensors measure the actual system behavior and send feedback to the controller and the FDI module. The FDI module compares the expected and actual system behavior and identifies any discrepancies that indicate a fault. If a fault is detected, the FDI module isolates the faulty component and sends a signal to the controller to reconfigure the system using the backup components.

The diagram is drawn using ASCII characters as follows:

```
    +-----------------+     +-----------------+
    |                 |     |                 |
    |    Controller   |---->|    Actuators    |
    |                 |     |                 |
    +-----------------+     +-----------------+
          ^   ^                     |
          |   |                     |
          |   +---------------------+
          |                         |
          |                         v
          |                   +-----------------+
          |                   |                 |
          +-------------------|     Sensors     |
          |                   |                 |
          |                   +-----------------+
          |                         |
          |                         |
          |                         v
          |                   +-----------------+
          |                   |                 |
          +-------------------|      FDI        |
                              |                 |
                              +-----------------+
                                    |
                                    |
                                    v
                              +-----------------+
                              |                 |
                              |   Reconfiguration   |
                              |                 |
                              +-----------------+
```