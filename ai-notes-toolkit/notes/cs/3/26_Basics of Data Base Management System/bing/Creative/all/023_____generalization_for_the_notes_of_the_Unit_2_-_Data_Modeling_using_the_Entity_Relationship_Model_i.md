# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Generalization is a bottom-up approach in which two lower level entities combine to form a higher level entity .
- In generalization, the higher level entity can also combine with other lower level entities to make further higher level entity.
- In generalization, the higher level entity inherits the properties of all the lower level entities.
- Generalization is used to hide the details of a set of objects and extract their common properties.
- Generalization is represented by a triangle with the word "is-a" above it .
- An example of generalization is the entity PERSON, which can be generalized from the entities STUDENT and TEACHER .

![Generalization Example](https://www.studytonight.com/dbms/images/generalization.png)

- The entity PERSON has the common attributes of STUDENT and TEACHER, such as name, address, phone, etc .
- The entity PERSON can also have its own attributes, such as date of birth, gender, etc .
- The entity PERSON can also be further generalized with other entities, such as EMPLOYEE, CUSTOMER, etc .

![Generalization Example 2](https://www.tutorialspoint.com/dbms/images/generalization_example.jpg)

- Generalization is useful for reducing redundancy and complexity in the data model.
- Generalization is also useful for representing hierarchical relationships among entities.