## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

An asynchronous counter is a sequential circuit that uses a series of flip-flops to generate a binary count. The output of one flip-flop drives the clock input of the next flip-flop. Each flip-flop changes state at the falling edge of the previous flip-flop's output, creating a ripple effect. 

A 4-bit asynchronous counter can count from 0 to 15, or in binary from 0000 to 1111. It can be designed using four J-K flip-flops, as shown in the following diagram:

![4-bit asynchronous counter using J-K flip-flops](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-asynchronous-counter-using-J-K-flip-flop.png)

The design steps are as follows:

- The first flip-flop (A) is connected to the external clock signal and toggles on every negative edge of the clock.
- The second flip-flop (B) is connected to the Q output of the first flip-flop and toggles on every negative edge of Q_A.
- The third flip-flop (C) is connected to the Q output of the second flip-flop and toggles on every negative edge of Q_B.
- The fourth flip-flop (D) is connected to the Q output of the third flip-flop and toggles on every negative edge of Q_C.
- All the J and K inputs of the flip-flops are connected to logic 1, which means that they will always toggle when the clock input changes from high to low.
- The outputs of the flip-flops are labeled as Q_A, Q_B, Q_C, and Q_D, which form the 4-bit binary count.

The truth table for the 4-bit asynchronous counter is as follows:

| Clock | Q_A | Q_B | Q_C | Q_D | Count |
| ----- | --- | --- | --- | --- | ----- |
| 0     | 0   | 0   | 0   | 0   | 0     |
| 1     | 0   | 0   | 0   | 0   | 0     |
| 0     | 1   | 0   | 0   | 0   | 1     |
| 1     | 1   | 0   | 0   | 0   | 1     |
| 0     | 0   | 1   | 0   | 0   | 2     |
| 1     | 0   | 1   | 0   | 0   | 2     |
| 0     | 1   | 1   | 0   | 0   | 3     |
| 1     | 1   | 1   | 0   | 0   | 3     |
| 0     | 0   | 0   | 1   | 0   | 4     |
| 1     | 0   | 0   | 1   | 0   | 4     |
| 0     | 1   | 0   | 1   | 0   | 5     |
| 1     | 1   | 0   | 1   | 0   | 5     |
| 0     | 0   | 1   | 1   | 0   | 6     |
| 1     | 0   | 1   | 1   | 0   | 6     |
| 0     | 1   | 1   | 1   | 0   | 7     |
| 1     | 1   | 1   | 1   | 0   | 7     |
| 0     | 0   | 0   | 0   | 1   | 8     |
| 1     | 0   | 0   | 0   | 1   | 8     |
| 0     | 1   | 0   | 0   | 1   | 9     |
| 1     | 1   | 0   | 0   | 1   | 9     |
| 0     | 0   | 1