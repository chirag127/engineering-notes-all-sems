 Here is the content in markdown format for the topic ### Data Independence for the notes of Unit 1 - Introduction in the subject of Basics of Data Base Management System:

### Data Independence

- Data independence refers to the immunity of the application programs from changes made in the database schema. The database schema may be changed for various reasons, such as adding new data items or modifying data types, etc. Such changes should not affect the existing application programs. This property of database systems is known as data independence.
- There are two types of data independence:

1. Physical data independence: It refers to the immunity of application programs to the changes in the physical structure of the database. The physical structure of a database includes the file organization, file locations, indexes used, access paths, etc. If the database management system provides physical data independence, the application programs are immune to the changes in physical database storage structures. They need to be modified only if the logical structure of the database changes.
2. Logical data independence: It refers to the immunity of application programs to the changes in the conceptual structure of the database. The conceptual structure includes the schema definitions of the database. If there is a change in the schema, the existing application programs should continue to function without any changes. Logical data independence is more difficult to achieve than the physical data independence.

- Advantages: The major advantages of data independence are:
- Changes made in the database do not affect application programs.
- Division of labor: Database administrators can change the physical database design to improve performance without affecting the application programs. Application programmers can change the logical schema without affecting the existing application programs.
- Increased productivity and reduced development and maintenance costs.
- Portability: Application programs that use logical data independence can be ported to other database systems easily.

- Applications: Data independence is a key property provided by database management systems to achieve increased productivity, reduced costs, and efficient maintenance. It separates the application programs from the complex internal details of the database. The users and application programmers need not worry about the physical storage details to access and manipulate the data in the database.