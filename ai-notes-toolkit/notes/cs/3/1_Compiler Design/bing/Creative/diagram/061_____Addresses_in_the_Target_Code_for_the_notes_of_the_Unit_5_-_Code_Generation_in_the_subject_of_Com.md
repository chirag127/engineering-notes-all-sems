### Addresses in the Target Code

- Addresses in the target code are the locations where the values of variables, constants, temporaries, and parameters are stored in the memory or registers of the target machine.
- Addresses in the target code are determined by the code generator, which is the final phase of the compiler.
- Addresses in the target code depend on the target machine architecture, the intermediate code representation, and the code optimization techniques.
- Addresses in the target code can be classified into four categories: absolute, relative, indirect, and register.
  - Absolute addresses are fixed locations in the memory, such as global variables or constants.
  - Relative addresses are offsets from a base address, such as local variables or parameters in a stack frame.
  - Indirect addresses are pointers to other addresses, such as dynamic arrays or linked lists.
  - Register addresses are names of the registers in the target machine, such as temporaries or frequently used variables.
- Addresses in the target code can be represented by three-address code, which is a form of intermediate code that uses at most three operands for each instruction.
  - Three-address code can be implemented by quadruples, triples, or indirect triples, which are different ways of storing and accessing the operands and the operator of each instruction.
  - Three-address code can be translated into target code by using registers to store the operands and by generating assembly-level instructions for each operator.
  - Three-address code can be optimized by using techniques such as common subexpression elimination, copy propagation, dead code elimination, and register allocation.