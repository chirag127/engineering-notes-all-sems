 Here is the content in markdown format for the topic #### Various Size Oriented Measures in Software Design:

#### Various Size Oriented Measures in Software Design

- **Lines of Code (LOC):** Counts the number of lines of code in a software. It is a basic measure but does not consider the complexity of lines.
- **Function Points:** Counts the number of functionalities in the software. Weights are assigned to external inputs, external outputs, logical internal files, external interface files and external queries. The sum of the weighted values gives the function point count. It is a better measure than LOC but subjective.
- **Cyclomatic Complexity:** Counts the number of independent paths in the control flow graph of a module. It considers the control flow structure. A higher value indicates higher complexity. It can be used to identify modules that need extra attention.
- **Halstead Metrics:** Counts the total operators and operands in a module and calculates software volume, difficulty, effort and time required based on this. It considers the vocabulary of the programming language used.

**Mnemonics:**
- Think of LOC as 'Length Of Code'
- For Function Points, remember 'EI2EQ5' i.e. External Inputs, External Outputs, Internal Logical Files, External Interface Files and External Queries
- For Cyclomatic Complexity, remember 'Independent Paths'

**Advantages:** Help in estimating effort and cost, identifying complex modules, comparing software and languges, etc.
**Disadvantages:** May not always correlate with understandability, maintainability or quality. Subjective for Function Points.
**Applications:** Software Estimation, Software Comparison, Complexity Analysis, etc.

[Detailed diagrams, examples and codes can be added here if required.]