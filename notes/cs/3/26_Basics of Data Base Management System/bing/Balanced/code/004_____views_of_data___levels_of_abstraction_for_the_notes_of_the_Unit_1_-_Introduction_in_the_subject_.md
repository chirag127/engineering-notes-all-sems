# Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data abstraction also supports data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in a database system: physical level, logical level, and view level.

## Physical Level

- The physical level is the lowest level of data abstraction. It describes how the data is physically stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level is also called the internal level or the implementation level.
- The physical level is concerned with the data structures, file organizations, indexes, hashing, compression, encryption, and other techniques that optimize the performance and security of the database system.
- The physical level is usually hidden from the users and applications, and only the database administrator (DBA) can access and modify it.
- The physical level is defined by the internal schema, which is a description of the physical representation of the data and the access methods.

## Logical Level

- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data.
- The logical level is also called the conceptual level or the data model level.
- The logical level is independent of the physical level, meaning that the logical structure of the data does not depend on how the data is stored or accessed.
- The logical level is the level that most users and applications interact with, as it provides a logical view of the data that is meaningful and understandable.
- The logical level is defined by the conceptual schema, which is a description of the data and the constraints on the data using a data model, such as the entity-relationship (ER) model or the relational model.

## View Level

- The view level is the highest level of data abstraction. It describes how the data is seen by different users and applications that access the database.
- The view level is also called the external level or the user level.
- The view level is independent of both the physical and the logical levels, meaning that the view of the data does not depend on how the data is stored or organized.
- The view level allows different users and applications to have different views of the same data, depending on their needs and preferences.
- The view level is defined by the external schema, which is a description of a subset of the data and the operations on the data using a query language, such as SQL or QBE.