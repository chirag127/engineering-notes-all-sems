## Verification of State Tables of RS, JK, T and D Flip-Flops using NAND & NOR Gates

In the Discrete Structure & Logic Lab, it is essential to understand how to verify state tables of different flip-flops using NAND and NOR gates. Here are some key points to keep in mind:

- The RS flip-flop has two inputs - S (set) and R (reset) - and two outputs - Q and Q'. It is used to store one bit of data. The state table for an RS flip-flop can be verified using NAND gates, as follows:

| S | R | Q(t+1) |
|---|---|--------|
| 0 | 0 | Q(t)   |
| 0 | 1 | 0      |
| 1 | 0 | 1      |
| 1 | 1 | Q(t)   |

To verify this state table using NAND gates, we can use two NAND gates connected as follows:

```
    S          R          Q(t+1)
    |          |            |
    |__________|____________
       |        |
       |        |
       |        |
     __|__   ___|___
    |     | |       |
    | NAND| | NAND  | 
    |_____| |_______|
       |        |
       |        |
    Q(t)       Q'(t)
```

- The JK flip-flop is similar to the RS flip-flop, but it has a "toggle" mode in addition to the set and reset modes. The state table for a JK flip-flop can be verified using NAND gates, as follows:

| J | K | Q(t+1) |
|---|---|--------|
| 0 | 0 | Q(t)   |
| 0 | 1 | 0      |
| 1 | 0 | 1      |
| 1 | 1 | ~Q(t)  |

To verify this state table using NAND gates, we can use four NAND gates connected as follows:

```
          J          K          Q(t+1)
          |          |            |
    ______|__________|____________|______
   |       |        _|_          |      |
   |       |  ___  |   |   ___  |      |
   |       | |   | |   | |     | |      |
   |       | |NAND| |NAND| |NAND| |      |
   |       | |___| |___| |_____| |      |
   |       |         |           |      |
   |_______|_________|___________|______|
           |         |           |
         Q'(t)     Q(t)        Q'(t)
```

- The T flip-flop has a single input - T - and two outputs - Q and Q'. It toggles its output state every time T is high. The state table for a T flip-flop can be verified using NOR gates, as follows:

| T | Q(t+1) |
|---|--------|
| 0 | Q(t)   |
| 1 | ~Q(t)  |

To verify this state table using NOR gates, we can use two NOR gates connected as follows:

```
    T          Q(t+1)
    |            |
    |____________|
       |        |
       |        |
       |        |
     __|__   ___|___
    |     | |       |
    | NOR | | NOR   | 
    |_____| |_______|
       |        |
    Q(t)       Q'(t)
```

- The D flip-flop has a single input - D - and two outputs - Q and Q'. It stores the input value at the rising edge of the clock signal. The state table for a D flip-flop can be verified using NAND gates, as follows:

| D | Q(t+1) |
|---|--------|
| 0 | 0      |
| 1 | 1      |

To verify this state table using NAND gates, we can use two NAND gates connected as follows:

```
    D          Q(t+1)
    |            |
    |____________|
       |        |
       |        |
       |        |
     __|__      
    |     |     
    | NAND|     
    |_____|     
       |        
     __|__      
    |     |     
    | NAND|     
    |_____|     
       |        |
    Q(t)       Q'(t)
```

In conclusion, understanding how to verify state tables of different flip-flops using NAND and NOR gates is an essential skill for the Discrete Structure & Logic Lab. By following the above points, you can improve your understanding of these concepts and succeed in your lab assignments and exams.