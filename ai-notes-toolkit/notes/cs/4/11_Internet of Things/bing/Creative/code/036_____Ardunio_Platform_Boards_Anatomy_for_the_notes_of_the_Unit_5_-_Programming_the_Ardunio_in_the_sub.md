### Arduino Platform Boards Anatomy

Arduino boards are the microcontroller development platform that will be at the heart of your projects. They sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators. When making something you will be building the circuits and interfaces for interaction, and telling the microcontroller how to interface with other components. Here are some of the main features of Arduino platform boards, using Arduino Uno as an example  :

- **Power jack**: This is where you can plug a power supply to power the board. The recommended voltage range is 7-12V, but the board can operate on 6-20V. The power jack has a polarity protection, so you won't damage the board if you plug it in the wrong way.
- **USB connector**: This is where you can connect the board to your computer using a USB cable. You can use the USB connection to upload sketches (programs) to the board, communicate with the board via serial monitor, and power the board. The USB connector also has a fuse to protect the board from overcurrent.
- **Voltage regulator**: This is a component that regulates the voltage supplied to the board from the power jack or the USB connector. It ensures that the board receives a stable 5V, which is the operating voltage of the microcontroller and most of the components on the board.
- **Reset button**: This is a button that you can press to reset the board. Resetting the board means restarting the sketch that is running on the board. You may need to reset the board when uploading a new sketch, or when the board is not working properly.
- **Microcontroller**: This is the brain of the board. It is a chip that contains a processor, memory, and input/output pins. The microcontroller on the Arduino Uno is the ATmega328P, which has 32 KB of flash memory (for storing sketches), 2 KB of SRAM (for storing variables), and 1 KB of EEPROM (for storing permanent data). The microcontroller can run at 16 MHz, which means it can execute 16 million instructions per second.
- **Crystal oscillator**: This is a component that provides a clock signal to the microcontroller. The clock signal is a periodic pulse that synchronizes the operations of the microcontroller. The crystal oscillator on the Arduino Uno has a frequency of 16 MHz, which matches the speed of the microcontroller.
- **ICSP header**: This is a set of pins that you can use to program the microcontroller using an external programmer, such as another Arduino board or a dedicated device. ICSP stands for In-Circuit Serial Programming, which means you can program the microcontroller without removing it from the board. You may need to use the ICSP header if you want to change the bootloader (the program that runs before the sketch) or use a different microcontroller on the board.
- **Digital pins**: These are pins that you can use to send and receive digital signals. Digital signals are either high (5V) or low (0V), and can represent binary data (0 or 1) or logic states (on or off). The Arduino Uno has 14 digital pins, numbered from 0 to 13. Some of the digital pins have special functions, such as PWM (Pulse Width Modulation), serial communication, and interrupt capabilities.
- **Analog pins**: These are pins that you can use to read analog signals. Analog signals are continuous signals that can have any value between 0V and 5V, and can represent physical quantities, such as temperature, light, sound, etc. The Arduino Uno has 6 analog pins, numbered from A0 to A5. The analog pins can also be used as digital pins, but they have different numbers, from 14 to 19.
- **Power pins**: These are pins that you can use to supply power to other components or circuits. The Arduino Uno has 4 power pins: 5V, 3.3V, GND, and VIN. The 5V and 3.3V pins provide regulated voltages from the board, while the GND pin provides a common ground for the circuits. The VIN pin provides the same voltage as the input power, either from the power jack or the USB connector.

Here is a diagram of the Arduino Uno board anatomy:

```
+----------------+  +----------------+
|                |  |                |
|                |  |                |
|                |  |                |
|                |  |                |
|

```
