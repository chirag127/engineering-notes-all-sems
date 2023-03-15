# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model

- An entity-relationship model (or ER model) describes interrelated things of interest in a specific domain of knowledge.
- A basic ER model is composed of entity types (which classify the things of interest) and specifies relationships that can exist between entities (instances of those entity types).
- Generalization is a bottom-up approach in which two lower level entities combine to form a higher level entity .
- In generalization, the higher level entity can also combine with other lower level entities to make further higher level entity.
- In generalization, the higher level entity inherits the properties of all the lower level entities .
- Generalization is used to hide the details of a set of objects and create a generalized entity from them.
- Generalization is represented by a triangle with a line connecting the higher level entity to the lower level entities  .
- An example of generalization is shown below:

![generalization example](https://www.studytonight.com/dbms/images/generalization.png)

- In this example, the entities Student and Teacher are generalized into a higher level entity Person, which inherits the attributes name, age and gender from them.
- The entity Person can also be generalized with other entities, such as Employee or Customer, to form a further higher level entity, such as Human.