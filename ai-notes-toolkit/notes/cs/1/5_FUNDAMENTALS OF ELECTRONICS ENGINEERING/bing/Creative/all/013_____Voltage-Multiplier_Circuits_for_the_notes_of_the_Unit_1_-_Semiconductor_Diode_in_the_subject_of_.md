# Voltage-Multiplier Circuits

- A voltage multiplier is an electronic circuit consisting of capacitors and diodes and is used to multiply or rise the voltage level of an AC signal.
- The voltage multiplier receives an AC voltage of lower value, converts it into a DC voltage and increases its voltage level.
- Voltage multipliers are classified as voltage doublers, triplers, quadruplers, etc, depending on the ratio of the output voltage to the input voltage.
- In theory, any desired amount of voltage multiplication can be obtained by cascading voltage doublers, but in practice, the output voltage drops due to the losses in the circuit components.
- Voltage multipliers can be used to generate a few volts for electronic appliances, to millions of volts for purposes such as high-energy physics experiments and lightning safety testing.

## Voltage Doubler Circuit

- A voltage doubler is a voltage multiplier circuit that produces an output voltage that is twice the peak input voltage of an AC signal.
- There are two types of voltage doubler circuits: half-wave and full-wave.
- A half-wave voltage doubler consists of two capacitors and two diodes connected as shown below:

![Half-wave voltage doubler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Half-Wave-Voltage-Doubler-Circuit.png)

- The operation of the half-wave voltage doubler can be explained as follows:
  - During the positive half-cycle of the input AC signal, diode D1 is forward biased and capacitor C1 is charged to the peak input voltage Vp.
  - During the negative half-cycle of the input AC signal, diode D2 is forward biased and capacitor C2 is charged to the peak input voltage Vp in series with capacitor C1, resulting in an output voltage of 2Vp across C2.
  - The output voltage is a pulsating DC voltage with a ripple frequency equal to the input frequency.
- A full-wave voltage doubler consists of four diodes and two capacitors connected as shown below:

![Full-wave voltage doubler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Full-Wave-Voltage-Doubler-Circuit.png)

- The operation of the full-wave voltage doubler can be explained as follows:
  - During the positive half-cycle of the input AC signal, diode D1 is forward biased and capacitor C1 is charged to the peak input voltage Vp, while diode D3 is reverse biased and capacitor C2 is disconnected from the circuit.
  - During the negative half-cycle of the input AC signal, diode D2 is forward biased and capacitor C2 is charged to the peak input voltage Vp in series with capacitor C1, resulting in an output voltage of 2Vp across C2, while diode D4 is reverse biased and capacitor C1 is disconnected from the circuit.
  - The output voltage is a pulsating DC voltage with a ripple frequency equal to twice the input frequency.
- The advantages of a full-wave voltage doubler over a half-wave voltage doubler are:
  - Higher output voltage due to lower voltage drop across the diodes.
  - Lower output ripple due to higher ripple frequency.
  - Higher output current due to lower output impedance.

## Voltage Tripler Circuit

- A voltage tripler is a voltage multiplier circuit that produces an output voltage that is three times the peak input voltage of an AC signal.
- A voltage tripler circuit can be constructed by adding a capacitor and a diode to a half-wave voltage doubler circuit as shown below:

![Voltage tripler circuit](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Voltage-Tripler-Circuit.png)

- The operation of the voltage tripler circuit can be explained as follows:
  - During the positive half-cycle of the input AC signal, diode D1 is forward biased and capacitor C1 is charged to the peak input voltage Vp, while diode D2 and D3 are reverse biased and capacitors C2 and C3 are disconnected from the circuit.
  - During the negative half-cycle of the input AC signal, diode D2 is forward biased and capacitor C2 is charged to the peak input voltage Vp in series with capacitor C1, resulting in a voltage of 2Vp across C2, while diode D3 is forward biased and capacitor C3 is charged to the peak input voltage Vp in