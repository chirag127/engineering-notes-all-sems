Post deployment testing is a type of testing in which the software is tested after it is being deployed to production. It involves verifying the functionality, performance, security, and usability of the software in the real environment. Some post deployment testing activities include :

- Retesting the software features to ensure they work as expected in production.
- Gathering user feedback to identify any issues or improvement areas.
- Monitoring the software to detect any errors, crashes, or performance degradation.
- Analyzing the usage data and metrics to evaluate the software quality and user satisfaction.
- Applying patches or updates to fix any bugs or vulnerabilities.

The following diagram illustrates the basic architecture of a post deployment testing process:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Pre-deployment|      |   Deployment   |      | Post-deployment|
|    Testing     |----->|                |----->|    Testing     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       v                       v                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Test          |      |  Production    |      |  Test          |
|  Environment   |      |  Environment   |      |  Environment   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       v                       v                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Test          |      |  Software      |      |  Test          |
|  Data          |      |  Application   |      |  Data          |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

: https://cloud.google.com/architecture/application-deployment-and-testing-strategies
: https://www.testim.io/blog/deployment-testing/
: https://www.geeksforgeeks.org/post-deployment-testing-in-software-testing/
: https://mattermost.com/blog/pre-and-post-deployment-testing-for-ci-cd/