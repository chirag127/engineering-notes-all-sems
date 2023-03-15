### 6. To study Operational Amplifier as Adder and Subtractor

- An operational amplifier (op-amp) is a high-gain, direct-coupled electronic circuit that can perform various linear operations such as amplification, filtering, differentiation, integration, etc.
- An op-amp has two input terminals: the inverting input (-) and the non-inverting input (+), and one output terminal. It also has two power supply terminals: the positive supply (+V) and the negative supply (-V).
- An op-amp can be used as an adder or a subtractor by connecting resistors to its input and output terminals. The resistors determine the gain and the polarity of the output signal with respect to the input signals.
- An op-amp adder is a circuit that produces an output voltage that is proportional to the sum of the input voltages. It can be implemented by connecting the input voltages to the inverting input of the op-amp through resistors of equal value, and connecting a feedback resistor from the output to the inverting input. The output voltage is given by:

  Vout = -Rf/R1(V1 + V2 + ... + Vn)

  where Rf is the feedback resistor, R1 is the input resistor, and V1, V2, ... Vn are the input voltages.
- An op-amp subtractor is a circuit that produces an output voltage that is proportional to the difference of two input voltages. It can be implemented by connecting one input voltage to the non-inverting input of the op-amp and the other input voltage to the inverting input of the op-amp through resistors of equal value, and connecting a feedback resistor from the output to the inverting input. The output voltage is given by:

  Vout = Rf/R1(V2 - V1)

  where Rf is the feedback resistor, R1 is the input resistor, and V1 and V2 are the input voltages.
- The advantages of using op-amp as adder and subtractor are:
  - The circuit is simple and easy to design.
  - The circuit has high input impedance and low output impedance, which means it does not load the input sources or the output load.
  - The circuit has high accuracy and linearity, which means it can perform precise arithmetic operations.
  - The circuit has high common-mode rejection ratio (CMRR), which means it can reject the noise or interference that is common to both input terminals.