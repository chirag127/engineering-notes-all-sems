Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here is the content for the topic of A First Java Server Page Example for the notes of the Unit 5 - Servlets.

### A First Java Server Page Example

- A Java Server Page (JSP) is a web page that contains Java code embedded in HTML or XML.
- The Java code is executed on the server side and the output is sent to the client as HTML or XML.
- A JSP can also include other JSPs, HTML fragments, or custom tags.
- A JSP is compiled into a servlet by the web container when it is first requested.
- A servlet is a Java class that handles HTTP requests and responses.
- A JSP has the following structure:

```
<%@ page ... %> // optional page directive
<%@ include ... %> // optional include directive
<%! ... %> // optional declaration section
<% ... %> // optional scriptlet section
<%= ... %> // optional expression section
<%-- ... --%> // optional comment section
HTML or XML content // optional static content
```

- The page directive defines the attributes of the JSP, such as the language, the content type, the error page, etc.
- The include directive allows the JSP to include another file, such as another JSP, an HTML fragment, or a custom tag library.
- The declaration section allows the JSP to declare variables and methods that are accessible throughout the JSP.
- The scriptlet section allows the JSP to execute Java code that can access the request, the response, the session, the application, and other implicit objects.
- The expression section allows the JSP to output the value of a Java expression to the client.
- The comment section allows the JSP to add comments that are ignored by the web container.

- An example of a simple JSP that displays the current date and time is:

```
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

- The output of this JSP is:

```
<html>
<head>
    <title>A First JSP Example</title>
</head>
<body>
    <h1>A First JSP Example</h1>
    <p>The current date and time is: Wed Mar 15 20:39:26 GMT 2023</p>
</body>
</html>
```
