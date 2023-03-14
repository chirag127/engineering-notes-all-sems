COSMIC function points are a unit of measure of software functional size. The size is a consistent measurement (or estimate) which is very useful for planning and managing software and related activities. The process of measuring software size is called functional size measurement (FSM). COSMIC function points are applicable to business software, real-time software and infrastructure software at any level of decomposition.

The COSMIC method is based on two main principles: the software context model and the generic software model. The software context model defines the software to be measured and its functional users, which are the senders and/or intended recipients of data to/from the software. The generic software model defines the four types of data movements that can occur between the software and its functional users: entry, exit, read and write. Each data movement has a functional process, which is a set of logically related and order-dependent data movements that satisfy a user's need.

The COSMIC method measures the functional size of software by counting the number of data movements and their associated data groups, which are sets of data attributes that are logically related from the user's perspective. The size of a data movement is equal to the number of data groups involved in it. The size of a functional process is equal to the sum of the sizes of its data movements. The size of a piece of software is equal to the sum of the sizes of its functional processes.

The following diagram illustrates the basic architecture of the COSMIC method using an example of a software that manages a library system:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Library User  |       |  Library Staff |       |  Library DB    |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |<-----------------------|                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |<-----------------------|
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |----------------------->|
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |----------------------->|                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |

```

The diagram shows the three functional users of the software: the library user, the library staff and the library database. The arrows represent the data movements between the software and the functional users. For example, the library user can enter a request to borrow a book, which is an entry data movement with one data group (request). The software can exit a confirmation message to the library user, which is an exit data movement with one data group (confirmation). The software can also read the availability of the book from the library database, which is a read data movement with one data group (availability). The software can write the updated status of the book to the library database, which is a write data movement with one data group (status).

The data movements are grouped into functional processes according to the user's needs. For example, the functional process of borrowing a book consists of four data movements: entry, exit, read and write. The size of this functional process is four data groups. The size of the software is the sum of the sizes of all the functional