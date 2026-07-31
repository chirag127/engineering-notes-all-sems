Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the extended ER model for the notes of the Unit 1 - Introduction in the subject of Database Management System.

### Extended ER Model

- The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases .
- The EER model reflects more precisely the properties and constraints that are found in complex databases, such as inheritance, specialization, generalization, union, and aggregation .
- The EER model introduces the following concepts :
  - Subclasses and Superclasses: A subclass is a subset of entities that belong to a superclass, and inherits all the attributes and relationships of the superclass. A superclass is a superset of entities that share some common attributes and relationships. For example, a subclass STUDENT can be derived from a superclass PERSON, and inherit the attributes name, address, and phone number.
  - Specialization and Generalization: Specialization is the process of defining one or more subclasses from a superclass based on some distinguishing characteristics. Generalization is the reverse process of abstraction, where common attributes and relationships are combined into a superclass from one or more subclasses. For example, a superclass VEHICLE can be generalized from the subclasses CAR, TRUCK, and BIKE, and have the common attribute license plate number.
  - Union or Category: A union or category is a subclass that is the result of combining entities from different entity sets that share some common characteristics. A union or category is also called a shared subclass. For example, a subclass PART-TIME-EMPLOYEE can be derived from the union of the entity sets STUDENT and EMPLOYEE, and have the common attribute hourly wage.
  - Aggregation: Aggregation is the process of grouping together entities and relationships into a single abstract entity type. Aggregation is used to represent a part-of relationship between an entity and a collection of entities. For example, an entity COURSE can be aggregated with the relationship OFFERED-BY to form an abstract entity type COURSE-OFFERING, which represents a course offered by a department in a semester.

- The EER model can be represented graphically using the following symbols :

![EER Symbols](https://www.geeksforgeeks.org/wp-content/uploads/Enhanced-ER-Diagram-1.png)

- An example of an EER diagram for a university database is shown below:

![EER Example](https://www.geeksforgeeks.org/wp-content/uploads/Enhanced-ER-Diagram-2.png)