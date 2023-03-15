### Bootstrapping

- Bootstrapping is the technique for producing a self-compiling compiler – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- A self-compiling compiler is also called a self-hosting compiler.
- Bootstrapping is used to create compilers for new programming languages or to improve existing ones.
- Bootstrapping involves a series of stages, each producing a more advanced compiler.
- The stages of bootstrapping are :
  - Stage 0: preparing an environment for the bootstrap compiler to work with. This is where the source language and output language are defined, and a minimal subset of the source language is implemented in another language (usually assembly language or an existing high-level language).
  - Stage 1: the bootstrap compiler is produced. This compiler is enough to translate its own source into a program which can run on the target machine. This compiler may have limited features or optimizations, but it can compile itself and other programs written in the same subset of the source language.
  - Stage 2: a full compiler is produced by using the bootstrap compiler to compile a more advanced version of the source code. This compiler may have more features or optimizations, and it can compile itself and other programs written in the full source language.
  - Stage 3: a self-optimizing compiler is produced by using the full compiler to compile an optimized version of the source code. This compiler may have better performance or code generation, and it can compile itself and other programs written in the full source language.
- Bootstrapping has several advantages, such as :
  - It allows the compiler to be written in the same language that it compiles, which makes it easier to maintain and debug.
  - It ensures that the compiler is consistent and correct, since it can compile itself and check its own output.
  - It demonstrates the expressiveness and power of the source language, since it can implement its own compiler.
  - It enables the compiler to use its own features or optimizations, which may not be available in other languages or compilers.
- Bootstrapping also has some challenges, such as :
  - It requires a lot of effort and time to create the initial compiler and the subsequent stages.
  - It may introduce circular dependencies or inconsistencies, since the compiler depends on its own output and may change its behavior or output over time.
  - It may make it harder to port the compiler to other platforms or architectures, since the compiler may rely on specific features or assumptions of the target machine.