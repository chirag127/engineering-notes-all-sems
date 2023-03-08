### Voltage-Multiplier Circuits

- A voltage multiplier is an electronic circuit consisting of capacitors and diodes and is used to multiply or rise the voltage level of an AC signal.
- The voltage multiplier receives an AC voltage of lower value, converts it into a DC voltage and increases its voltage level.
- Voltage multiplier circuits are classified as voltage doubler’s, tripler’s, or quadrupler’s, etc, depending on the ratio of the output voltage to the input voltage.
- In theory any desired amount of voltage multiplication can be obtained and a cascade of “N” doublers, would produce an output voltage of 2N.Vp volts, where Vp is the peak input voltage.
- Voltage multipliers can be used to generate a few volts for electronic appliances, to millions of volts for purposes such as high-energy physics experiments and lightning safety testing.

#### Voltage Doubler Circuit

- A voltage doubler is a voltage multiplier circuit that produces an output voltage that is twice the peak input voltage.
- There are two types of voltage doubler circuits: half-wave and full-wave.
- A half-wave voltage doubler consists of two capacitors and two diodes connected as shown below:

```
    +----|>|----+----|>|----+
    |    D1    |    D2    |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |    C1    |    C2    |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    +----+-----+-----+----+
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
AC       |           |       DC
Input    |           |     Output
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         +-----------+
```

- The operation of the half-wave voltage doubler is as follows:

  - During the positive half-cycle of the input, diode D1 is forward biased and diode D2 is reverse biased. Capacitor C1 is charged to the peak input voltage Vp through diode D1. The output voltage is zero.
  - During the negative half-cycle of the input, diode D1 is reverse biased and diode D2 is forward biased. Capacitor C2 is charged to the peak input voltage Vp through diode D2 and capacitor C1. The output voltage is the sum of the voltages across C1 and C2, which is 2Vp.

- A full-wave voltage doubler consists of four diodes and two capacitors connected as shown below:

```
    +----|>|----+----|>|----+
    |    D1    |    D2    |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |    C1    |    C2    |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    +----+-----+-----+----+
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
         |           |
    +----|>|----+----|>|----+
    |    D3    |    D4    |
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    |          |          |

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of the diodes and capacitors in the half-wave voltage doubler, you can use the acronym **D1C1D2C2** or the phrase **D**on't **1** **C**ry **1** **D**ay **2** **C**hange **2**.
- To remember the order of the diodes and capacitors in the full-wave voltage doubler, you can use the acronym **D1C1D2C2D3D4** or the phrase **D**on't **1** **C**ry **1** **D**ay **2** **C**hange **2** **D**o **3** **D**ifferent **4**.
- To remember the output voltage of the voltage doubler, you can use the formula **Vout = 2Vp** or the phrase **V**ery **out**standing **2** **V**ery **p**ositive.