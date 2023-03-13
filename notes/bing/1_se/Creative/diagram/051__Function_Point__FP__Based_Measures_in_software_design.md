Function Point (FP) Based Measures are a technique to estimate the cost and effort of software development and maintenance based on the functionality that the user requests and receives. FP are derived using an empirical relationship based on countable measures of software's information domain and assessments of software complexity  .

The following diagram illustrates the basic steps of FP based estimation in software design:

```
+-----------------+     +-----------------+     +-----------------+
| Count the types |     | Calculate the   |     | Apply the       |
| of user         |     | unadjusted FP   |     | complexity      |
| functions       |---->| (UFP)           |---->| adjustment      |
| (inputs,        |     |                 |     | factor (CAF)    |
| outputs,        |     |                 |     |                 |
| inquiries,      |     |                 |     |                 |
| files,          |     |                 |     |                 |
| interfaces)     |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                                                        |
                                                        |
                                                        V
                                               +-----------------+
                                               | Calculate the   |
                                               | adjusted FP     |
                                               | (AFP)           |
                                               |                 |
                                               | AFP = UFP * CAF |
                                               +-----------------+
                                                        |
                                                        |
                                                        V
                                               +-----------------+
                                               | Estimate the    |
                                               | cost and effort |
                                               | based on AFP    |
                                               | and other       |
                                               | factors         |
                                               +-----------------+
```