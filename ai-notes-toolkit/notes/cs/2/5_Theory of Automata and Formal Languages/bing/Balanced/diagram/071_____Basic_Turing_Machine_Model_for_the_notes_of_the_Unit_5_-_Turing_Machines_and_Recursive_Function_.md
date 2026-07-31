### Basic Turing Machine Model

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It was proposed by Alan Turing in 1936 as a way to study the limits of computability .

A basic Turing machine consists of the following components :

- An infinite tape divided into cells, each cell containing a symbol from a finite alphabet. The tape serves as the input and output of the machine, as well as its memory.
- A tape head that can read and write symbols on the tape, and move one cell to the left or right at a time.
- A finite set of states, one of which is designated as the initial state, and some of which are designated as accepting or rejecting states. The state represents the internal configuration of the machine.
- A transition function that specifies, for each state and tape symbol, what the machine should do next: write a new symbol on the tape, move the head left or right, and change to a new state.

The machine starts in the initial state with the input string on the tape, and the head positioned on the leftmost cell. It then follows the transition function until it reaches an accepting or rejecting state, or loops indefinitely. The output of the machine is the final tape content when it halts, or undefined if it never halts.

A Turing machine can be represented by a diagram that shows the states and the transitions between them, labeled with the tape symbols and the actions of the machine. For example, the following diagram shows a Turing machine that accepts the language of even-length palindromes over the alphabet {a, b}:

![Turing machine diagram](https://plato.stanford.edu/entries/turing-machine/fig1.png)

The diagram can be interpreted as follows:

- The machine starts in state q0 and scans the leftmost symbol of the input.
- If the symbol is a, the machine writes a on the tape, moves the head right, and goes to state q1. If the symbol is b, the machine writes b on the tape, moves the head right, and goes to state q2. If the symbol is blank, the machine accepts the input and halts.
- In state q1, the machine scans the next symbol of the input. If the symbol is a, the machine writes a on the tape, moves the head right, and stays in state q1. If the symbol is b, the machine writes b on the tape, moves the head right, and stays in state q1. If the symbol is blank, the machine moves the head left and goes to state q3.
- In state q2, the machine scans the next symbol of the input. If the symbol is a, the machine writes a on the tape, moves the head right, and stays in state q2. If the symbol is b, the machine writes b on the tape, moves the head right, and stays in state q2. If the symbol is blank, the machine moves the head left and goes to state q4.
- In state q3, the machine scans the previous symbol of the input. If the symbol is a, the machine writes a on the tape, moves the head left, and goes to state q5. If the symbol is b, the machine rejects the input and halts. If the symbol is blank, the machine rejects the input and halts.
- In state q4, the machine scans the previous symbol of the input. If the symbol is a, the machine rejects the input and halts. If the symbol is b, the machine writes b on the tape, moves the head left, and goes to state q5. If the symbol is blank, the machine rejects the input and halts.
- In state q5, the machine scans the previous symbol of the input. If the symbol is a, the machine writes a on the tape, moves the head left, and stays in state q5. If the symbol is b, the machine writes b on the tape, moves the head left, and stays in state q5. If the symbol is blank, the machine moves the head right and goes to state q0.

The machine accepts the input if it reaches the blank symbol after scanning the entire input from left to right and then from right to left, and rejects the input otherwise. For example, the machine accepts the input abba, but rejects the input aba.

A Turing machine can be used to model any computation that can be performed by a computer, as well as some computations that are not physically possible,