### A First Java Server Page Example

- JavaServer Pages (JSP) is a technology that allows us to create dynamic web pages using Java code embedded in HTML tags.
- JSP files have the extension `.jsp` and are compiled by the web server into servlets, which are Java classes that handle HTTP requests and responses.
- JSP files can contain HTML elements, JSP directives, JSP scriptlets, JSP expressions, JSP declarations, and JSP actions.
- JSP directives are instructions to the web server that control how the JSP file is processed. They start with `<%@` and end with `%>`.
- JSP scriptlets are blocks of Java code that are executed by the web server. They start with `<%` and end with `%>`.
- JSP expressions are snippets of Java code that are evaluated by the web server and the result is inserted into the HTML output. They start with `<%=` and end with `%>`.
- JSP declarations are blocks of Java code that define variables and methods for the JSP file. They start with `<%!` and end with `%>`.
- JSP actions are tags that invoke built-in or custom functionality. They start with `<jsp:` and end with `/>`.

- A simple JSP example that displays the current date and time is shown below :

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A Simple JSP Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line is a JSP directive that specifies the content type, the character encoding, and the scripting language of the JSP file.
- The HTML elements are rendered as normal by the web browser.
- The JSP expression `<%= new java.util.Date() %>` is evaluated by the web server and the result is inserted into the HTML output. In this case, it will display the current date and time in the default format.