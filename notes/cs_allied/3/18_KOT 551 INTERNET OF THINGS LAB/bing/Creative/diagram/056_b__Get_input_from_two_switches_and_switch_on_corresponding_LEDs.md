Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use to learn and read from for exams.

# Get input from two switches and switch on corresponding LEDs

- The objective of this topic is to learn how to use two switches as inputs and control two LEDs as outputs using a microcontroller.
- A switch is a device that can open or close an electrical circuit. A switch can be used to send a signal to the microcontroller when it is pressed or released.
- An LED (light-emitting diode) is a device that emits light when an electric current passes through it. An LED can be used to indicate the state of the microcontroller or the switch.
- A microcontroller is a small computer that can be programmed to perform various tasks. A microcontroller has input and output pins that can be connected to switches, LEDs, and other devices.
- To get input from two switches and switch on corresponding LEDs, we need to do the following steps:

  - Connect the switches and the LEDs to the microcontroller pins using wires and resistors. The switches should be connected to the input pins and the LEDs to the output pins. The resistors are used to limit the current and protect the devices from damage.
  - Write a program for the microcontroller that reads the state of the switches and controls the state of the LEDs. The program should use a loop to continuously check the input pins and turn on or off the output pins accordingly.
  - Upload the program to the microcontroller and test the circuit. The LEDs should light up when the corresponding switches are pressed and turn off when they are released.

- Here is a diagram that shows the circuit and the program for this topic:

```markdown
+-----------------+         +-----------------+
|                 |         |                 |
|  Microcontroller|         |  Program        |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Input pins     |         |  Loop           |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Output pins    |         |  If switch 1 is |
|                 |         |  pressed, turn  |
+-----------------+         |  on LED 1       |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Power supply   |         |  If switch 2 is |
|                 |         |  pressed, turn  |
+-----------------+         |  on LED 2       |
|                 |         |                 |
+-----------------+         +-----------------+

+-----------------+         +-----------------+
|                 |         |                 |
|  Switch 1       |---------|  Input pin 1    |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Switch 2       |---------|  Input pin 2    |
|                 |         |                 |
+-----------------+         +-----------------+

+-----------------+         +-----------------+
|                 |         |                 |
|  LED 1          |---------|  Output pin 1   |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  LED 2          |---------|  Output pin 2   |
|                 |         |                 |
+-----------------+         +-----------------+

+-----------------+         +-----------------+
|                 |         |                 |
|  Resistor 1     |---------|  LED 1          |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Resistor 2     |---------|  LED 2          |
|                 |         |                 |
+-----------------+         +-----------------+

+-----------------+         +-----------------+
|                 |         |                 |
|  Ground         |---------|  Switch 1       |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Ground         |---------|  Switch 2       |
|                 |         |                 |
+-----------------+         +-----------------+

+-----------------+         +-----------------+
|                 |         |                 |
|  Ground         |---------|  Resistor 1     |
|                 |         |                 |
+-----------------+         +-----------------+
|                 |         |                 |
|  Ground         |---------|  Resistor 2     |
|                 |         |                 |
+

```
