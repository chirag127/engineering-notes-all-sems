### Java Server Pages (JSP)

- Java Server Pages (JSP) is a server-side technology for developing dynamic web pages.
- JSP allows embedding Java code and logic into static HTML or XML content using special tags and directives.
- JSP is based on the Java Servlet API and runs on a web server that supports servlets.
- JSP can access the entire family of Java APIs, including the JDBC API to access databases, the JNDI API to access directory services, the JAXP API to process XML documents, and the JavaBeans API to reuse components.
- JSP follows a life cycle that consists of the following phases: translation, compilation, loading, initialization, request processing, and destruction.

#### Elements of JSP

- JSP has four types of elements: directives, scriptlets, action tags, and expressions.
- Directives are used to control the processing of a JSP page, such as setting the page encoding, importing packages, defining error pages, etc. Directives start with <%@ and end with %> and have the syntax <%@ directive attribute="value" %>.
- Scriptlets are used to write Java code in a JSP page. Scriptlets start with <% and end with %> and have the syntax <% Java code %>. Scriptlets can access the implicit objects and variables declared in the page scope.
- Action tags are used to perform an action during the request processing phase of the JSP life cycle, such as including another resource, forwarding the request, invoking a JavaBean, etc. Action tags start with <jsp: and end with /> and have the syntax <jsp:action attribute="value" /> or <jsp:action attribute="value">body</jsp:action>.
- Expressions are used to evaluate a Java expression and insert its value into the output stream. Expressions start with <%= and end with %> and have the syntax <%= expression %>. Expressions cannot contain semicolons or assignment statements.

#### JSP Implicit Objects

- JSP provides nine implicit objects that are created by the web container and can be used in the JSP page without explicit declaration. They are: request, response, out, session, application, config, page, pageContext, and exception.
- The request object is an instance of the HttpServletRequest class and represents the HTTP request from the client. It can be used to access the request parameters, headers, cookies, attributes, etc.
- The response object is an instance of the HttpServletResponse class and represents the HTTP response to the client. It can be used to set the response status, headers, cookies, content type, etc.
- The out object is an instance of the JspWriter class and represents the output stream to write the response content. It can be used to print text, HTML, or XML content to the client.
- The session object is an instance of the HttpSession class and represents the session associated with the request. It can be used to store and retrieve session attributes, get the session ID, check the session validity, etc.
- The application object is an instance of the ServletContext class and represents the web application context. It can be used to access the application parameters, attributes, resources, etc.
- The config object is an instance of the ServletConfig class and represents the configuration information of the JSP page. It can be used to access the initialization parameters, the servlet context, etc.
- The page object is an instance of the java.lang.Object class and represents the current JSP page. It can be used to access the methods and properties of the page class.
- The pageContext object is an instance of the PageContext class and represents the context information of the JSP page. It can be used to access the implicit objects, the page scope attributes, the JSP writer, etc.
- The exception object is an instance of the Throwable class and represents the exception thrown in the JSP page. It can be used to access the exception message, stack trace, cause, etc. It is only available in the error pages that have the directive <%@ page isErrorPage="true" %>.

#### JSP Standard Actions

- JSP provides a set of standard actions that can be used to perform common tasks in a JSP page. They are: jsp:include, jsp:forward, jsp:param, jsp:plugin, jsp:useBean, jsp:setProperty, jsp:getProperty, and jsp:fallback.
- The jsp:include action is used to include the content of another resource, such as a JSP page, a servlet, or a static file, in the current JSP page. It has the