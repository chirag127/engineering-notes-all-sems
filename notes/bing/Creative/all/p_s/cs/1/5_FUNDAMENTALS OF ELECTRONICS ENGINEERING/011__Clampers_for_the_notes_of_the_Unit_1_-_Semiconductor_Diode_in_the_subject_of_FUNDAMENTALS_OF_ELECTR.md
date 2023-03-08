### Clampers

- Clampers are electronic circuits that change the DC level of an AC signal without changing its shape or amplitude  .
- Clampers are also known as DC voltage restorers or level shifters.
- Clampers are used to add or subtract a DC level to an AC input signal . For example, a clamper can be used to shift a sinusoidal signal from a range of -5V to +5V to a range of 0V to +10V.
- Clampers are composed of a diode, a capacitor and a resistor  . The diode determines the direction of the clamping, the capacitor stores the peak voltage of the input signal, and the resistor discharges the capacitor when the input signal changes polarity .
- Clampers can be classified into four types based on their operation: positive clamper, negative clamper, positive biased clamper and negative biased clamper  .
- A positive clamper (or negative peak clamper) shifts the input signal so that its negative peak is at 0V  . A positive clamper circuit is shown below:

```
    +Vcc
     |
     |
    | |
    | | R
    | |
     |
     |    +------+
     +----| A    |----+---- Output
          |      |    |
          |  D1  |    |
          | K    |----+
          +------+
                |
                |
               ===
               | |
               | | C
               | |
               ===
                |
                |
               GND
```

- A negative clamper (or positive peak clamper) shifts the input signal so that its positive peak is at 0V  . A negative clamper circuit is shown below:

```
    +Vcc
     |
     |
    | |
    | | R
    | |
     |
     |    +------+
     +----| K    |----+---- Output
          |      |    |
          |  D1  |    |
          | A    |----+
          +------+
                |
                |
               ===
               | |
               | | C
               | |
               ===
                |
                |
               GND
```

- A positive biased clamper adds a positive DC voltage to the input signal, shifting it upward  . A positive biased clamper circuit is shown below:

```
    +Vcc
     |
     |
    | |
    | | R
    | |
     |
     |    +------+
     +----| A    |----+---- Output
          |      |    |
          |  D1  |    |
          | K    |----+
          +------+
                |
                |
               ===
               | |
               | | C
               | |
               ===
                |
                |
               GND
                |
                |
               +Vb
```

- A negative biased clamper subtracts a negative DC voltage from the input signal, shifting it downward  . A negative biased clamper circuit is shown below:

```
    +Vcc
     |
     |
    | |
    | | R
    | |
     |
     |    +------+
     +----| K    |----+---- Output
          |      |    |
          |  D1  |    |
          | A    |----+
          +------+
                |
                |
               ===
               | |
               | | C
               | |
               ===
                |
                |
               GND
                |
                |
               -Vb
```

- Some of the advantages of clampers are :
  - They can be used to restore the DC level of a signal that has been distorted by a coupling capacitor or a transformer.
  - They can be used to shift the DC level of a signal to match the input range of a device or a circuit.
  - They can be used to modulate or demodulate a signal by varying the clamping voltage.
- Some of the disadvantages of clampers are [^

Some of the mnemonics and learning tricks for the topic are:

- To remember the direction of the clamping, use the acronym PAD: Positive Anode Down. This means that if the anode of the diode is connected to the positive terminal of the capacitor, the output signal will be clamped down. Conversely, if the anode of the diode is connected to the negative terminal of the capacitor, the output signal will be clamped up.
- To remember the effect of the bias voltage, use the acronym BUD: Bias Upward Downward. This means that if the bias voltage is positive, the output signal will be shifted upward. Conversely, if the bias voltage is negative, the output signal will be shifted downward.
- To remember the formula for the peak output voltage of a clamper, use the acronym COP: Clamping Output Peak. This means that the peak output voltage is equal to the peak input voltage plus the clamping voltage. The clamping voltage is the voltage across the capacitor, which is equal to the peak input voltage for an unbiased clamper, and equal to the peak input voltage plus the bias voltage for a biased clamper. The formula can be written as:

```
Vout(peak) = Vin(peak) + Vclamp
```

- To remember the formula for the time constant of a clamper, use the acronym CRT: Clamping Resistor Time. This means that the time constant is equal to the product of the clamping resistor and the clamping capacitor. The time constant determines how fast the capacitor charges and discharges, and affects the stability and accuracy of the clamping. The formula can be written as:

```
tau = RC
```

- To remember the condition for a stable and accurate clamping, use the acronym TPT: Time Period Time. This means that the time constant of the clamper should be much smaller than the time period of the input signal. This ensures that the capacitor can charge and discharge quickly enough to follow the input signal and maintain the clamping voltage. The condition can be written as:

```
tau << T
```

where T is the time period of the input signal.