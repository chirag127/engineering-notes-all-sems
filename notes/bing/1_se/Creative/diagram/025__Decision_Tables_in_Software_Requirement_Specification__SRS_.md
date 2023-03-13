A decision table is a tool that helps to specify the behavior of a software system based on different combinations of input conditions and actions. It is a tabular representation of logical rules that can be used to document the requirements of a software system. A decision table consists of four parts: condition stubs, action stubs, condition entries, and action entries. The condition stubs are the input conditions that affect the behavior of the system. The action stubs are the output actions that the system performs. The condition entries are the possible values of the input conditions, usually represented by Y (yes), N (no), or - (don't care). The action entries are the expected outcomes of the output actions, usually represented by X (execute) or - (don't execute).

The following diagram illustrates the basic structure of a decision table:

```
+-----------------+-----------------+-----------------+-----------------+
| Condition Stub  | Condition Entry | Condition Entry | Condition Entry |
+-----------------+-----------------+-----------------+-----------------+
| Condition 1     | Y               | N               | -               |
+-----------------+-----------------+-----------------+-----------------+
| Condition 2     | Y               | -               | N               |
+-----------------+-----------------+-----------------+-----------------+
| Condition 3     | -               | Y               | N               |
+-----------------+-----------------+-----------------+-----------------+
| Action Stub     | Action Entry    | Action Entry    | Action Entry    |
+-----------------+-----------------+-----------------+-----------------+
| Action 1        | X               | -               | -               |
+-----------------+-----------------+-----------------+-----------------+
| Action 2        | -               | X               | -               |
+-----------------+-----------------+-----------------+-----------------+
| Action 3        | -               | -               | X               |
+-----------------+-----------------+-----------------+-----------------+
```

The diagram shows that the system performs different actions depending on the values of the input conditions. For example, if condition 1 and condition 2 are both true, then the system executes action 1. If condition 1 is false and condition 3 is true, then the system executes action 2. If condition 2 and condition 3 are both false, then the system executes action 3.

A decision table can be used to document the requirements of a software system in a Software Requirement Specification (SRS) document. An SRS is a document that defines what a given software system needs to do and takes care of various requirements. It is written according to the needs of the software and ensures that the software does not cause any problems to the end-users. The different features of the software are clearly detailed and given particular attention. A decision table can help to specify the functional requirements of the software, which describe the behavior and functionality of the system. A decision table can also help to avoid ambiguity and inconsistency in the requirements, as it shows all the possible scenarios and outcomes of the system. A decision table can also help to verify and validate the requirements, as it can be used to test the system against the expected behavior and actions. A decision table can also help to communicate the requirements to the developers, as it provides a clear and concise representation of the logic and rules of the system.

### Decision Tables in Software Requirement Specification (SRS)

```
+-----------------+-----------------+-----------------+-----------------+
| Condition Stub  | Condition Entry | Condition Entry | Condition Entry |
+-----------------+-----------------+-----------------+-----------------+
| User is logged in| Y               | N               | -               |
+-----------------+-----------------+-----------------+-----------------+
| User has access to file| Y               | -               | N               |
+-----------------+-----------------+-----------------+-----------------+
| File is encrypted| -               | Y               | N               |
+-----------------+-----------------+-----------------+-----------------+
| Action Stub     | Action Entry    | Action Entry    | Action Entry    |
+-----------------+-----------------+-----------------+-----------------+
| Open file       | X               | -               | -               |
+-----------------+-----------------+-----------------+-----------------+
| Request password| -               | X               | -               |
+-----------------+-----------------+-----------------+-----------------+
| Display error message| -               | -               | X               |
+-----------------+-----------------+-----------------+-----------------+
```

The diagram above shows an example of