#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a simple way to control the GPIO pins using the command line.
- The steps to flash an LED based on cron output are:

  1. Connect the LED to the GPIO pin 17 and the resistor to the ground pin on the breadboard, using the jumper wires. Refer to the diagram below for the wiring.

  ```
  +3.3V  +5V
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |  +5V
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |  GND
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |  GPIO 17
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |  GND
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |  LED
  |      |  |  |  |  |