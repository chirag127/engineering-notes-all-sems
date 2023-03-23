 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Stochastic Search Methods

- Stochastic search methods involve introducing randomness into the search process. They do not guarantee to find the global optimum, but can avoid getting stuck in local optima.
- Some popular stochastic search methods are:

1. Simulated Annealing: The method is inspired by the metallurgical process of annealing where a material is heated and then cooled slowly to reduce defects. A random perturbation is introduced to the current solution and the change is accepted probabilistically based on a temperature parameter. The temperature is decreased slowly leading to fewer acceptance of uphill moves resulting in convergence to a good solution.
- Genetic Algorithms: The method is inspired by natural evolution and selection. A population of solutions is maintained and evolved over generations using selection, crossover and mutation operators. Selection chooses fitter solutions, crossover creates new solutions from existing ones and mutation introduces randomness. Over generations, the population evolves towards optimal solutions.
- Particle Swarm Optimization: The method is inspired by bird flocking or fish schooling. A population of particles (potential solutions) fly through the solution space. Each particle adjusts its position based on its own experience as well as the experience of neighboring particles. This leads to the swarm converging towards the optimal solution.

The stochastic search methods can be useful when:

- The search space is complex with many local optima
- Gradient information is not available
- A quick solution is needed rather than guaranteed optimality
- The objective function is stochastic or noisy

The methods can be combined with local search techniques to achieve a balance between exploration and exploitation.