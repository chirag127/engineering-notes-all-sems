#### Java Server Pages Overview in Servlets

- JavaServer Pages (JSP) is a technology that allows developers to create dynamic web pages using Java and Java Servlets .
- JSP pages are compiled into Java servlets and run on the server. JSP uses a special syntax that embeds snippets of Java code within HTML, and these pages are stored as regular HTML files with a .jsp extension.
- JSP pages can access all the powerful Enterprise Java APIs, including JDBC, JNDI, EJB, JAXP, etc. JSP pages can also use custom tags, expression language, and JavaBeans components to encapsulate reusable functionality.
- JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines. Servlets are Java classes that handle requests, process them, and reply back with a response.
- JSP pages have a life cycle that consists of the following phases:
  - Translation: The JSP page is translated into a Java servlet class by the JSP container.
  - Compilation: The servlet class is compiled into a bytecode class by the Java compiler.
  - Loading: The bytecode class is loaded into the JVM by the class loader.
  - Instantiation: An instance of the servlet class is created by the JSP container.
  - Initialization: The init() method of the servlet class is invoked by the JSP container to initialize the servlet.
  - Request processing: The service() method of the servlet class is invoked by the JSP container to process the request and generate the response.
  - Destruction: The destroy() method of the servlet class is invoked by the JSP container to release the resources used by the servlet.

- A mnemonic to remember the JSP life cycle phases is: **T**om **C**at **L**ikes **I**ce **C**ream **R**eally **D**elicious.
- An example of a simple JSP page that displays the current date and time is:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>JSP Example</title>
</head>
<body>
    <h1>JSP Example</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- Some advantages of using JSP are:
  - It is easy to write and maintain, as it separates the presentation logic from the business logic.
  - It is portable, as it runs on any platform that supports Java and servlets.
  - It is efficient, as it is compiled and cached by the server.
  - It is extensible, as it supports custom tags, expression language, and JavaBeans components.
  - It is compatible, as it can work with any web server that supports servlets.

- Some disadvantages of using JSP are:
  - It is not suitable for complex business logic, as it can make the code messy and hard to debug.
  - It is not secure, as it exposes the Java code to the client-side.
  - It is not fast, as it requires translation and compilation before execution.
  - It is not flexible, as it depends on the server configuration and the JSP container implementation.