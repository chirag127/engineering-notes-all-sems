# Universal Turing machine

- A universal Turing machine (UTM) is a Turing machine that can simulate an arbitrary Turing machine on arbitrary input .
- A UTM essentially achieves this by reading both the description of the machine to be simulated as well as the input to that machine from its own tape .
- A UTM can be used to model the notion of computability, as any function that can be computed by a Turing machine can also be computed by a UTM.
- A UTM can also be used to study the properties and limitations of Turing machines, such as decidability, undecidability, and complexity.
- A UTM can be constructed from a simple Turing machine by adding a special symbol to the tape alphabet, such as #, to separate the description of the machine to be simulated from the input to that machine.
- A UTM can then use a finite set of rules to decode the description of the machine to be simulated and execute its transitions on the input, while keeping track of the current state and head position of the simulated machine.
- A UTM can also be designed to accept a standard encoding of Turing machines, such as the Gödel number, and use a universal function to decode and simulate them.
- A UTM is not more powerful than any other Turing machine, as it can only compute what is computable, but it is more versatile and convenient, as it can simulate any Turing machine with a single fixed program.