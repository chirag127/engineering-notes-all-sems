A BJT in CE configuration is a type of transistor circuit where the emitter is the common terminal for both input and output. The input voltage is applied between the base and the emitter, and the output voltage is taken from the collector and the emitter. The CE configuration is an inverting amplifier, meaning that the output signal is 180 degrees out of phase with the input signal.

The following ASCII diagram illustrates the basic architecture of a BJT in CE configuration:

```
    Vcc
     |
     |
     R
     C
     |
     |    Rc
     +----/\/\----+
     |           |
     |           |
     |           C
     |           |
     |           |
     |           B
     |           |
     |           |
     |           E
     |           |
     |           |
     |           R
     |           E
     |           |
     +----/\/\----+
     |           |
     |           |
     |           R
     |           B
     |           |
     |           |
     |           R
     |           E
     |           |
     +----/\/\----+
     |           |
     |           |
     |           R
     |           S
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
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
    GND
```

The symbols used in the diagram are as follows:

- Vcc: The supply voltage
- Rc: The collector resistor
- Re: The emitter resistor
- Rb: The base resistor
- Rs: The source resistor
- C: The collector terminal of the BJT
- B: The base terminal of the BJT
- E: The emitter terminal of the BJT
- R: The resistance symbol
- /\/\: The resistor symbol
- +: The junction symbol
- |: The wire symbol
- GND: The ground symbol

The input voltage is applied across Rs and Rb, and the output voltage is measured across Rc and Re. The input current is the base current Ib, and the output current is the collector current Ic. The current gain of the BJT is the ratio of Ic to Ib, denoted by beta. The voltage gain of the CE configuration is the ratio of the output voltage to the input voltage, denoted by Av. The input and output characteristics of the BJT in CE configuration are the graphs that show the relationship between Ib and Vbe, and Ic and Vce, respectively.