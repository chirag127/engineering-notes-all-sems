# Real Time System

A real time system is a system that can process and respond to events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to handle concurrent and unpredictable events and guarantee the correctness and timeliness of its outputs. A real time system can be classified into two types based on the consequences of missing the deadlines:

- **Hard real time system**: A system that must meet all the deadlines, otherwise it will cause a catastrophic failure or unacceptable loss. For example, a flight control system, a nuclear reactor control system, or a pacemaker.
- **Soft real time system**: A system that can tolerate some deadline misses, but the quality of service or performance will degrade. For example, a video streaming system, a voice recognition system, or a web server.

Some of the characteristics of a real time system are:

- **Determinism**: The system must produce the same output for the same input and initial state, regardless of the timing of events or the execution order of tasks.
- **Responsiveness**: The system must react to events as soon as they occur and complete the required actions within the deadlines.
- **Predictability**: The system must be able to estimate the worst-case execution time and resource usage of each task and ensure that they are feasible and schedulable.
- **Reliability**: The system must be able to handle faults and errors and recover from them without compromising the safety or functionality of the system.
- **Time synchronization**: The system must be able to coordinate the actions of different components or devices that have independent clocks and operate in parallel.

Some of the applications of real time systems are:

- **Process control systems**: These systems are used to monitor and control physical processes such as temperature, pressure, flow, level, etc. in industrial plants, power plants, chemical plants, etc. They use sensors, actuators, controllers, and communication networks to achieve the desired output.
- **Machine vision systems**: These systems are used to help machines interpret visual data such as images, videos, or 3D models and perform tasks such as object recognition, face detection, gesture recognition, etc. They use cameras, processors, algorithms, and display devices to process the data and provide feedback or commands to the machines.
- **Robotics systems**: These systems are used to create machines that can perform tasks that are difficult, dangerous, or repetitive for humans, such as manufacturing, assembly, exploration, surgery, etc. They use sensors, motors, controllers, and communication networks to perceive the environment, plan the actions, and execute the movements.
- **Medical imaging systems**: These systems are used to capture, process, and display images of the internal structures or functions of the human body, such as X-rays, MRI, ultrasound, etc. They use scanners, processors, algorithms, and display devices to provide diagnosis or treatment to the patients.
- **Video wall systems**: These systems are used to create large-scale displays that consist of multiple screens or projectors that show synchronized images or videos. They use processors, communication networks, and display devices to provide entertainment or information to the viewers.