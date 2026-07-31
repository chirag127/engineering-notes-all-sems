### Turing Machine as Computer of Integer Functions

- A Turing machine is a theoretical model of computation that can perform any algorithmic task given enough time and space.
- A Turing machine consists of a finite set of states, a finite alphabet of symbols, a tape divided into cells that can store symbols, a tape head that can read and write symbols and move left or right, and a transition function that determines the next state, symbol, and head movement based on the current state and symbol.
- A Turing machine can compute functions that map integers or pairs of integers to integers, such as addition, multiplication, factorial, etc .
- To compute a function f(x) or f(x,y) with a Turing machine, the following steps are followed:
  - The input x or (x,y) is encoded as a string of symbols on the tape, using a suitable encoding scheme, such as unary, binary, decimal, etc.
  - The Turing machine is started in an initial state and scans the input from left to right, performing transitions according to the transition function.
  - The Turing machine eventually halts in a final state and replaces the input with the output f(x) or f(x,y) on the tape, using the same encoding scheme as the input.
  - The Turing machine returns the tape head to the beginning of the output and stops.
- For example, to compute the function f(x) = x + 1 using a unary encoding scheme, where each integer is represented by a string of 1s of the same length, the following Turing machine can be used:

  - States: {q0, q1, q2, q3, q4}
  - Alphabet: {1, B} (B is the blank symbol)
  - Initial state: q0
  - Final state: q4
  - Transition function:

| Current state | Current symbol | Next state | Next symbol | Head movement |
|---------------|----------------|------------|-------------|---------------|
| q0            | 1              | q0         | 1           | Right         |
| q0            | B              | q1         | B           | Right         |
| q1            | 1              | q2         | B           | Left          |
| q1            | B              | q4         | 1           | Left          |
| q2            | 1              | q3         | 1           | Left          |
| q2            | B              | q4         | B           | Left          |
| q3            | 1              | q2         | 1           | Left          |
| q3            | B              | q4         | B           | Left          |

  - Example input/output:

| Input | Output |
|-------|--------|
| 111   | 1111   |
| 1     | 11     |
| 11111 | 111111 |

- A Turing machine can compute any function that is computable, meaning that there exists an algorithm that can produce the output for any given input in a finite number of steps .
- A function that is not computable is called uncomputable or undecidable, meaning that there is no algorithm that can always produce the correct output for any given input .
- Examples of uncomputable functions are the halting problem, which asks whether a given Turing machine will halt on a given input, and the busy beaver problem, which asks for the maximum number of 1s that a Turing machine with a given number of states can print on a blank tape before halting .