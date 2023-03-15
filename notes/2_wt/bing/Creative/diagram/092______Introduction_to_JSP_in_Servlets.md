#### Introduction to JSP in Servlets

JSP stands for Java Server Pages. It is a server-side technology that lets you build dynamic web applications that work on any platform. JSP can use all Java APIs, including the JDBC API, which lets them connect to enterprise databases  .

Servlets are the Java programs that run on the Java-enabled web server or application server. They are used to handle the request obtained from the web server, process the request, produce the response, then send a response back to the web server. Servlets work on the server-side.

JSP is an extension to Servlet because it provides more functionality than servlet such as expression language, JSTL, etc. A JSP page consists of HTML tags and JSP tags. JSP is similar to HTML pages, but they also contain Java code executed on the server side  .

The following diagram shows how JSP and Servlet work together to create dynamic web applications:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Web Browser    |      |  Web Server     |      |  Application    |
|                 |      |                 |      |  Server         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |  HTTP Request       |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      |  JSP Page           |
       |                      |--------------------->|
       |                      |                      |
       |                      |                      |
       |                      |  Servlet            |
       |                      |<---------------------|
       |                      |                      |
       |                      |                      |
       |                      |  HTML Response       |
       |                      |<---------------------|
       |                      |                      |
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
       V                      V                      V
```