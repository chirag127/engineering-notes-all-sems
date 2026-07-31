### 5. Write program to convert NFA with ε transition to NFA without ε transition.

Converting an NFA with ε transition to an NFA without ε transition is an important step in automata theory. It involves removing the ε transitions and replacing them with the corresponding transitions that can be taken without any input symbol. Here are the steps to write a program for this conversion:

1. Define the NFA with ε transition
   - Define the number of states, the set of input symbols, the set of final states, and the transition function with ε transitions.

2. Create an NFA without ε transition
   - Define a new set of states, where each state represents a set of states from the original NFA that can be reached without consuming any input symbol.
   - Define the new set of final states based on the previous step.
   - Define the new transition function, where each transition is determined by the transitions in the original NFA.

3. Implement the algorithm for converting ε transitions to normal transitions
   - For each state in the new NFA, compute the set of states that can be reached from it without consuming any input symbol.
   - For each input symbol, compute the set of states that can be reached from the current state by consuming that input symbol.
   - Combine the two sets of states to get the set of states that can be reached by consuming the input symbol or by taking an ε transition.
   - Repeat the above steps until no new states are added to the new NFA.

4. Simplify the new NFA by removing unreachable states
   - Use the depth-first search algorithm to find all the states that can be reached from the initial state.
   - Remove all the states that cannot be reached from the initial state.

5. Output the new NFA without ε transition
   - Output the number of states, the set of input symbols, the set of final states, and the transition function without ε transitions.

By following these steps, you can write a program to convert an NFA with ε transition to an NFA without ε transition. This program is a useful tool for automata theory students to practice and understand the conversion process.