### Bootstrapping

Bootstrapping is the process of creating a self-sustaining system that is capable of performing a task without external input. In the context of compiler design, bootstrapping refers to the process of writing a compiler for a programming language in that same language.

Here are some key points to remember about bootstrapping in compiler design:

1. Bootstrapping is used to create a self-hosting compiler, which is a compiler that is written in the same language that it compiles.
2. The first step in bootstrapping a compiler is to write a minimal compiler in a different language. This minimal compiler is used to compile the source code of the full compiler written in the target language.
3. Once the full compiler is compiled, it can be used to compile its own source code, creating a self-sustaining system.
4. Bootstrapping can be used to develop compilers for new programming languages, as well as to improve existing compilers by rewriting them in the language they compile.
5. Bootstrapping can also be used to port a compiler to a new platform by using an existing compiler to compile the source code of the new compiler for the target platform.

In summary, bootstrapping is an important concept in compiler design that allows for the creation of self-sustaining compilers that can be used to develop and improve programming languages. It involves writing a minimal compiler in a different language, using it to compile the full compiler written in the target language, and then using the full compiler to compile its own source code. This creates a self-hosting compiler that can be used to develop and improve the language it compiles.