### Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data abstraction also supports data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in the ANSI/SPARC database architecture :
  - Physical level: This is the lowest level of data abstraction. It describes how the data is physically stored in the storage devices and the access methods used to retrieve and update the data. It also reveals the data structures and file organizations used to store the data, such as B+ trees, hashing, etc. The physical level is also called the internal level or the implementation level .
  - Logical level: This is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data. It also defines the constraints and rules that apply to the data. The logical level is independent of the physical level and can be changed without affecting the physical level. The logical level is also called the conceptual level or the schema level .
  - View level: This is the highest level of data abstraction. It describes how the data is seen by the users and the applications. It can show only a part of the database that is relevant to a specific user or application. It can also hide some details of the data types, constraints, and relationships from the users and applications. The view level is also called the external level or the user level .
- The views of data at different levels of abstraction are shown in the following diagram:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    View level   |       |   Logical level |       |  Physical level |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  User view 1    |       |   Conceptual    |       |   Internal      |
|                 |       |     schema      |       |    schema       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  User view 2    |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  User view 3    |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```