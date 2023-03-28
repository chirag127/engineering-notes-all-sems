
## Implementing 4x1 and 8x1 MULTIPLEXERS 

The Computer Organization Lab in the subject of Computer Organization requires the implementation of 4x1 and 8x1 MULTIPLEXERS. 

1. A multiplexer is a digital circuit that selects one of several input signals and forwards it to the output. 
2. A 4x1 multiplexer has four data inputs (D0, D1, D2, and D3) and one output (Y). 
3. A 4x1 multiplexer also has two select inputs (S0 and S1). 
4. The select inputs are used to select which of the four data inputs is sent to the output. 
5. An 8x1 multiplexer is similar to a 4x1 multiplexer, but with eight data inputs (D0, D1, D2, D3, D4, D5, D6, and D7) and three select inputs (S0, S1, and S2). 
6. The select inputs are used to select which of the eight data inputs is sent to the output. 
7. The truth table of a 4x1 multiplexer is as follows: 

| S1 | S0 | D3 | D2 | D1 | D0 | Y  |
|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | D0 |
| 0  | 1  | 0  | 0  | 0  | 1  | D1 |
| 1  | 0  | 0  | 1  | 0  | 0  | D2 |
| 1  | 1  | 0  | 1  | 0  | 1  | D3 |

8. The truth table of an 8x1 multiplexer is as follows: 

| S2 | S1 | S0 | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Y  |
|----|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | D0 |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | D1 |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | D2 |
| 0  | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  | D3 |
| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | D4 |
| 1  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 1  | D5 |
| 1  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 0  | D6 |
| 1  | 1  | 1  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 1  | D7 |