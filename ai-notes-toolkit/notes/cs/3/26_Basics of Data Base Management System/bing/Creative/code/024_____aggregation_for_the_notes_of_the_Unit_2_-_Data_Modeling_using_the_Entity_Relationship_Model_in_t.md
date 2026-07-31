### Aggregation

- Aggregation is a concept in the entity relationship model that allows us to represent a relationship between an entity set and a relationship set as a single entity set .
- Aggregation is useful when we want to model a relationship involving a relationship set and another entity set, and then treat the resulting entity set as a participant in another relationship .
- Aggregation helps to simplify the ER diagram and reduce the number of relationships.
- Aggregation also protects the integrity of a group of objects by defining a single point of control.

#### Example of Aggregation

- Consider the following ER diagram, where a visitor can enroll in a course offered by a center, and a course requires some machinery.

![ER diagram without aggregation](https://www.javatpoint.com/dbms/images/dbms-aggregation1.png)

- We can use aggregation to model the relationship between the course and the machinery as a single entity set, and then relate it to the visitor entity set.

![ER diagram with aggregation](https://www.javatpoint.com/dbms/images/dbms-aggregation2.png)

- The aggregated entity set is shown by a dashed rectangle, and the relationship between the visitor and the aggregated entity set is shown by a solid line .
- The advantage of using aggregation is that we can now specify attributes for the relationship between the visitor and the course-machinery entity set, such as the date of enrollment, the fee paid, etc. 
- We can also avoid the ambiguity of whether a visitor enrolls in a course or a machinery, or both.