# Implementation of 4:1 multiplexer using logic gates

A multiplexer is a combinational circuit that takes multiple inputs and delivers only a single output. It consists of input data lines, selection lines and a single output line. A 4:1 multiplexer has 4 input data lines, 2 selection lines and 1 output line. The output is determined by the values of the selection lines. The truth table for a 4:1 multiplexer is shown below:

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | A0 |
| 0  | 1  | A1 |
| 1  | 0  | A2 |
| 1  | 1  | A3 |

The output Y can be expressed as a Boolean function of the inputs and the selection lines as follows:

Y = A0.S1'.S0' + A1.S1'.S0 + A2.S1.S0' + A3.S1.S0

This function can be implemented using logic gates as shown in the diagram below:

![4:1 multiplexer using logic gates](https://programmerbay.com/wp-content/uploads/2020/10/4-to-1-multiplexer-using-logic-gates.png)

The circuit requires two NOT gates, four AND gates and one OR gate. The NOT gates are used to invert the selection lines S1 and S0. The AND gates are used to perform the product terms of the function. The OR gate is used to perform the sum of the product terms. The output Y is obtained at the output of the OR gate.

The 4:1 multiplexer can be used to implement any logic function of four variables by assigning the input data lines to the appropriate logic values. For example, to implement the function F = A.B + C.D, we can assign A0 = 0, A1 = C, A2 = B, A3 = 1 and connect the variables A and D to the selection lines S1 and S0 respectively. The output Y will then be equal to F.