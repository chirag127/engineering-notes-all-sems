 Here is the content in markdown format for the given topic:

### Design Issues for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

1. Register Allocation:
- Assigning variables to machine registers to minimize the number of memory references which improves the efficiency of the generated code.
- Live variable analysis is used to determine the variables that are "live" at each point in the program and allocate registers to them.
- Graph coloring approach can be used for register allocation.

2. Instruction Selection:
- Choosing appropriate low-level instructions for the expressions in the intermediate code.
- Should optimize the instruction sequence for time and space.
- Common subexpression elimination and peephole optimization can be applied to optimize the generated code.

3. Data Flow Analysis:
- Analysis of how the values of variables change at various points in a program.
- Used for code optimization as in eliminating redundant computations and determining the correctness of the code.
- Uses data flow equations and graph reachability algorithms.

4. Code Scheduling:
- Reordering instructions to optimize the usage of processors and resources while preserving the original semantics.
- Helps to overcome dependencies between instructions and utilize parallelism using techniques like software pipelining.
- Leads to faster execution of the generated code.

5. Target Code Generation:
- Generation of final target code in the machine language of the target processor.
- Uses the information collected and decisions made in the previous steps to output the optimal sequence of instructions in the target language.
- Targets efficiency, correctness and portability of the generated code.