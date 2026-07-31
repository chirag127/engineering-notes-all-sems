### Attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- An attribute is a describing characteristic or property that defines all items pertaining to a certain category applied to all cells of a column in a relational database .
- Attributes map to database table columns, and both table columns and attributes should describe precisely one property of the entity.
- An entity is a person, place, thing, or concept that can be uniquely identified and about which data can be stored in a database.
- A relationship is a logical connection between two or more entities, indicating how they are associated or interact with each other.
- There are several different types of attributes represented on an entity relationship diagram (ERD), which is a graphical representation of the entities, attributes, and relationships in a database:
  - Simple: an attribute that cannot be split into other attributes, such as a first name.
  - Composite: an attribute that can be split into other attributes, such as name being split into first, middle, and last name.
  - Derived: an attribute that is calculated or determined from another attribute, such as the age of record being calculated from the created date.
  - Single-valued: an attribute that has only one value for a given entity, such as gender.
  - Multi-valued: an attribute that can have more than one value for a given entity, such as hobbies.
  - Stored: an attribute that is physically stored in the database, such as address.
  - Null: an attribute that has no value for a given entity, such as middle name for some people.
  - Key: an attribute that uniquely identifies an entity, such as student ID.
  - Foreign key: an attribute that references the key attribute of another entity, such as course ID in the enrollment entity.
  - Candidate key: an attribute that can potentially be a key attribute, such as email address.
  - Alternate key: an attribute that is a candidate key but not chosen as the key attribute, such as phone number.
  - Composite key: a combination of two or more attributes that uniquely identifies an entity, such as order ID and product ID in the order detail entity.
- An example of an ERD with different types of attributes is shown below:

![ERD example](https://www.databasestar.com/wp-content/uploads/2017/01/erd-example.png)

: A Guide to the Entity Relationship Diagram (ERD) - Database Star
: What is an Attribute in Database Systems? - Techopedia.com
: What are attributes in a relational database? - Studybuff
: Database Design: Entities, Attributes, and Relationships