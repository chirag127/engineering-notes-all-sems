# Reduced Instruction Set Computer

- A reduced instruction set computer (RISC) is a computer architecture that uses a small, highly optimized set of instructions, rather than the more specialized set often found in other types of architecture, such as in a complex instruction set computer (CISC) .
- RISC is designed to simplify the individual instructions given to the computer to accomplish tasks, and to make them execute very fast .
- RISC is the most efficient CPU architecture technology, and it is an evolution and alternative to CISC.
- RISC has the following characteristics :
  - Each instruction performs a single, well-defined operation, such as load, store, add, or branch.
  - Each instruction has a fixed length and format, which makes decoding and pipelining easier and faster.
  - Most instructions use the register-to-register (or load/store) model, where operands are either registers or memory locations, and results are stored in registers.
  - The number of registers is large, typically 32 or more, to reduce the need for accessing memory.
  - The instruction set is orthogonal, meaning that any instruction can use any register or addressing mode, without restrictions or penalties.
  - The addressing modes are simple and few, usually limited to immediate, displacement, and indexing.
  - The memory access is aligned, meaning that data must be stored and retrieved on natural boundaries (such as word or byte boundaries).
  - The control flow is based on conditional branch instructions, rather than on flags or condition codes.
- Some examples of RISC architectures are MIPS, ARM, SPARC, PowerPC, and RISC-V.