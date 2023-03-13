Java Server Pages (JSP) are a technology that allows dynamic content injection into static web pages using Java and Java Servlets. JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines .

The basic architecture of JSP in servlets is as follows:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Browser     |     |    Web Server  |     |    Database    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |  HTTP Request        |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      |  JSP/Servlet Engine |
       |                      |--------------------->|
       |                      |                      |
       |                      |  JDBC/SQL           |
       |                      |--------------------->|
       |                      |                      |
       |                      |<---------------------|
       |                      |                      |
       |                      |  HTML Response       |
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
```

The browser sends an HTTP request to the web server, which then forwards it to the JSP/servlet engine. The JSP/servlet engine processes the request and generates dynamic content using Java code and optionally accesses the database using JDBC/SQL. The JSP/servlet engine then sends back an HTML response to the web server, which then forwards it to the browser. The browser displays the HTML response to the user.