Java Server Pages (JSP) are a technology that allows dynamic content injection into static web pages using Java and Java Servlets. JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines .

A JSP page is compiled into a Java servlet by the web container, which then executes the servlet to generate the HTML output that is sent to the client browser. The JSP page can also include HTML, XML, or other types of markup that are passed through to the output .

The following diagram shows the basic architecture of JSP in servlets:

### Java Server Pages (JSP) in Servlets

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Web Browser   |    |   Web Server    |    |   Web Container |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |  HTTP Request       |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      |  HTTP Request       |
       |                      |--------------------->|
       |                      |                      |
       |                      |  JSP Page           |
       |                      |<---------------------|
       |                      |                      |
       |                      |  Servlet            |
       |                      |--------------------->|
       |                      |                      |
       |                      |  HTML Output        |
       |                      |<---------------------|
       |                      |                      |
       |  HTTP Response      |                      |
       |<---------------------|                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
```