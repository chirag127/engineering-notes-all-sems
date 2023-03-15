 Here is the content in markdown format for the given topic:

### Decision Table Based Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

Decision table based testing is a black box testing technique that uses the logic defined in the form of a decision table to test the system.

- A decision table contains conditions and corresponding actions. It is used to capture the logic of a process or system.
- The conditions and actions are arranged in a tabular format with conditions in rows and actions in columns.
- Each row in the table defines rules or conditions and the corresponding action.
- To test using decision tables:
	- Identify the inputs and outputs of the system. These become the conditions and actions in the decision table.
	- List down all possible combinations of inputs. These will become the rows in the decision table.
	- For each combination of inputs, specify the expected output. These become the actions in the decision table.
- Advantages:
	- It is easy to understand as the logic is represented in a tabular format.
	- It is easy to maintain as any changes in logic can be easily incorporated into the table.
	- The table can be directly used as a test script.
	- All possible logical combinations can be captured to provide exhaustive testing.
- Disadvantages:
	- The number of test cases can increase exponentially with increasing conditions and rules. This can lead to increased effort and cost.
	- It is not suitable for complex logical conditions with many nested decisions.
	- The table can become unmanageably large for highly complex logic.

To summarize, decision table based testing is a useful technique to capture logic and derive test cases for functional testing. However, it has limitations in scaling for highly complex scenarios. Other techniques may be combined with decision tables to handle such scenarios.