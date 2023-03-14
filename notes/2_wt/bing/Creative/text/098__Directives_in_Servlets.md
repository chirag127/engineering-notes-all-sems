#### Directives in Servlets

- Directives are special instructions that provide global information about the entire JSP page.
- Directives affect the overall structure and behavior of the servlet class that is generated from the JSP page.
- Directives have the following syntax: `<%@ directive attribute="value" %>` or `<jsp:directive.directive attribute="value" />` in XML.
- Directives can have multiple attributes separated by commas.
- Directives can be placed anywhere in the JSP page, but by convention they are coded at the top of the page.
- There are three types of directives in JSP: page, include, and taglib.

##### Page Directive
- The page directive is used to provide instructions to the container that pertain to the current JSP page.
- The page directive can specify attributes such as scripting language, error page, buffering requirements, content type, session management, etc.
- The page directive can be used multiple times in a JSP page, but it is recommended to use it only once for readability and maintainability.
- The page directive has the following syntax: `<%@ page attribute="value" %>` or `<jsp:directive.page attribute="value" />` in XML.
- Some of the common attributes of the page directive are:

| Attribute | Purpose |
|-----------|---------|
| buffer | Specifies a buffering model for the output stream. |
| autoFlush | Controls the behavior of the servlet output buffer. |
| contentType | Defines the character encoding scheme. |
| errorPage | Defines the URL of another JSP that reports on Java unchecked runtime exceptions. |
| isErrorPage | Indicates if this JSP page is a URL specified by another JSP page's errorPage attribute. |
| extends | Specifies a superclass that the generated servlet must extend. |
| import | Specifies a list of packages or classes for use in the JSP as the Java import statement does for Java classes. |
| info | Defines a string that can be accessed with the servlet's getServletInfo() method. |
| isThreadSafe | Defines the threading model for the generated servlet. |
| language | Defines the programming language used in the JSP page. |
| session | Specifies whether or not the JSP page participates in HTTP sessions. |
| isELIgnored | Specifies whether or not the EL expression within the JSP page will be ignored. |
| isScriptingEnabled | Determines if the scripting elements are allowed for use. |

##### Include Directive
- The include directive is used to include a file during the translation phase of the JSP page.
- The include directive tells the container to merge the content of another file with the current JSP page before generating the servlet code.
- The include directive can be used to reuse common code fragments, such as headers, footers, menus, etc.
- The include directive has the following syntax: `<%@ include file="relative url" %>` or `<jsp:directive.include file="relative url" />` in XML.
- The file attribute specifies the relative URL of the file to be included.
- The file to be included can be a static file (such as HTML, CSS, etc.) or a dynamic file (such as JSP, Servlet, etc.).
- The include directive is different from the include action (`<jsp:include page="relative url" />`) which includes a file at the request time of the JSP page.

##### Taglib Directive
- The taglib directive is used to declare a tag library that contains custom actions used in the JSP page.
- The taglib directive tells the container where to find the tag library descriptor (TLD) file that defines the custom tags and their attributes.
- The taglib directive can be used to simplify the JSP code by using custom tags instead of scriptlets or expressions.
- The taglib directive has the following syntax: `<%@ taglib uri="uri" prefix="prefix" %>` or `<jsp:directive.taglib uri="uri" prefix="prefix" />` in XML.
- The uri attribute specifies the uniform resource identifier (URI) of the tag library descriptor file.
- The prefix attribute specifies the prefix that is used to invoke the custom tags in the JSP page.
- The taglib directive can be used multiple times in a JSP page to declare different tag libraries with different prefixes.