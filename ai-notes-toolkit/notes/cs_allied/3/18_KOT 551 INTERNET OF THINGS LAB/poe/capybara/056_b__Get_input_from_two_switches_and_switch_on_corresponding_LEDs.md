## b) Get Input from Two Switches and Switch on Corresponding LEDs

Here are the steps to get input from two switches and switch on corresponding LEDs:

1. First, set up the hardware. Connect two switches to two different pins of the microcontroller and also connect two LEDs to two different pins of the microcontroller.

2. Define the pins to which the switches and LEDs are connected in the code.

3. Initialize the pins as input for switches and output for LEDs.

4. Set up an infinite loop to continuously read the state of the two switches.

5. Use the digitalRead() function to read the state of the switches. The digitalRead() function returns either HIGH or LOW depending on the state of the switch.

6. Use an if-else statement to check the state of the switches. If the first switch is pressed, turn on the first LED. If the second switch is pressed, turn on the second LED.

7. Use the digitalWrite() function to turn on the respective LED.

8. If none of the switches are pressed, turn off both LEDs.

9. Repeat the loop to continuously read the state of the switches and turn on/off the respective LEDs.

10. Finally, test the code by pressing the switches and see if the corresponding LEDs turn on/off.

By following these steps, you can easily get input from two switches and switch on corresponding LEDs using a microcontroller.