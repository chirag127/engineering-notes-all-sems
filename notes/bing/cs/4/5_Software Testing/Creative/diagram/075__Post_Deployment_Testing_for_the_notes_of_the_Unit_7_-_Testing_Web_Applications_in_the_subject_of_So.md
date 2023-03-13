Post deployment testing is a type of testing in which the software is tested after it is being deployed to production. It involves verifying the software features, gathering user feedback, and monitoring the software to ensure it functions as intended in production  . Post deployment testing continues throughout the entire life cycle of the software.

The following diagram illustrates the basic architecture of a post deployment testing process for web applications:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Test Plan     |    |  Test Cases    |    |  Test Scripts  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
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
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Web Server    |    |  Application    |    |  Database      |
|                |    |  Server         |    |  Server        |
+----------------+    +----------------+    +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
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
                              |
                              |
                              v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  User          |    |  Feedback      |    |  Monitoring    |
|  Interface     |    |  Collection    |    |  Tools         |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The diagram shows the following steps:

- The test plan, test cases, and test scripts are prepared before the deployment based on the software requirements and specifications.
- The web server, application server, and database server are deployed to production using a deployment strategy such as rolling update, blue-green, or canary.
- The user interface is the front-end of the web application that interacts with the users and displays the web pages.
- The feedback collection is the process of gathering user feedback on the web application features, usability, performance, and satisfaction .
- The monitoring tools are the software tools that monitor the web application for availability, reliability, performance, security, and errors  .
- The test plan, test cases, and test scripts are executed after the deployment to verify the software features and functionality  .
- The feedback collection and monitoring tools are used to identify and resolve any issues or defects in the web application throughout its life cycle  .