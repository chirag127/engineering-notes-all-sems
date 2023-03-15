# Voltage-Multiplier Circuits

- A voltage multiplier is an electronic circuit consisting of capacitors and diodes and is used to multiply or rise the voltage level of an AC signal.
- The voltage multiplier receives an AC voltage of lower value, converts it into a DC voltage and increases its voltage level.
- Voltage multipliers are classified as voltage doublers, triplers, quadruplers, etc, depending on the ratio of the output voltage to the input voltage.
- In theory, any desired amount of voltage multiplication can be obtained by cascading voltage doublers, but in practice, the efficiency and ripple of the output voltage decrease as the number of stages increases.
- Voltage multipliers can be used to generate a few volts for electronic appliances, to millions of volts for purposes such as high-energy physics experiments and lightning safety testing.

## Voltage Doubler Circuit

- A voltage doubler is a voltage multiplier circuit that produces an output voltage that is twice the peak input voltage.
- There are two types of voltage doubler circuits: half-wave and full-wave.
- A half-wave voltage doubler consists of two capacitors and two diodes connected as shown below:

![Half-wave voltage doubler circuit](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/blog-voltage-multiplier-1.gif)

- The operation of the half-wave voltage doubler can be explained as follows:
  - During the positive half-cycle of the input AC voltage, diode D1 is forward biased and capacitor C1 is charged to the peak value of the input voltage Vp.
  - During the negative half-cycle of the input AC voltage, diode D2 is forward biased and capacitor C2 is charged to the peak value of the input voltage Vp in series with the voltage across C1, which is also Vp. Therefore, the total voltage across C2 is 2Vp.
  - The output voltage Vo is taken across C2 and is equal to 2Vp minus the diode voltage drops.
- A full-wave voltage doubler consists of four diodes and two capacitors connected as shown below:

![Full-wave voltage doubler circuit](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/blog-voltage-multiplier-2.gif)

- The operation of the full-wave voltage doubler can be explained as follows:
  - During the positive half-cycle of the input AC voltage, diodes D1 and D4 are forward biased and capacitors C1 and C2 are charged to the peak value of the input voltage Vp in parallel.
  - During the negative half-cycle of the input AC voltage, diodes D2 and D3 are forward biased and capacitors C1 and C2 are connected in series across the output terminals, giving a total voltage of 2Vp.
  - The output voltage Vo is taken across C1 and C2 and is equal to 2Vp minus the diode voltage drops.
- The advantages of the full-wave voltage doubler over the half-wave voltage doubler are that it has a higher output current, lower output impedance, lower ripple and better regulation.

## Voltage Tripler Circuit

- A voltage tripler is a voltage multiplier circuit that produces an output voltage that is three times the peak input voltage.
- A voltage tripler circuit can be constructed by adding an additional stage to the half-wave voltage doubler circuit as shown below:

![Voltage tripler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Voltage-Tripler-Circuit.png)

- The operation of the voltage tripler circuit can be explained as follows:
  - During the positive half-cycle of the input AC voltage, diode D1 is forward biased and capacitor C1 is charged to the peak value of the input voltage Vp.
  - During the negative half-cycle of the input AC voltage, diode D2 is forward biased and capacitor C2 is charged to the peak value of the input voltage Vp in series with the voltage across C1, which is also Vp. Therefore, the total voltage across C2 is 2Vp.
  - During the next positive half-cycle of the input AC voltage, diode D3 is forward biased and capacitor C3 is charged to the peak value of the input voltage Vp in series with the voltage across C2, which is 2Vp. Therefore, the total