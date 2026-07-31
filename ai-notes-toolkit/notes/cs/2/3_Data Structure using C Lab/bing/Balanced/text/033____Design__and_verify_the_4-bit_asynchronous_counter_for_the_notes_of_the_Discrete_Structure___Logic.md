## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

An asynchronous counter is a type of binary counter that does not use a common clock signal for all the flip-flops in the circuit. Instead, each flip-flop receives the output of the previous one as its clock input, creating a ripple effect. This makes the counter simpler to design, but also slower and less reliable than a synchronous counter.

A 4-bit asynchronous counter can count from 0 to 15 (0000 to 1111 in binary) before it resets to 0. It can be implemented using four J-K flip-flops, which are logic devices that can toggle their output state depending on their inputs. The design steps of a 4-bit asynchronous counter using J-K flip-flops are as follows:

- Connect the clock pulse to the J and K inputs of the first flip-flop (A). This will make the flip-flop toggle its output (Q) every time the clock pulse goes from high to low. This output will be the least significant bit (LSB) of the counter.
- Connect the Q output of the first flip-flop (A) to the clock input of the second flip-flop (B). Also, connect the J and K inputs of the second flip-flop to logic 1. This will make the second flip-flop toggle its output (Q) every time the Q output of the first flip-flop goes from high to low. This output will be the second least significant bit of the counter.
- Repeat the same process for the third and fourth flip-flops (C and D), connecting the Q output of the previous flip-flop to the clock input of the next one, and the J and K inputs to logic 1. The Q output of the fourth flip-flop will be the most significant bit (MSB) of the counter.
- The final circuit will look like this:

![4-bit asynchronous counter circuit](https://i.imgur.com/8wZf0zT.png)

- To verify the 4-bit asynchronous counter, we can use a truth table that shows the output states of the four flip-flops for each clock pulse. The truth table will look like this:

| Clock | Q<sub>D</sub> | Q<sub>C</sub> | Q<sub>B</sub> | Q<sub>A</sub> | Count |
| ----- | ------------- | ------------- | ------------- | ------------- | ----- |
| 0     | 0             | 0             | 0             | 0             | 0     |
| 1     | 0             | 0             | 0             | 1             | 1     |
| 0     | 0             | 0             | 1             | 0             | 2     |
| 1     | 0             | 0             | 1             | 1             | 3     |
| 0     | 0             | 1             | 0             | 0             | 4     |
| 1     | 0             | 1             | 0             | 1             | 5     |
| 0     | 0             | 1             | 1             | 0             | 6     |
| 1     | 0             | 1             | 1             | 1             | 7     |
| 0     | 1             | 0             | 0             | 0             | 8     |
| 1     | 1             | 0             | 0             | 1             | 9     |
| 0     | 1             | 0             | 1             | 0             | 10    |
| 1     | 1             | 0             | 1             | 1             | 11    |
| 0     | 1             | 1             | 0             | 0             | 12    |
| 1     | 1             | 1             | 0             | 1             | 13    |
| 0     | 1             | 1             | 1             | 0             | 14    |
| 1     | 1             | 1             | 1             | 1             | 15    |
| 0     | 0             | 0             | 0             | 0             | 0     |

-