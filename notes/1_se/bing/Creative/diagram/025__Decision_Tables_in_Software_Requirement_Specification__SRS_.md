A decision table is a tool that helps to specify the behavior of a software system based on different combinations of input conditions and actions. It is a tabular representation of the logic and rules that govern the system's functionality. A decision table can be used to document the requirements of a software system in a clear and concise way.

A decision table consists of four parts: condition stubs, action stubs, condition entries, and action entries. Condition stubs are the input conditions that affect the system's behavior. Action stubs are the output actions that the system performs. Condition entries are the possible values or states of the condition stubs. Action entries are the indicators that show which action stubs are executed for each combination of condition entries.

A decision table can have different formats, such as horizontal, vertical, or matrix. The most common format is the horizontal one, where the condition stubs are listed on the left and the action stubs are listed on the bottom. The condition entries and action entries are arranged in columns, forming the rules of the decision table.

An example of a decision table for a software system that calculates the discount for a customer based on their age and membership status is shown below:

### Decision Tables in Software Requirement Specification (SRS)

```
+-----------------+-----------------+-----------------+-----------------+-----------------+
| Condition Stubs |    Rule 1       |    Rule 2       |    Rule 3       |    Rule 4       |
+-----------------+-----------------+-----------------+-----------------+-----------------+
| Age             |  < 18           |  >= 18 and < 65 |  >= 18 and < 65 |  >= 65          |
+-----------------+-----------------+-----------------+-----------------+-----------------+
| Membership      |  No             |  No             |  Yes            |  No             |
+-----------------+-----------------+-----------------+-----------------+-----------------+
| Action Stubs    |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
| Discount        |  10%            |  0%             |  20%            |  15%            |
+-----------------+-----------------+-----------------+-----------------+-----------------+
```

The decision table above shows that the software system will apply a 10% discount if the customer is under 18 years old, a 20% discount if the customer is between 18 and 65 years old and has a membership, a 15% discount if the customer is over 65 years old, and no discount otherwise. Each column represents a rule that defines the relationship between the condition stubs and the action stubs.

A decision table can be useful for writing software requirements specifications (SRS) because it can:

- Reduce ambiguity and complexity by presenting the logic and rules of the system in a structured and consistent way.
- Facilitate communication and understanding among different stakeholders, such as developers, testers, and users.
- Support verification and validation of the system's behavior by providing test cases and expected outcomes.
- Enhance maintainability and modifiability of the system by allowing easy identification and modification of the rules.