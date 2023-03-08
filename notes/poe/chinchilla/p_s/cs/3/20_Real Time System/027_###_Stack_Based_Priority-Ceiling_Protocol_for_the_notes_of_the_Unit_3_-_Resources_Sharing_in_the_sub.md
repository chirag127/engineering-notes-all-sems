### Stack Based Priority-Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

The Stack Based Priority-Ceiling Protocol (SBPCP) is a synchronization protocol used in Real Time Systems (RTS) for resource sharing. It prevents priority inversion and ensures that a higher priority task is not blocked by a lower priority task holding onto a shared resource.

#### How it works:
1. Each resource is assigned a priority ceiling value, which is the highest priority of any task that can access that resource.
2. When a task requests a resource, its priority is temporarily raised to the ceiling value of the resource it is requesting.
3. If a higher priority task attempts to access the same resource, it is blocked until the lower priority task releases the resource.
4. Once the task has finished using the resource, its priority is lowered back to its original value.

#### Advantages:
- SBPCP prevents priority inversion, which can cause delays or missed deadlines in RTS.
- It is an efficient and easy-to-implement protocol.
- It ensures that higher priority tasks have access to shared resources when they need them.

#### Disadvantages:
- SBPCP can result in priority inheritance, where a lower priority task inherits the priority of a higher priority task that is blocked on a shared resource. This can cause priority inversion in other parts of the system.
- It does not guarantee deadlock-free behavior.

#### Example:
Consider a system with three tasks: T1, T2, and T3. T1 has the highest priority, T2 has medium priority, and T3 has the lowest priority. T2 and T3 both require access to a shared resource with a priority ceiling value of T2's priority. When T2 requests the resource, its priority is raised to the ceiling value (medium). If T3 tries to access the resource while T2 is using it, it will be blocked until T2 releases the resource.

#### Applications:
SBPCP is commonly used in RTS for resource sharing. It can be applied to any system where shared resources are used and priority inversion must be prevented. It is especially useful in systems where missed deadlines can have serious consequences, such as in avionics or medical devices.

Overall, SBPCP is a useful and effective protocol for preventing priority inversion and ensuring that higher priority tasks have access to shared resources when they need them.