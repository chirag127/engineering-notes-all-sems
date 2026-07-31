### Generational Cycle for the notes of the Unit 5 - Genetic Algorithm(GA) in the subject of Application of Soft Computing

- A genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural process of evolution and selection  .
- A GA works on a population of candidate solutions, each encoded as a string of symbols (usually binary digits) that represent the values of the decision variables  .
- A GA operates on the evolutionary generational cycle, which consists of the following steps  :
  - Initialization: Generate an initial population of random strings, usually of a fixed size .
  - Evaluation: Assign a fitness value to each individual in the population, based on how well it solves the problem .
  - Selection: Choose a subset of individuals from the current population to be the parents of the next generation, based on their fitness values  .
  - Genetic operators: Apply genetic operators such as crossover and mutation to the selected parents, to produce new offspring that inherit some characteristics from their parents  .
  - Replacement: Replace the current population with the new offspring, or combine them in some way, to form the next generation  .
  - Termination: Check if a stopping criterion is met, such as reaching a maximum number of generations, or finding an optimal or near-optimal solution . If not, go back to the evaluation step and repeat the cycle .
- The generational cycle aims to improve the quality of the population over time, by preserving the best individuals and exploring new regions of the search space .
- The generational cycle can be represented by a flow chart as shown below:

![Flow chart of generational cycle](https://i.ytimg.com/vi/8VaSFQ0yNSA/maxresdefault.jpg)