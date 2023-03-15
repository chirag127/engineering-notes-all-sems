### Java Server Pages (JSP) in Servlets

- Java Server Pages (JSP) are a technology that allows web developers to create dynamic web pages using Java code embedded in HTML or XML documents.
- JSP are compiled into servlets by a JSP compiler, which is usually part of a web server or a web container such as Tomcat or Jetty.
- JSP have access to the same objects and methods as servlets, such as the request, response, session, and application objects, and the out, config, and pageContext objects.
- JSP can also use custom tags, which are reusable components that encapsulate Java code or other JSP elements, and can be defined in tag libraries or in the same JSP file.
- JSP support various directives, scripting elements, and expressions that control the behavior and output of the JSP page, such as:
  - `<%@ page ... %>`: Specifies attributes of the JSP page, such as the language, contentType, buffer size, error page, etc.
  - `<%@ include file="..." %>`: Includes the content of another file, such as an HTML fragment or another JSP file, at the time of translation.
  - `<%@ taglib uri="..." prefix="..." %>`: Declares a tag library that can be used in the JSP page, and assigns a prefix to refer to its custom tags.
  - `<% ... %>`: Contains Java code that is executed at the time of request processing.
  - `<%= ... %>`: Contains a Java expression that is evaluated and inserted into the output stream.
  - `<%! ... %>`: Contains Java code that is executed once when the JSP page is initialized, and can be used to declare variables or methods that are accessible throughout the JSP page.
  - `<jsp:include page="..." />`: Includes the content of another JSP page or a servlet, at the time of request processing.
  - `<jsp:forward page="..." />`: Forwards the request to another JSP page or a servlet, and terminates the current JSP page.
  - `<jsp:useBean id="..." class="..." scope="..." />`: Creates or retrieves a JavaBean object with the given id, class, and scope, and makes it available to the JSP page.
  - `<jsp:setProperty name="..." property="..." value="..." />`: Sets a property of a JavaBean object with the given name, property, and value.
  - `<jsp:getProperty name="..." property="..." />`: Gets a property of a JavaBean object with the given name and property, and inserts it into the output stream.
  - `<%-- ... --%>`: Contains a comment that is ignored by the JSP compiler.