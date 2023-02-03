### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

The ε-closure of a state in a Nondeterministic Finite Automaton (NFA) with ε transitions is the set of all states that can be reached from the original state through ε transitions. To find the ε-closure of all states in a NFA, you need to write a program that implements the algorithm for computing the ε-closure.

Here's a high-level overview of the steps involved:

1. Initialize a set to keep track of the ε-closure of each state.
2. For each state in the NFA, perform a depth-first search to find all reachable states through ε transitions.
3. Add each reachable state to the set for the original state.
4. Repeat the process for all states in the NFA.

The program should output the ε-closure of all states in the NFA, represented as a set of states for each state in the NFA.
