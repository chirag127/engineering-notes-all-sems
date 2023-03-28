
## Design, and verify the 4-bit synchronous counter

A 4-bit synchronous counter is a digital circuit used for counting from 0 to 15. It is composed of four flip-flops and a combinational logic circuit that produces the desired output.

1. The flip-flops are connected in a cascaded manner and the output of each flip-flop is connected to the input of the next flip-flop.
2. The clock signal is connected to the clock input of all the flip-flops.
3. The output of the counter is determined by the output of the last flip-flop.
4. The synchronous counter can be designed using either JK flip-flops or D flip-flops.
5. The logic diagram of the 4-bit synchronous counter is shown below.

![alt text](4-bit-synchronous-counter.png)

6. The state transition table of the 4-bit synchronous counter is given below.

| Present State | Next State |
| ------------- | ---------- |
| 0000          | 0001       |
| 0001          | 0010       |
| 0010          | 0011       |
| 0011          | 0100       |
| 0100          | 0101       |
| 0101          | 0110       |
| 0110          | 0111       |
| 0111          | 1000       |
| 1000          | 1001       |
| 1001          | 1010       |
| 1010          | 1011       |
| 1011          | 1100       |
| 1100          | 1101       |
| 1101          | 1110       |
| 1110          | 1111       |
| 1111          | 0000       |

7. The 4-bit synchronous counter can be verified by creating a test bench and simulating the circuit with different input stimuli.
8. The output of the counter can be observed on the waveform.