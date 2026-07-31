### 6. To study Operational Amplifier as Adder and Subtractor

An operational amplifier, or op-amp, is a high-gain electronic voltage amplifier with a differential input and a single-ended output. It is used in a variety of electronic circuits and systems to perform mathematical operations such as addition and subtraction.

#### Adder
An adder circuit using an op-amp can be designed to add multiple input voltages and produce a single output voltage that is the sum of the input voltages. The circuit consists of an op-amp with multiple input resistors connected to the inverting input and a feedback resistor connected between the output and the inverting input. The non-inverting input is connected to ground.

The output voltage of the adder circuit is given by the formula:
Vout = -(Rf/R1)V1 - (Rf/R2)V2 - ... - (Rf/Rn)Vn

Where:
- Vout is the output voltage
- Rf is the feedback resistor
- R1, R2, ..., Rn are the input resistors
- V1, V2, ..., Vn are the input voltages

#### Subtractor
A subtractor circuit using an op-amp can be designed to subtract two input voltages and produce a single output voltage that is the difference between the input voltages. The circuit consists of an op-amp with two input resistors connected to the inverting and non-inverting inputs and a feedback resistor connected between the output and the inverting input.

The output voltage of the subtractor circuit is given by the formula:
Vout = (Rf/R2)(V2 - V1)

Where:
- Vout is the output voltage
- Rf is the feedback resistor
- R1 and R2 are the input resistors
- V1 and V2 are the input voltages

In summary, an operational amplifier can be used as an adder or subtractor to perform mathematical operations on multiple input voltages. The design of the circuit and the values of the resistors determine the operation performed by the op-amp.