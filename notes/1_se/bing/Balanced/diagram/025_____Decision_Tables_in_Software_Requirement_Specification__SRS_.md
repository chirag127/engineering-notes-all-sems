A decision table is a tabular representation of several input values, cases, rules, and test conditions. It is a highly effective tool utilized for both requirements management and complex software testing. Through this table, we can check and verify all possible combinations of testing conditions  .

A decision table consists of four quadrants: condition stubs, condition entries, action stubs, and action entries. The condition stubs are the input values or conditions that affect the outcome of the decision. The condition entries are the possible values or states of each condition. The action stubs are the output values or actions that result from the decision. The action entries are the values or states of each action for each combination of conditions. The rows of the table are called rules, and each rule represents a unique combination of conditions and actions  .

An example of a decision table for a software requirement specification (SRS) is shown below. The requirement is to determine the discount rate for a customer based on their membership status and purchase amount. The decision table has four condition stubs and two action stubs. The condition entries are Y (yes) or N (no) for each condition, and the action entries are the discount rates for each rule. The table has eight rules, covering all possible combinations of conditions.

### Decision Tables in Software Requirement Specification (SRS)

| Condition Stubs | C1 | C2 | C3 | C4 | Action Stubs | A1 | A2 |
|-----------------|----|----|----|----|--------------|----|----|
| Is the customer a member? | Y | Y | Y | Y | Discount rate | 10% | 15% |
| | N | N | N | N | | 0% | 5% |
| Is the purchase amount >= $100? | Y | Y | N | N | | | |
| | Y | N | Y | N | | | |
| Is the purchase amount >= $200? | Y | N | N | N | | | |
| | N | N | N | N | | | |
| Is the purchase amount >= $300? | Y | N | N | N | | | |
| | N | N | N | N | | | |