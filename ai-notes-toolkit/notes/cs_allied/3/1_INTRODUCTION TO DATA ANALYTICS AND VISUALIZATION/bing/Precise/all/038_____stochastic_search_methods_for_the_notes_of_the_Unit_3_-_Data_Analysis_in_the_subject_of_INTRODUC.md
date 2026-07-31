### Stochastic Search Methods

Stochastic search methods are a type of optimization algorithm that use randomness to find the global optimum of a function. These methods are often used when the search space is large and the function being optimized is complex, making it difficult to find the global optimum using deterministic methods.

Some common stochastic search methods include:

1. **Simulated Annealing:** This method is inspired by the annealing process in metallurgy, where a material is heated and then slowly cooled to reduce defects and improve its structure. In simulated annealing, the algorithm starts with a high "temperature" and explores the search space randomly. As the temperature decreases, the algorithm becomes more likely to accept solutions that are worse than the current solution, allowing it to escape local optima and find the global optimum.

2. **Genetic Algorithms:** These algorithms are inspired by the process of natural selection and use concepts such as reproduction, mutation, and selection to evolve a population of solutions towards the global optimum. The algorithm starts with a population of randomly generated solutions and iteratively applies genetic operators to create new solutions. The best solutions are selected to survive and reproduce, while the worst solutions are discarded.

3. **Particle Swarm Optimization:** This method is inspired by the social behavior of bird flocks and fish schools. The algorithm represents each potential solution as a particle in a swarm, and the particles move through the search space based on their own best position and the best position of their neighbors. Over time, the swarm converges towards the global optimum.

These are just a few examples of stochastic search methods. These methods can be effective for solving complex optimization problems, but they may require more computational resources and time compared to deterministic methods. Additionally, the randomness inherent in these methods means that the results may not be consistent across multiple runs of the algorithm.