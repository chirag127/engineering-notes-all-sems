# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Generalization is a bottom-up approach in which two or more lower level entities are combined to form a higher level entity  .
- In generalization, the higher level entity inherits the properties of all the lower level entities  .
- Generalization is used to represent a group of entities that share some common characteristics or attributes  .
- Generalization is also called abstraction or generalization/specialization  .
- Generalization can be represented by a triangle with the word "is a" above it, connecting the higher level entity to the lower level entities  .
- An example of generalization is the entity PERSON, which can be generalized from the entities STUDENT and TEACHER, as shown below  :

```
    PERSON
    /    \
   /      \
  /        \
 /          \
STUDENT   TEACHER
```

- Generalization can be applied recursively to create further higher level entities from existing generalized entities  .
- An example of recursive generalization is the entity EMPLOYEE, which can be generalized from the entities MANAGER and WORKER, which are themselves generalized from the entities STUDENT and TEACHER, as shown below  :

```
    EMPLOYEE
    /      \
   /        \
  /          \
 /            \
MANAGER     WORKER
 /   \       /   \
/     \     /     \
STUDENT TEACHER STUDENT TEACHER
```

- Generalization can be used to simplify the design of a database by reducing the number of entities and relationships  .
- Generalization can also be used to capture the inheritance or subtyping relationships among entities in an object-oriented or semantic data model .