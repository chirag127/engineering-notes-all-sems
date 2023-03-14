## Unit 5 - Programming the Arduino

The following diagram illustrates the basic architecture of a typical Arduino board and its connection to a computer and external components.

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |   Computer      |     |   Arduino       |     |   External      |
    |                 |     |   Board         |     |   Components    |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  Arduino IDE    |     |  Microcontroller|     |  LEDs, sensors, |
    |  or other tool  |     |  (e.g. ATmega)  |     |  actuators, etc.|
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  USB port       |<--->|  USB to Serial  |     |                 |
    |                 |     |  chip           |     |                 |
    +-----------------+     +-----------------+     +-----------------+
                            |                 |     |                 |
                            |  Digital pins   |<--->|  Digital inputs |
                            |                 |     |  and outputs    |
                            +-----------------+     +-----------------+
                            |                 |     |                 |
                            |  Analog pins    |<--->|  Analog inputs  |
                            |                 |     |                 |
                            +-----------------+     +-----------------+
                            |                 |     |                 |
                            |  5V / 3.3V pins |<--->|  Power supply   |
                            |                 |     |                 |
                            +-----------------+     +-----------------+
```

The Arduino board is programmed using the Arduino IDE or other software tools that can communicate with the board via the USB port. The USB port is connected to a USB to Serial chip that translates the data from the computer to the microcontroller. The microcontroller is the brain of the Arduino board and executes the code that is loaded into it. The code can control the digital and analog pins of the board, which can be used to interface with external components such as LEDs, sensors, actuators, etc. The board can also provide 5V or 3.3V power to the external components via the dedicated pins.