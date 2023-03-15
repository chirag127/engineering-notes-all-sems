### Voltage-Multiplier Circuits

- A voltage multiplier is an electronic circuit consisting of capacitors and diodes and is used to multiply or rise the voltage level of an AC signal.
- The voltage multiplier receives an AC voltage of lower value, converts it into a DC voltage and increases its voltage level.
- Voltage multipliers are classified as voltage doublers, triplers, quadruplers, etc, depending on the ratio of the output voltage to the input voltage.
- In theory, any desired amount of voltage multiplication can be obtained by cascading voltage doublers, but in practice, the output voltage drops due to the losses in the circuit components.
- Voltage multipliers can be used to generate a few volts for electronic appliances, to millions of volts for purposes such as high-energy physics experiments and lightning safety testing.

#### Voltage Doubler Circuit

- A voltage doubler is a voltage multiplier circuit that produces an output voltage that is twice the peak input voltage of an AC signal.
- A voltage doubler circuit consists of two diodes and two capacitors connected in series as shown below:

![Voltage Doubler Circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Voltage-Doubler-Circuit.png)

- The operation of the voltage doubler circuit can be explained in two half cycles of the input AC signal  :

  - During the positive half cycle, diode D1 is forward biased and diode D2 is reverse biased. Capacitor C1 is charged to the peak input voltage Vp through diode D1. Capacitor C2 is not charged as it is blocked by diode D2. The output voltage is zero as both the terminals of capacitor C2 are at the same potential.
  - During the negative half cycle, diode D1 is reverse biased and diode D2 is forward biased. Capacitor C1 is not discharged as it is blocked by diode D1. Capacitor C2 is charged to the peak input voltage Vp through diode D2 and capacitor C1. The output voltage is the sum of the voltages across capacitor C1 and C2, which is 2Vp.

- The output voltage of the voltage doubler circuit is not exactly 2Vp, but slightly less due to the voltage drops across the diodes and the leakage currents of the capacitors.
- The output voltage can be smoothed by adding a filter capacitor across the load resistor as shown below:

![Voltage Doubler Circuit with Filter Capacitor](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Voltage-Doubler-Circuit-with-Filter-Capacitor.png)

#### Voltage Tripler Circuit

- A voltage tripler is a voltage multiplier circuit that produces an output voltage that is three times the peak input voltage of an AC signal.
- A voltage tripler circuit consists of three diodes and three capacitors connected in series as shown below:

![Voltage Tripler Circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Voltage-Tripler-Circuit.png)

- The operation of the voltage tripler circuit can be explained in two half cycles of the input AC signal  :

  - During the positive half cycle, diode D1 is forward biased and diodes D2 and D3 are reverse biased. Capacitor C1 is charged to the peak input voltage Vp through diode D1. Capacitors C2 and C3 are not charged as they are blocked by diodes D2 and D3. The output voltage is zero as both the terminals of capacitor C3 are at the same potential.
  - During the negative half cycle, diode D1 is reverse biased and diodes D2 and D3 are forward biased. Capacitor C1 is not discharged as it is blocked by diode D1. Capacitor C2 is charged to the peak input voltage Vp through diode D2 and capacitor C1. Capacitor C3 is charged to the peak input voltage Vp through diode D3 and capacitors C1 and C2. The output voltage is the sum of the voltages across capacitors C1, C2 and C3, which is 3Vp.

- The output voltage of the voltage tripler circuit is not exactly 3Vp, but slightly less due to the voltage drops across the diodes and the leakage currents of the capacitors[^3^