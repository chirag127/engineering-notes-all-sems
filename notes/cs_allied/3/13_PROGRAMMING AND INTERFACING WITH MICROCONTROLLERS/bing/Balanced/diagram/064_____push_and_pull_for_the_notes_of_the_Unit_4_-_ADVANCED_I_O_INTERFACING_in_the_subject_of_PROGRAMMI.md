### Push and Pull

- Push and pull are two types of output modes that a microcontroller pin can use when configured as an output.
- Push-pull mode means that the pin can actively drive the output high or low by connecting it to the supply voltage (Vcc) or ground (GND) through a transistor. This mode can provide a strong output signal that can source or sink more current.
- Open-drain mode means that the pin can only actively drive the output low by connecting it to ground through a transistor. The pin cannot drive the output high, but it can leave it floating (high-impedance state). This mode requires an external pull-up resistor to provide a weak output signal that can only source a small amount of current.
- Push-pull mode is more suitable for driving LEDs, relays, motors, and other devices that need a high or low output signal with sufficient current.
- Open-drain mode is more suitable for interfacing with other devices that have their own pull-up resistors, such as I2C or 1-Wire buses, or for creating a wired-OR logic with multiple outputs connected together.
- Some microcontrollers can switch between push-pull and open-drain modes dynamically, or have a third mode that combines both features. This can increase the flexibility and compatibility of the output pins for different applications.