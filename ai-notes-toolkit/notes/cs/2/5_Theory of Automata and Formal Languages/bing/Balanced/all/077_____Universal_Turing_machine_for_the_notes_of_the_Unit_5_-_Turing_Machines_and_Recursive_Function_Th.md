# Universal Turing machine

- A universal Turing machine (UTM) is a Turing machine that can simulate any other Turing machine on any input.
- A UTM essentially achieves this by reading both the description of the machine to be simulated and the input to that machine from its own tape .
- A UTM can also compute everything that a real computer can compute. For example, a UTM can simulate any function used in a programming language.
- A UTM was introduced by Alan Turing in 1936-1937 as a mathematical tool to investigate the extent and limitations of what can be computed.
- A UTM can also be used to prove the undecidability of some problems, such as the halting problem. The halting problem asks whether there exists an algorithm that can determine, given any Turing machine and any input, whether the machine will eventually halt or run forever.
- A UTM can be constructed from a finite number of states and symbols, depending on the encoding scheme used for the descriptions of the machines and the inputs. For example, one possible UTM has 22 states and 18 symbols.
- A UTM can be represented by a transition table, a transition diagram, or a set of instructions, similar to any other Turing machine.
- A UTM operates by reading the description of the machine to be simulated and the input to that machine from the left end of the tape, and then executing the instructions of the simulated machine on the input, using the rest of the tape as its work area.
- A UTM can be modified to accept multiple inputs, output the results of the simulation, or perform other tasks, by adding more states and symbols to the original UTM.