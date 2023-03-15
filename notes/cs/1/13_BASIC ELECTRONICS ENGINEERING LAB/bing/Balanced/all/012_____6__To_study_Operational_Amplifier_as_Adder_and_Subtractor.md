# 6. To study Operational Amplifier as Adder and Subtractor

An operational amplifier (op-amp) is a DC-coupled high-gain electronic voltage amplifier with a differential input and a single-ended output. It can be used to perform various mathematical operations such as addition, subtraction, integration and differentiation. In this section, we will study how to use op-amps as adders and subtractors.

## Op-amp as Adder

An adder is an electronic circuit that produces an output, which is equal to the sum of the applied inputs. An op-amp based adder circuit is shown in the figure below.

![Op-amp adder circuit](https://www.tutorialspoint.com/linear_integrated_circuits_applications/images/adder.jpg)

The circuit consists of an op-amp with three inputs (V1, V2 and V3) and one output (Vout). The inputs are connected to the inverting terminal of the op-amp through resistors R1, R2 and R3, respectively. The output is connected to the inverting terminal through a feedback resistor Rf. The non-inverting terminal is grounded.

The output voltage of the op-amp is given by the equation:

Vout = -Rf * (V1/R1 + V2/R2 + V3/R3)

If we assume that all the resistors have the same value R, then the equation simplifies to:

Vout = -Rf/R * (V1 + V2 + V3)

This shows that the output voltage is proportional to the negative sum of the input voltages. Therefore, the circuit acts as an adder with a negative sign.

## Op-amp as Subtractor

A subtractor is an electronic circuit that produces an output, which is equal to the difference of the applied inputs. An op-amp based subtractor circuit is shown in the figure below.

![Op-amp subtractor circuit](https://www.tutorialspoint.com/linear_integrated_circuits_applications/images/subtractor.jpg)

The circuit consists of an op-amp with two inputs (V1 and V2) and one output (Vout). The input V1 is connected to the non-inverting terminal of the op-amp through a resistor R1. The input V2 is connected to the inverting terminal of the op-amp through a resistor R2. The output is connected to the inverting terminal through a feedback resistor Rf. The non-inverting terminal is also connected to the inverting terminal through a resistor R3.

The output voltage of the op-amp is given by the equation:

Vout = Rf/R2 * V2 - Rf/R1 * V1 - Rf/R3 * V1

If we assume that all the resistors have the same value R, then the equation simplifies to:

Vout = Rf/R * (V2 - 2 * V1)

This shows that the output voltage is proportional to the difference of the input voltages with a negative sign. Therefore, the circuit acts as a subtractor with a negative sign.