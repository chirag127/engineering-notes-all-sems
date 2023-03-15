### Basic Turing Machine Model

A Turing machine is a theoretical computing machine invented by Alan Turing in 1936 to serve as an idealized model for mathematical calculation. A Turing machine consists of:

1. A tape divided into cells, one next to the other. Each cell contains a symbol from some finite alphabet. The alphabet contains a special blank symbol and one or more other symbols. The tape is assumed to be arbitrarily extendable to the left and to the right, i.e., the Turing machine is always supplied with as much tape as it needs for its computation.
2. A head that can read and write symbols on the tape and move left and right.
3. A state register that stores the state of the Turing machine, one of finitely many. Among these is the special start state with which the state register is initialized. These states, writes Turing, replace the "state of mind" a person performing a computation would ordinarily be in.
4. A finite table of instructions that tells the machine what to do based on the current symbol it is reading from the tape and the current state it is in. The table tells the machine to do the following in sequence for each entry (current symbol, current state):
    - Erase or write a symbol.
    - Move the head one cell to the left or right.
    - Assume the same or a new state as prescribed.

The Turing machine is capable of processing an unrestricted grammar, which further implies that it is capable of robustly evaluating first-order logic in an infinite number of ways. This is famously demonstrated through lambda calculus. A Turing machine that is able to simulate any other Turing machine is called a universal Turing machine (UTM, or simply a universal machine). A more mathematically oriented definition with a similar "universal" nature was introduced by Alonzo Church, whose work on lambda calculus intertwined with Turing's in a formal theory of computation known as the Church–Turing thesis. The thesis states that Turing machines indeed capture the informal notion of effective methods in logic and mathematics, and provide a precise definition of an algorithm or "mechanical procedure". Studying their abstract properties yields many insights into computer science and complexity theory.