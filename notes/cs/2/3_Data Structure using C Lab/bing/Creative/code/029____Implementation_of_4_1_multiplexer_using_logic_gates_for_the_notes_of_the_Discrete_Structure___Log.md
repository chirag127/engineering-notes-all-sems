## Implementation of 4:1 multiplexer using logic gates

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

![4:1 multiplexer using logic gates](https://programmerbay.com/wp-content/uploads/2020/09/4-to-1-multiplexer-using-logic-gates.png)

The circuit requires two NOT gates, four AND gates and one OR gate. The NOT gates are used to invert the selection lines S1 and S0. The AND gates are used to perform the product terms of the function. The OR gate is used to perform the sum of the product terms.

The 4:1 multiplexer can act as a universal combinational circuit, meaning that it can implement any Boolean function with four variables or less. This is because any Boolean function can be expressed in the sum of products form, and the multiplexer can select any of the product terms based on the selection lines. For example, to implement a NOT gate using a 4:1 multiplexer, we can connect the input X to A0 and A2, and connect 0 to A1 and A3. Then, the output Y will be X' when S1 = 0 and S0 = 0, and 0 otherwise. The diagram below shows the implementation of a NOT gate using a 4:1 multiplexer:

![NOT gate using 4:1 multiplexer](https://www.geeksforgeeks.org/wp-content/uploads/NOT-Gate-using-2-1-MUX.png)