# Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how the data is stored and manipulated from the users and applications.
- Data abstraction also enables data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in a database system: physical, logical, and view level.

## Physical Level

- The physical level is the lowest level of data abstraction. It describes how the data is physically stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level is also called the internal level or the implementation level.
- The physical level is concerned with the data structures, file organizations, indexing techniques, and compression methods that optimize the performance and storage efficiency of the database system.
- The physical level is usually hidden from the users and applications, and only the database administrator (DBA) can access and modify it.
- The physical level is also the most difficult and complex level to design and maintain.

## Logical Level

- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data.
- The logical level is also called the conceptual level or the data model level.
- The logical level is independent of the physical level, which means that the logical structure of the data does not depend on how the data is stored or accessed physically.
- The logical level is usually represented by a data model, such as the entity-relationship (ER) model, the relational model, or the object-oriented model.
- The logical level is the level that the users and applications interact with, and it provides a logical view of the entire database.

## View Level

- The view level is the highest level of data abstraction. It describes how the data is seen by different users and applications according to their needs and preferences.
- The view level is also called the external level or the user level.
- The view level is derived from the logical level, which means that the view level is a subset or a projection of the logical level.
- The view level can have multiple views, each of which represents a different aspect or perspective of the database.
- The view level is the level that provides the most flexibility and security to the users and applications, as they can access only the data that they are authorized to see and manipulate.