 Here are the notes for Unit 4 - Database Design & Normalization in the subject of Basics of Database Management System:

### Database Design

- The process of producing a detailed data model of a database. It includes defining the data types, structures and constraints of data to be stored in the database.
- The goal is to create an accurate and efficient model of data storage.
- Steps:
	1. Determine requirements - Analyse the purpose of the database and requirements of the users.
	2. Choose data structure - Decide how to represent data, relations, hierarchies, etc.
	3. Design relations - Define tables, columns, data types, keys, constraints, etc.
	4. Normalize relations - Remove anomalies and redundancies.
	5. Evaluate and refine design - Check performance, fix any issues.

### Database Normalization

- The process of organizing data into tables in a database by removing duplicated data and ensuring data dependencies make sense.
- It is done by applying a series of guidelines called normal forms.
- Advantages:
	- Minimizes duplicate data
	- Prevents anomalies (update, insertion, deletion)
	- Creates efficient storage
- Disadvantages:
	- Can be complex
	- May require additional tables and joins, decreasing performance

[Include diagrams and examples here if required]

The 1st, 2nd and 3rd normal forms are the most common and ensure atomicity, uniqueness and referential integrity respectively. Higher normal forms handle more complex dependencies but are rarely used in practice.

[Include more details and points as required.]