### Java Server Pages (JSP)

- Java Server Pages (JSP) are text-based documents that contain two types of text: static data and JSP elements.
- Static data can be expressed in any text-based format, such as HTML, XML, SVG, or WML.
- JSP elements are dynamic and can generate data for the response, modify the static data, or affect the overall structure of the response.
- JSP elements include directives, scripting elements, actions, and custom tags.
- Directives are instructions to the JSP container that affect the overall structure and behavior of the JSP page. They have the syntax <%@ directive attribute="value" %>.
- Scripting elements are fragments of Java code that are executed at certain phases of the request processing. They have the syntax <% code %>, <%= expression %>, and <%! declaration %>.
- Actions are XML-style tags that can invoke built-in or custom functionality. They have the syntax <jsp:action attribute="value" /> or <jsp:action attribute="value"> body </jsp:action>.
- Custom tags are user-defined tags that encapsulate reusable functionality. They have the syntax <prefix:tag attribute="value" /> or <prefix:tag attribute="value"> body </prefix:tag>.
- JSP pages are compiled into servlets by the JSP container at runtime. The servlets are then executed by the web container to generate the response for the client.
- JSP pages follow a life cycle that consists of the following phases: translation, compilation, loading, initialization, request processing, and destruction.
- JSP pages can access various implicit objects that are created by the JSP container and passed to the servlet. These objects include request, response, session, application, out, config, page, pageContext, and exception.
- JSP pages can also use various implicit variables that are defined by the JSP container and available to the scripting elements. These variables include pageScope, requestScope, sessionScope, applicationScope, and param.
- JSP pages can be configured using deployment descriptors, which are XML files that specify various settings and properties for the web application. The deployment descriptor for a web application is named web.xml and is located in the WEB-INF directory of the web application.