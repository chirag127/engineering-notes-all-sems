### Bootstrapping

- Bootstrapping is the process of creating a compiler (or assembler) using the language that it intends to compile (or assemble).
- Bootstrapping is possible because a compiler is just a program that takes some input (source code) and produces some output (target code or executable code).
- Bootstrapping can be done in several ways, such as:
  - Writing an interpreter for the source language in some other language, and then using the interpreter to run the source code of the compiler.
  - Writing a compiler for a subset of the source language in some other language, and then using the compiler to compile the rest of the compiler written in the source language.
  - Writing a cross-compiler that runs on a different platform and produces target code for the desired platform, and then using the cross-compiler to compile the compiler for the desired platform.
  - Using an existing compiler for the source language to compile the compiler, and then replacing the existing compiler with the new compiler.
- Bootstrapping has several advantages, such as:
  - It allows the compiler writer to use the features and abstractions of the source language to implement the compiler, making the development easier and faster.
  - It ensures that the compiler is consistent and compatible with the source language, avoiding errors and discrepancies that may arise from using a different language.
  - It demonstrates the expressiveness and completeness of the source language, showing that it can be used to implement any computable function, including itself.
  - It improves the performance and quality of the compiler, as the compiler can optimize and debug itself using the same techniques that it applies to other programs.