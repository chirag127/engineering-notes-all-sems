#### b) Get input from two switches and switch on corresponding LEDs

In this section, we will learn how to get input from two switches and switch on corresponding LEDs. This is a fundamental concept in digital electronics and is commonly used in various applications. The following points will guide you through the process:

1. Firstly, we need to connect the switches and LEDs to the microcontroller. Use jumper wires to connect the switches to any two input pins of the microcontroller, and the LEDs to any two output pins of the microcontroller.

2. Set the input pins as inputs by configuring them as digital inputs in the code. Set the output pins as outputs by configuring them as digital outputs in the code.

3. In the main loop of the code, we need to continuously read the input pins to check if the switches are pressed or not. If a switch is pressed, the corresponding input pin will read a logic level of 1, and if it is not pressed, it will read a logic level of 0.

4. Once we have detected that a switch is pressed, we need to switch on the corresponding LED. To do this, set the output pin of the corresponding LED to a logic level of 1. If the switch is released, set the output pin of the LED to a logic level of 0 to turn it off.

5. Repeat the process for the other switch and LED.

6. It is essential to have a delay between each loop iteration to prevent the microcontroller from executing the loop too quickly. This can be achieved by using the delay function in the code.

7. Test the circuit by pressing each switch and observing the corresponding LED turning on and off.

In conclusion, getting input from two switches and switching on corresponding LEDs is a fundamental concept in digital electronics. By following these steps, you can easily implement this concept in your projects.