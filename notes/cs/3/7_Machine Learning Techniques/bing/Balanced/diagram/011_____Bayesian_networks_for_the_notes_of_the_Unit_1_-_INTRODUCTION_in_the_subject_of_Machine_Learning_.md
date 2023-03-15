### Bayesian networks

- Bayesian networks are a type of **probabilistic graphical model** that can be used to build models from data and/or expert opinion .
- They represent a set of **variables** and their **conditional dependencies** via a **directed acyclic graph (DAG)**  .
- They can be used for a wide range of tasks including **diagnostics, reasoning, causal modeling, decision making under uncertainty, anomaly detection, automated insight and prediction** .
- They are ideal for taking an event that occurred and predicting the likelihood that any one of the possible causes was the actual cause.
- They can also be used to update the probabilities of the variables based on new evidence or observations, using **Bayes' theorem** .
- A simple example of a Bayesian network is shown below:

```
    A
   / \
  B   C
 / \ / \
D   E   F
```

- In this network, each node represents a variable, and each edge represents a conditional dependency. For example, the probability of E depends on both B and C, and the probability of F depends only on C.