Standard actions in servlets are predefined tags that control the behavior of the servlet engine. They can be used to include other files, reuse JavaBeans components, forward or redirect requests, and perform other tasks. There are 12 types of standard actions in servlets, which are:

- <jsp:include> : Includes the content of another resource at the time of request processing.
- <jsp:forward> : Forwards the current request to another resource for further processing.
- <jsp:param> : Specifies a parameter for the <jsp:include> or <jsp:forward> action.
- <jsp:plugin> : Generates browser-specific code to embed an applet or a JavaBean component.
- <jsp:fallback> : Specifies the content to display if the browser does not support the <jsp:plugin> action.
- <jsp:useBean> : Declares and instantiates a JavaBean component.
- <jsp:setProperty> : Sets the properties of a JavaBean component.
- <jsp:getProperty> : Gets the properties of a JavaBean component.
- <jsp:attribute> : Defines a dynamic attribute for a custom action or a standard action that accepts dynamic attributes.
- <jsp:body> : Defines a body for a custom action or a standard action that accepts a body.
- <jsp:element> : Creates an XML element dynamically and adds it to the XML document.
- <jsp:text> : Allows the use of literal text that might otherwise be interpreted as a JSP element.

The following diagram illustrates the basic architecture of a servlet that uses standard actions:

```
+------------------+      +-----------------+      +-----------------+
|  Web Browser     |      |  Web Server     |      |  Database       |
|                  |      |                 |      |                 |
|                  |      |  +-----------+  |      |                 |
|                  |      |  |  Servlet  |  |      |                 |
|                  |      |  | Container |  |      |                 |
|                  |      |  +-----------+  |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<------------------------|
       |                         |  Database query        |
       |                         |  and response          |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |<------------------------|                         |
       |  HTTP request          |                         |
       |------------------------>|                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<------------------------|
       |                         |  Include file content  |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<------------------------|
       |                         |  Forward request       |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<------------------------|
       |                         |  Use JavaBean          |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<------------------------|
       |                         |  Set/Get property      |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<------------------------|
       |                         |  Generate plugin code  |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |<----------------