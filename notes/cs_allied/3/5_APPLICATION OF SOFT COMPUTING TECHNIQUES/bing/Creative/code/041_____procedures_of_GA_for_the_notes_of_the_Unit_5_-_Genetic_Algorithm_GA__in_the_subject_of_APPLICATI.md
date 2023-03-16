Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content in markdown format for the topic of procedures of GA for the notes of the Unit 5 - Genetic Algorithm(GA) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES.

### Procedures of GA

Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve.

The basic procedure of GA can be summarized as follows  :

1. **Initialization**: Generate an initial population of candidate solutions, usually randomly. Each candidate solution is represented by a chromosome, which is a string of genes. Genes can be binary, integer, real, or symbolic values, depending on the problem domain.
2. **Evaluation**: Assign a fitness value to each candidate solution, based on how well it solves the problem. The fitness function is problem-specific and reflects the objective or goal of the optimization.
3. **Selection**: Choose a subset of the population to produce the next generation, based on their fitness values. The selection process is stochastic and biased towards fitter solutions, mimicking the survival of the fittest principle in nature. There are different selection methods, such as roulette wheel, tournament, rank, etc.
4. **Crossover**: Apply a recombination operator to pairs of selected solutions, to create new offspring solutions. Crossover is the main source of exploration and diversity in GA, and it allows the exchange of genetic material between solutions. There are different crossover methods, such as one-point, two-point, uniform, etc.
5. **Mutation**: Apply a random modification operator to some of the offspring solutions, to introduce some variation and prevent premature convergence. Mutation is the secondary source of exploration and diversity in GA, and it allows the creation of new genetic material. There are different mutation methods, such as bit-flip, swap, insert, etc.
6. **Replacement**: Replace the old population with the new offspring population, or combine them and select the best ones, depending on the replacement strategy. There are different replacement methods, such as generational, steady-state, elitist, etc.
7. **Termination**: Check if a stopping criterion is met, such as reaching a maximum number of generations, finding an optimal or near-optimal solution, or reaching a fitness plateau. If the criterion is met, stop the algorithm and return the best solution found. Otherwise, go back to step 2 and repeat the process.

The following diagram illustrates the basic procedure of GA:

![GA procedure](https://www.tutorialspoint.com/genetic_algorithms/images/ga_flowchart.jpg)