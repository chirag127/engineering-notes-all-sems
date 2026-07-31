# Design and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An asynchronous counter is a type of binary counter that does not use a common clock signal for all the flip-flops in the circuit. Instead, each flip-flop is triggered by the output of the previous one, creating a ripple effect. This makes the counter simpler to design, but also slower and less reliable than a synchronous counter.
- A 4-bit asynchronous counter can count from 0 to 15 (0000 to 1111 in binary) before it resets to 0. It can be implemented using four J-K flip-flops, which are edge-triggered devices that can toggle, set, reset, or hold their output depending on the inputs J and K.
- The design steps of a 4-bit asynchronous counter using J-K flip-flops are as follows:
  - Connect the clock input of the first flip-flop (A) to an external clock source, and the clock inputs of the other flip-flops (B, C, and D) to the Q outputs of the previous flip-flops. This creates a chain of flip-flops that are triggered by the output changes of the previous ones.
  - Connect the J and K inputs of all the flip-flops to logic 1 (HIGH). This ensures that the flip-flops will toggle their output on every negative edge of the clock signal.
  - Connect the Q outputs of the flip-flops to LEDs or other devices to display the count value.
- The circuit diagram of a 4-bit asynchronous counter using J-K flip-flops is shown below:

![4-bit asynchronous counter circuit diagram](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-asynchronous-up-counter-using-J-K-flip-flop.png)

- The truth table of a 4-bit asynchronous counter using J-K flip-flops is shown below:

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

- The verification of a 4-bit asynchronous counter using J-K flip-flops can be done by simulating the circuit using software tools such as Logisim or Proteus, or by building the circuit using hardware components such as ICs, breadboards, and LEDs. The verification steps are as follows:
  - Apply