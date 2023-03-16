# Real Time System

A real time system is a system that can process and respond to inputs or events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to meet its deadlines, otherwise it may cause a system failure or undesirable consequences.

Some examples of real time systems are:

- Flight control systems that control the movement and stability of aircrafts
- Industrial control systems that monitor and regulate the production processes in factories
- Machine vision systems that help machines to recognize and analyze images or videos
- Robotics systems that enable robots to perform tasks such as navigation, manipulation, or coordination
- Medical imaging systems that process and display the images of internal organs or tissues

## Types of real time systems

Real time systems can be classified into two types based on their timing constraints:

- Hard real time systems: These systems have absolute deadlines that must be met without any exception. Missing a deadline can result in a catastrophic failure or a severe loss. For example, a flight control system must respond to the inputs from the pilot or the sensors within a few milliseconds, otherwise the aircraft may crash or deviate from its course.
- Soft real time systems: These systems have relative deadlines that can be missed occasionally with some acceptable probability. Missing a deadline may degrade the performance or the quality of the system, but not cause a fatal error. For example, a video streaming system may drop some frames or reduce the resolution if the network bandwidth is low, but it can still provide a satisfactory service to the user.

## Characteristics of real time systems

Real time systems have some common characteristics that distinguish them from other types of systems, such as:

- Time sensitivity: Real time systems must be able to sense, process, and act on the inputs or events within a predefined time limit. The time limit may vary depending on the application or the environment, but it is usually much shorter than the human perception of time. For example, a human may not notice a delay of a few seconds, but a real time system may need to respond within a few microseconds or nanoseconds.
- Time synchronization: Real time systems must be able to coordinate and communicate with other systems or devices that have independent clocks and operate in parallel. The systems or devices must agree on a common notion of time and adjust their clocks accordingly to avoid errors or inconsistencies. For example, a robotic system may need to synchronize its movements with other robots or sensors to achieve a coordinated task.
- Predictability: Real time systems must be able to guarantee that they can meet their deadlines under any possible scenario or condition. The systems must be designed and tested to ensure that they can handle the worst-case situations and avoid any unexpected behavior or failure. For example, a real time system must be able to cope with the variations in the input data, the system load, the hardware failures, or the external disturbances.