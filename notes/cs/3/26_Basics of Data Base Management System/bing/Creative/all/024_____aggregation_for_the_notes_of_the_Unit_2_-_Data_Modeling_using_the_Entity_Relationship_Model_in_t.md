# Aggregation in Entity Relationship Model

- Aggregation is a concept in the entity relationship model that allows us to represent a relationship between a relationship set and an entity set as a single entity set.
- Aggregation is useful when we want to model a relationship involving a relationship set and another entity set, and then participate that aggregated entity set in another relationship.
- Aggregation helps us to avoid creating redundant or complex relationships and to simplify the design of the entity relationship diagram.
- Aggregation is represented by drawing a dashed rectangle around the relationship set and the entity set that are involved in the aggregation, and then connecting the rectangle to another entity set or relationship set by a solid line.

## Example of Aggregation

- Consider the following scenario: A center offers various courses, and each course is taught by a teacher. A visitor can enroll in one or more courses offered by a center. We want to model the relationship between the visitor and the course-teacher pair.
- One way to model this is to use a ternary relationship called Enrolls that involves the entity sets Visitor, Course, and Teacher. However, this would create a redundancy, as the relationship between Course and Teacher is already captured by the relationship set Offers.
- A better way to model this is to use aggregation. We can treat the relationship set Offers as an entity set, and call it CourseOffering. Then, we can create a binary relationship called Enrolls between Visitor and CourseOffering. This way, we avoid the redundancy and simplify the design.
- The following diagram shows the aggregation in the entity relationship model:

![aggregation example](https://www.javatpoint.com/dbms/images/dbms-aggregation.png)