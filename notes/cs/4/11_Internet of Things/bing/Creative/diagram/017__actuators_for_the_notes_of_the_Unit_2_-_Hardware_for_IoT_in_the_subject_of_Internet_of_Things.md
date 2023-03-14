An actuator is a device that converts energy into motion. It does this by taking an electrical signal and combining it with an energy source. In an IoT system, the actuator can act on data collected by sensors to create an outcome as determined by the chosen settings of the user.

There are different types of actuators for IoT, such as:

- Servo Motors: A servomotor is a rotary actuator or linear actuator that allows for precise control of angular or linear position, velocity and acceleration.
- Stepper Motors: Stepper motors are DC motors that move in discrete steps. They are used for applications that require high precision and low speed.
- DC Motors (Continuous Rotation Motors): DC (Direct Current) Motors are two wire (power & ground), continuous rotation motors. They are used for applications that require high speed and low torque.
- Linear actuator: A linear actuator is a device that converts rotational motion into linear motion. They are used for applications that require linear movement, such as opening and closing doors, valves, etc.

The following diagram illustrates the basic architecture of an IoT system with actuators:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Sensors     |     |    Controller   |     |    Actuators    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Detect events  |     |  Process data   |     |  Perform actions|
|  in the physical|     |  from sensors   |     |  based on data  |
|  environment    |     |  and user input |     |  and user input |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +---------------------->                      |
       |                      |                      |
       |                      +--------------------->|
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |