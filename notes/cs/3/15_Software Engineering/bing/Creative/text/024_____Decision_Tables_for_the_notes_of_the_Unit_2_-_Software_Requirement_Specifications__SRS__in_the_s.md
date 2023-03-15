### Decision Tables

- A decision table is a tabular representation of the conditions and actions of a system or a software module.
- A decision table consists of four quadrants: condition stub, condition entries, action stub, and action entries.
- The condition stub lists the possible conditions or inputs that affect the system or module behavior.
- The condition entries are the combinations of values (true/false, yes/no, etc.) that the conditions can take.
- The action stub lists the possible actions or outputs that the system or module can perform.
- The action entries are the indicators (X, check mark, etc.) that show which actions are executed for each combination of condition values.
- A decision table can be used to specify the functional requirements of a system or module in a clear and concise way.
- A decision table can also be used to test the system or module by checking if the actual behavior matches the expected behavior for each combination of condition values.
- A decision table can be constructed using the following steps:
  - Identify the conditions and actions that are relevant to the system or module.
  - Determine the number of columns needed for the condition entries. This is equal to the number of possible combinations of condition values, which is 2^n, where n is the number of conditions.
  - Assign a column number to each combination of condition values. A common method is to use binary notation, where each bit represents a condition value (0 for false, 1 for true).
  - Fill in the condition entries for each column by writing the corresponding condition values.
  - Fill in the action entries for each column by writing an indicator for each action that is executed for that column.
  - Simplify the decision table by eliminating duplicate or redundant columns or rows, or by using rules or expressions to represent complex conditions or actions.