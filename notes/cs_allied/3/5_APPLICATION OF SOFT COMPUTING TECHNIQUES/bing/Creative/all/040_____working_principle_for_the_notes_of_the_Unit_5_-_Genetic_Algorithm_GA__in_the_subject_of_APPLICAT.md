# Working Principle of Genetic Algorithm

- A genetic algorithm (GA) is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** (EA) .
- Genetic algorithms are commonly used to generate **high-quality solutions** to optimization and search problems by relying on biologically inspired operators such as **mutation**, **crossover** and **selection** .
- The basic principle behind the genetic algorithms is that they generate and maintain a **population** of individuals represented by **chromosomes**. Chromosomes are a character string practically equivalent to the chromosomes appearing in DNA. These chromosomes are usually encoded solutions to a problem .
- The working principle of a standard Genetic Algorithm is illustrated in the given figure .

![GA flowchart](https://static.javatpoint.com/tutorial/artificial-intelligence/images/artificial-neural-network-genetic-algorithm.png)

- The significant steps involved are the following  :
  - **Generation of a population of the solution**: The algorithm begins by creating a random initial population of chromosomes, each representing a possible solution to the problem.
  - **Identifying the objective function and fitness function**: The objective function is the function that needs to be optimized, and the fitness function is the measure of how well a chromosome performs on the objective function. The fitness function assigns a numerical value to each chromosome based on its objective function value.
  - **Application of genetic operators**: The algorithm then creates a sequence of new populations by applying genetic operators such as selection, crossover and mutation. These operators mimic the natural processes of reproduction and evolution, and they aim to improve the quality of the population over time.
    - **Selection**: This operator selects the best or the fittest chromosomes from the current population to be the parents of the next generation. There are different methods of selection, such as roulette wheel, tournament, rank-based, etc.
    - **Crossover**: This operator combines two parent chromosomes to produce one or more offspring chromosomes. Crossover is the main source of variation in genetic algorithms, and it allows the exchange of information between chromosomes. There are different methods of crossover, such as one-point, two-point, uniform, etc.
    - **Mutation**: This operator introduces random changes in one or more chromosomes to create new solutions. Mutation is a secondary source of variation in genetic algorithms, and it helps to prevent premature convergence and maintain diversity in the population. There are different methods of mutation, such as bit-flip, swap, insert, etc.
  - **Calculation of fitness for new population**: The algorithm evaluates the fitness of each chromosome in the new population using the fitness function, and compares it with the previous population. The algorithm repeats the steps of selection, crossover, mutation and fitness calculation until a **convergence** criterion is met. The convergence criterion can be a predefined number of generations, a desired fitness value, a lack of improvement, etc.
- The algorithm returns the best chromosome or the best population as the final solution to the problem .