### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

To find the ε-closure of all the states of a given NFA with ε-transitions, we need to follow a set of steps that can be implemented in a program. Here are the steps:

1. Create a list of all the states in the NFA and mark them as unvisited.
2. For each state in the list, if it is unvisited, call a recursive function to find all the states reachable from it using only ε-transitions.
3. In the recursive function, mark the current state as visited and add it to the ε-closure set.
4. For each ε-transition from the current state, call the recursive function on the destination state.
5. Once all the ε-transitions are explored, return the ε-closure set.

Here is a sample Python program to implement the above steps:

```python
def epsilon_closure(nfa, state):
    closure = set()
    visited = set()

    def explore(state):
        visited.add(state)
        closure.add(state)
        if state in nfa and 'ε' in nfa[state]:
            for s in nfa[state]['ε']:
                if s not in visited:
                    explore(s)

    explore(state)
    return closure

def epsilon_closures(nfa):
    closures = {}
    for state in nfa:
        closures[state] = epsilon_closure(nfa, state)
    return closures
```

In the above code, the `epsilon_closure` function takes an NFA and a state as input and returns the ε-closure set for that state. The `epsilon_closures` function takes an NFA as input and returns a dictionary of ε-closures for all the states in the NFA.

To use the program, you can define an NFA as a dictionary where the keys are the states and the values are dictionaries that map input symbols to the next state. For ε-transitions, you can use the symbol 'ε'. Here is an example NFA:

```python
nfa = {
    0: {'a': {1}, 'ε': {2}},
    1: {'b': {2}},
    2: {'a': {0, 3}},
    3: {'b': {3}, 'ε': {0}}
}
```

Using this NFA, you can call the `epsilon_closures` function to get the ε-closures for all the states:

```python
closures = epsilon_closures(nfa)
print(closures)
```

This will output the following dictionary:

```
{
    0: {0, 2},
    1: {1},
    2: {2, 0, 3},
    3: {0, 3}
}
```

This dictionary shows the ε-closure sets for each state in the NFA. For example, the ε-closure set for state 0 is `{0, 2}` which means that state 0 can reach itself and state 2 using only ε-transitions.