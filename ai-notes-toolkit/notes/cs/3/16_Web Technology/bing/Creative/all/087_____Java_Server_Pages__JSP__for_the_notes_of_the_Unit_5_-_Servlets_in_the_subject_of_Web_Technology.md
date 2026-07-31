# Java Server Pages (JSP)

## Overview

- Java Server Pages (JSP) is a server-side technology for developing dynamic web pages.
- JSP is mainly used for implementing presentation layer (GUI Part) of an application.
- JSP allows us to embed Java code into HTML pages using special tags.
- JSP pages are compiled into servlets by a JSP compiler and executed by a web container.
- JSP have access to the entire family of Java APIs, including the JDBC API to access enterprise databases.

## JSP Life Cycle

- A JSP life cycle consists of the following phases:
  - Translation: The web container translates the JSP page into a servlet class.
  - Compilation: The web container compiles the servlet class into an executable class.
  - Loading: The web container loads the servlet class into the memory.
  - Initialization: The web container invokes the init() method of the servlet to initialize it.
  - Request Processing: The web container invokes the service() method of the servlet to process the client request.
  - Destroy: The web container invokes the destroy() method of the servlet to destroy it.

## Elements of JSP

- A JSP page can contain the following elements:
  - Directives: JSP directives are used for controlling the processing of a JSP page. They provide information to the web container such as page encoding, scripting language, error page, etc. They have the following syntax: <%@ directive attribute="value" %>
  - Scriptlets: JSP scriptlets are used for writing Java code in a JSP page. They have the following syntax: <% Java code %>
  - Action Tags: JSP action tags are used for performing an action during request processing phase of JSP life cycle. They have the following syntax: <jsp:action attribute="value" />
  - Expressions: JSP expressions are used for evaluating a Java expression and displaying the result in the output. They have the following syntax: <%= Java expression %>
  - Declarations: JSP declarations are used for declaring variables and methods in a JSP page. They have the following syntax: <%! Java code %>
  - Comments: JSP comments are used for adding remarks or notes in a JSP page. They have the following syntax: <%-- comment --%>

## JSP Implicit Objects

- JSP implicit objects are predefined variables that are created by the web container and available to all JSP pages.
- JSP implicit objects are: request, response, out, session, application, config, page, pageContext, and exception.