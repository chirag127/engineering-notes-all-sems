### Basic Turing Machine Model

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It was invented by Alan Turing in 1936 to study the limits of computability.

A basic Turing machine consists of the following components :

- An infinite tape divided into cells, each cell containing a symbol from a finite alphabet. The tape serves as the input and output of the machine.
- A tape head that can read and write symbols on the tape, and move one cell to the left or right at a time.
- A finite set of states, one of which is the initial state and some of which are accepting or rejecting states. The state of the machine determines its behavior at each step.
- A transition function that specifies, for each state and tape symbol, what the machine should do next: write a new symbol, move the head, and change the state.

The machine starts in the initial state with the input string on the tape, and the head positioned on the leftmost cell. It then follows the transition function until it reaches an accepting or rejecting state, or loops indefinitely. The output of the machine is the final configuration of the tape, or undefined if the machine does not halt.

The following diagram illustrates the basic model of a Turing machine:

![Turing machine diagram](https://plato.stanford.edu/entries/turing-machine/turing-machine.png)

: Turing machine - Wikipedia
: Turing Machine Introduction - tutorialspoint.com
: Turing Machines - Stanford Encyclopedia of Philosophy
: Turing machine | Definition & Facts | Britannica