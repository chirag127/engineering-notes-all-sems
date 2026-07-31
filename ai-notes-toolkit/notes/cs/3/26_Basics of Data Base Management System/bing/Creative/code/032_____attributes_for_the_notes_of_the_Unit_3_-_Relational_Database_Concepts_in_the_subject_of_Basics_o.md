### Attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- An attribute is a describing characteristic or property that defines all items pertaining to a certain category applied to all cells of a column in a relational database .
- Attributes map to database table columns, and both table columns and attributes should describe precisely one property of the entity.
- An entity is a person, place, thing, or concept that can be uniquely identified and about which data can be stored in a database.
- A relationship is a logical connection or association between two or more entities that share some common attributes or properties.
- There are several different types of attributes represented on an entity relationship diagram (ERD), which is a graphical representation of the entities, attributes, and relationships in a database:
  - Simple: an attribute that cannot be split into other attributes, such as a first name.
  - Composite: an attribute that can be split into other attributes, such as name being split into first, middle, and last name.
  - Derived: an attribute that is calculated or determined from another attribute, such as the age of record being calculated from the created date.
  - Single-valued: an attribute that has only one value for a given entity, such as gender.
  - Multi-valued: an attribute that can have more than one value for a given entity, such as hobbies.
  - Stored: an attribute that is physically stored in the database, such as address.
  - Key: an attribute that uniquely identifies an entity or a relationship, such as employee ID.
  - Foreign key: an attribute that references a key attribute of another entity or relationship, such as department ID.
  - Primary key: a key attribute or a combination of key attributes that uniquely identifies an entity or a relationship, such as order ID.
  - Composite key: a combination of key attributes that uniquely identifies an entity or a relationship, such as order ID and product ID.
- An example of an ERD with different types of attributes is shown below:

![ERD example](https://www.databasestar.com/wp-content/uploads/2017/01/erd-example.png)