#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a special type of web page that contains Java code embedded in HTML or XML.
- A JSP is compiled into a servlet by a JSP compiler, which is a part of the web server or application server.
- A servlet is a Java class that handles HTTP requests and generates dynamic web content.
- A JSP can use Java expressions, scriptlets, declarations, directives, and custom tags to create dynamic web content.
- A JSP can also access JavaBeans, servlets, and other Java components to perform business logic and data processing.
- A JSP follows a specific syntax and structure, which is explained in detail in the following sections.

- A simple JSP example is shown below:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A First JSP Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line of the JSP is a directive, which starts with `<%@` and ends with `%>`.
- A directive provides information to the JSP compiler and the web server, such as the content type, the language, the import statements, the error page, etc.
- The directive in this example specifies that the content type is `text/html`, the language is `java`, and the page encoding is `UTF-8`.
- The rest of the JSP is a mix of HTML and Java code.
- The HTML code defines the structure and appearance of the web page, such as the title, the headings, and the paragraphs.
- The Java code is enclosed in `<%=` and `%>`, which are called expression tags.
- An expression tag evaluates a Java expression and inserts the result into the web page as a string.
- The expression in this example is `new java.util.Date()`, which creates a new Date object and returns the current date and time.
- When the JSP is requested by a web browser, the web server invokes the JSP compiler, which converts the JSP into a servlet.
- The servlet then executes the Java code and generates the HTML output, which is sent back to the web browser.
- The web browser displays the web page as shown below:

![A First JSP Example](https://i.imgur.com/9yZJX9L.png)

- This is a basic example of how a JSP works and what it can do.
- In the next sections, we will learn more about the different types of JSP elements and how to use them effectively.