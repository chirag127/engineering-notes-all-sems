# Real Time System

A real time system is a system that can process and respond to events within a specific and predictable time frame. A real time system must meet its deadlines, otherwise it may cause a system failure or undesirable consequences. A real time system is often used to control or interact with an environment that changes dynamically and requires timely responses.

Some examples of real time systems are:

- Process control systems: These systems are used to monitor and regulate industrial processes, such as chemical plants, power plants, oil refineries, etc. They use sensors, actuators, and controllers to maintain the desired state of the system and prevent accidents or malfunctions.
- Machine vision: These systems are used to help machines interpret visual data, such as images, videos, or 3D scans. They can be used for various purposes, such as face recognition, object detection, quality inspection, navigation, etc. They require high-speed processing and low-latency communication to perform their tasks effectively.
- Robotics: These systems are used to control robots that can perform various actions, such as manipulation, locomotion, exploration, etc. They use sensors, motors, and algorithms to coordinate the movements and behaviors of the robots and adapt to the environment and the goals.
- Flight control: These systems are used to control the flight of aircraft, such as airplanes, helicopters, drones, etc. They use sensors, actuators, and computers to stabilize the flight, follow the flight plan, avoid collisions, and handle emergencies.

There are two types of real time systems based on their timing constraints:

- Hard real time system: This type of system has absolute deadlines, and if those deadlines are missed, the system will fail or cause severe damage. For example, a flight control system must respond to the pilot's commands or the sensor inputs within milliseconds, otherwise the aircraft may crash.
- Soft real time system: This type of system has relative deadlines, and if those deadlines are missed, the system will degrade its performance or quality of service, but not fail completely. For example, a video streaming system must deliver the video frames within a certain time, otherwise the video quality will be reduced or the frames will be skipped.

Some characteristics of real time systems are:

- Concurrency: A real time system may have multiple tasks or processes that run simultaneously and share resources, such as CPU, memory, or I/O devices. The system must manage the concurrency and ensure that the tasks are executed in the correct order and without conflicts or deadlocks.
- Scheduling: A real time system must allocate the CPU time to the tasks according to their priorities and deadlines. The system must use a scheduling algorithm that can guarantee the timeliness and fairness of the tasks and handle the dynamic changes in the system load and the task arrival.
- Synchronization: A real time system must synchronize the clocks and the events of the system components, such as the sensors, the actuators, and the controllers. The system must use a synchronization protocol that can ensure the accuracy and consistency of the system state and the data exchange.
- Reliability: A real time system must be able to handle faults and errors that may occur in the system components or the environment. The system must use fault-tolerance techniques that can detect, isolate, and recover from the faults and maintain the system functionality and safety.