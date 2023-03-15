# Bootstrapping

- Bootstrapping is the technique for producing a **self-compiling compiler** – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- A self-compiling compiler is also called a **self-hosting compiler**.
- Bootstrapping is used to create compilers for new or existing languages, or to improve the performance or features of existing compilers.
- Bootstrapping involves the following steps :
  - Stage 0: preparing an environment for the bootstrap compiler to work with. This may include writing a minimal compiler or interpreter for a subset of the source language, or using an existing compiler or interpreter for another language.
  - Stage 1: the bootstrap compiler is produced. This compiler is enough to translate its own source into a program which can run on the target platform.
  - Stage 2: a full compiler is produced by using the bootstrap compiler to compile the source code of the full compiler. This compiler may have more features or optimizations than the bootstrap compiler.
  - Stage 3: the full compiler is used to compile itself. This may result in a faster or more reliable compiler than the one produced in stage 2.
  - Stage 4: the full compiler is used to compile future versions of itself or other programs in the source language.
- Bootstrapping has several advantages, such as :
  - It allows the compiler to be written in a high-level language, which may be easier to understand, debug, and maintain than a low-level language.
  - It reduces the dependency on external tools or platforms, which may not be available or compatible with the target platform.
  - It ensures that the compiler is consistent and compatible with the source language, as it can compile itself and other programs in the same language.
  - It allows the compiler to benefit from its own optimizations and features, as it can apply them to itself and other programs in the same language.
  - It demonstrates the expressiveness and completeness of the source language, as it can implement its own compiler in the same language.