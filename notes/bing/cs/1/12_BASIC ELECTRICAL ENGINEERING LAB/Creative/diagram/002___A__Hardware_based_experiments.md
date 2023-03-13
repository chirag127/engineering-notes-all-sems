Hardware based experiments are experiments that depend on physical components and devices for their operation and testing. Hardware based experiments can be used for various purposes, such as teaching, learning, research, innovation, and problem-solving. Hardware based experiments can involve different types of components, such as sensors, actuators, buses, microcontrollers, integrated circuits, and more.

#### (A) Hardware based experiments

The following diagram illustrates the basic architecture of a hardware based experiment:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Controller   |<---->|   Interface    |<---->|   Hardware     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Software      |      |  Hardware      |      |  Sensors       |
|  (MATLAB,      |      |  (Arduino,     |      |  (Temperature, |
|  Simulink,     |      |  Raspberry Pi, |      |  Humidity,     |
|  etc.)         |      |  etc.)         |      |  etc.)         |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Logic,        |      |  Communication |      |  Measurement   |
|  Control,      |      |  (Serial,      |      |  (Analog,      |
|  Analysis,     |      |  Bluetooth,    |      |  Digital,      |
|  Visualization |      |  Wi-Fi, etc.)  |      |  etc.)         |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The controller is the software component that provides the logic, control, analysis, and visualization of the experiment. The controller can be programmed using various tools, such as MATLAB, Simulink, Python, etc.

The interface is the hardware component that provides the communication between the controller and the hardware. The interface can be implemented using various devices, such as Arduino, Raspberry Pi, etc. The interface can use different protocols, such as serial, Bluetooth, Wi-Fi, etc.

The hardware is the physical component that provides the measurement and actuation of the experiment. The hardware can consist of various sensors, such as temperature, humidity, light, etc. The hardware can also consist of various actuators, such as motors, valves, LEDs, etc.