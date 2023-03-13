An actuator is a device that converts energy into motion. It does this by taking an electrical signal and combining it with an energy source. In an IoT system, the actuator can act on data collected by sensors to create an outcome as determined by the user.

There are different types of actuators for IoT, such as:

- Servo Motors: A servomotor is a rotary actuator or linear actuator that allows for precise control of angular or linear position, velocity and acceleration. Servo motors are commonly used in robotics, automation, and CNC machines.
- Stepper Motors: Stepper motors are DC motors that move in discrete steps. They have a fixed number of poles, or electromagnets, around a central gear-shaped piece of iron. Stepper motors are used for applications that require high torque, low speed, and accurate positioning, such as 3D printers, scanners, and cameras.
- DC Motors (Continuous Rotation Motors): DC motors are two wire (power & ground), continuous rotation motors. They can vary their speed and direction by changing the polarity and voltage of the power supply. DC motors are used for applications that require high speed, low torque, and simple control, such as fans, toys, and pumps.
- Linear Actuators: Linear actuators are devices that produce linear motion by converting electrical, hydraulic, or pneumatic energy. They can push or pull a load along a straight line. Linear actuators are used for applications that require linear movement, such as valves, doors, lifts, and switches.
- Thermal/Magnetic Actuators: These are actuated by thermal or mechanical energy. Shape Memory Alloys (SMAs) or Magnetic Shape Memory Alloys (MSMAs) are materials that can change their shape when heated or exposed to a magnetic field. They can be used for applications that require small, fast, and precise movements, such as microvalves, microswitches, and micropumps.
- Mechanical Actuators: A mechanical actuator executes movement by converting rotary motion into linear motion. It consists of a screw, a nut, and a rod. The screw rotates inside the nut, which moves the rod along its axis. Mechanical actuators are used for applications that require high force, long stroke, and low speed, such as jacks, presses, and clamps.
- Soft Actuators: Soft actuators are made of flexible materials that can deform and change shape when stimulated by electricity, light, heat, or chemicals. They can mimic the movements of natural muscles and organs. Soft actuators are used for applications that require soft, adaptive, and biocompatible interfaces, such as artificial muscles, soft robots, and wearable devices.

The following diagram illustrates the basic architecture of an IoT system with actuators:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|     Sensors     |----->|     Gateway     |----->|     Cloud       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
                                                 /|\
                                                  |
                                                  |
                                                  |
+-----------------+      +-----------------+      | +-----------------+
|                 |      |                 |      | |                 |
|    Actuators    |<-----|     Gateway     |<-----+-|     Cloud       |
|                 |      |                 |        |                 |
+-----------------+      +-----------------+        +-----------------+
```

The sensors collect data from the physical environment and send it to the gateway. The gateway aggregates and preprocesses the data and sends it to the cloud. The cloud performs data analysis and decision making and sends commands to the gateway. The gateway forwards the commands to the actuators. The actuators execute the commands and produce physical actions in the environment.