### Voltage-Multiplier Circuits

- A voltage multiplier is an electronic circuit consisting of capacitors and diodes and is used to multiply or rise the voltage level of an AC signal.
- The voltage multiplier receives an AC voltage of lower value, converts it into a DC voltage and increases its voltage level.
- Voltage multipliers are classified as voltage doublers, triplers, quadruplers, etc, depending on the ratio of the output voltage to the input voltage.
- In theory, any desired amount of voltage multiplication can be obtained by cascading voltage doublers, but in practice, the output voltage is limited by the breakdown voltage of the diodes and capacitors, and the load current.
- Voltage multipliers can be used to generate a few volts for electronic appliances, to millions of volts for purposes such as high-energy physics experiments and lightning safety testing.

#### Voltage Doubler Circuit

- A voltage doubler is a voltage multiplier circuit that produces an output voltage that is twice the peak input voltage.
- There are two types of voltage doublers: half-wave and full-wave.
- A half-wave voltage doubler consists of two capacitors and two diodes connected as shown below:

![Half-wave voltage doubler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Half-Wave-Voltage-Doubler.png)

- The operation of the half-wave voltage doubler can be explained as follows:
  - During the positive half-cycle of the input AC voltage, diode D1 is forward biased and capacitor C1 is charged to the peak value of the input voltage Vp.
  - During the negative half-cycle of the input AC voltage, diode D2 is forward biased and capacitor C2 is charged to the peak value of the input voltage Vp through diode D1 and capacitor C1.
  - The output voltage across capacitor C2 is the sum of the voltages across C1 and C2, which is 2Vp.
  - The output voltage is a pulsating DC voltage with a ripple frequency equal to the input frequency.
- A full-wave voltage doubler consists of four diodes and two capacitors connected as shown below:

![Full-wave voltage doubler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Full-Wave-Voltage-Doubler.png)

- The operation of the full-wave voltage doubler can be explained as follows:
  - During the positive half-cycle of the input AC voltage, diode D1 is forward biased and capacitor C1 is charged to the peak value of the input voltage Vp.
  - During the negative half-cycle of the input AC voltage, diode D2 is forward biased and capacitor C2 is charged to the peak value of the input voltage Vp through diode D1 and capacitor C1.
  - The output voltage across capacitor C2 is the sum of the voltages across C1 and C2, which is 2Vp.
  - The output voltage is a pulsating DC voltage with a ripple frequency equal to twice the input frequency.
  - The full-wave voltage doubler has the advantage of higher output voltage, lower ripple, and better efficiency than the half-wave voltage doubler.

#### Voltage Tripler Circuit

- A voltage tripler is a voltage multiplier circuit that produces an output voltage that is three times the peak input voltage.
- A voltage tripler circuit can be constructed by adding a capacitor and a diode to a half-wave voltage doubler circuit as shown below:

![Voltage tripler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Voltage-Tripler.png)

- The operation of the voltage tripler circuit can be explained as follows:
  - During the positive half-cycle of the input AC voltage, diode D1 is forward biased and capacitor C1 is charged to the peak value of the input voltage Vp.
  - During the negative half-cycle of the input AC voltage, diode D2 is forward biased and capacitor C2 is charged to the peak value of the input voltage Vp through diode D1 and capacitor C1.
  - The voltage across capacitor C2 is 2Vp.
  - During the next positive half-cycle of the input AC voltage, diode D3 is forward biased and capacitor C3 is charged to the peak value of the input voltage Vp through diode D2 and capacitor C2.
  - The voltage across capacitor C3 is 3Vp.
  - The output voltage across capacitor C3 is the sum