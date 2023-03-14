The following diagram illustrates the impracticality of testing all data for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing.

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Input Domain   |      |  Program Under  |      |  Output Domain  |
|                 |      |     Test        |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  All possible   |      |                 |      |  All possible   |
|  inputs to the  |=====>|  Executes the   |=====>|  outputs from   |
|  program        |      |  program with   |      |  the program    |
|                 |      |  selected       |      |                 |
|                 |      |  inputs         |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The input domain is the set of all possible inputs to the program under test. The output domain is the set of all possible outputs from the program. The program under test executes the program with selected inputs from the input domain and produces corresponding outputs in the output domain. However, for most programs, it is impractical to attempt to test the program with all possible inputs, due to a combinational explosion . For those inputs selected, a testing oracle is needed to determine the correctness of the output for a particular test input. Therefore, testing all data is not feasible and effective. Instead, testing should focus on selecting a representative and meaningful subset of inputs that can reveal the most defects in the program.