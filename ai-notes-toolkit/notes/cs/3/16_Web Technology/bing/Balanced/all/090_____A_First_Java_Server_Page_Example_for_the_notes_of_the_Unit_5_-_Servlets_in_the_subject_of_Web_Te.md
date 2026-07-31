# A First Java Server Page Example

- JavaServer Pages (JSP) is a technology that allows web developers to create dynamic web pages using Java code embedded in HTML or XML documents.
- JSP files are compiled into servlets by the web container and executed on the server side.
- JSP files have the extension .jsp and can contain HTML tags, JSP directives, JSP scriptlets, JSP expressions, JSP declarations, and custom tags.
- A simple JSP example that displays the current date and time is shown below:

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A First Java Server Page Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line of the JSP file is a page directive that specifies the content type, the scripting language, and other attributes of the page.
- The HTML tags are used to define the structure and layout of the web page.
- The JSP expression `<%= new java.util.Date() %>` is evaluated at runtime and the result is inserted into the HTML output.
- The JSP expression is enclosed by `<%=` and `%>` delimiters and can contain any valid Java expression.
- To run this JSP file, it needs to be placed in the web application directory of the web container and accessed by the URL http://localhost:8080/first.jsp (assuming the web container is running on port 8080 and the web application is named first).
- The web container will compile the JSP file into a servlet class and execute it on the server side.
- The servlet class will generate the HTML output and send it back to the browser.
- The browser will display the web page with the current date and time.