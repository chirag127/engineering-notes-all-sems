### 5. Write program to convert NFA with ε transition to NFA without ε transition.

Here are the steps to write a program that converts NFA with ε transition to NFA without ε transition:

1. Create a function to remove ε transition from the given NFA:
   - Input: An NFA with ε transition.
   - Output: An NFA without ε transition.

2. Create a function to get ε closure of a state:
   - Input: A state in the NFA.
   - Output: A set of states that can be reached from the given state by following ε transitions.

3. Create a function to get the transition table of the NFA:
   - Input: An NFA.
   - Output: A transition table that shows the transitions between states for each input symbol.

4. Create a function to create a new NFA without ε transition:
   - Input: An NFA with ε transition.
   - Output: An NFA without ε transition.

5. Call the functions in the following order to create a new NFA:
   - Get the transition table of the given NFA.
   - For each state in the NFA, get its ε closure and add it to the set of states.
   - For each state in the set of states, create a new state in the new NFA.
   - For each state in the set of states, create a new row in the transition table of the new NFA.
   - For each input symbol in the transition table, calculate the set of states that can be reached from the current state by following the input symbol and ε transition.
   - Add the calculated set of states to the transition table of the new NFA.

6. Return the new NFA without ε transition.

By following these steps, you can write a program that converts NFA with ε transition to NFA without ε transition.