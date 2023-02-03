### 5. Write program to convert NFA with ε transition to NFA without ε transition.

The conversion of an NFA (Nondeterministic Finite Automaton) with ε-transitions to an NFA without ε-transitions is a process of eliminating the ε-transitions from the NFA. The program must implement the following steps:

1. Create a new NFA with the same states and final states as the original NFA.

2. For each state in the original NFA, find all reachable states using only ε-transitions.

3. For each state in the new NFA, add a transition from that state to each of the reachable states found in step 2.

4. Repeat steps 2 and 3 for each state in the new NFA until no new reachable states are found.

5. The resulting NFA will be an equivalent NFA without ε-transitions.

The program must be written in a programming language such as C, Java, or Python, and must be able to take the NFA with ε-transitions as input and produce the NFA without ε-transitions as output.
