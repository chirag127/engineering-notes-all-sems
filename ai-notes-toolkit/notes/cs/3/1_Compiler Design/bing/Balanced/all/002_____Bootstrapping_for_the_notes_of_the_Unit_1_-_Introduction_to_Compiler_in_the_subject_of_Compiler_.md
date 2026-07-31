# Bootstrapping

- Bootstrapping is the technique for producing a self-compiling compiler – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- A self-compiling compiler is also called a self-hosting compiler.
- Bootstrapping is used to create a programming language that is compiled with itself.
- Bootstrapping involves the following steps:
  - Stage 0: Preparing an environment for the bootstrap compiler to work with. This is where the source language and output language are defined, and a minimal compiler is written in assembly language or another low-level language.
  - Stage 1: The bootstrap compiler is produced. This compiler is enough to translate its own source into a program which can compile itself.
  - Stage 2: A full compiler is produced by using the bootstrap compiler to compile a more advanced version of the source code, which may include features that are not supported by the bootstrap compiler.
  - Stage 3: The full compiler is used to compile itself, producing an optimized and self-contained compiler.
- Bootstrapping has several advantages, such as:
  - It allows the compiler to be written in a high-level language, which makes it easier to maintain and debug.
  - It ensures that the compiler is consistent and correct, since it can compile itself and produce the same output.
  - It enables the compiler to use the features of the language that it compiles, which may improve the performance and functionality of the compiler.
  - It demonstrates the expressiveness and completeness of the language that it compiles, since it can implement its own compiler.