### Zener diode as shunt regulator

- A shunt regulator is a circuit that regulates the output voltage by diverting excess current away from the load.
- A Zener diode is a special type of diode that operates in the reverse breakdown region, where it maintains a nearly constant voltage across its terminals.
- A Zener diode can be used as a shunt regulator by connecting it in parallel with the load, as shown in the figure below.

![Zener diode shunt regulator](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio8.gif)

- The input voltage, V<sub>in</sub>, is applied across the series resistor, R<sub>s</sub>, and the parallel combination of the Zener diode and the load resistor, R<sub>L</sub>.
- The Zener diode is reverse biased, so it does not conduct until the input voltage exceeds the Zener breakdown voltage, V<sub>Z</sub>.
- When the input voltage is equal to or greater than V<sub>Z</sub>, the Zener diode starts to conduct and maintains a constant voltage of V<sub>Z</sub> across the load.
- The excess current, I<sub>Z</sub>, flows through the Zener diode and is shunted away from the load.
- The output voltage, V<sub>out</sub>, is equal to V<sub>Z</sub> as long as the input voltage is high enough and the load current, I<sub>L</sub>, is within the limit of the Zener diode.
- The series resistor, R<sub>s</sub>, limits the current through the Zener diode and protects it from damage.
- The Zener diode shunt regulator provides a simple and low-cost way of regulating the voltage across small loads.
- However, it has some disadvantages, such as poor efficiency, high power dissipation, and limited current and voltage range.