# Real Time System

A real time system is a system that can process and respond to events within a specified time limit. The system must meet the deadlines imposed by the environment, otherwise it may cause a system failure or undesirable consequences. A real time system is also able to synchronize its internal clocks with the external clocks of other systems or devices.

Some examples of real time systems are:

- Flight control systems: These systems control the flight of an aircraft by receiving inputs from sensors, processing them, and sending outputs to actuators. The system must react quickly and accurately to the changing conditions of the flight, such as speed, altitude, orientation, weather, etc.
- Industrial control systems: These systems monitor and control industrial processes, such as manufacturing, power generation, chemical processing, etc. The system must ensure the safety, efficiency, and quality of the process by regulating the parameters, such as temperature, pressure, flow, level, etc.
- Machine vision: These systems use cameras and image processing algorithms to analyze and interpret visual data, such as faces, objects, gestures, etc. The system must perform the tasks, such as recognition, identification, tracking, inspection, etc. in real time, with high accuracy and reliability.
- Robotics: These systems use sensors, actuators, and controllers to perform various tasks, such as navigation, manipulation, coordination, etc. The system must adapt to the dynamic and uncertain environment, and interact with other robots or humans in real time.

There are two types of real time systems based on the timing constraints:

- Hard real time systems: These systems have absolute deadlines, and missing a deadline can result in a catastrophic failure or severe damage. For example, a flight control system must respond to a stall warning within a few milliseconds, otherwise the aircraft may crash.
- Soft real time systems: These systems have relative deadlines, and missing a deadline can result in a degraded performance or reduced quality of service. For example, a video streaming system must deliver the frames within a certain delay, otherwise the video quality may suffer.