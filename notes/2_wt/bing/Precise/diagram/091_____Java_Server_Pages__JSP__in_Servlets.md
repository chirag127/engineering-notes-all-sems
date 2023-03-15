### Java Server Pages (JSP) in Servlets

Java Server Pages (JSP) is a technology that allows developers to create dynamic web pages using HTML, XML, or other document types. JSP is built on top of the Java Servlet API, which provides a framework for handling HTTP requests and responses.

Here is an ASCII diagram that illustrates the relationship between JSP and Servlets:

```
+----------------+
|                |
|     Client     |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|     Server     |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|   Web Server   |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|   Servlet      |
|   Container    |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|   JSP Page     |
|                |
+----------------+
```

In this diagram, the client sends a request to the server, which is then forwarded to the web server. The web server passes the request to the servlet container, which processes the request and generates a response. If the response includes a JSP page, the servlet container will process the JSP page and generate the final response, which is then sent back to the client.
