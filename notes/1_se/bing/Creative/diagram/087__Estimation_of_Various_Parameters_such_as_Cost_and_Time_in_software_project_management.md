Estimation of various parameters such as cost and time in software project management is a complex process that involves using different techniques and models to predict the resources and effort required to complete a project successfully. Some of the common techniques and models are:

- Parametric estimating: This technique uses a set of algorithms, statistics or models to describe the project and calculate the cost, duration and effort based on the relationship between variables. For example, the parametric estimating formula is E_parametric = A_old / P old x P curr, where E_parametric is the parametric estimate, A_old is the historical amount of cost or time, P_old is the historical value of the parameter, and P_curr is the value of the parameter in the current project .
- Analogous estimating: This technique uses data from similar past projects to determine the cost, duration and effort of the current project. It is based on the analogy or comparison between projects, and it is less accurate than parametric estimating. For example, if a previous project of similar scope and complexity took 100 hours and $10,000 to complete, then the analogous estimate for the current project would be the same.
- COCOMO model: This is a regression model based on the number of lines of code (LOC) in the software project. It is a procedural cost estimate model that predicts the size, effort, cost, time and quality of the project. It was proposed by Barry Boehm in 1981 and is based on the study of 63 projects. It has three levels: basic, intermediate and detailed, each with different formulas and parameters.

The following diagram illustrates the basic architecture of a parametric estimating technique in software project management:

```
+-----------------+     +-----------------+     +-----------------+
| Historical data |     | Statistical data|     | Project data    |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| - Cost          |     | - Algorithms    |     | - Scope         |
| - Time          |     | - Models        |     | - Complexity    |
| - Effort        |     | - Variables     |     | - Quality       |
| - Size          |     |                 |     | - Risk          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
          |                     |                     |
          +---------------------+---------------------+
                                |
                                v
                      +-----------------+
                      | Parametric      |
                      | estimating      |
                      | technique       |
                      +-----------------+
                      |                 |
                      | - Formula       |
                      | - Calculation   |
                      | - Estimation    |
                      |                 |
                      +-----------------+
                                |
                                v
                      +-----------------+
                      | Project         |
                      | estimation      |
                      +-----------------+
                      |                 |
                      | - Cost          |
                      | - Time          |
                      | - Effort        |
                      | - Size          |
                      |                 |
                      +-----------------+
```