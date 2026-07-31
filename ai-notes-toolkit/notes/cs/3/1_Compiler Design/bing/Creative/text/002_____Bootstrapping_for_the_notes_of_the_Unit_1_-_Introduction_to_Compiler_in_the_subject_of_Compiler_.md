### Bootstrapping

- Bootstrapping is the technique for producing a **self-compiling compiler** – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- Bootstrapping is widely used in the compilation development and has several advantages, such as:
  - It allows the compiler to be written in a high-level language instead of assembly or machine code.
  - It enables the compiler to use its own features and constructs.
  - It reduces the dependency on other compilers and tools.
  - It improves the portability and maintainability of the compiler.
  - It eliminates the possibility of bugs in the compiler that are caused by another compiler.
- Bootstrapping usually involves the following stages:
  - Stage 1: the bootstrap compiler is produced. This compiler is enough to translate its own source into a program which can be executed on the target machine. At this point, all further development is done using the language defined by the bootstrap compiler, and stage 2 begins.
  - Stage 2: a full compiler is produced by the bootstrap compiler. This compiler may have additional features and optimizations that were not present in the bootstrap compiler. The full compiler is then used to compile itself, resulting in a self-hosting compiler.
  - Stage 3: (optional) the self-hosting compiler is used to compile itself again, to verify its correctness and consistency. This stage may be repeated several times to ensure that the compiler produces the same output for the same input. This is also known as the **Turing test** for compilers.