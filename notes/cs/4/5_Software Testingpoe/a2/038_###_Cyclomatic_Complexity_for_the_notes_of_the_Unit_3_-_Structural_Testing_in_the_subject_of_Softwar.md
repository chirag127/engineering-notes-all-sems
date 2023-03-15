 Here is the content in markdown format for the topic ### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing:

### Cyclomatic Complexity

- Cyclomatic complexity is a software metric (measurement) used to indicate the complexity of a program.
- It is a quantitative measure of the number of linearly independent paths through a program's source code.
- It was developed by Thomas J. McCabe, Sr. in 1976.
- The cyclomatic complexity of a section of source code is calculated as:

CC = E - N + 2

Where:

E = the number of edges of the graph
N = the number of nodes of the graph

- A lower cyclomatic complexity indicates less complex logic and fewer potential defects.
- As complexity increases, it becomes more difficult to fully test a module and ensure that all potential defects have been identified.
- A complexity score of 10 or less is generally considered best. Scores of 20 or more are signs of very complex logic that may need simplification.

**Mnemonics:**

- "E - N + 2" is easy to remember as "Edges minus Nodes plus 2"
- A low CC score is simple and easy, a high score is complex and hazy!

**Advantages:**

- It is a quantitative measure that can be calculated objectively.
- It gives an indication of the test effort required to achieve adequate coverage.
- It highlights complex areas of code that may need simplification.

**Disadvantages:**

- It only considers the control flow of the code, not the data flow.
- It does not indicate anything about the quality of the design or algorithms used.
- The chosen threshold for acceptable complexity is subjective.

**Examples:**

- If a code has 3 conditions (if/else) and 4 functions, then:
E = 3 (edges from conditions)
N = 4 (nodes from functions)
CC = E - N + 2 = 3 - 4 + 2 = 1

- A more complex code with multiple nested conditions and loops may have a CC of 5 or more.

**Applications:**

- CC is commonly used as a software metric to help assess the maintainability and testability of code.
- It can highlight overly complex code sections that would benefit from simplification.
- The CC score can be used as an input to estimating testing effort and costs.