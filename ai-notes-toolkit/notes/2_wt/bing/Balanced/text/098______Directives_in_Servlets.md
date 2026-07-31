#### Directives in Servlets

- Directives are instructions that control the structure and properties of a servlet.
- Directives are not executed at runtime, but are processed by the servlet container at compile time or deployment time.
- Directives are enclosed in <%@ and %> tags and can appear anywhere in the servlet code, but are usually placed at the beginning for clarity.
- There are three types of directives in servlets: page, include and taglib.

- Page directive: It defines the attributes of the servlet, such as the content type, language, error page, buffer size, etc. It has the following syntax:

<%@ page attribute="value" %>

- Include directive: It includes the content of another resource, such as a static file or another servlet, into the current servlet. It has the following syntax:

<%@ include file="resource" %>

- Taglib directive: It declares the use of a custom tag library in the servlet. It has the following syntax:

<%@ taglib uri="uri" prefix="prefix" %>

- Some examples of directives in servlets are:

<%@ page contentType="text/html" %>
<%@ include file="header.html" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>