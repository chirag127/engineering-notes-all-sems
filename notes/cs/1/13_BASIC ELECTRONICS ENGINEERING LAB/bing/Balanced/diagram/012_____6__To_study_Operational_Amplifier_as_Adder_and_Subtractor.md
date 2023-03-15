### 6. To study Operational Amplifier as Adder and Subtractor

An operational amplifier (op-amp) is a DC-coupled high-gain electronic voltage amplifier with a differential input and, usually, a single-ended output. It can perform mathematical operations such as addition, subtraction, integration and differentiation. In this section, we will study how to use op-amps as adders and subtractors.

#### Adder

An adder is an electronic circuit that produces an output, which is equal to the sum of the applied inputs. The op-amp based adder circuit is shown below:

![Op-amp adder circuit](https://www.tutorialspoint.com/linear_integrated_circuits_applications/images/adder.jpg)

The circuit consists of an op-amp with a negative feedback resistor Rf and three input resistors R1, R2 and R3. The input voltages are V1, V2 and V3, and the output voltage is Vout.

The op-amp operates in the inverting mode, which means that the output voltage is proportional to the negative of the input voltage. The output voltage is given by:

Vout = -Rf * (V1/R1 + V2/R2 + V3/R3)

If we choose Rf = R1 = R2 = R3 = R, then the output voltage simplifies to:

Vout = -R * (V1 + V2 + V3) / R

Vout = -(V1 + V2 + V3)

Therefore, the output voltage is the negative of the sum of the input voltages. To obtain a positive output, we can either invert the output voltage using another op-amp, or use a non-inverting adder circuit.

#### Subtractor

A subtractor is an electronic circuit that produces an output, which is equal to the difference of the applied inputs. The op-amp based subtractor circuit is shown below:

![Op-amp subtractor circuit](https://www.tutorialspoint.com/linear_integrated_circuits_applications/images/subtractor.jpg)

The circuit consists of an op-amp with a negative feedback resistor Rf and two input resistors R1 and R2. The input voltages are V1 and V2, and the output voltage is Vout.

The op-amp operates in the differential mode, which means that the output voltage is proportional to the difference of the input voltages. The output voltage is given by:

Vout = Rf * (V2/R2 - V1/R1)

If we choose Rf = R1 = R2 = R, then the output voltage simplifies to:

Vout = R * (V2 - V1) / R

Vout = V2 - V1

Therefore, the output voltage is the difference of the input voltages. To obtain a negative output, we can either invert the output voltage using another op-amp, or use a non-inverting subtractor circuit.