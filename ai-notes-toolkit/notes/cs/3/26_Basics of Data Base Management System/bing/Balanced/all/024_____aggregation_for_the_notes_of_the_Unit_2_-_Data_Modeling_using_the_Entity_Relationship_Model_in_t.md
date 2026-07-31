# Aggregation in Entity Relationship Model

- Aggregation is a technique to model a relationship involving a relationship set and one or more entity sets .
- Aggregation allows us to treat a relationship set as an entity set for purposes of participation in other relationships .
- Aggregation is an abstraction through which we can represent relationships as higher level entity sets.
- Aggregation protects the integrity of an assembly of objects by defining a single point of control.
- Aggregation is useful when we need to express a relationship among relationships .

## Example of Aggregation

- Consider a scenario where an employee works for a project and requires some machinery.
- We can model the relationship between employee and project as WORKS_FOR, and the relationship between employee and machinery as REQUIRES.
- However, this does not capture the fact that the employee requires the machinery for a specific project, not in general.
- To express this constraint, we can use aggregation to treat the WORKS_FOR relationship as an entity set, and relate it to the machinery entity set with a new relationship called NEEDS.
- The diagram below shows the aggregation of WORKS_FOR and NEEDS.

![Aggregation Example](https://www.javatpoint.com/dbms/images/dbms-aggregation.png)