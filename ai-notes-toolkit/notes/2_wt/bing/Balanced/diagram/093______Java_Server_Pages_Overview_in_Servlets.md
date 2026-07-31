#### Java Server Pages Overview in Servlets

JavaServer Pages (JSP) is a technology that allows developers to create dynamic web pages using Java and Java Servlets. JSP pages are compiled into Java servlets and run on the server. JSP uses a special syntax that embeds snippets of Java code within HTML, and these pages are stored as regular HTML files with a .jsp extension.

A servlet is a Java class that handles requests, processes them, and responds back with a response. Servlets run inside a servlet container, which is a component of a web server that provides an environment for servlet execution. Servlets can access various Java APIs, such as JDBC, JNDI, EJB, JAXP, etc.

The following diagram shows the basic architecture of JSP and servlets:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Web Browser   |<-->|   Web Server    |<-->|   Servlet/JSP   |
|                 |    |                 |    |   Container     |
+-----------------+    +-----------------+    +-----------------+
                                  |                     |
                                  |                     |
                                  v                     v
                          +-----------------+    +-----------------+
                          |                 |    |                 |
                          |   Static Files  |    |   Java APIs     |
                          |                 |    |                 |
                          +-----------------+    +-----------------+
```

The web browser sends a request to the web server, which forwards it to the servlet container. The servlet container either invokes an existing servlet or loads and invokes a JSP page. The servlet or JSP page performs the necessary processing and generates a response, which is sent back to the web browser via the web server. The servlet or JSP page can also access static files, such as images, CSS, JavaScript, etc., and various Java APIs, such as databases, messaging, transactions, etc.