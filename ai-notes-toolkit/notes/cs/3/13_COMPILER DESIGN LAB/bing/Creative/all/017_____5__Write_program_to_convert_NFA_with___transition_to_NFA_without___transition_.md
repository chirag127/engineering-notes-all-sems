# 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transition is a nondeterministic finite automaton that can make transitions without consuming any input symbol, denoted by ε. An NFA without ε transition is a nondeterministic finite automaton that can only make transitions by consuming input symbols.

To convert an NFA with ε transition to an NFA without ε transition, we can use the following algorithm:

- For each state q in the NFA with ε transition, compute ε-closure(q), which is the set of states that can be reached from q by following only ε transitions.
- For each state q in the NFA with ε transition, and for each input symbol a, compute the transition function δ'(q, a) as follows:
  - δ'(q, a) = ∪{δ(p, a) | p ∈ ε-closure(q)}, where δ(p, a) is the set of states that can be reached from p by consuming a in the NFA with ε transition.
- The NFA without ε transition has the same set of states and final states as the NFA with ε transition, but the transition function is δ' instead of δ.
- The initial state of the NFA without ε transition is ε-closure(q0), where q0 is the initial state of the NFA with ε transition.

Here is a pseudocode for the algorithm:

```
function convert(NFA with ε transition):
  NFA without ε transition = new NFA()
  NFA without ε transition.states = NFA with ε transition.states
  NFA without ε transition.final_states = NFA with ε transition.final_states
  NFA without ε transition.initial_state = ε-closure(NFA with ε transition.initial_state)
  for each state q in NFA without ε transition.states:
    for each input symbol a in NFA without ε transition.alphabet:
      NFA without ε transition.transition_function[q, a] = ∅
      for each state p in ε-closure(q):
        NFA without ε transition.transition_function[q, a] = NFA without ε transition.transition_function[q, a] ∪ NFA with ε transition.transition_function[p, a]
  return NFA without ε transition
```