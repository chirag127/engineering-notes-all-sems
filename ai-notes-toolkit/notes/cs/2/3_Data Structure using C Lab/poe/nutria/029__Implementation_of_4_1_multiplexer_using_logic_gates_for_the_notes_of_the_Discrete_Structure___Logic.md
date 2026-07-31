
## Implementation of 4:1 Multiplexer Using Logic Gates

1. A multiplexer (MUX) is a combinational logic circuit that is used to select one of several inputs and route it to the output.
2. A 4:1 multiplexer is a multiplexer with four data inputs and one output.
3. The selection of the input is based on the value of the selection lines.
4. The logic diagram of a 4:1 multiplexer is shown below:

![Logic diagram of a 4:1 multiplexer](https://i.imgur.com/n8E9XG2.png)

5. The logic equation of a 4:1 multiplexer is given by:

$$ Y = \overline{S_0}\overline{S_1}A + \overline{S_0}S_1B + S_0\overline{S_1}C + S_0S_1D $$

6. A 4:1 multiplexer can be implemented using logic gates such as AND, OR, and NOT.
7. The logic diagram of a 4:1 multiplexer using logic gates is shown below:

![Logic diagram of a 4:1 multiplexer using logic gates](https://i.imgur.com/HxI9XdC.png)

8. The logic equation of a 4:1 multiplexer using logic gates is given by:

$$ Y = \overline{S_0}(A\overline{S_1} + B S_1) + S_0(C\overline{S_1} + D S_1) $$