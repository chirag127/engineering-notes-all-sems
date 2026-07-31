#### Standard Actions in Servlets

Standard actions are predefined tags that are used to perform common tasks in JSP. These tags are provided by the JSP container and are used to manipulate the objects in the page context. Some of the standard actions in Servlets are:

- `<jsp:useBean>`: This action is used to create or locate a JavaBean object and make it available to the JSP page.
- `<jsp:setProperty>`: This action is used to set the properties of a JavaBean object.
- `<jsp:getProperty>`: This action is used to get the properties of a JavaBean object.
- `<jsp:include>`: This action is used to include the content of another resource, such as a JSP page or an HTML file, in the current JSP page.
- `<jsp:forward>`: This action is used to forward the request to another resource, such as a JSP page or a servlet.
- `<jsp:param>`: This action is used to pass parameters to the included or forwarded resource.
- `<jsp:plugin>`: This action is used to include a Java applet or a JavaBeans component in the JSP page.

Here is an example of using the `<jsp:useBean>` and `<jsp:setProperty>` actions in a JSP page:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Standard Actions Example</title>
</head>
<body>
    <jsp:useBean id="person" class="com.example.Person" />
    <jsp:setProperty name="person" property="name" value="John Doe" />
    <p>Name: <%= person.getName() %></p>
</body>
</html>
```

This code creates a `Person` object and sets its `name` property to "John Doe". The value of the `name` property is then displayed on the page using a scriptlet.