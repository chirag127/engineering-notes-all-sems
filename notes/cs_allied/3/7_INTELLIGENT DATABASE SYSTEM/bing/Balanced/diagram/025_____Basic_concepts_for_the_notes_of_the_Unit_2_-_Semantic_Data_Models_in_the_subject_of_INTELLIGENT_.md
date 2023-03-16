### Basic concepts for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a high-level, conceptual data model that includes semantic information that adds meaning to the data and the relationships between them .
- A semantic data model is designed to capture more of the meaning of an application environment than is possible with contemporary database models, such as the relational model or the entity-relationship model.
- A semantic data model can express and exchange information that enables interoperability, integration, and reasoning across heterogeneous data sources .
- A semantic data model consists of three main components: objects, attributes, and relationships .
  - Objects are the entities or concepts that exist in the application domain, such as students, courses, books, etc. Objects can be classified into types or classes using the "instance of" relation, such as a student is an instance of a person .
  - Attributes are the properties or characteristics of objects, such as name, age, address, etc. Attributes can have values or ranges of values, such as a name can be a string, an age can be a number, etc .
  - Relationships are the associations or connections between objects, such as a student enrolls in a course, a book belongs to a library, etc. Relationships can have cardinalities or constraints, such as a student can enroll in many courses, a book can belong to only one library, etc .
- A semantic data model can use various techniques to represent the structure and semantics of the data, such as :
  - Classification: This classifies different objects in objective reality by using "instance of" relations, such as a student is an instance of a person, a person is an instance of a living being, etc.
  - Aggregation: This defines a new object from a set of objects that become its components using "has a" relations, such as a course has a name, a code, a description, etc.
  - Generalization: This defines a new object from a set of objects that share some common characteristics using "is a" relations, such as a person is a generalization of a student and a teacher, a living being is a generalization of a person and an animal, etc.
  - Specialization: This defines a new object from a set of objects that have some specific characteristics using "is a" relations, such as a student is a specialization of a person, a person is a specialization of a living being, etc.
  - Abstraction: This defines a new object from a set of objects that have some abstract or conceptual meaning using "represents" or "denotes" relations, such as a grade represents the performance of a student in a course, a name denotes the identity of a person, etc.
- A semantic data model can be represented graphically using a semantic network or a conceptual graph, which are nodes and links diagrams that show the objects, attributes, and relationships in the data .
- A semantic data model can be implemented using various technologies, such as semantic web standards (RDF, OWL, SPARQL, etc), knowledge representation languages (KRL, KL-ONE, etc), or object-oriented databases (OODB, ODMG, etc) .