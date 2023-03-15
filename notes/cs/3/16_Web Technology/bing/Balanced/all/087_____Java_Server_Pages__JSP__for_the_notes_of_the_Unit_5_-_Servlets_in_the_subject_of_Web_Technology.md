# Java Server Pages (JSP)

## Introduction

- Java Server Pages (JSP) is a server-side technology for developing dynamic web pages.
- JSP allows us to embed Java code and logic into HTML, XML, or other types of documents.
- JSP is based on the Java Servlet technology, which provides the platform-independent and efficient way of handling web requests.
- JSP enables the separation of presentation and business logic by using tag libraries and expression language.
- JSP can access the entire family of Java APIs, including the JDBC API to access databases, the JNDI API to access directory services, the JAXP API to process XML documents, and the JavaBeans API to reuse components.

## JSP Life Cycle

- The JSP life cycle describes the phases that a JSP page goes through from its creation to its destruction.
- The JSP life cycle consists of the following steps:

  1. Translation: The web server converts the JSP page into a Java servlet class. This step is performed only once when the JSP page is first requested or when the JSP page is modified.
  2. Compilation: The web server compiles the servlet class into a bytecode file that can be executed by the Java Virtual Machine (JVM). This step is also performed only once unless the JSP page is modified.
  3. Loading: The web server loads the servlet class into the memory and creates an instance of it. This step is performed once per servlet class or when the servlet class is modified or unloaded.
  4. Initialization: The web server invokes the init() method of the servlet class to perform any initialization tasks. This step is performed once per servlet instance or when the servlet instance is reloaded.
  5. Request processing: The web server invokes the service() method of the servlet class to process the incoming requests from the clients. This step is performed for each request to the JSP page.
  6. Response generation: The servlet class generates the dynamic content and sends it back to the client as the response. This step is also performed for each request to the JSP page.
  7. Destruction: The web server invokes the destroy() method of the servlet class to perform any cleanup tasks. This step is performed when the servlet instance is unloaded from the memory or when the web server is shut down.

## Elements of JSP

- JSP pages can contain various types of elements that are processed by the web server or the web browser. The main elements of JSP are:

  - Directives: JSP directives are used to control the processing of a JSP page. They can specify the page attributes, the import statements, the tag libraries, the error pages, and the output content type. JSP directives start with <%@ and end with %> and have the following syntax:

    ```jsp
    <%@ directive attribute="value" ... %>
    ```

    For example, the following directive sets the language, the content type, and the error page of the JSP page:

    ```jsp
    <%@ page language="java" contentType="text/html" errorPage="error.jsp" %>
    ```

  - Scriptlets: JSP scriptlets are used to write Java code in a JSP page. They can declare variables, call methods, perform calculations, and manipulate data. JSP scriptlets start with <% and end with %> and have the following syntax:

    ```jsp
    <% Java code %>
    ```

    For example, the following scriptlet declares a variable and prints its value:

    ```jsp
    <% int x = 10; %>
    <p>The value of x is <%= x %></p>
    ```

  - Action tags: JSP action tags are used to perform an action during the request processing phase of the JSP life cycle. They can include another file, forward the request to another resource, invoke a JavaBean, or use a custom tag. JSP action tags start with <jsp: and end with /> and have the following syntax:

    ```jsp
    <jsp:action attribute="value" ... />
    ```

    For example, the following action tag includes the file header.jsp in the JSP page:

    ```jsp
    <jsp:include page="header.jsp" />
    ```

  - Expressions: JSP expressions are used to evaluate a Java expression and insert its value into the output. They can access variables, methods, and objects. JSP expressions start with <%= and end with %> and have the following syntax:

    ```jsp
    <%= Java expression %