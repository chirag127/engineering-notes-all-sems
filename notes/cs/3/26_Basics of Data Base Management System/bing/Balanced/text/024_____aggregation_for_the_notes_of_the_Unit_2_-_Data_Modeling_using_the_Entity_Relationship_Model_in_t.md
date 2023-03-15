### Aggregation in Entity Relationship Model

- Aggregation is a technique to model a relationship involving a relationship set and one or more entity sets .
- Aggregation allows us to treat a relationship set as an entity set for purposes of participation in other relationships .
- Aggregation is an abstraction through which we can represent relationships as higher level entity sets.
- Aggregation protects the integrity of an assembly of objects by defining a single point of control.
- Aggregation is useful when we need to express a relationship among relationships, or when we need to attach attributes to relationships.

#### Example of Aggregation

- Consider a scenario where an employee works for a project and requires some machinery. We can model this as follows:

![Aggregation Example](https://www.javatpoint.com/dbms/images/dbms-aggregation.png)

- In this example, WORKS_FOR is a relationship between EMPLOYEE and PROJECT entity sets, and REQUIRE is a relationship between WORKS_FOR and MACHINERY entity sets .
- We can use aggregation to treat WORKS_FOR as a higher level entity set, and form a relationship set OFFERS between CENTER and WORKS_FOR .
- This way, we can express that a center offers a work opportunity for an employee on a project with some machinery .

![Aggregation Example with OFFERS](https://www.javatpoint.com/dbms/images/dbms-aggregation2.png)

- Aggregation vs. ternary relationship: In some cases, we can use a ternary relationship instead of aggregation to model a similar scenario. For example, we can use a ternary relationship MONITORS between CENTER, EMPLOYEE and PROJECT to express that a center monitors an employee working on a project.
- However, aggregation is preferred when we need to distinguish the relationship between EMPLOYEE and PROJECT from the relationship between CENTER and EMPLOYEE-PROJECT pair, or when we need to attach attributes to the relationship between EMPLOYEE and PROJECT.

![Ternary Relationship Example](http://www.csbio.unc.edu/mcmillan/Media/Comp521F12Lecture02_files/image018.gif)