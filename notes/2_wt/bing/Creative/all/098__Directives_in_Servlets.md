#### Directives in Servlets

- Directives are special instructions that provide information about the entire JSP page to the servlet container.
- Directives can affect the overall structure and behavior of the servlet class that is generated from the JSP page.
- Directives have the following syntax: `<%@ directive attribute="value" %>` or `<jsp:directive.directive attribute="value" />` in XML.
- Directives can have multiple attributes separated by commas. The blanks between the @ symbol and the directive name, and between the last attribute and the closing %>, are optional.
- There are three types of directives in JSP: page, include, and taglib.

##### Page Directive

- The page directive is used to provide instructions to the servlet container that pertain to the current JSP page.
- The page directive can be used to specify attributes such as scripting language, error page, buffering requirements, content type, session management, etc.
- The page directive can be coded anywhere in the JSP page, but by convention, it is placed at the top of the page.
- The page directive can be used multiple times in a JSP page, but it is recommended to use only one page directive with all the attributes.
- Some of the common attributes of the page directive are:

| Attribute | Description |
|-----------|-------------|
| buffer | Specifies the size of the output buffer for the response. |
| autoFlush | Controls the behavior of the output buffer when it is full. |
| contentType | Specifies the MIME type and the character encoding of the response. |
| errorPage | Specifies the URL of another JSP page that handles the runtime exceptions. |
| isErrorPage | Indicates if the current JSP page is an error page for another JSP page. |
| extends | Specifies the name of a superclass that the generated servlet class must extend. |
| import | Specifies a list of packages or classes that are imported for use in the JSP page. |
| info | Specifies a string that can be accessed by the getServletInfo() method of the generated servlet class. |
| isThreadSafe | Specifies whether the generated servlet class implements the SingleThreadModel interface or not. |
| language | Specifies the scripting language used in the JSP page. The default is Java. |
| session | Specifies whether the JSP page participates in HTTP sessions or not. |
| isELIgnored | Specifies whether the expression language expressions are evaluated or ignored in the JSP page. |
| isScriptingEnabled | Specifies whether the scripting elements are allowed or disabled in the JSP page. |

##### Include Directive

- The include directive is used to include the content of another file during the translation phase of the JSP page.
- The include directive tells the servlet container to merge the content of the specified file with the current JSP page before compiling it into a servlet class.
- The include directive can be used to include static files such as HTML, CSS, JavaScript, etc. or dynamic files such as JSP, Servlet, etc.
- The include directive can be coded anywhere in the JSP page where the included file content is valid.
- The include directive has only one attribute: file, which specifies the relative URL of the file to be included.
- The syntax of the include directive is: `<%@ include file="relative url" %>` or `<jsp:directive.include file="relative url" />` in XML.

##### Taglib Directive

- The taglib directive is used to declare a tag library that contains custom tags or actions used in the JSP page.
- The taglib directive tells the servlet container where to find the tag library descriptor (TLD) file that defines the custom tags or actions and their attributes.
- The taglib directive can be coded anywhere in the JSP page, but by convention, it is placed at the top of the page.
- The taglib directive can be used multiple times in a JSP page to declare different tag libraries.
- The taglib directive has two attributes: uri and prefix.

| Attribute | Description |
|-----------|-------------|
| uri | Specifies the location of the TLD file that defines the tag library. It can be a relative URL, an absolute URL, or a URI. |
| prefix | Specifies the prefix that is used to identify the custom tags or actions in the JSP page. It must be a valid XML name. |

- The syntax of the taglib directive is: `<%@ taglib uri="location" prefix="name" %>` or `<jsp:directive.taglib uri="location" prefix="name" />` in XML.