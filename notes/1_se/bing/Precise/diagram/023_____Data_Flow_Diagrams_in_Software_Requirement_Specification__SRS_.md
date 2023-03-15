### Data Flow Diagrams in Software Requirement Specification (SRS)

A data flow diagram (DFD) is a graphical representation of the flow of data in an information system. It shows how data is input, processed, stored, and output from the system. Here is an example of a DFD for a simple login process:

```
+------------+       +------------+
|            |       |            |
|   User     |       |   System   |
|            |       |            |
+------+-----+       +------+-----+
       |                    |
       |  Enter Credentials |
       |-------------------->|
       |                    |
       |   Verify Credentials|
       |<--------------------|
       |                    |
       |   Access Granted   |
       |<--------------------|
       |                    |
```

In this diagram, the user enters their credentials, which are then sent to the system for verification. If the credentials are valid, the system grants access to the user. This is a simple example of how a DFD can be used to represent the flow of data in a system.
