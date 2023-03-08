 Here is the content in markdown format for the topic ### Searching with Partial Observations for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS:

### Searching with Partial Observations

- In many real-world problems, the input may not be fully specified or may be noisy or uncertain. Such problems require searching with partial observations or partial information.
- Some methods for searching with partial information are:
    - Mean Field Search: It estimates the distribution over all feasible solutions and finds the maximum a posteriori solution. It iteratively refines the estimate of the posterior distribution using the current solution.
    - Partially Observable Monte Carlo Search: It uses Monte Carlo tree search but deals with partial observability using particle filters. It represents the belief state as a set of particles/samples and weights. The weights are updated based on observations and the tree is searched stochastically based on the weights.
    - Memory-based Monte Carlo Search: It uses the idea of caching and reusing computations from previous searches to speed up search with partial observations. It maintains a cache of belief states and reuses/retrieves entries from the cache when similar belief states are encountered again.
    - Adaptive Monte Carlo Search: It adapts the exploration strategy during search based on the amount of uncertainty in the current state. It increases exploration in uncertain regions and focuses on exploitation in regions with high confidence.

- The key challenges in searching with partial information are:
    - Representing and updating beliefs or probability distributions over possible states.
    - Handling the increased branching factor and search space.
    - Balancing exploration and exploitation.
    - Scaling the methods to large, complex problems.

- Some applications of searching with partial information are:
    - Planning under uncertainty with sensing actions.
    - Partially observable games like Poker.
    - Diagnosis of faults or diseases with uncertain symptoms and tests.
    - Robot navigation with uncertain sensing.