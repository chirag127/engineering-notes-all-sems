### Voltage-Multiplier Circuits

- A voltage multiplier is an electronic circuit consisting of capacitors and diodes and is used to multiply or rise the voltage level of an AC signal.
- The voltage multiplier receives an AC voltage of lower value, converts it into a DC voltage and increases its voltage level.
- Voltage multipliers are classified as voltage doublers, triplers, quadruplers, etc, depending on the ratio of the output voltage to the input voltage.
- In theory, any desired amount of voltage multiplication can be obtained by cascading voltage doublers, but in practice, the output voltage drops due to the losses in the circuit components.
- Voltage multipliers can be used to generate a few volts for electronic appliances, to millions of volts for purposes such as high-energy physics experiments and lightning safety testing.

#### Voltage Doubler Circuit

- A voltage doubler is a voltage multiplier circuit that produces an output voltage that is twice the peak input voltage of an AC signal.
- A voltage doubler circuit consists of two diodes and two capacitors connected in series as shown below:

```
    +----|>|----+----|>|----+
    |    D1    |    D2    |
    |          |          |
   ~|~        ---        ---        +Vout
   Vp        C1         C2          |
    |          |          |          |
    +----------+----------+----------+
                                   GND
```

- The operation of the voltage doubler circuit can be explained in two half cycles of the input AC signal  :
  - During the positive half cycle, diode D1 is forward biased and diode D2 is reverse biased. Capacitor C1 is charged to the peak input voltage Vp through diode D1. Capacitor C2 does not charge in this half cycle.
  - During the negative half cycle, diode D1 is reverse biased and diode D2 is forward biased. Capacitor C1 and C2 are connected in series and the voltage across them is equal to 2Vp. Capacitor C2 is charged to 2Vp through diode D2. The output voltage is taken across capacitor C2 and is equal to 2Vp minus the diode voltage drops.

#### Voltage Tripler Circuit

- A voltage tripler is a voltage multiplier circuit that produces an output voltage that is three times the peak input voltage of an AC signal.
- A voltage tripler circuit consists of three diodes and three capacitors connected as shown below:

```
    +----|>|----+----|>|----+
    |    D1    |    D2    |
    |          |          |
   ~|~        ---        ---        +Vout
   Vp        C1         C2          |
    |          |          |          |
    +----|>|----+         |          |
    |    D3    |          |          |
    |          |         ---         |
    |          |         C3          |
    |          |          |          |
    +----------+----------+----------+
                                   GND
```

- The operation of the voltage tripler circuit can be explained in two half cycles of the input AC signal  :
  - During the positive half cycle, diode D1 and D3 are forward biased and diode D2 is reverse biased. Capacitor C1 is charged to the peak input voltage Vp through diode D1. Capacitor C3 is charged to 2Vp through diode D3 and capacitor C1. Capacitor C2 does not charge in this half cycle.
  - During the negative half cycle, diode D1 and D3 are reverse biased and diode D2 is forward biased. Capacitor C1 and C2 are connected in series and the voltage across them is equal to 2Vp. Capacitor C2 is charged to 2Vp through diode D2. The output voltage is taken across capacitor C2 and C3 and is equal to 3Vp minus the diode voltage drops.

#### Voltage Quadrupler Circuit

- A voltage quadrupler is a voltage multiplier circuit that produces an output voltage that is four times the peak input voltage of an AC signal.
- A voltage quadrupler circuit consists of four diodes and four capacitors connected as shown below:

```
    +

```
