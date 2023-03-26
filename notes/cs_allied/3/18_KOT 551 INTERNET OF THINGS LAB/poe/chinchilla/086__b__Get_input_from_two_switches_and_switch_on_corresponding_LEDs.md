#### b) Get input from two switches and switch on corresponding LEDs

In embedded systems, switches and LEDs are essential components for controlling the system's behavior. In this section, we will discuss how to get input from two switches and switch on corresponding LEDs.

To achieve this, we need to follow the below steps:

1. Connect two switches to the microcontroller, and connect two LEDs to the microcontroller's output pins.

2. Configure the input pins to which switches are connected as input pins. We can configure input pins as input using the microcontroller's GPIO registers.

3. Configure the output pins to which LEDs are connected as output pins. We can configure output pins as output using the microcontroller's GPIO registers.

4. In the main function, we can continuously monitor the state of the input pins using polling or interrupts.

5. If the state of any of the input pins changes, we can read the state of the input pins and switch on the corresponding LED by setting the output pin high.

6. If the state of any of the input pins remains the same, we can continue to monitor the state of the input pins.

7. We can use a delay between checking the input pins' state to avoid unnecessary CPU utilization.

8. Once the system is up and running, we can use the switches to control the corresponding LEDs.

In conclusion, getting input from two switches and switching on corresponding LEDs is a crucial aspect of embedded systems. By following the above steps, we can implement this functionality in our system.