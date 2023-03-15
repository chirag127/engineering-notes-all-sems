#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a web page that contains Java code embedded in HTML or XML.
- A JSP is compiled into a servlet by a JSP compiler, which is a special type of servlet container.
- A servlet is a Java class that handles HTTP requests and generates HTTP responses.
- A servlet can access the request and response objects, as well as other objects that provide information about the web application and the server environment.
- A servlet can also use JavaBeans, custom tags, expression language, and other features to simplify the web development process.
- A JSP can be seen as a convenient way of writing servlets, as it allows the separation of presentation logic (HTML or XML) and business logic (Java code).
- A JSP can also be seen as a template engine, as it can dynamically generate web pages based on the data provided by the servlet or other sources.
- A JSP follows a specific syntax and structure, which includes directives, declarations, scriptlets, expressions, comments, and actions.
- A JSP directive is a statement that provides instructions to the JSP compiler or the servlet container, such as the page language, the content type, the import statements, etc.
- A JSP declaration is a statement that declares variables or methods that can be used in the JSP.
- A JSP scriptlet is a block of Java code that is executed when the JSP is processed by the servlet container.
- A JSP expression is a Java expression that is evaluated and inserted into the output stream of the JSP.
- A JSP comment is a comment that is ignored by the JSP compiler and the servlet container, but can be seen in the source code of the JSP.
- A JSP action is a tag that invokes a built-in or custom functionality, such as including another JSP, forwarding the request to another resource, setting or getting a JavaBean property, etc.

- A simple JSP example that displays the current date and time is shown below:

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
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

- The first line of the JSP is a directive that specifies the page language, the content type, and the character encoding of the JSP.
- The HTML tags define the structure and appearance of the web page.
- The JSP expression `<%= new java.util.Date() %>` is evaluated and inserted into the output stream of the JSP, displaying the current date and time.