 Here is the content in markdown format for the given topic:

### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

Cyclomatic complexity is a software metric (measurement) that provides a quantitative measure of the logical complexity of a program. It defines the number of independent paths through a program's source code. It was developed by Thomas J. McCabe, Sr. in 1976.

**Formula:** Cyclomatic complexity = E - N + 2

Where:

- E = Number of edges of the graph
- N = Number of nodes of the graph

**Properties:**

- Value is always greater than or equal to 1.
- A complexity of 1 indicates a simple sequence of statements with no branching.
- Greater values indicate multiple paths and increased complexity.
- Can be used to identify complex areas of code that may require more testing.

**Advantages:**

- Provides an objective measurement of code complexity.
- Can be calculated automatically from the structure of the code.
- Highlights complex areas of code that may require more testing or simplification.

**Disadvantages:**

- Does not directly measure functionality or quality of code.
- Does not measure other types of complexity e.g. Data complexity.
- Threshold values for acceptable complexity can be difficult to determine.

**Example:**

```
if (x == 5)
   y = 10
else
   y = 15
```

Cyclomatic complexity = 1 (1 conditional)

```
if (x == 5)
   y = 10
else if (x == 6)
   y = 11
else
   y = 15
```

Cyclomatic complexity = 2 (2 conditionals)

**Mnemonics:**

- Think of Cyclomatic Complexity as the number of "Circles" (independent paths) through your code.
- The more "Circles", the more complex the code.