### Bootstrapping

- Bootstrapping is the technique for producing a **self-compiling compiler** – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- A self-compiling compiler is also called a **self-hosting compiler**.
- Bootstrapping is used to create a programming language that is compiled with itself.
- Bootstrapping involves the following steps:
  - Stage 0: Preparing an environment for the bootstrap compiler to work with. This is where the source language and output language are defined, and a minimal set of features are implemented.
  - Stage 1: The bootstrap compiler is produced. This compiler is enough to translate its own source into a program which can compile itself.
  - Stage 2: A full compiler is produced by using the bootstrap compiler to compile its own source code. This compiler may have more features and optimizations than the bootstrap compiler.
  - Stage 3: The full compiler is used to compile itself again, to ensure that the output is consistent and correct.
- Bootstrapping has several advantages:
  - It simplifies the development and maintenance of the compiler, as the source code is written in a high-level language instead of a low-level language.
  - It allows the compiler to use the features and libraries of the source language, which may not be available in the output language.
  - It demonstrates the expressiveness and completeness of the source language, as it can implement its own compiler.
  - It increases the portability and compatibility of the compiler, as it can run on any platform that supports the output language.
- Bootstrapping also has some challenges:
  - It requires a careful design and implementation of the bootstrap compiler, as it has to be able to compile itself and the full compiler.
  - It may introduce circular dependencies and inconsistencies between the bootstrap compiler and the full compiler, which have to be resolved by testing and debugging.
  - It may increase the complexity and size of the compiler, as it has to include the source code of itself and the full compiler.