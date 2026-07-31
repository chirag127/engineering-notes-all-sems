Java Server Pages (JSP) are a technology that allows dynamic content injection into static web pages using Java and Java Servlets. JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines .

A JSP page is compiled into a Java servlet by the web container, which then executes the servlet to generate the HTML output that is sent to the client browser. The JSP page can contain HTML tags, JSP directives, JSP expressions, JSP scriptlets, and JSP actions that are processed by the web container .

The following diagram shows the basic architecture of JSP in servlets:

### Java Server Pages (JSP) in Servlets

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|   Web Browser  | <----> |   Web Server   | <----> |   Database     |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
                             |       ^
                             v       |
                         +----------------+
                         |                |
                         |   Web Container|
                         |                |
                         +----------------+
                             |       ^
                             v       |
                         +----------------+
                         |                |
                         |   JSP Engine   |
                         |                |
                         +----------------+
                             |       ^
                             v       |
                         +----------------+
                         |                |
                         |   JSP Page     |
                         |                |
                         +----------------+
                             |       ^
                             v       |
                         +----------------+
                         |                |
                         |   Servlet      |
                         |                |
                         +----------------+
```