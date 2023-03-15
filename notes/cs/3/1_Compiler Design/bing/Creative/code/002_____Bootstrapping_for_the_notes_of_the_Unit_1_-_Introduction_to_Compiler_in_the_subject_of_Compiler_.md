# Bootstrapping

- Bootstrapping is the technique for producing a self-compiling compiler – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- Bootstrapping is used to produce a self-hosting compiler – that is, a compiler that can compile its own source code.
- Bootstrapping involves the following steps:
  - Step 1: Write a compiler for a small subset of the source language in assembly language. This is called the bootstrap compiler.
  - Step 2: Write a compiler for the full source language using the subset of the source language. This is called the second compiler.
  - Step 3: Compile the second compiler using the bootstrap compiler. This produces the full compiler in assembly language.
  - Step 4: Compile the second compiler using the full compiler. This produces the full compiler in the source language.
- Bootstrapping has the following advantages:
  - It simplifies the development and maintenance of the compiler, as the source language is more expressive and easier to work with than assembly language.
  - It allows the compiler to use the features and libraries of the source language, which can improve the performance and portability of the compiler.
  - It demonstrates the expressiveness and completeness of the source language, as it can implement its own compiler.
- Bootstrapping has the following challenges:
  - It requires a bootstrap compiler to start the process, which can be difficult to write and debug in assembly language.
  - It can introduce errors or inconsistencies in the compiler, as the bootstrap compiler and the second compiler may have different behaviors or assumptions.
  - It can make the compiler dependent on the source language, which can limit the flexibility and extensibility of the compiler.