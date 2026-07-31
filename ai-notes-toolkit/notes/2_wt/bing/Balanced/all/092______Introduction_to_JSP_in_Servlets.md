#### Introduction to JSP in Servlets

- JSP stands for **Java Server Pages**. It is a server-side technology that lets you build dynamic web applications that work on any platform    .
- JSP is an extension to Servlet technology, which is another server-side technology that handles requests from web servers and produces responses  .
- JSP can use all Java APIs, including the JDBC API, which lets them connect to enterprise databases.
- A JSP page consists of HTML tags and JSP tags. HTML tags are used to display static content, while JSP tags are used to insert Java code into HTML pages  .
- JSP tags can be of three types: **directives**, **scriptlets**, and **actions** .
  - Directives are used to provide instructions to the JSP engine, such as importing packages, setting page attributes, or including other files .
  - Scriptlets are used to write Java code that is executed on the server side .
  - Actions are used to perform specific tasks, such as invoking JavaBeans, forwarding requests, or including other resources .
- JSP also supports **expression language** and **JSTL**. Expression language is used to simplify the access to data and properties, while JSTL is used to provide common functionality such as iteration, conditionals, or formatting  .
- JSP pages are compiled into servlets by the JSP engine, which is a part of the web server or application server   .
- JSP pages have the advantage of being easy to write and maintain, as they separate the presentation logic from the business logic   .
- JSP pages have the disadvantage of being slower than servlets, as they need to be compiled every time they are modified or accessed for the first time  .

A simple example of a JSP page that displays the current date and time is:

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

The output of this JSP page is:

```html
<html>
<head>
    <title>JSP Example</title>
</head>
<body>
    <h1>JSP Example</h1>
    <p>The current date and time is: Wed Mar 15 13:46:29 GMT 2023</p>
</body>
</html>
```

A possible mnemonic to remember the three types of JSP tags is:

- **D**irectives are **D**irections for the JSP engine.
- **S**criptlets are **S**cripts of Java code.
- **A**ctions are **A**ctions to perform tasks.