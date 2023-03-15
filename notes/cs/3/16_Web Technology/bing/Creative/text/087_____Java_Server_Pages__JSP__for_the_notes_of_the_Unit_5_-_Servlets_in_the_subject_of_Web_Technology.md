### Java Server Pages (JSP) for the notes of the Unit 5 - Servlets in the subject of Web Technology

- Java Server Pages (JSP) is a server-side technology that enables the creation of dynamic web pages using Java and Java Servlets .
- JSP is mainly used for implementing the presentation layer (GUI Part) of an application.
- JSP have access to the entire family of Java APIs, including the JDBC API to access enterprise databases.
- JSP follows a life cycle that consists of the following phases :
  - Translation: The JSP page is translated into a Java servlet class by the web container.
  - Compilation: The Java servlet class is compiled into a bytecode file by the Java compiler.
  - Loading: The bytecode file is loaded into the web container's memory by the class loader.
  - Initialization: The servlet's init() method is invoked by the web container to initialize the servlet instance.
  - Request processing: The servlet's service() method is invoked by the web container to process the client's request and generate a response.
  - Destruction: The servlet's destroy() method is invoked by the web container to release the resources used by the servlet instance.
- JSP supports various elements that can be used to write Java code, control the processing of the page, perform actions, and display dynamic content . These elements are:
  - Directives: JSP directives are used to provide instructions to the web container about the page, such as the page language, the import statements, the error page, etc. They are written as <%@ directive attribute="value" %>.
  - Scriptlets: JSP scriptlets are used to write Java code that is executed during the request processing phase of the JSP life cycle. They are written as <% Java code %>.
  - Expressions: JSP expressions are used to evaluate a Java expression and display its result in the output. They are written as <%= Java expression %>.
  - Declarations: JSP declarations are used to declare variables and methods that can be used by the scriptlets and expressions. They are written as <%! Java code %>.
  - Comments: JSP comments are used to write notes or explanations that are ignored by the web container. They are written as <%-- comment --%>.
  - Action tags: JSP action tags are used to perform specific actions during the request processing phase of the JSP life cycle, such as including another page, forwarding the request, invoking a JavaBean, etc. They are written as <jsp:action attribute="value" /> or <jsp:action attribute="value"> body </jsp:action>.
  - Implicit objects: JSP implicit objects are predefined variables that are created by the web container and can be used by the scriptlets and expressions. They are request, response, out, session, application, config, page, pageContext, and exception.