### Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data abstraction also supports data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in a database system: physical, logical, and view level.

#### Physical Level
- The physical level is the lowest level of data abstraction. It describes how the data is actually stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level is also called the internal level or the implementation level.
- The physical level is concerned with the data structures, file organizations, indexes, hashing, compression, encryption, and other physical aspects of data storage and access.
- The physical level is usually hidden from the users and applications, and only the database administrator (DBA) can access and modify it.
- The physical level is defined by the physical schema, which is the description of the physical organization and access methods of the data.

#### Logical Level
- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data.
- The logical level is also called the conceptual level or the data model level.
- The logical level is independent of the physical level, meaning that the logical structure and meaning of the data do not depend on how the data is physically stored and accessed.
- The logical level is the level that most users and applications interact with, as it provides a logical and meaningful view of the data.
- The logical level is defined by the logical schema, which is the description of the data and the data relationships in terms of a data model, such as the entity-relationship (ER) model, the relational model, or the object-oriented model.

#### View Level
- The view level is the highest level of data abstraction. It describes how the data is seen by different users and applications, according to their needs and preferences.
- The view level is also called the external level or the user level.
- The view level is derived from the logical level, meaning that the views are subsets or transformations of the data and the data relationships defined at the logical level.
- The view level can have multiple views, each tailored for a specific user group or application. For example, a view can show only a part of the data, hide some attributes, combine data from different tables, or perform some calculations on the data.
- The view level is defined by the view schema, which is the description of a view in terms of a data model, such as the relational model or the object-oriented model.