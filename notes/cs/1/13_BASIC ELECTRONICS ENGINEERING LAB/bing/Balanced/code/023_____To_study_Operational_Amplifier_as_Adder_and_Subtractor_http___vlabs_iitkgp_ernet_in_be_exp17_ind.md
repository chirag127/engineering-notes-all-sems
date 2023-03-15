# To study Operational Amplifier as Adder and Subtractor

- An operational amplifier (op-amp) is a high-gain electronic voltage amplifier with a differential input and a single-ended output.
- An op-amp can be used as part of a positive or negative feedback amplifier or as an adder or subtractor type circuit using just pure resistances in both the input and the feedback loop.
- An adder circuit is a type of op-amp circuit that can perform the sum of two or more input voltages and produce a single output voltage.
- A subtractor circuit is a type of op-amp circuit that can perform the difference of two input voltages and produce a single output voltage.
- A differential amplifier is a type of op-amp circuit that can perform both addition and subtraction of two input voltages and produce a single output voltage .
- The circuit diagrams and formulas for the adder, subtractor and differential amplifier circuits are shown below:

## Adder Circuit

![Adder Circuit](https://www.gopracticals.com/wp-content/uploads/2017/08/Op-Amp-Adder-Circuit.png)

The output voltage of the adder circuit is given by:

$$V_{out} = -R_f \left( \frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3} \right)$$

If all the resistors are equal, then the output voltage is the negative of the sum of the input voltages:

$$V_{out} = -(V_1 + V_2 + V_3)$$

## Subtractor Circuit

![Subtractor Circuit](https://www.eeeguide.com/wp-content/uploads/2017/07/Subtractor-using-Op-Amp-or-Difference-Amplifier-Circuit.png)

The output voltage of the subtractor circuit is given by:

$$V_{out} = \frac{R_2}{R_1} V_2 - \frac{R_4}{R_3} V_1$$

If all the resistors are equal, then the output voltage is the difference of the input voltages:

$$V_{out} = V_2 - V_1$$

## Differential Amplifier Circuit

![Differential Amplifier Circuit](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp52.gif)

The output voltage of the differential amplifier circuit is given by:

$$V_{out} = \frac{R_2}{R_1} (V_2 - V_1)$$

If all the resistors are equal, then the output voltage is the same as the subtractor circuit:

$$V_{out} = V_2 - V_1$$

However, if the resistors are not equal, then the output voltage can be adjusted to perform both addition and subtraction of the input voltages. For example, if $R_1 = R_3$ and $R_2 = 2R_4$, then the output voltage is:

$$V_{out} = \frac{V_2}{2} - V_1$$