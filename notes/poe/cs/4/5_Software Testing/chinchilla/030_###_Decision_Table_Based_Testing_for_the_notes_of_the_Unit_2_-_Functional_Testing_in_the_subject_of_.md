### Decision Table Based Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

Decision Table Based Testing (DTBT) is a black-box testing technique used to test the combinations of inputs and their associated outputs for a particular system. This technique is widely used in software testing to ensure that the system performs as expected under different input conditions. In this technique, a decision table is used to describe the input-output combinations that need to be tested.

#### Decision Table

A decision table is a table that represents the logic of a system. It lists all the possible combinations of inputs and their associated outputs. The decision table is divided into four sections:

- Condition stubs: It represents the inputs to the system. Each condition stub represents a single input.
- Condition entries: It represents the possible values of the inputs.
- Action stubs: It represents the outputs of the system. Each action stub represents a single output.
- Action entries: It represents the expected results of the system for a given set of inputs.

#### How to create a decision table?

To create a decision table, follow the below steps:

1. Identify the inputs and outputs of the system.
2. Create a table with condition stubs, condition entries, action stubs, and action entries.
3. Fill in the condition entries and action entries based on the inputs and outputs of the system.
4. Identify the test cases to be executed based on the decision table.

#### Advantages of Decision Table Based Testing

- Easy to understand and implement.
- Covers all possible combinations of inputs and outputs.
- Helps in identifying the missing or redundant test cases.
- Reduces the number of test cases needed to be executed.
- Helps in identifying the dependencies between inputs and outputs.

#### Disadvantages of Decision Table Based Testing

- It may lead to a large number of test cases.
- It may not be suitable for complex systems.
- It may not cover all possible scenarios.

#### Mnemonics and Learning Tricks

- Use the acronym CCDT (Condition, Condition Entries, Decision Table, Test Cases) to remember the steps involved in creating a decision table.
- Use the phrase "If-Then-Else" to remember the structure of a decision table.

#### Example

Consider a system that calculates the price of a product based on its type, size, and color. The decision table for this system could look like:

| Type | Size | Color | Price |
|------|------|-------|-------|
| Small| Small| Red   | $10   |
| Small| Small| Green | $12   |
| Small| Large| Red   | $15   |
| Small| Large| Green | $18   |
| Large| Small| Red   | $14   |
| Large| Small| Green | $16   |
| Large| Large| Red   | $20   |
| Large| Large| Green | $25   |

Based on this decision table, the test cases to be executed would be:

1. Test case 1: Type = Small, Size = Small, Color = Red, Expected Price = $10
2. Test case 2: Type = Small, Size = Small, Color = Green, Expected Price = $12
3. Test case 3: Type = Small, Size = Large, Color = Red, Expected Price = $15
4. Test case 4: Type = Small, Size = Large, Color = Green, Expected Price = $18
5. Test case 5: Type = Large, Size = Small, Color = Red, Expected Price = $14
6. Test case 6: Type = Large, Size = Small, Color = Green, Expected Price = $16
7. Test case 7: Type = Large, Size = Large, Color = Red, Expected Price = $20
8. Test case 8: Type = Large, Size = Large, Color = Green, Expected Price = $25

#### Applications

- Decision Table Based Testing is widely used in the automotive industry to test the different combinations of sensors and their associated outputs.
- It is used in the telecom industry to test the different combinations of input signals and their associated outputs.
- It is also used in the financial industry to test the different combinations of input parameters and their associated outputs.