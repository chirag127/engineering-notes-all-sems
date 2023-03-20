 Here is the content in markdown format without any emojis or external links and in a formal tone:

### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

1. Take the input NFA with ε transitions. Represent it using adjacency list.
2. Initialize a stack and push the start state of NFA to stack. This stack will be used to store the states whose ε-closures are yet to be found.
3. While stack is not empty:

- Pop a state from stack. If ε-closure of this state is not calculated then:

- Mark this state as visited.
- Get all neighbouring states of the popped state. If a neighbouring state is not visited and it is reachable through ε transition then push it to the stack.
- Include the neighbouring states in the ε-closure of popped state.

4. Repeat step#3 until stack becomes empty. This will calculate ε-closure of all states of given NFA.
5. Print the ε-closure of all states.

The above program calculates ε-closure of all states of a given NFA with ε transitions. The time complexity of the program is O(V+E) where V is number of states and E is number of transitions in NFA.

Does this content fulfill the given requirements? Let me know if you would like me to modify or expand the content in any way.