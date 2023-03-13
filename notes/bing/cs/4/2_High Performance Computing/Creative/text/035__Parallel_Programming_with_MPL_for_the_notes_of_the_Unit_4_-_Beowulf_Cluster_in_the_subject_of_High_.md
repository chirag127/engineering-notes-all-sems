### Parallel Programming with MPL

- MPL stands for **MaPLe**, a compiler for parallel programming on shared-memory multicore machines .
- The MPL language is essentially **Standard ML (SML)** with extensions for parallelism .
- SML is a **functional programming language** that supports **higher-order functions**, **pattern matching**, **algebraic data types**, **modules**, and **exceptions**.
- MPL extends SML with **fork-join parallelism**, which allows the programmer to create and synchronize parallel tasks using the **par** and **sync** constructs .
- MPL also supports **parallel arrays**, which are arrays that can be manipulated in parallel using **map**, **reduce**, **scan**, **filter**, and **zip** operations .
- MPL generates executables with excellent multicore performance, utilizing a novel approach to memory management based on the theory of **disentanglement**.
- Disentanglement is a property of parallel programs that ensures that **no two parallel tasks access the same memory location**.
- MPL uses a **static type system** and a **whole-program analysis** to check the disentanglement property at compile time.
- MPL also provides a **dynamic check** for disentanglement using a **runtime system** that tracks the memory regions accessed by each parallel task.
- MPL is compatible with the **MLton compiler** for SML, which means that MPL programs can use the **MLton libraries** and **foreign function interface**.
- MPL is an open-source project hosted on GitHub , where the source code, documentation, and tutorials are available.