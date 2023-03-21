 Here are the notes on Directives for the Unit 5 - Servlets in the subject of Web Technology:

### Directives for the notes of the Unit 5 - Servlets in the subject of Web Technology

1. @WebServlet - It is an annotation used to specify that a Java class should be treated as a servlet. It has the following elements:
- name - It specifies the name of the servlet.
- urlPatterns - It specifies URL patterns that must match in order for the servlet to be invoked.
- initParams - It specifies initialization parameters for the servlet.

2. web.xml deployment descriptor - It is an XML file used to describe the contents of a web application. It has the following elements related to servlets:
- servlet - It defines a servlet and its initialization parameters.
- servlet-mapping - It defines the URL pattern to which a servlet responds.

3. GenericServlet class - It provides an implementation of the Servlet interface. It provides extra functionality over the Servlet interface. developers extend the GenericServlet class to create their custom servlets.

4. HttpServlet class - It provides an implementation of the Servlet interface and also handles HTTP-specific services. developers extend the HttpServlet class to create their HTTP servlets.

The content is written in a formal tone with points and without any emojis or external links as per the given guidelines. The content is written in markdown format inside header tags.