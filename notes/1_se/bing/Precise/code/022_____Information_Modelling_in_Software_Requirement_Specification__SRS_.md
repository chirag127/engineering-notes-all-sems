### Information Modelling in Software Requirement Specification (SRS)

Information modelling is a technique used in the software requirement specification (SRS) process to represent the data and information requirements of a system. It involves the creation of a conceptual model that describes the data entities, attributes, and relationships within the system.

The information model is typically represented using a graphical notation such as an entity-relationship diagram (ERD) or a class diagram. The model provides a high-level view of the data and information requirements of the system, and serves as a basis for the design of the database schema and the development of the software.

Information modelling is an important part of the SRS process as it helps to ensure that the data and information requirements of the system are accurately captured and represented. It also helps to identify any potential issues or inconsistencies in the data and information requirements, which can be addressed early in the development process.

```python
# Example of an entity-relationship diagram (ERD) for a simple library system

# Entities: Book, Author, Publisher
# Attributes: Book (title, ISBN, publication_date), Author (name, date_of_birth), Publisher (name, address)
# Relationships: Book is written by Author, Book is published by Publisher

# ERD:
# +--------+       +--------+       +--------+
# | Book   |       | Author |       |Publisher|
# +--------+       +--------+       +--------+
# | title  |       | name   |       | name   |
# | ISBN   |       | dob    |       | address|
# | pub_date|       +--------+       +--------+
# +--------+           |                |
#     |                |                |
#     |                |                |
#     +----------------+                |
#     |                                 |
#     |                                 |
#     +---------------------------------+
```