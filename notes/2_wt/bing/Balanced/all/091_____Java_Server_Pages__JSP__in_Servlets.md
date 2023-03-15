### Java Server Pages (JSP) in Servlets

- Java Server Pages (JSP) is a technology that allows us to create dynamic web pages using Java and Java Servlets.
- JSP pages are built on top of the Java Servlets API, which means they can access all the powerful Enterprise Java APIs, such as JDBC, JNDI, EJB, JAXP, etc.
- JSP pages can also be used in combination with servlets that handle the business logic, following the model-view-controller (MVC) pattern.
- JSP pages are composed of HTML, XML, or other text-based content, along with special tags that contain Java code or expressions.
- JSP pages are processed by a JSP engine, which is a part of the web server or application server. The JSP engine translates the JSP page into a servlet class, compiles it, and executes it to generate the output.
- JSP pages have several advantages over servlets, such as:
  - They are easier to write and maintain, as they separate the presentation logic from the business logic.
  - They allow the use of custom tags, which are reusable components that encapsulate complex functionality.
  - They support expression language (EL), which is a simple and powerful way to access data and invoke methods in JSP pages.
  - They support JavaServer Pages Standard Tag Library (JSTL), which is a collection of predefined tags that provide common functionality, such as iteration, conditional, formatting, etc.
- JSP pages have some disadvantages, such as:
  - They are less efficient than servlets, as they require an extra translation and compilation step.
  - They are less secure than servlets, as they expose the Java code to the web server and the browser.
  - They are less portable than servlets, as they depend on the JSP engine and the custom tags implementation.
- A simple example of a JSP page is:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>JSP Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- A possible mnemonic to remember the JSP life cycle is: **TIC** (Translation, Initialization, and Call).
- A possible learning trick to understand the difference between JSP and servlets is to think of JSP as a **template** and servlets as a **program**.