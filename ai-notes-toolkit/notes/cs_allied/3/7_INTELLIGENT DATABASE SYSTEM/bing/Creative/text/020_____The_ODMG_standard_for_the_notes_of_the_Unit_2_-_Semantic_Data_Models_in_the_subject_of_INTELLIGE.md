### The ODMG standard for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data model (SDM) is a high-level semantics-based database description and structuring formalism (database model) for databases.
- It is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- The Object Database Management Group (ODMG) was created in 1991 by five object database vendors under the chairmanship of Rick Cattell.
- It was meant to provide a standard data model for object databases, just as SQL describes a standard data model for relational databases.
- The ODMG standard consists of four components:
  - The object model, which defines the basic concepts and terminology of object data management.
  - The object definition language (ODL), which is a schema definition language for specifying the structure and types of object data.
  - The object query language (OQL), which is a declarative query language for retrieving and manipulating object data.
  - The object manipulation languages (OMLs), which are bindings of ODL and OQL to various programming languages, such as C++, Java, and Smalltalk.
- The ODMG object model is based on the following principles:
  - Objects are uniquely identified by object identifiers (OIDs), which are system-generated and immutable.
  - Objects have state and behavior, which are defined by their classes and interfaces.
  - Objects can be atomic or complex, depending on whether they have subobjects or not.
  - Objects can be persistent or transient, depending on whether they are stored in the database or not.
  - Objects can be related by associations, which are named and typed links between objects.
  - Objects can be organized into collections, which are sets, bags, lists, or arrays of objects.
  - Objects can be inherited from other objects, which means they share their state and behavior with their superclasses.
  - Objects can be polymorphic, which means they can have different behavior depending on their actual class.