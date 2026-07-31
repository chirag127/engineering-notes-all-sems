Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of Standard Actions for the Unit 5 - Servlets.

### Standard Actions

- Standard actions are predefined tags that perform some common tasks in JSP pages.
- They are used to control the execution flow, include other resources, use JavaBeans components, and communicate with servlets.
- They start with the prefix `jsp:` and follow the XML syntax.
- Some of the commonly used standard actions are:

  - `<jsp:include>`: This action includes the content of another resource, such as a JSP page, an HTML file, or a servlet, at the request time. It has two attributes: `page` and `flush`. The `page` attribute specifies the relative URL of the resource to be included, and the `flush` attribute indicates whether the output buffer should be flushed before including the resource. The default value of `flush` is `false`.
  - `<jsp:forward>`: This action forwards the request to another resource, such as a JSP page, an HTML file, or a servlet, and terminates the execution of the current page. It has one attribute: `page`, which specifies the relative URL of the resource to be forwarded to.
  - `<jsp:useBean>`: This action creates or locates a JavaBean component and associates it with a scripting variable. It has four attributes: `id`, `scope`, `class`, and `beanName`. The `id` attribute specifies the name of the scripting variable, the `scope` attribute specifies the visibility of the bean (possible values are `page`, `request`, `session`, or `application`), the `class` attribute specifies the fully qualified name of the bean class, and the `beanName` attribute specifies the name of the bean as registered in a JSP configuration file.
  - `<jsp:setProperty>`: This action sets the properties of a JavaBean component. It has three attributes: `name`, `property`, and `value`. The `name` attribute specifies the name of the scripting variable that references the bean, the `property` attribute specifies the name of the property to be set, and the `value` attribute specifies the value of the property. Alternatively, the `value` attribute can be replaced by a body content that provides the value of the property.
  - `<jsp:getProperty>`: This action gets the value of a property of a JavaBean component and writes it to the output stream. It has two attributes: `name` and `property`. The `name` attribute specifies the name of the scripting variable that references the bean, and the `property` attribute specifies the name of the property to be retrieved.

- Here is an example of using standard actions in a JSP page:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Standard Actions Example</title>
</head>
<body>
    <h1>Standard Actions Example</h1>
    <p>This page demonstrates the use of standard actions in JSP.</p>
    <p>First, we create a JavaBean component that represents a person with name and age properties.</p>
    <jsp:useBean id="person" class="com.example.Person" scope="page"/>
    <p>Next, we set the name and age properties of the person bean using the setProperty action.</p>
    <jsp:setProperty name="person" property="name" value="Alice"/>
    <jsp:setProperty name="person" property="age">
        25
    </jsp:setProperty>
    <p>Then, we get the name and age properties of the person bean using the getProperty action and display them.</p>
    <p>The name of the person is: <jsp:getProperty name="person" property="name"/></p>
    <p>The age of the person is: <jsp:getProperty name="person" property="age"/></p>
    <p>Finally, we include another JSP page that displays the current date and time using the include action.</p>
    <jsp:include page="date.jsp" flush="true"/>
</body>
</html>
```