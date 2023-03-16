# Real Time System

A real time system is a system that can perform its tasks within a specified time constraint, and can coordinate with other systems or devices that have different clocks or time frames. A real time system can be classified into two types based on the severity of missing the deadline: hard real time system and soft real time system.

## Hard Real Time System

A hard real time system is a system that has absolute deadlines, and any violation of the deadlines can result in a system failure or a catastrophic consequence. For example, a flight control system, a nuclear reactor control system, or a pacemaker are hard real time systems, because any delay in their responses can endanger human lives or cause severe damage.

## Soft Real Time System

A soft real time system is a system that has relative deadlines, and missing the deadlines occasionally can be tolerated with some acceptable degradation in performance or quality. For example, a video streaming system, a voice recognition system, or a web server are soft real time systems, because some delay or jitter in their responses can be acceptable without affecting the user experience significantly.

## Applications of Real Time Systems

Real time systems are widely used in various domains and industries, such as:

- Process control systems: These systems are used to monitor and control physical processes, such as chemical plants, power plants, oil refineries, etc. They use sensors and actuators to collect data and manipulate the process variables, and they require timely and accurate feedback to maintain the desired state of the system.
- Machine vision: These systems are used to help machines interpret visual data, such as images or videos, and perform tasks based on the information. They can be used for object detection, face recognition, gesture recognition, etc. They require fast and reliable processing of large amounts of data to enable the machines to interact with their environment.
- Robotics: These systems are used to design and operate machines that can perform tasks autonomously or semi-autonomously, such as industrial robots, service robots, or autonomous vehicles. They use sensors, actuators, and algorithms to perceive, plan, and execute actions, and they require real time coordination and communication with other systems or devices.