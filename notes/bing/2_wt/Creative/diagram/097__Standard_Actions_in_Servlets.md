Standard actions in servlets are JSP elements that use XML syntax to control the behavior of the servlet engine. They can be used to dynamically insert a file, reuse a bean component, forward the user to another page, etc. There are 12 types of standard actions in JSP, each with a specific tag name and attributes.

The following diagram illustrates the basic architecture of a servlet that uses standard actions to process a request and generate a response:

#### Standard Actions in Servlets

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Web Browser   |      |  Web Server    |      |  Servlet       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |  HTTP Request        |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      |  Servlet Request     |
       |                      |--------------------->|
       |                      |                      |
       |                      |                      |  Process request
       |                      |                      |  and use standard
       |                      |                      |  actions to
       |                      |                      |  - include a file
       |                      |                      |  - use a bean
       |                      |                      |  - forward to another page
       |                      |                      |  - etc.
       |                      |                      |
       |                      |  Servlet Response    |
       |                      |<---------------------|
       |                      |                      |
       |  HTTP Response       |                      |
       |<---------------------|                      |
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
       V                      V                      V
```