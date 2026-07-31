# Real Time System

A real time system is a system that can process and respond to events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to handle concurrent and unpredictable events and guarantee the correctness and timeliness of its outputs. 

Some examples of real time systems are:

- Flight control systems that monitor and adjust the position and speed of an aircraft
- Process control systems that regulate the temperature, pressure, and flow of fluids in industrial plants
- Machine vision systems that analyze images and guide robots or vehicles
- Medical imaging systems that capture and process images of internal organs or tissues
- Video wall systems that display and synchronize multiple video streams

There are two main types of real time systems based on the severity of the consequences of missing a deadline:

- Hard real time systems: These systems have absolute deadlines that must be met at all costs. A missed deadline can result in a catastrophic failure or a loss of life. For example, a flight control system must respond to a pilot's input or a sensor's reading within milliseconds, otherwise the aircraft may crash.
- Soft real time systems: These systems have relative deadlines that can be occasionally missed without causing a major damage. A missed deadline can result in a degraded performance or a lower quality of service. For example, a video wall system must display and synchronize video frames within a certain interval, otherwise the viewers may notice a delay or a glitch.

Real time systems are often deployed at the edge of a network, where they can interact with the physical world and process data locally. This reduces the latency and bandwidth requirements of sending data to a central server or a cloud. However, real time systems at the edge also face challenges such as limited resources, security threats, and environmental conditions. Therefore, real time systems require specialized hardware and software components that can meet the performance, reliability, and safety requirements of the application domain.