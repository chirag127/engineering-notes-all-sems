# Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- A switch is a device that can open or close a circuit, allowing current to flow or stop. A LED (light-emitting diode) is a device that emits light when current passes through it.
- We can use the digital pins of the Arduino to read the state of the switches (HIGH or LOW) and to control the state of the LEDs (ON or OFF).
- We need to use resistors to limit the current flowing through the LEDs and to prevent them from burning out. We also need to use pull-down resistors to ensure that the switches have a defined state when they are not pressed.
- The circuit diagram for this project is shown below:

```
+5V
 |
 |    10k
 |---/\/\/\---+---/\/\/\---+---/\/\/\---+---/\/\/\---+
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 +            +            +            +            +
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |            |            |
 |            |            |

```
