#### Directives in Servlets

- Directives are special instructions to the servlet container that affect the processing of the servlet.
- Directives are not part of the servlet's output, but are enclosed in <% and %> tags in the servlet code.
- There are three types of directives in servlets: page, include and taglib.
- Page directive: It defines the attributes of the servlet such as language, content type, buffer size, error page, etc. It can be used multiple times in a servlet, but only once per attribute. The syntax is:

<%@ page attribute="value" %>

- Some common attributes of the page directive are:

  - language: Specifies the scripting language used in the servlet. The default is Java.
  - contentType: Specifies the MIME type and character encoding of the servlet output. The default is text/html; charset=ISO-8859-1.
  - import: Specifies the packages or classes to be imported for the servlet. It can be used multiple times or with comma-separated values.
  - buffer: Specifies the size of the output buffer in kilobytes. The default is 8 KB. It can also be set to none, which means no buffering.
  - errorPage: Specifies the URL of another servlet or JSP page that handles the exception thrown by the current servlet. The error page must have isErrorPage="true" attribute in its page directive.
  - isErrorPage: Specifies whether the current servlet is an error page or not. The default is false. If true, the implicit object exception is available in the servlet, which contains the exception information.
  - session: Specifies whether the servlet participates in the session or not. The default is true. If false, the implicit object session is not available in the servlet.
  - isThreadSafe: Specifies whether the servlet is thread-safe or not. The default is true. If false, the servlet container ensures that only one thread executes the servlet at a time.
  - extends: Specifies the superclass that the servlet extends. The default is javax.servlet.http.HttpServlet for HTTP servlets.
  - info: Specifies the information about the servlet that can be retrieved by the getServletInfo() method.

- Include directive: It includes the content of another resource (servlet, JSP page, HTML file, etc.) in the current servlet at the time of translation. It can be used multiple times in a servlet. The syntax is:

<%@ include file="url" %>

- The include directive is different from the include action (<jsp:include page="url" />), which includes the content of another resource at the request time. The include directive is faster and more efficient, but it does not allow dynamic changes in the included resource.
- Taglib directive: It declares the tag library that contains the custom tags used in the servlet. It can be used multiple times in a servlet. The syntax is:

<%@ taglib uri="uri" prefix="prefix" %>

- The uri attribute specifies the location of the tag library descriptor (TLD) file, which defines the custom tags and their attributes. The prefix attribute specifies the prefix that is used to invoke the custom tags in the servlet. For example, if the prefix is "c", then the custom tag can be used as <c:tagName>.