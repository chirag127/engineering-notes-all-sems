Implicit objects in servlets are Java objects that are created by the servlet container during the translation phase of JSP, when JSP is converted to servlet . These objects can be directly used in scriptlets that go in the service method. They are created by the container automatically, and they can be accessed using objects. There are 9 implicit objects in JSP: request, response, out, session, application, config, page, pageContext, and exception.

The following diagram illustrates the basic architecture of implicit objects in servlets using ASCII art:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Browser     |      |    Web Server  |      |    Database    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |  HTTP Request       |                       |
       |--------------------->|                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |  JSP Page            |
       |                      |--------------------->|
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |  Servlet             |
       |                      |<---------------------|
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |  Implicit Objects     |
       |                      |<---------------------|
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |  SQL Query           |
       |                      |--------------------->|
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |  SQL Result          |
       |                      |<---------------------|
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |  HTTP Response       |
       |                      |<---------------------|
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |  HTML Page          |                       |
       |<---------------------|                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
```