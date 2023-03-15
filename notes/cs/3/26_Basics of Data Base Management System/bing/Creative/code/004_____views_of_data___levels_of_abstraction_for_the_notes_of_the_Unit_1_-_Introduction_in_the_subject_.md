### Views of Data – Levels of Abstraction

- Views of data are the ways of representing the data in a database system at different levels of abstraction.
- Data abstraction is the process of hiding the details of how the data is stored and manipulated from the users and applications.
- Data abstraction allows the separation of the logical and physical aspects of the data, and provides data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three main levels of data abstraction in a database system: physical, logical, and view level.

#### Physical Level

- The physical level is the lowest level of data abstraction. It describes how the data is actually stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level reveals the details of the data structures, such as records, files, indexes, and hashing schemes, and the physical locations and addresses of the data blocks.
- The physical level is usually hidden from the users and applications, and is only visible to the database administrators and system programmers.

#### Logical Level

- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data, without specifying how the data is stored or accessed.
- The logical level defines the conceptual schema of the database, which is a representation of the data using a data model, such as the entity-relationship model or the relational model.
- The logical level is independent of the physical level, which means that changes in the physical level do not affect the logical level. The logical level is also independent of the view level, which means that changes in the view level do not affect the logical level.

#### View Level

- The view level is the highest level of data abstraction. It describes how the data is seen by the users and applications, without revealing the details of the logical or physical level.
- The view level defines the external schema of the database, which is a subset of the conceptual schema that is relevant to a particular user or application.
- The view level allows the users and applications to access the data in a customized and simplified way, and to hide the data that they do not need or are not authorized to see.
- The view level is dependent on the logical level, which means that changes in the logical level may affect the view level. However, the view level can be modified without affecting the logical level, as long as the view level is consistent with the conceptual schema.