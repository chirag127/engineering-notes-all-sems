# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model

- Generalization is a bottom-up approach in which two or more lower level entities (subclasses) combine to form a higher level entity (superclass)   .
- In generalization, the superclass inherits the common properties and relationships of the subclasses   .
- Generalization is used to represent a hierarchy of entities that share some attributes or operations  .
- Generalization is depicted by a triangle with a horizontal line connecting the subclasses to the superclass   .
- An example of generalization is the entity Person, which can be generalized from the entities Student and Employee, as shown below:

```
    Person
    /    \
Student  Employee
```

- In this example, Person is the superclass and Student and Employee are the subclasses. Person has some attributes that are common to both Student and Employee, such as name, address, and phone number. Student and Employee have some attributes that are specific to them, such as student_id and salary, respectively. Person also has some relationships that are common to both Student and Employee, such as lives_in and works_for. Student and Employee have some relationships that are specific to them, such as enrolled_in and manages, respectively   .
- Generalization can also be applied recursively to form further higher level entities from existing superclasses. For example, the entity Animal can be generalized from the entities Mammal and Bird, and Mammal can be further generalized from the entities Dog and Cat, as shown below:

```
       Animal
       /    \
   Mammal  Bird
   /    \
 Dog    Cat
```

- In this example, Animal is the highest level superclass and Dog and Cat are the lowest level subclasses. Animal has some attributes that are common to all its subclasses, such as name, color, and weight. Mammal has some attributes that are common to its subclasses, such as fur and milk. Bird has some attributes that are specific to it, such as feathers and wings. Dog and Cat have some attributes that are specific to them, such as breed and tail. Animal also has some relationships that are common to all its subclasses, such as belongs_to and eats. Mammal has some relationships that are common to its subclasses, such as mates_with and gives_birth_to. Bird has some relationships that are specific to it, such as flies and lays_eggs. Dog and Cat have some relationships that are specific to them, such as barks and scratches, respectively   .