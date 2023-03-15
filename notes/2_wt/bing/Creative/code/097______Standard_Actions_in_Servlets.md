#### Standard Actions in Servlets

Standard actions are JSP elements that use XML syntax to control the behavior of the servlet engine. They can be used to dynamically insert a file, reuse JavaBeans components, forward or redirect the user to another page, and more. There are 12 types of standard actions in JSP, as listed below:

- `<jsp:include>`: Includes the content of another resource (such as a JSP, HTML, or servlet) at the time of request processing.
- `<jsp:forward>`: Forwards the current request to another resource (such as a JSP, HTML, or servlet) and terminates the current page.
- `<jsp:param>`: Specifies a parameter for the `<jsp:include>` or `<jsp:forward>` action.
- `<jsp:plugin>`: Generates browser-specific code to embed an applet in the page.
- `<jsp:useBean>`: Declares and instantiates a JavaBean component.
- `<jsp:setProperty>`: Sets the properties of a JavaBean component.
- `<jsp:getProperty>`: Gets the properties of a JavaBean component and displays them in the page.
- `<jsp:attribute>`: Defines an attribute for a custom action or a standard action that accepts a body.
- `<jsp:body>`: Specifies the body of a custom action or a standard action that accepts a body.
- `<jsp:text>`: Specifies plain text in a JSP page.
- `<jsp:output>`: Controls the output settings of the current page, such as the content type, the buffer size, and the doctype declaration.
- `<jsp:element>`: Creates an XML element dynamically and adds it to the page.

Here is an example of using some of the standard actions in a JSP page:

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Standard Actions Example</title>
</head>
<body>
    <h1>Standard Actions Example</h1>
    <p>This is the main page.</p>
    <p>Here is the content of another page:</p>
    <jsp:include page="another.jsp">
        <jsp:param name="name" value="Alice"/>
    </jsp:include>
    <p>Here is the value of a JavaBean property:</p>
    <jsp:useBean id="bean" class="com.example.MyBean" scope="session"/>
    <jsp:setProperty name="bean" property="message" value="Hello"/>
    <jsp:getProperty name="bean" property="message"/>
    <p>Here is an applet:</p>
    <jsp:plugin type="applet" code="com.example.MyApplet.class" width="300" height="200"/>
</body>
</html>
```