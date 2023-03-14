Automated Test Data Generation (ATDG) is an activity that in the course of software testing automatically generates test data for the software under test (SUT). It usually makes the testing more efficient, effective and reliable. There are many tools and techniques for ATDG, such as DATPROF, MOSTLY AI, Orson, etc.   

The following diagram illustrates the basic architecture of an ATDG system:

```
+-----------------+     +-----------------+     +-----------------+
| Test Data       |     | Test Data       |     | Test Data       |
| Requirements    |     | Generation      |     | Validation      |
| Specification   |     | Engine          |     | Engine          |
+-----------------+     +-----------------+     +-----------------+
| - Test coverage |     | - Data sources  |     | - Data quality  |
| - Data types    |     | - Data models   |     | - Data accuracy |
| - Data formats  |     | - Data rules    |     | - Data feedback |
| - Data domains  |     | - Data methods  |     | - Data metrics  |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      v                      |
        +------------------> +-----------------+ <------------------+
                             | Test Data       |
                             | Repository      |
                             +-----------------+
                             | - Data storage  |
                             | - Data access   |
                             | - Data delivery |
                             +-----------------+
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     v
                             +-----------------+
                             | Software Under  |
                             | Test (SUT)      |
                             +-----------------+
                             | - Test cases    |
                             | - Test scripts  |
                             | - Test results  |
                             +-----------------+
```