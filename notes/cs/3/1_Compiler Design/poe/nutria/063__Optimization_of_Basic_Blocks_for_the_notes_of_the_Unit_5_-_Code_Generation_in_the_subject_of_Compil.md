
### Optimization of Basic Blocks for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

* Basic blocks are sequences of instructions with no branches in except at the end. 
* Optimizing basic blocks involves removing redundant instructions, rearranging instructions to take advantage of instruction-level parallelism, and improving data locality.
* Redundant instructions can often be removed by recognizing common subexpressions and eliminating duplicates.
* Rearranging instructions can increase instruction-level parallelism by allowing instructions to be executed in parallel. 
* Improving data locality involves reordering instructions to reduce cache misses.
* The goal of basic block optimization is to reduce the number of instructions in a basic block and to improve the execution time of the block.