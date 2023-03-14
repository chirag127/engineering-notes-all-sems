### Decision Table Based Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Decision table testing is a software testing technique used to test system behavior for different input combinations.
- This is a systematic approach where the different input combinations and their corresponding system behavior (output) are captured in a tabular form.
- That is why it is also called as a cause-effect table where cause and effects are captured for better test coverage.
- A decision table is a tabular representation of inputs versus rules/cases/test conditions.
- It is a very effective tool used for both complex software testing and requirements management.
- A decision table helps to check all possible combinations of conditions for testing and testers can also identify missed conditions easily.
- The conditions are indicated as true (T) and false (F) values.
- In software testing, the decision table has four parts which are divided into portions:
  - Condition stubs: The conditions are listed in the first upper left part of the decision table that is used to determine a particular action or set of actions.
  - Action stubs: All the possible actions are given in the first lower left portion (i.e., below condition stub) of the decision table.
  - Condition entries: The values are inputted in the upper right portion of the decision table. In the condition entries part of the table, there are multiple rows and columns which are known as rules.
  - Action entries: Every entry has some associated action or set of actions in the lower right portion of the decision table and these values are called outputs.
- The decision tables are categorized into two types:
  - Limited entry: In the limited entry decision tables, the condition entries are restricted to binary values.
  - Extended entry: In the extended entry decision table, the condition entries have more than two values. The decision tables use multiple conditions where a condition may have many possibilities instead of only ‘true’ and ‘false’ are known as extended entry decision tables.
- The advantages of decision table testing are :
  - When the system behavior is different for different inputs and not the same for a range of inputs, both equivalent partitioning and boundary value analysis are not applicable. In such cases, decision table testing is useful.
  - The representation is simple so that it can be easily interpreted and is used for development and business as well.
  - This table will help to make sure that all combinations of inputs are covered and there is no ambiguity in the requirements.
  - It reduces the number of test cases by eliminating redundant or impossible scenarios.
  - It improves the test coverage and traceability by mapping the test cases to the requirements.
- The disadvantages of decision table testing are:
  - It can be difficult and time-consuming to create decision tables for complex scenarios with many conditions and actions.
  - It can be hard to maintain and update decision tables when the requirements change frequently.
  - It can be challenging to automate decision table testing as the test cases are derived from the table structure.
- An example of decision table testing is given below:

| Conditions | R1 | R2 | R3 | R4 |
|------------|----|----|----|----|
| Username (T/F) | F | T | F | T |
| Password (T/F) | F | F | T | T |
| Output (E/H) | E | E | E | H |

Legend:

T – Correct username/password

F – Wrong username/password

E – Error message is displayed

H – Home screen is displayed

Interpretation:

Case 1 – Username and password both were wrong. The user is shown an error message.

Case 2 – Username was correct, but the password was wrong. The user is shown an error message.

Case 3 – Username was wrong, but the password was correct. The user is shown an error message.

Case 4 – Username and password both were correct, and the user navigated to the homepage

- A mnemonic to remember the parts of a decision table is CACA: Condition stubs, Action stubs, Condition entries, Action entries.
- A learning trick to create a decision table is to follow these steps:
  - Identify the conditions and actions