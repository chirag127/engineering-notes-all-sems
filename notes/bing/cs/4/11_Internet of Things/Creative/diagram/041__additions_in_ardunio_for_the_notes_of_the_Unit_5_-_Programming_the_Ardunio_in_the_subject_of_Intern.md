The following is a detailed ASCII diagram for additions in Arduino for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things.

The diagram shows how an Arduino Uno board can be connected to a Bluetooth module (HC-06) and a temperature sensor (LM35) to send and receive data over the Internet. The Arduino Uno board has digital and PWM pins that can be controlled by text commands from a smartphone or a PC. The temperature sensor can measure the ambient temperature and send it to the Arduino board, which can then transmit it to the smartphone or the PC over Bluetooth serial. The smartphone or the PC can also send commands to the Arduino board to turn on or off an LED connected to a digital pin.

The diagram uses the following symbols:

- `+` and `-` for power and ground connections
- `~` for PWM pins
- `D` for digital pins
- `A` for analog pins
- `TX` and `RX` for serial communication pins
- `[]` for components
- `()` for labels
- `--` for wires
- `||` for resistors
- `>` for LEDs
- `*` for temperature sensor

The diagram is as follows:

```
    +5V  +----------------+  GND
    +----|VCC          GND|----+
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
    +----|RX           TX |----+
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    +----------------+    |
    |    [   HC-06    ]        |
    |    (Bluetooth module)    |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    +--------------------------+
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    +5V  +----------------+  GND
    +----|5V           GND|----+
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
    +----|A0           A5 |----+
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    +----------------+    |
    |    [   LM35    ]        |
    |    (Temperature sensor)  |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    +--------------------------+
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    |                          |
    +5V  +----------------+  GND
    +----|3.3V        GND |----+
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
         |                |
    +----|RESET       VIN |----+
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    |                |    |
    |    +----------------+    |
    |    [   Arduino   ]      |
    |    (Uno board)          |
    |                          |