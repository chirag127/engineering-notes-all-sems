
### Equivalence of NFA’s with and without ε-Transition 

1. Non-deterministic finite automata (NFA) are machines that can take multiple paths to reach a final state. 
2. NFA's can be further divided into two types - those with ε-transitions, and those without. 
3. NFA's with ε-transitions are machines that can transition from one state to another without consuming any input symbols. 
4. NFA's without ε-transitions are machines that can only transition from one state to another by consuming input symbols. 
5. It is possible to convert an NFA with ε-transitions into an NFA without ε-transitions. 
6. This conversion is done by introducing additional states and transitions, so that the resulting NFA without ε-transitions is equivalent to the original NFA with ε-transitions. 
7. The conversion process involves the following steps: 
    * Identify all the ε-transitions in the original NFA.
    * Replace each ε-transition with a series of transitions that do not involve ε-transitions.
    * Add additional states to the NFA, as needed.
8. The resulting NFA without ε-transitions is equivalent to the original NFA with ε-transitions.