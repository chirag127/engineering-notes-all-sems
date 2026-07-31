### Bus Arbitration

Bus arbitration is the process by which the current bus master accesses and then releases the control of the bus and passes it to the next device that requires it. This is necessary in a computer system where multiple devices may need to access the bus at the same time.

There are several methods of bus arbitration, including:

1. **Centralized arbitration**: A single device, usually the processor, acts as the arbiter and determines which device gets access to the bus.
2. **Distributed arbitration**: Each device on the bus has its own arbitration logic and can request access to the bus. The devices communicate with each other to determine which device gets access to the bus.
3. **Daisy chain arbitration**: Devices are connected in a daisy chain and the device at the end of the chain has the highest priority. When a device wants to access the bus, it sends a request to the device next to it in the chain. If that device is not using the bus, it passes the request along the chain until it reaches the device with the highest priority. That device then grants access to the bus.

Bus arbitration is an important concept in computer organization and architecture as it ensures that multiple devices can access the bus in an orderly and efficient manner. It is covered in Unit 1 - Introduction of the subject of Computer Organization and Architecture.