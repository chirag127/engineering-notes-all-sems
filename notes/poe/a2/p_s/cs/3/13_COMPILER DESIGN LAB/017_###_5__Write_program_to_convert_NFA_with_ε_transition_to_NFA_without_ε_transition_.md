 Here is the content in markdown format:

### 5. Write program to convert NFA with ε transition to NFA without ε transition.

1. Given an NFA with ε transitions, first identify all the ε transitions present in the NFA.
2. For each state `q` having an ε transition to another state `p`, introduce a new intermediate state `q'` and replace the ε transition from `q` to `p` with a regular transition from `q` to `q'` and another regular transition from `q'` to `p`.
3. This ensures that there are no more ε transitions present in the NFA. The new NFA thus obtained would be functionally equivalent to the original NFA.
4. Repeat step#2 for all the ε transitions present to convert the complete NFA with ε transitions to an NFA without any ε transitions.

**Algorithm:**
1. Identify all states `q` with outgoing ε transitions.
2. For each such state `q`, introduce a new intermediate state `q'`.
3. For each ε transition from `q` to `p`, replace it with a regular transition from `q` to `q'` and from `q'` to `p`.
4. Repeat steps 2 and 3 until there are no more ε transitions.

*The algorithm terminates since we introduce a finite number of new states (one for each ε transition).*

**Example:** Consider the NFA with ε transitions:

![NFA with Epsilon Transitions](https://www.geeksforgeeks.org/wp-content/uploads/NFA-with-Epsilon-Tran.png)

We replace ε transitions as follows:

1. ε transition from `q0` to `q1` is replaced by transitions from `q0` to a new state `q01` and from `q01` to `q1`.
2. ε transition from `q1` to `q2` is replaced by transitions from `q1` to a new state `q12` and from `q12` to `q2`.

The resulting NFA without ε transitions is:

![NFA without Epsilon Transitions](https://www.geeksforgeeks.org/wp-content/uploads/NFA-without-Epsilon-Tran.png)

**Advantages:** The major advantages of converting an NFA with ε transitions to an NFA without ε transitions are:

1. It simplifies the transition function of the NFA.
2. It makes the states of the NFA disjoint, i.e. no two states of the new NFA have the same set of possible transitions.
3. Many algorithms for NFAs work efficiently only when ε transitions are not present. So, converting an NFA with ε transitions to one without ε transitions enables us to use such algorithms.