#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a web page that contains Java code embedded in HTML or XML.
- A JSP is compiled into a servlet by a JSP compiler, which is a special type of servlet container.
- A servlet is a Java class that handles HTTP requests and generates dynamic web content.
- A JSP can use Java expressions, scriptlets, declarations, directives, and custom tags to create dynamic web content.
- A JSP can also access JavaBeans, servlets, and other Java components to perform business logic and data processing.

- A simple JSP example is shown below:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A First JSP Example</title>
</head>
<body>
    <h1>A First JSP Example</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
    <p>The value of pi is: <%= Math.PI %></p>
</body>
</html>
```

- The first line of the JSP is a directive that specifies the content type, the language, and other attributes of the page.
- The HTML tags create the structure and style of the web page.
- The <%= %> tags are expressions that evaluate to a value and insert it into the output stream.
- The new java.util.Date() expression creates a Date object and returns its string representation.
- The Math.PI expression returns the value of the constant pi.

- When this JSP is requested by a browser, the JSP compiler compiles it into a servlet class and executes it on the server.
- The servlet generates the HTML output and sends it back to the browser.
- The browser displays the web page with the dynamic content.