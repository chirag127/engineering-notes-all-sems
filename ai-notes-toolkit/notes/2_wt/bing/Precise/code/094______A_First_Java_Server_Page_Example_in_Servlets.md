#### A First Java Server Page Example in Servlets

Here is an example of a simple Java Server Page (JSP) that can be used in a servlet:

```java
<%@ page import="java.io.*,java.util.*" %>
<%
    String message = "Hello, World!";
%>
<html>
    <body>
        <h1><%= message %></h1>
    </body>
</html>
```

This JSP code imports the necessary Java classes, defines a `message` variable, and outputs the value of the `message` variable within an HTML `h1` element. When this JSP is accessed, it will display the text "Hello, World!" on the page.
