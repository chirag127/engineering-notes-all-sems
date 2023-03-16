# Push and Pull

- Push and pull are two types of output modes for microcontroller pins.
- Push-pull output mode means that the pin can actively drive the signal high or low by using a pair of complementary transistors.
- Open-drain output mode means that the pin can only drive the signal low by using a single transistor, while the signal is pulled high by an external resistor.
- Push-pull output mode can provide more current and faster switching than open-drain output mode, but it cannot be used for bidirectional communication or interfacing with devices that have different voltage levels.
- Open-drain output mode can be used for bidirectional communication or interfacing with devices that have different voltage levels, but it requires an external pull-up resistor and has slower switching speed than push-pull output mode.
- Push-pull output mode is also called totem-pole output mode, while open-drain output mode is also called open-collector output mode.
- Push-pull and open-drain output modes are not to be confused with push-pull and open-drain converters, which are types of DC-to-DC converters that use transformers to change the voltage of a DC power supply.