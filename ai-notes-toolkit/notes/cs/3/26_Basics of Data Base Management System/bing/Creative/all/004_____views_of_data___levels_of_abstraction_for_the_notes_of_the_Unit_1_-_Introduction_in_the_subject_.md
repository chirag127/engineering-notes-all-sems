# Views of Data – Levels of Abstraction

- Views of data in DBMS describe the abstraction of data at three levels: physical, logical, and view level.
- Data abstraction is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data independence is the property that allows data at a certain level to be modified without affecting the data at higher levels.

## Physical Level

- The physical level of abstraction defines how data is stored in the storage and also reveals its access path.
- It is the lowest level of data abstraction and it tells us how the data is actually stored in memory.
- The access methods like sequential or random access and file organization methods like B+ trees and hashing are used for the same.
- The physical level is also called the internal level.

## Logical Level

- The logical level of abstraction defines what data is stored in the database and the relationships among the data.
- It is the middle level of data abstraction and it tells us what data is stored and how it is organized.
- The logical level is independent of the physical level and it can be represented by a conceptual diagram like an ER model.
- The logical level is also called the conceptual level.

## View Level

- The view level of abstraction describes the application which the users use to retrieve the information from the database.
- It is the highest level of data abstraction and it describes only a part of the database and hides some information to the user.
- At the view level, computer users see a set of application programs that hide details of data types.
- The view level is also called the external level.