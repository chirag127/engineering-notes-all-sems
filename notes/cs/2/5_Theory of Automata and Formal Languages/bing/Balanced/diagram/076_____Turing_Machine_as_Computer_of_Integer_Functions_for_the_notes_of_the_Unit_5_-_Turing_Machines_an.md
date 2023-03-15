### Turing Machine as Computer of Integer Functions

- A Turing machine is a simple abstract computational device that can perform any computation that can be done by a mechanical procedure.
- A Turing machine can compute functions of the form y = f(x), where x and y are integers or pairs of integers .
- To compute a function, a Turing machine needs to have an input tape, an output tape, a finite control, and a read-write head.
- The input tape contains the value of x, encoded in some way, such as binary or unary. The output tape is initially blank and will contain the value of y after the computation. The finite control is a set of states and transitions that determine the behavior of the machine. The read-write head can move along the tapes, read symbols, and write symbols.
- The computation starts with the read-write head at the leftmost position of the input tape, and the finite control in the initial state. The machine follows the transitions based on the current state and the symbol read from the input tape. The machine can write a symbol on the output tape, move the read-write head left or right on either tape, or halt. The machine halts when it reaches a final state or when there is no transition defined for the current state and symbol.
- The computation is successful if the machine halts and the output tape contains the value of y, encoded in the same way as x. The computation is unsuccessful if the machine does not halt or the output tape does not contain the correct value.
- For example, to compute the function y = x + 1, where x and y are positive integers encoded in unary, a Turing machine can use the following finite control:

| State | Symbol read | Symbol written | Head movement | Next state |
| ----- | ----------- | -------------- | ------------- | ---------- |
| q0    | 1           | 1              | Right         | q0         |
| q0    | Blank       | 1              | Right         | q1         |
| q1    | Blank       | Blank          | Left          | q2         |
| q2    | 1           | 1              | Left          | q2         |
| q2    | Blank       | Blank          | Right         | Halt       |

- The machine starts with the input tape containing x ones, such as 111 for x = 3, and the output tape blank. The machine scans the input tape from left to right, copying each one to the output tape. When it reaches the end of the input tape, it writes one more one on the output tape, and then moves back to the leftmost position of the output tape. The machine halts and the output tape contains y ones, such as 1111 for y = 4.
- A Turing machine can compute any function that can be computed by a mechanical procedure, and vice versa. This is known as the Church-Turing thesis . There is no known model of computation more powerful than Turing machines.