### Test Data Generation Using Genetic Algorithm

- Genetic Algorithm has been implemented to automate the generation of test data.
- The test data is derived from the program's structure with the aim to traverse every line of code in the software.
- This work uses a fitness function and variables are represented in binary code.
- The Genetic Algorithm (GA) generators that can examine a program’s structure starts by creating an initial population of individuals, and generate adequate test data automatically.
- A genetic algorithm is a heuristic that mimics the evolution of natural species in searching for the optimal solution to a problem.
- In the test-data generation application, the solution sought by the genetic algorithm is test data that causes execution of a given statement, branch, path, or definition-use pair in the program under test.
- The results showed that genetic algorithms have been successfully applied to simple test data generation, but are rarely used to generate complex test data such as images, videos, sounds, and 3D (three-dimensional) models.
- A genetic algorithm is used to satisfy the constraints and then test cases are generated.
- If the constraints have temporary variables in them, and the GA needs their values to evaluate fitness functions, the values of the temporary variables can be obtained by augmenting the source code of the tested program to output them.