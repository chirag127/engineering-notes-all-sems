### 3. Applications of PN Junction diode: Half & Full wave rectifier-Measurement of Vrms, Vdc, and ripple factor.

PN Junction diodes are widely used in various applications in electronics, including rectification of AC voltage to DC voltage. The rectification process is necessary to convert the AC voltage to a DC voltage, which is required for many electronic devices to operate. PN Junction diodes are used in half-wave and full-wave rectifiers to perform this task.

#### Half-wave rectifier

A half-wave rectifier is a circuit that converts the positive half cycle of an AC voltage into a DC voltage. The negative half cycle is suppressed. A PN Junction diode is used in a half-wave rectifier to perform this task. The circuit diagram of a half-wave rectifier is shown below:

![Half Wave Rectifier](https://i.imgur.com/nJlNVmE.png)

The input voltage is applied across the diode in series with the load resistor. During the positive half cycle of the input voltage, the diode is forward biased, and current flows through the load resistor. During the negative half cycle, the diode is reverse biased, and no current flows through the load resistor. The output voltage across the load resistor is the rectified DC voltage.

#### Full-wave rectifier

A full-wave rectifier is a circuit that converts both the positive and negative half cycles of an AC voltage into a DC voltage. Two PN Junction diodes are used in a full-wave rectifier to perform this task. The circuit diagram of a full-wave rectifier is shown below:

![Full Wave Rectifier](https://i.imgur.com/MZn9XJf.png)

The input voltage is applied across the center-tapped transformer, and the two diodes are connected to the ends of the secondary winding. During the positive half cycle of the input voltage, the diode D1 is forward biased, and current flows through the load resistor RL1. During the negative half cycle, the diode D2 is forward biased, and current flows through the load resistor RL2. The output voltage across the load resistor is the rectified DC voltage.

#### Measurement of Vrms, Vdc, and ripple factor

In a rectifier circuit, the output voltage is not pure DC voltage but contains some AC voltage, which is called the ripple voltage. The measurement of various parameters of the rectified voltage is necessary to determine the performance of the rectifier circuit. The following parameters can be measured:

- **Vrms**: The root mean square value of the output voltage is called the Vrms value. It is calculated as the square root of the mean of the squares of the instantaneous values of the output voltage over one cycle.

- **Vdc**: The average value of the output voltage is called the Vdc value. It is calculated as the average of the instantaneous values of the output voltage over one cycle.

- **Ripple factor**: The ratio of the RMS value of the ripple voltage to the Vdc value is called the ripple factor. It is a measure of the amount of AC voltage present in the output voltage.

These parameters can be measured using a multimeter or an oscilloscope. The Vrms and Vdc values can be measured using a multimeter, while the ripple factor can be calculated using the formula:

Ripple factor = Vrms / Vdc

In conclusion, PN Junction diodes are widely used in rectifier circuits to convert AC voltage to DC voltage. The half-wave and full-wave rectifiers are the two most commonly used rectifier circuits. The measurement of various parameters of the rectified voltage is necessary to determine the performance of the rectifier circuit. The Vrms, Vdc, and ripple factor can be measured using a multimeter or an oscilloscope.