# Arduino Platform Boards Anatomy

Arduino boards are the microcontroller development platform that will be at the heart of your projects. When making something you will be building the circuits and interfaces for interaction, and telling the microcontroller how to interface with other components.

The most common Arduino board is the Arduino UNO, which is based on the ATmega328P microcontroller. It has the following features :

- 14 digital input/output pins (of which 6 can be used as PWM outputs)
- 6 analog inputs
- A 16 MHz ceramic resonator
- A USB connection
- A power jack
- An ICSP header
- A reset button

The anatomy of the Arduino UNO board can be seen in the following diagram:

![Arduino UNO Board Anatomy](https://www.arduino.cc/en/uploads/Guide/BoardAnatomy.png)

The main parts of the Arduino UNO board are:

- **Power LED indicator**: This LED lights up when the board is powered on.
- **Digital pins**: These pins can be used as input or output, and can also provide PWM signals for controlling motors, LEDs, etc.
- **TX and RX LEDs**: These LEDs indicate the serial communication activity between the board and the computer or other devices.
- **Main IC**: This is the ATmega328P microcontroller that runs the Arduino code.
- **Voltage regulator**: This regulates the voltage from the external power source or the USB port to the 5V required by the board.
- **DC power barrel jack**: This allows the board to be powered by an external power source, such as a battery or an adapter.
- **USB connector**: This allows the board to be connected to the computer for programming and serial communication, and also provides power to the board.
- **Reset button**: This resets the microcontroller and restarts the Arduino code.
- **Analog pins**: These pins can read analog signals from sensors, such as temperature, light, sound, etc.
- **AREF**: This stands for Analog Reference, and is used to set the reference voltage for the analog inputs.
- **ICSP header**: This stands for In-Circuit Serial Programming, and is used to program the microcontroller directly with an external programmer.
- **Power pins**: These pins provide 3.3V, 5V, and ground (GND) voltages to the board and the external components.