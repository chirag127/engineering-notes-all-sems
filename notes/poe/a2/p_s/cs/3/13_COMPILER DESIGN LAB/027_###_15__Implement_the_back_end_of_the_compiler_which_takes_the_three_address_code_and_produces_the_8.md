 Here is the content in markdown format:

### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language.

* The back end of the compiler takes the three address code as input and produces the corresponding 8086 assembly language code as output.
* The three address code contains instructions of the form `t = t1 op t2` where `t`, `t1` and `t2` are temporary variables and `op` is the operator.
* The backend must perform the following steps:
    1. Allocate registers to temporary variables for efficiency wherever possible. Save excess temporaries in the stack.
    2. Choose appropriate 8086 instructions like `mov`, `add`, `sub`, etc. based on the operators in the three address code.
    3. Spill register variables to memory if registers get exhausted.
    4. Perform register allocation, instruction scheduling and peephole optimization for efficient code.
* Examples of translation from three address code to 8086 assembly:
    * `t3 = t1 + t2` -> `mov ax, t1; add ax, t2; mov t3, ax` (if t1 and t2 map to registers)
    * `t4 = t3 * t5` -> `mov ax, t3; imul t5; mov t4, ax`
* The produced 8086 assembly code can be assembled using an assembler to generate the machine language code for execution.
* The backend plays an important role in determining the efficiency and performance of the generated machine code. Various optimization techniques can be implemented in the backend to produce compact and fast code.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.