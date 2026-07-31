### Aggregation

- Aggregation is a concept in the entity relationship model that allows us to represent a relationship between an entity set and a relationship set as a single entity set .
- Aggregation is useful when we want to model a relationship involving a relationship set and another entity set, and then treat the resulting entity set as a participant in another relationship .
- Aggregation helps to simplify the ER diagram and reduce the number of relationships.
- Aggregation also protects the integrity of a group of objects by defining a single point of control.

#### Example of Aggregation

- Consider the following ER diagram, where a visitor can enroll in a course offered by a center, and a course requires some machinery.

![ER diagram without aggregation](https://www.geeksforgeeks.org/wp-content/uploads/ER-Diagram-1.png)

- We can use aggregation to model the relationship between the course and the machinery as a single entity set, and then relate it to the visitor entity set.

![ER diagram with aggregation](https://www.geeksforgeeks.org/wp-content/uploads/ER-Diagram-2.png)

- The aggregated entity set is shown as a dashed rectangle, and the relationship between the visitor and the aggregated entity set is shown as a solid line .