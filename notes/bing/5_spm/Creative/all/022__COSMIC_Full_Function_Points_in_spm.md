### COSMIC Full Function Points in spm

- COSMIC stands for Common Software Measurement International Consortium, which is an organization that develops and maintains a standard method for measuring software functional size.
- COSMIC function points are a unit of measure of software functional size, which is the amount of functionality that a software provides to its users, based on their requirements  .
- The functional size is consistent regardless of the technology used to build the software, and can be estimated or measured at any stage of the software life cycle .
- The functional size measurement (FSM) process using COSMIC method involves identifying and counting four types of data movements between the software and its functional users   :
  - Entry: an input of data from a functional user to the software
  - Exit: an output of data from the software to a functional user
  - Read: a retrieval of data from persistent storage by the software
  - Write: a storage of data to persistent storage by the software
- Each data movement is counted as one COSMIC function point (CFP), regardless of the complexity or volume of the data   .
- The software functional users can be human users, other software systems, or hardware devices that interact with the software   .
- The software is divided into functional processes, which are groups of data movements that contribute to a user-recognizable function   .
- The functional size of the software is the sum of the CFPs of all the functional processes   .
- The COSMIC method can be applied to a wide range of software domains, such as business, real-time, embedded, and infrastructure software   .
- The COSMIC method can be used for various purposes, such as estimating effort, cost, and duration of software projects, benchmarking productivity and quality, and evaluating software maintenance    .

#### Example of COSMIC FSM

Consider a simple software that allows a user to create, read, update, and delete (CRUD) records of employees in a database. The software has the following functional processes and data movements:

- Create employee: the user enters the employee data (Entry), the software validates the data (Exit), and stores the data in the database (Write).
- Read employee: the user enters the employee ID (Entry), the software retrieves the employee data from the database (Read), and displays the data to the user (Exit).
- Update employee: the user enters the employee ID (Entry), the software retrieves the employee data from the database (Read), displays the data to the user (Exit), the user modifies the data (Entry), the software validates the data (Exit), and updates the data in the database (Write).
- Delete employee: the user enters the employee ID (Entry), the software retrieves the employee data from the database (Read), displays the data to the user (Exit), the user confirms the deletion (Entry), and the software deletes the data from the database (Write).

The functional size of the software is calculated as follows:

| Functional process | Entry | Exit | Read | Write | CFP |
|--------------------|-------|------|------|-------|-----|
| Create employee    | 1     | 1    | 0    | 1     | 3   |
| Read employee      | 1     | 1    | 1    | 0     | 3   |
| Update employee    | 2     | 2    | 1    | 1     | 6   |
| Delete employee    | 2     | 1    | 1    | 1     | 5   |
| Total              | 6     | 5    | 3    | 3     | 17  |

Therefore, the functional size of the software is 17 CFPs.

#### Advantages of COSMIC method

- It is simple, intuitive, and easy to learn and apply