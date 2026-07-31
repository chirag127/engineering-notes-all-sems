A decision table is a tool that can be used to specify the behavior of a software system based on different combinations of input conditions and actions. A decision table consists of four parts: condition stubs, action stubs, condition entries, and action entries. Condition stubs are the input conditions that affect the behavior of the system. Action stubs are the output actions that the system performs. Condition entries are the possible values of the input conditions. Action entries are the corresponding values of the output actions. A decision table can be represented in a tabular format, where each row represents a rule and each column represents a condition or an action. A rule is a combination of condition entries and action entries that defines the behavior of the system for a specific scenario. A decision table can also be represented in a graphical format, where each node represents a condition or an action, and each branch represents a value of the condition or the action. A graphical decision table can be converted into a tabular decision table by following a systematic procedure.

Here is an example of a decision table for a software system that calculates the discount for a customer based on their age and membership status:

### Decision Tables in Software Requirement Specification (SRS)

```
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Condition Stubs | Condition Entry | Condition Entry | Condition Entry | Condition Entry | Condition Entry |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Age             | < 18            | < 18            | >= 18           | >= 18           | Any             |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Membership      | Yes             | No              | Yes             | No              | No              |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Action Stubs    | Action Entry    | Action Entry    | Action Entry    | Action Entry    | Action Entry    |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Discount        | 20%             | 10%             | 15%             | 5%              | 0%              |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
```

Here is the graphical representation of the same decision table:

```
+-----------------+
| Age             |
+-----------------+
|                 |
|                 |
|                 |
|                 |
+-----+-----+-----+
| <18 | >=18| Any |
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
| Membership      |
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
| Yes | No  | No  |
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
| Discount        |
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
| 20% | 10% | 0%  |
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
| 15% | 5%  |     |
+-----+-----+-----+
```