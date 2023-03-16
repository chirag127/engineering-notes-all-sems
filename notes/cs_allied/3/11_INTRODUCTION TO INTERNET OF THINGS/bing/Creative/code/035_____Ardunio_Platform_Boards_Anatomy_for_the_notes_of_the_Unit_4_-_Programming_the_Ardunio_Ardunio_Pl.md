# Ardunio Platform Boards Anatomy

- Arduino boards are the microcontroller development platform that will be at the heart of your projects .
- Arduino boards sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators.
- Arduino boards can be programmed using the Arduino IDE, which is a cross-platform application that allows you to write code, compile it, and upload it to the board.
- Arduino boards can also use libraries, which are collections of code that provide additional functionality for specific sensors, displays, communication protocols, etc.
- Arduino boards can be used for IoT applications, which are devices that can connect to the internet and exchange data with other devices or services.
- Arduino Uno is one of the most popular and widely used Arduino boards. It has the following main components  :

  - Microcontroller: Think of it as a tiny computer, designed to execute only a specific number of things. It is the brain of the board and runs the code that you upload to it. The Arduino Uno uses the ATmega328P microcontroller, which has 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM.
  - USB port: Used to connect the board to the computer and upload the code. It also provides power to the board when connected to the computer or a USB charger.
  - USB to Serial chip: This is what makes it possible to program the Arduino board from your computer. It converts the USB signals to serial signals that the microcontroller can understand. The Arduino Uno uses the ATmega16U2 chip for this purpose.
  - Power jack: Used to power the board from an external source, such as a battery or a wall adapter. The board can accept voltages from 7 to 20 volts, but the recommended range is 7 to 12 volts.
  - Voltage regulator: Used to regulate the voltage from the power jack or the USB port to a stable 5 volts, which is the operating voltage of the microcontroller and most of the components on the board.
  - Reset button: Used to reset the microcontroller and restart the code. It can also be used to enter the bootloader mode, which is a special mode that allows the board to receive new code from the computer.
  - Digital pins: Commonly used for switches and LEDs, but can also be used for other purposes. They can be configured as inputs or outputs, and can read or write digital values of either HIGH (5 volts) or LOW (0 volts). The Arduino Uno has 14 digital pins, numbered from 0 to 13. Some of them have special functions, such as:

    - Pin 0 (RX) and Pin 1 (TX): Used for serial communication between the board and the computer or other devices. They are connected to the USB to Serial chip and can also be used as regular digital pins.
    - Pin 2 and Pin 3: Can be used for external interrupts, which are signals that can trigger the microcontroller to execute a specific function. They can also be used as regular digital pins.
    - Pin 3, Pin 5, Pin 6, Pin 9, Pin 10, and Pin 11: Can be used for PWM (Pulse Width Modulation), which is a technique that can vary the brightness of LEDs or the speed of motors by switching them on and off very fast. They can also be used as regular digital pins.
    - Pin 10, Pin 11, Pin 12, and Pin 13: Can be used for SPI (Serial Peripheral Interface), which is a communication protocol that can transfer data between the board and other devices, such as sensors, displays, or memory cards. They can also be used as regular digital pins.
    - Pin 13: Has a built-in LED that can be turned on and off by writing HIGH or LOW to the pin. It can also be used as a regular digital pin.

  - Analog pins: Used to read the signal from an analog sensor, such as a potentiometer, a light sensor, or a temperature sensor. They can convert the analog voltage (from 0 to 5 volts) to a digital value (from 0 to 1023) that can be read by the microcontroller. The Arduino Uno has 6 analog pins, numbered from A0 to A5. They can also be used as digital pins by referring to them as 14 to 19