### Genetic representations

- A genetic representation is a way of encoding a candidate solution to a problem in a form that can be manipulated by a genetic algorithm (GA).
- A genetic representation consists of two components: a genotype and a phenotype.
- A genotype is the actual encoding of the solution, usually as a string of symbols (such as binary digits, characters, or real numbers).
- A phenotype is the interpretation of the genotype, usually as a meaningful object or structure (such as a graph, a function, or a design).
- A genetic representation must satisfy two properties: completeness and heritability.
- Completeness means that every possible genotype corresponds to a valid phenotype, and every possible phenotype can be encoded by some genotype.
- Heritability means that the genotype determines the phenotype, and that small changes in the genotype result in small changes in the phenotype.
- There are different types of genetic representations, depending on the nature of the problem and the desired features of the solution.
- Some common types of genetic representations are:

  - Binary representation: The genotype is a string of bits (0 or 1), and the phenotype is obtained by interpreting the bits as numbers, symbols, or instructions. This is the simplest and most general type of representation, but it may not capture the structure or constraints of the problem domain well.
  - Real-valued representation: The genotype is a vector of real numbers, and the phenotype is obtained by using the numbers as parameters, coefficients, or coordinates. This type of representation is suitable for problems involving continuous optimization, such as function approximation or engineering design.
  - Permutation representation: The genotype is a permutation of a set of elements, and the phenotype is obtained by ordering the elements according to the permutation. This type of representation is suitable for problems involving combinatorial optimization, such as traveling salesman problem or scheduling.
  - Tree representation: The genotype is a tree of nodes, and the phenotype is obtained by evaluating the tree as an expression, a program, or a grammar. This type of representation is suitable for problems involving symbolic manipulation, such as function induction or genetic programming.
  - Graph representation: The genotype is a graph of nodes and edges, and the phenotype is obtained by using the graph as a network, a structure, or a model. This type of representation is suitable for problems involving complex systems, such as neural networks or social networks.