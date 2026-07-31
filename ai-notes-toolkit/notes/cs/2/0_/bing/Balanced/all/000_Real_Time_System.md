# Real Time System

A real time system is an information processing system that can respond to events within predictable and specific time constraints. The system must produce the expected result within a defined deadline, otherwise it may cause a system failure or undesirable consequences. A real time system also needs to coordinate independent clocks and operate together in unison (time synchronization).

Some examples of real time systems are:

- Process control systems: These systems are used in industrial applications where production is continuous and requires precise and timely control of physical processes, such as chemical plants, power plants, oil refineries, etc. 
- Machine vision: These systems are used to help machines rapidly interpret data so they can see their surroundings and perform tasks, such as object recognition, face detection, barcode scanning, etc. 
- Robotics: These systems are used to control the movements and actions of robots, such as industrial robots, autonomous vehicles, drones, etc. Robotics systems need to sense the environment, plan the actions, and execute them in real time. 
- Flight control systems: These systems are used to control the flight of aircraft, such as airplanes, helicopters, rockets, etc. Flight control systems need to monitor the sensors, adjust the actuators, and maintain the stability and safety of the flight. 

There are two types of real time systems based on the timing constraints:

- Hard real time systems: These systems have absolute deadlines, and if those deadlines are missed, a system failure or a catastrophic event will occur. For example, a flight control system must respond to the pilot's commands within milliseconds, otherwise the aircraft may crash. 
- Soft real time systems: These systems have relative deadlines, and if those deadlines are missed, the system performance or quality of service will degrade, but not fail. For example, a video streaming system must deliver the frames within a certain time, otherwise the video quality will be poor, but not stop. 

Some characteristics of real time systems are:

- Concurrency: A real time system may have multiple tasks or processes running at the same time, and they need to be coordinated and synchronized to avoid conflicts and ensure correctness.
- Determinism: A real time system must behave predictably and consistently, and produce the same output for the same input and state, regardless of the external factors or disturbances.
- Reliability: A real time system must be able to handle errors and faults, and recover from them quickly and gracefully, without compromising the system functionality or safety.
- Efficiency: A real time system must be able to utilize the available resources, such as CPU, memory, disk, network, etc., optimally and effectively, and avoid wastage or overload.