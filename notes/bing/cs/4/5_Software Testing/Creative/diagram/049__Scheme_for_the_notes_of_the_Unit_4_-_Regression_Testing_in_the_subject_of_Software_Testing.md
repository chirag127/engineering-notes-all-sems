Regression testing is a type of software testing that verifies that a code change in the software does not impact the existing functionality of the product. Regression testing is performed to ensure the quality and reliability of the software after any modification or update.

A possible diagram for the scheme for the notes of the unit 4 - regression testing in the subject of software testing is as follows:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Code Change    |---->|  Re-Testing     |---->|  Regression     |
|                 |     |                 |     |  Testing        |
+-----------------+     +-----------------+     +-----------------+
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  Bug Fix        |---->|  Re-Testing     |---->|  Regression     |
    |                 |     |                 |     |  Testing        |
    +-----------------+     +-----------------+     +-----------------+
```

The diagram shows the flow of regression testing in a software development cycle. The code change is the initial trigger for re-testing, which verifies that the change has not introduced any new defects. The regression testing is then performed to check that the existing functionality of the software is still working as expected. The same process is repeated for any bug fix that is applied to the software. Regression testing helps to maintain the quality and performance of the software throughout its lifecycle.