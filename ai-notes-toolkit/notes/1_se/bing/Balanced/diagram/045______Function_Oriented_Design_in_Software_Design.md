Function Oriented Design is a method to software design where the model is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function  . The system is designed from a functional viewpoint  .

#### Function Oriented Design in Software Design

A common way to represent Function Oriented Design is using Data Flow Diagrams (DFDs) and Data Dictionaries . A DFD maps out the flow of information for any process or system. It uses symbols to represent the different entities, processes, data stores, and data flows in the system . A Data Dictionary is a repository to store information about all data items defined in DFDs, such as their names, descriptions, formats, and sources .

An example of a DFD for a student registration system is shown below:

```
+----------------+        +-----------------+        +----------------+
|                |        |                 |        |                |
|  Student       |------->|  Registration   |------->|  Database      |
|  Information   |        |  Process        |        |  System        |
|                |        |                 |        |                |
+----------------+        +-----------------+        +----------------+
```

The symbols used in the DFD are:

- A rectangle represents an external entity, such as a user or another system, that provides or receives data from the system.
- A circle represents a process, such as a function or a module, that transforms the input data into the output data.
- A double line represents a data store, such as a file or a database, that stores or retrieves data from the system.
- An arrow represents a data flow, which shows the direction and the name of the data that flows between the entities, processes, and data stores.

A Data Dictionary for the DFD above could look like this:

| Data Item | Description | Format | Source | Destination |
|-----------|-------------|--------|--------|-------------|
| Student Information | The personal and academic details of a student | Name, ID, Address, Course, etc. | Student | Registration Process |
| Registration Process | The function that validates and registers the student for a course | N/A | Student Information | Database System |
| Database System | The system that stores and manages the student records | N/A | Registration Process | N/A |
