Hello, I am Sydney, your AI assistant. I can help you with your topic.

To convert NFA with ε transition to NFA without ε transition, we can use the following algorithm:

1. For each state q in the NFA, find the set of states that can be reached from q by following only ε transitions. This set is called the ε-closure of q and is denoted by ε-closure(q).
2. For each state q and each input symbol a in the NFA, find the set of states that can be reached from q by following one a transition and then any number of ε transitions. This set is called the a-transition of q and is denoted by a-transition(q).
3. Construct a new NFA without ε transitions by using the same set of states and input symbols as the original NFA. For each state q and each input symbol a, add a transition from q to every state in a-transition(q) in the new NFA. The initial state and the final states of the new NFA are the same as the original NFA.
4. If the original NFA has more than one initial state, create a new initial state and add ε transitions from the new initial state to all the original initial states. Then apply the above algorithm to the modified NFA.

Here is an example of applying the algorithm to an NFA with ε transitions:

![NFA with ε transitions](https://i.imgur.com/8Zl0ZtH.png)

The ε-closures and a-transitions of each state are:

- ε-closure(q0) = {q0, q1, q2}
- ε-closure(q1) = {q1}
- ε-closure(q2) = {q2, q3}
- ε-closure(q3) = {q3}
- a-transition(q0) = {q1, q2, q3}
- a-transition(q1) = {q1}
- a-transition(q2) = {q2, q3}
- a-transition(q3) = {q3}
- b-transition(q0) = {q1, q2, q3}
- b-transition(q1) = {q1}
- b-transition(q2) = {q2, q3}
- b-transition(q3) = {q3}

The new NFA without ε transitions is:

![NFA without ε transitions](https://i.imgur.com/9y7X0yL.png)