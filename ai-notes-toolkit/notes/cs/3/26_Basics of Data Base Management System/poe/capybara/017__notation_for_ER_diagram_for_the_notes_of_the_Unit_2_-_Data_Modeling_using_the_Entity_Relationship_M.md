### Notation for ER Diagram

An Entity Relationship (ER) diagram is a visual representation of entities and their relationships to each other. It is used to model and design database systems. The notation used in an ER diagram consists of symbols that represent entities, attributes, relationships, and cardinalities. Below are the symbols used in an ER diagram notation:

#### Entity Symbol
- An entity symbol is represented by a rectangle with rounded corners.
- It represents a real-world object, concept, or thing that can be identified by its attributes.
- The entity name is written inside the rectangle.

#### Attribute Symbol
- An attribute symbol is represented by an oval.
- It represents a property or characteristic of an entity.
- The attribute name is written inside the oval.

#### Relationship Symbol
- A relationship symbol is represented by a diamond shape.
- It represents the association between two or more entities.
- The relationship name is written inside the diamond shape.

#### Cardinality Symbol
- Cardinality symbols are used to express the number of entities that are involved in a relationship.
- There are three types of cardinality symbols:
  - One-to-one (1:1) - each entity in the first set is associated with only one entity in the second set, and vice versa.
  - One-to-many (1:N) - each entity in the first set is associated with one or more entities in the second set, but each entity in the second set is associated with only one entity in the first set.
  - Many-to-many (N:M) - each entity in the first set is associated with one or more entities in the second set, and vice versa.

#### Example
```
### ER Diagram for a University Database

#### Entities
- Student (Student_ID, Name, Gender, DOB, Address)
- Course (Course_ID, Course_Name, Credits)
- Department (Dept_ID, Dept_Name, Location)

#### Relationships
- Enrolls (Student_ID, Course_ID)
- Teaches (Course_ID, Faculty_ID)
- Belongs_To (Student_ID, Dept_ID)
- Offers (Course_ID, Dept_ID)

#### Cardinalities
- Enrolls: 1:N
- Teaches: 1:N
- Belongs_To: N:1
- Offers: N:M
```

In conclusion, the notation used in an ER diagram is important in modeling and designing database systems. Understanding the symbols used in an ER diagram notation is crucial in creating accurate and efficient database systems.