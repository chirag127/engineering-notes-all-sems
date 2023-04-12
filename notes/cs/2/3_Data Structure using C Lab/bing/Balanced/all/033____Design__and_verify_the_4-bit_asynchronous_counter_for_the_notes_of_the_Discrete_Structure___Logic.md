## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An asynchronous counter is a sequential circuit that uses flip-flops as memory elements and changes its output state in response to the clock pulses applied to one or more of its flip-flops.
- A 4-bit asynchronous counter can count from 0 to 15 (0000 to 1111 in binary) before it returns to its initial state. It is also called a MOD-16 counter, as it has 16 distinct states.
- To design a 4-bit asynchronous counter using J-K flip-flops, the following steps are required:

  - Connect the clock input of the first flip-flop (A) to an external clock source, and connect the output of each flip-flop to the clock input of the next flip-flop in the chain (B, C, and D).
  - Connect the J and K inputs of each flip-flop to logic 1, so that they toggle on every negative edge of the clock signal.
  - Connect the output of the last flip-flop (D) to an LED or a display device to indicate the overflow condition.

- The circuit diagram of the 4-bit asynchronous counter is shown below:

```
    +-----+    +-----+    +-----+    +-----+
    | J K |    | J K |    | J K |    | J K |
    | 1 1 |    | 1 1 |    | 1 1 |    | 1 1 |
    |     |    |     |    |     |    |     |
    |  Q  |    |  Q  |    |  Q  |    |  Q  |
    |  A  |    |  B  |    |  C  |    |  D  |
    +-----+    +-----+    +-----+    +-----+
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       +----------+----------+----------+
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       +----------+----------+----------+
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       +----------+----------+----------+
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       +----------+----------+----------+
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       +----------+----------+----------+
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       |          |          |          |
       +----------+----------+----------+
       |          |          |          |
       |          |

```
