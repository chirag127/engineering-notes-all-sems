Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of Java Server Pages (JSP) for the notes of the Unit 5 - Servlets in the subject of Web Technology. Here is the content:

# Java Server Pages (JSP)

## Introduction

- Java Server Pages (JSP) is a technology that allows web developers to create dynamic web pages using Java code embedded in HTML or XML documents.
- JSP is an extension of the servlet technology, which is a Java class that runs on a web server and handles HTTP requests and responses.
- JSP files are compiled into servlets by a JSP compiler, which is part of the web server or the application server that supports JSP.
- JSP files have the extension `.jsp` and are stored in the web application directory, usually under the `WEB-INF` folder.
- JSP files can contain HTML tags, JSP directives, JSP scriptlets, JSP expressions, JSP declarations, JSP comments, and custom tags.

## JSP Syntax

- JSP directives are instructions to the JSP compiler that control the behavior and structure of the JSP file. They start with `<%@` and end with `%>`. For example, `<%@ page language="java" %>` specifies the scripting language of the JSP file as Java.
- JSP scriptlets are blocks of Java code that are executed when the JSP file is processed. They start with `<%` and end with `%>`. For example, `<% int x = 10; %>` declares and initializes a local variable `x` with the value 10.
- JSP expressions are Java expressions that are evaluated and inserted into the output stream. They start with `<%=` and end with `%>`. For example, `<%= x + 5 %>` inserts the value of `x + 5` into the output stream.
- JSP declarations are blocks of Java code that declare variables or methods that are accessible throughout the JSP file. They start with `<%!` and end with `%>`. For example, `<%! int y = 20; %>` declares a global variable `y` with the value 20.
- JSP comments are comments that are ignored by the JSP compiler and the web browser. They start with `<%--` and end with `--%>`. For example, `<%-- This is a JSP comment --%>` is a JSP comment.
- Custom tags are tags that are defined by the developer or a third-party library that provide reusable functionality or custom behavior. They start with `<` and end with `>`, and have a prefix that identifies the tag library. For example, `<c:out value="${name}" />` is a custom tag from the JSTL (JavaServer Pages Standard Tag Library) that outputs the value of the `name` attribute.

## JSP Lifecycle

- The JSP lifecycle consists of the following phases:
  - Translation: The JSP file is translated into a servlet class by the JSP compiler.
  - Compilation: The servlet class is compiled into a bytecode file by the Java compiler.
  - Loading: The bytecode file is loaded into the web server or the application server by the class loader.
  - Initialization: The servlet class is instantiated and the `init()` method is invoked by the web container.
  - Request processing: The `service()` method is invoked by the web container for each HTTP request and response. The `service()` method calls the `doGet()`, `doPost()`, or other methods depending on the HTTP method of the request.
  - Destruction: The `destroy()` method is invoked by the web container when the servlet is unloaded from the server. The `destroy()` method releases any resources used by the servlet.

## JSP Advantages

- JSP has the following advantages over servlets:
  - JSP separates the presentation logic from the business logic, making the web development more modular and maintainable.
  - JSP allows the web developers to use HTML or XML tags to create the web pages, making the web development more intuitive and easy.
  - JSP supports the use of custom tags, which provide reusable functionality or custom behavior, making the web development more flexible and powerful.
  - JSP supports the use of expression language (EL) and JavaServer Pages Standard Tag Library (JSTL), which simplify the access and manipulation of data and objects, making the web development more efficient and concise.