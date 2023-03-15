### Common Base Configuration of BJT

- The common base configuration is one of the three basic ways to connect a bipolar junction transistor (BJT) as an amplifier.
- In this configuration, the base terminal of the BJT is a common terminal to both the input and output signals, hence its name common base (CB).
- The input signal is applied between the emitter and the base, and the output signal is taken from the collector and the base.
- The common base configuration is less common as an amplifier than compared to the more popular common emitter (CE) or common collector (CC) configurations, but it is still used due to its unique input/output characteristics.
- Some of the advantages of the common base configuration are:
  - It has a high voltage gain, which is the ratio of output voltage to input voltage.
  - It has a high input impedance, which means it does not load the input source too much.
  - It has a low output impedance, which means it can drive a low resistance load easily.
  - It has a wide bandwidth, which means it can amplify a wide range of frequencies without distortion.
- Some of the disadvantages of the common base configuration are:
  - It has a low current gain, which is the ratio of output current to input current.
  - It has a low power gain, which is the product of voltage gain and current gain.
  - It has a low input-output isolation, which means the output signal can affect the input signal and vice versa.
  - It has a low stability, which means it is sensitive to temperature changes and variations in transistor parameters.
- The common base configuration can be analyzed using the hybrid-pi model of the BJT, which is a small-signal equivalent circuit that approximates the behavior of the BJT around a given operating point.
- The hybrid-pi model consists of a controlled current source that represents the transconductance of the BJT, and a parallel combination of a resistor and a capacitor that represents the output resistance and capacitance of the BJT.
- The hybrid-pi model can be used to derive the voltage gain, input impedance, output impedance, and bandwidth of the common base configuration.
- The following diagram shows the hybrid-pi model of the common base configuration, where:
  - Vi is the input voltage
  - Vo is the output voltage
  - Ii is the input current
  - Io is the output current
  - Vcc is the supply voltage
  - Rc is the collector resistor
  - Re is the emitter resistor
  - gm is the transconductance of the BJT
  - ro is the output resistance of the BJT
  - Cpi is the input capacitance of the BJT
  - Cpo is the output capacitance of the BJT

![Common base configuration with hybrid-pi model](https://i.imgur.com/6Y1wQ0x.png)

- The voltage gain of the common base configuration is given by:

  - Av = Vo / Vi = -gm * Rc / (1 + gm * Re)

- The input impedance of the common base configuration is given by:

  - Zi = Vi / Ii = Re / (1 + gm * Re)

- The output impedance of the common base configuration is given by:

  - Zo = Vo / Io = ro || Rc

- The bandwidth of the common base configuration is given by:

  - Bw = gm / (2 * pi * (Cpi + Cpo))

- The current gain of the common base configuration is given by:

  - Ai = Io / Ii = -gm * Rc / (1 + gm * Re) * Re / (Re + ro || Rc)

- The power gain of the common base configuration is given by:

  - Ap = Vo * Io / Vi * Ii = Av * Ai