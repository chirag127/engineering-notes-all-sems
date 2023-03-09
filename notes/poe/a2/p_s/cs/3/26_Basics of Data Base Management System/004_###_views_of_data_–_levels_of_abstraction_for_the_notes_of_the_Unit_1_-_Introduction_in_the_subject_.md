 Here are the views of data – levels of abstraction for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System:

1. Physical level:
- Lowest level of abstraction.
- Describes how the data is actually stored in the database.
- Deals with the exact storage structure used to store and access data. E.g. files, indexes etc.
- Implementation and functionality details are exposed at this level.
- Used by DBMS developers, database administrators and sometimes application programmers.

2. Logical level:
- Higher level of abstraction than the physical level.
- Describes what data is stored in the database, and the relationships between the data.
- Modelled using the database schema in a data definition language. E.g. CREATE TABLE statements in SQL.
- Used by database designers and application programmers.

3. View level:
- Highest level of abstraction.
- Provides different views of the data for different users based on their requirements.
- Data is not directly from tables but derived using queries on the tables.
- Used by end users and public.

Advantages:
- Data independence: The upper levels are isolated from changes in the lower levels.
- Increased efficiency: The complexity is hidden and only relevant details are exposed at each level.
- Flexibility: Various views can be created for different users at the view level.

Disadvantages:
- There may be some loss of efficiency due to the additional abstraction layer.
- It can be difficult to choose the right balance of abstraction.

Applications:
- Complex databases with multiple types of users.
- Very large databases where physical optimization is important.
- Databases that need to be flexible and adaptable to changing requirements.