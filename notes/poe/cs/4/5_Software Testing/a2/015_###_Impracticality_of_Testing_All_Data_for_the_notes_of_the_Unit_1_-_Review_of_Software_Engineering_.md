 Here is the content in markdown format for the topic ### Impracticality of Testing All Data for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing:

### Impracticality of Testing All Data

- It is impossible to test a software with all possible input data due to following reasons:

- The input domain may be infinite (e.g. input representing integer values from -infinity to +infinity or real numbers with infinite precision)
- The input domain may be too large to be explicitly described or exhausted via testing (e.g. input for a word processor or a database)
- Input domains of many systems exhibit high dimensionality and hence is difficult to cover.
- Many systems exhibit stochastic behavior that leads to input interdependencies and complex interactions that are hard to model for testing purposes.

- Hence, it is impractical and infeasible to test a software with all possible input data. We have to use other methods to identify potential defects using limited test cases. Some techniques for the same are:

- Equivalence partitioning - dividing the input domain into classes of data with similar behavior
- Boundary value analysis - testing boundaries of the input domain and valid/invalid regions
- Error guessing - based on experience, identify inputs that are likely to cause problems
- Mutation testing - systematically modifying program code and testing if defects can be detected

- Mnemonic: TEST DATA INFINITY - Testing all data is impractical due to INFinite input domain possibilities.

- Advantages: Identifies major defects, increases confidence in software correctness.
- Disadvantages: May miss integration defects or complex interactions, time-consuming and expensive.

- Examples: Testing integer range, word processor with dictionary words, database with huge records.
- Applications: Used in software testing to identify potential defects using limited test cases due to impracticality of exhaustively testing all input data.