#### b) Get input from two switches and switch on corresponding LEDs

When working with microcontrollers, it is often necessary to read input from external devices and use that input to control other devices. One common example of this is reading input from switches and using that input to control LEDs.

Here are the steps required to get input from two switches and switch on corresponding LEDs:

1. Connect the switches to the microcontroller. This can be done by connecting one side of each switch to a digital input pin on the microcontroller and the other side of each switch to ground.

2. Configure the digital input pins as inputs. This can be done by setting the corresponding bits in the data direction register to 0.

3. Read the state of the switches. This can be done by reading the values of the digital input pins. If a switch is closed, the corresponding pin will read 0. If a switch is open, the corresponding pin will read 1.

4. Determine which LEDs correspond to each switch. This will depend on the specific wiring of the circuit.

5. Connect the LEDs to the microcontroller. This can be done by connecting the anode of each LED to a digital output pin on the microcontroller and the cathode of each LED to ground.

6. Configure the digital output pins as outputs. This can be done by setting the corresponding bits in the data direction register to 1.

7. Turn on the corresponding LED based on the state of the switch. If a switch is closed, the corresponding LED should be turned on by setting the corresponding digital output pin to 1. If a switch is open, the corresponding LED should be turned off by setting the corresponding digital output pin to 0.

By following these steps, it is possible to read input from switches and use that input to control LEDs. This can be a useful skill when building projects with microcontrollers.