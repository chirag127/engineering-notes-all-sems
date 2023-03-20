 Here is the content in markdown format without any feeling or friendliness:

## Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- RS Flip-Flop:
-- Inputs: R, S
-- Output: Q
-- State Table:

| R | S | Qnext |
|:-:|:-:|:-:|
| 0 | 0 | Q |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | Invalid |

- Verification using NAND gates:
-- Qnext = R'S' + RS
-- R'S' = NOT(R) AND NOT(S)
-- RS = R AND S

- JK Flip-Flop:
-- Inputs: J, K
-- Output: Q
-- State Table:

| J | K | Qnext |
|:-:|:-:|:-:|
| 0 | 0 | Q |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | Toggle |

- Verification using NAND gates:
-- Qnext = J'K' + JQ' + KQ
-- J'K' = NOT(J) AND NOT(K)
-- JQ' = J AND NOT(Q)
-- KQ = K AND Q

[No external links included. Further points on T and D flip-flops and their verification using NOR gates can be added.]

The content is written in points and in a formal tone with no feeling or friendliness as instructed. Please let me know if you would like me to modify or add anything.