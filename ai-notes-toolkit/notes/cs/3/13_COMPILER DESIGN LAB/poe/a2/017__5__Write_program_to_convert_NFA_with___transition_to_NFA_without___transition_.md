 Here is the content in markdown format without any emojis or external links and in a formal tone:

### 5. Write program to convert NFA with ε transition to NFA without ε transition.

1. Take the input NFA with ε transitions.
2. Create a new NFA without ε transitions. This will be the output NFA.
3. For each state `q` in the input NFA:
    - If there is an ε transition from `q` to a state `p`, add a new state `q'` and transitions from `q` to `q'` and `q'` to `p`.
    - Add all other transitions from `q` to `q'`.
4. In the input NFA, replace each state `q` with the new state `q'`.
5. Repeat step #3 until there are no remaining ε transitions.
6. The resulting NFA is the required output NFA without ε transitions.

The algorithm essentially replaces each ε transition with a non-ε transition involving a new intermediate state. This ensures that the language accepted by the NFA remains unchanged while removing all ε transitions.