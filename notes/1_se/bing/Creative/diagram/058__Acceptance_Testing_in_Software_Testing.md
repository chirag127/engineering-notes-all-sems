Acceptance testing is a formal testing process that verifies whether a software product meets the user needs, requirements, and business processes. It is usually performed by the end-users or customers before accepting the software for production or deployment. Acceptance testing can be done manually or with the help of automated tools.

The following diagram illustrates the basic architecture of acceptance testing in software testing:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Development   |      |    Testing      |      |   Production    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Unit tests    |      |  Smoke tests    |      |  User feedback  |
|   Integration   |----->|  Integration    |----->|  Monitoring     |
|   tests         |      |  tests          |      |  Maintenance    |
|   System tests  |      |  Regression     |      |                 |
|                 |      |  tests          |      |                 |
|                 |      |  Security tests |      |                 |
|                 |      |  Performance    |      |                 |
|                 |      |  tests          |      |                 |
|                 |      |  API tests      |      |                 |
|                 |      |                 |      |                 |
|                 |      |  Acceptance     |      |                 |
|                 |      |  tests          |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows that acceptance testing is the final stage of testing before the software is moved to production. It is done after the software has passed unit tests, integration tests, system tests, and other types of tests. Acceptance testing ensures that the software meets the business requirements and operates correctly in real-world scenarios. It also helps the users or customers to decide whether to accept the software or not.