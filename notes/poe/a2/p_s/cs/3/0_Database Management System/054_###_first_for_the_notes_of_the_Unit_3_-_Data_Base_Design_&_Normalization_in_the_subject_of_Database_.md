 Here are the notes for Unit 3 - Data Base Design & Normalization in the subject of Database Management System:

### Database Design

1. What is Database Design?
- The process of producing a detailed data model of a database.
- The design should guarantee that the database structure is suitable to store and retrieve data with efficiency, reliability and security.
- The main objectives of database design are:
    - Data Integrity
    - Redundancy Minimization
    - Data Manipulation Efficiency

2. Types of Design
- Conceptual Design: Represents data entities and relationships in a database. Focuses on what data is required and how it should be organized.
- Logical Design: Translates the conceptual design into a schema that can be implemented using a specific DBMS. Focuses on how the data should be represented and stored.
- Physical Design: Focuses on the physical implementation of the database. Specifies data structures, file organizations, indexes, etc.

[Additional points and examples can be added here for the types of design]

3. Design Process
- Analyze system requirements and identify data to be stored
- Determine relationships between data
- Arrange data into tables with rows and columns
- Determine primary keys for tables
- Normalize the tables to eliminate redundancy
- Evaluate and tune the design for performance

[Detailed steps and descriptions can be added here for the design process with examples]

### Normalization

1. What is Normalization?
- The process of organizing data in a database by minimizing redundancy and dependency.
- It divides larger tables into smaller tables and links them using relationships.
- The aim is to isolate data so that additions, deletions, and modifications of an attribute can be made in just one table.

[Continue with more points and details on normalization, different normal forms with examples]