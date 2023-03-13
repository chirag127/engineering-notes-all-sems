COSMIC function points are a unit of measure of software functional size. The size is a consistent measurement (or estimate) which is very useful for planning and managing software and related activities. The process of measuring software size is called functional size measurement (FSM).

COSMIC function points are based on the concept of data movements, which are the smallest pieces of functionality that can be recognized by a user. There are four types of data movements: Entry, Exit, Read, and Write. Each data movement has a corresponding function point, which is counted according to the number of data attributes and data groups involved .

The basic architecture of a COSMIC function point measurement is shown in the following diagram, which is drawn using ASCII characters:

### COSMIC Full Function Points in spm
```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Functional   |    |    Functional   |    |    Functional   |
|     Process     |    |     Process     |    |     Process     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Entry (EIF)     |    | Entry (ILF)     |    | Exit (ILF)      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Exit (EIF)      |    | Read (ILF)      |    | Write (ILF)     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Read (EIF)      |    | Write (EIF)     |    | Entry (EIF)     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Write (EIF)     |    | Read (EIF)      |    | Exit (EIF)      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```
The diagram illustrates the possible data movements between a functional process and the data groups that it manipulates. A data group is a set of data attributes that are logically related and recognizable by a user. A data attribute is a single piece of data that has a meaning for a user.

A functional process is a set of data movements that satisfies a user's functional requirement. A functional process can be triggered by an Entry or an Exit data movement, or by an external event. A functional process can have any number of data movements, as long as they are logically related and coherent.

An Entry data movement is a movement of data from the user or another functional process to the functional process being measured. An Exit data movement is a movement of data from the functional process being measured to the user or another functional process. A Read data movement is a movement of data from a persistent data group to the functional process being measured. A Write data movement is a movement of data from the functional process being measured to a persistent data group.

A persistent data group is a data group that is stored in the software and can be accessed by more than one functional process. A persistent data group can be either an Internal Logical File (ILF) or an External Interface File (EIF). An ILF is a data group that is maintained by the software being measured. An EIF is a data group that is maintained by another software, but is used by the software being measured.

The size of a data movement is determined by the number of data attributes and data groups involved. A data movement has a size of one function point if it involves one data attribute and one data group. A data movement has a size of two function points if it involves either two or more data attributes and one data group, or one data attribute and two or more data groups. A data movement has a size of three function points if it involves two or more data attributes and two or more data groups.

The size of a functional process is the sum of the sizes of its data movements. The size of the software is the sum of the sizes of its functional processes.