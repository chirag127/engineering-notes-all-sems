#### b) Get input from two switches and switch on corresponding LEDs

To get input from two switches and switch on corresponding LEDs, you can follow these steps:

1. Connect the two switches to the input pins of the microcontroller. Make sure to use the appropriate pull-up or pull-down resistors to ensure a stable input signal.
2. Connect the two LEDs to the output pins of the microcontroller. Make sure to use current-limiting resistors to protect the LEDs from excessive current.
3. In the program, configure the input pins as digital inputs and the output pins as digital outputs.
4. Continuously read the state of the input pins using the appropriate digital input function.
5. If the state of an input pin is high, set the corresponding output pin to high using the appropriate digital output function. This will turn on the corresponding LED.
6. If the state of an input pin is low, set the corresponding output pin to low using the appropriate digital output function. This will turn off the corresponding LED.

By following these steps, you can get input from two switches and switch on the corresponding LEDs. This can be useful in various applications, such as creating a simple user interface or controlling the state of external devices.