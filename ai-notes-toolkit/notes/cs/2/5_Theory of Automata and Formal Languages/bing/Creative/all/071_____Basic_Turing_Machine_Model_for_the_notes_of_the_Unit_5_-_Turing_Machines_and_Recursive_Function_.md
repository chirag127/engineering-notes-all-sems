# Basic Turing Machine Model

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It was invented by Alan Turing in 1936 to study the limits of computability.

A basic Turing machine consists of the following components :

- An **infinite tape** divided into cells, each cell containing a symbol from a finite alphabet. The tape serves as the input, output and memory of the machine.
- A **tape head** that can read and write symbols on the tape, and move one cell to the left or right at a time.
- A **finite state control** that stores the current state of the machine, and determines the next action based on the current state and the symbol read by the tape head.
- A **transition function** that specifies the rules for changing the state, writing a symbol and moving the tape head, given the current state and symbol.
- A **start state** that indicates the initial state of the machine before any computation.
- A **halt state** that indicates the termination of the computation.

A Turing machine operates as follows :

- The input string is placed on the tape, starting from the leftmost cell, and the rest of the tape is filled with a blank symbol.
- The tape head is positioned on the leftmost cell of the input, and the state control is set to the start state.
- The machine reads the symbol under the tape head, and consults the transition function to determine the next state, the symbol to write, and the direction to move the tape head.
- The machine updates the tape, the state control and the tape head according to the transition function.
- The machine repeats steps 3 and 4 until it reaches the halt state, or until it encounters an undefined transition.
- The output of the machine is the string on the tape after the computation ends, or the fact that the machine does not halt.

The following diagram illustrates a basic Turing machine model:

![A basic Turing machine model](https://www.tutorialspoint.com/automata_theory/images/turing_machine.jpg)

: https://www.tutorialspoint.com/automata_theory/turing_machine_introduction.htm
: https://www.javatpoint.com/automata-basic-model-of-turing-machine
: https://en.wikipedia.org/wiki/Turing_machine
: https://plato.stanford.edu/entries/turing-machine/
: https://www.britannica.com/technology/Turing-machine