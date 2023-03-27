#### b) Get input from two switches and switch on corresponding LEDs

In embedded systems, switches are used to take input from the user. Once the switch is pressed, it produces a signal that can be used to control the operation of the system. Similarly, LEDs are used to give feedback to the user. They are used to indicate the state of the system, such as whether the system is on or off.

In this section, we will discuss how to get input from two switches and switch on corresponding LEDs.

Here are the steps involved:

1. Connect the switches to the input pins of the microcontroller. The switches can be connected in series or parallel, depending on the requirement.

2. Connect the LEDs to the output pins of the microcontroller. The LEDs can be connected in series or parallel, depending on the requirement.

3. Write the code to read the input from the switches. This can be done using a digitalRead() function in Arduino or a GPIO read function in other microcontrollers.

4. Write the code to switch on the corresponding LEDs based on the input from the switches. This can be done using a digitalWrite() function in Arduino or a GPIO write function in other microcontrollers.

5. Test the system to ensure that it is working correctly. Press the switches and observe the corresponding LEDs to ensure that they switch on and off correctly.

6. If necessary, add debouncing to the switches to ensure that the system is not affected by noise or other disturbances.

In summary, getting input from switches and switching on corresponding LEDs is a basic operation in embedded systems. By following the above steps, you can easily implement this functionality in your system.