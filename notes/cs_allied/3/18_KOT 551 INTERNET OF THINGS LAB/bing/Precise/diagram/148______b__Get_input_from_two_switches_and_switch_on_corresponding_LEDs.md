#### b) Get input from two switches and switch on corresponding LEDs

To get input from two switches and switch on corresponding LEDs, the following steps can be followed:

1. Connect the two switches to the input pins of the microcontroller. The input pins should be configured as digital inputs.
2. Connect the two LEDs to the output pins of the microcontroller. The output pins should be configured as digital outputs.
3. In the program, read the state of the switches using the digitalRead() function.
4. If the state of the first switch is HIGH, turn on the first LED by setting the corresponding output pin to HIGH using the digitalWrite() function.
5. If the state of the second switch is HIGH, turn on the second LED by setting the corresponding output pin to HIGH using the digitalWrite() function.
6. If the state of the first switch is LOW, turn off the first LED by setting the corresponding output pin to LOW using the digitalWrite() function.
7. If the state of the second switch is LOW, turn off the second LED by setting the corresponding output pin to LOW using the digitalWrite() function.

This process can be repeated in a loop to continuously read the state of the switches and control the LEDs accordingly.