# A Language Accepted by NPDA

- A language is accepted by a non-deterministic pushdown automaton (NPDA) if there exists a sequence of transitions that leads the NPDA from the initial configuration to a final configuration for any input string in the language.
- A NPDA can accept any context-free language (CFL), but not all CFLs can be accepted by a deterministic pushdown automaton (DPDA).
- A NPDA can have multiple moves for a given input symbol and the current state, and it can also have moves without consuming any input symbol (called epsilon or lambda transitions).
- A NPDA can use the stack to store and retrieve symbols that can help it to recognize the structure of the input string.
- A NPDA can have multiple final states, or it can also accept by empty stack, or both.

## Example of a language accepted by NPDA

- Consider the language L = {a<sup>2n</sup>b<sup>n</sup> : n ≥ 0}, which consists of strings of a's followed by an equal number of b's.
- A NPDA that accepts this language is shown below:

![NPDA for L](https://i.stack.imgur.com/9j0Zs.png)

- The NPDA starts in the initial state q<sub>0</sub> with the stack symbol z. When it reads the first symbol a, it pushes two 1's on the stack (δ (q<sub>0</sub>, a, z) = { (q<sub>1</sub>, 11z)}).
- When it reads the second symbol a, it pushes two more 1's on the stack (δ (q<sub>1</sub>, a, 1) = { (q<sub>1</sub>, 111)}).
- When it reads the first symbol b, it pops one 1 from the stack (δ (q<sub>1</sub>, b, 1) = { (q<sub>1</sub>, λ)}).
- When it reads the second symbol b, it pops another 1 from the stack (δ (q<sub>1</sub>, b, 1) = { (q<sub>1</sub>, λ)}).
- When the stack becomes empty (i.e., when all the a's have been paired with b's), the NPDA transitions to the final state q<sub>f</sub> (δ (q<sub>1</sub>, λ, z) = { (q<sub>f</sub>, z)}).
- Therefore, the NPDA accepts the input string aabb by reaching a final state.