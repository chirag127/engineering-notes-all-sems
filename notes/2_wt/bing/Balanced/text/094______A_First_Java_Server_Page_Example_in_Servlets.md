#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a special type of web page that contains Java code embedded in HTML or XML.
- A JSP is compiled into a servlet by a web container, such as Tomcat or Jetty, and executed on the server side to generate dynamic content for the client.
- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and handles HTTP requests and responses.
- A JSP can use various elements to include Java code, such as:
  - Scriptlets: `<% ... %>` for arbitrary Java code
  - Expressions: `<%= ... %>` for printing the result of a Java expression
  - Declarations: `<%! ... %>` for declaring variables and methods
  - Directives: `<%@ ... %>` for setting page attributes and importing packages
  - Actions: `<jsp: ... />` for invoking built-in or custom tags
- A simple JSP example that prints the current date and time is:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A First JSP Example</title>
</head>
<body>
    <h1>A First JSP Example</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- To run this JSP, you need to:
  - Save it as `first.jsp` in the web application directory of your web container, such as `webapps/ROOT` in Tomcat.
  - Start your web container and open a browser to access the URL `http://localhost:8080/first.jsp`.
  - You should see the output similar to:

![JSP output](https://i.imgur.com/0Q7n0ZT.png)

- You can also use JSP to interact with servlets, beans, databases, and other web components.