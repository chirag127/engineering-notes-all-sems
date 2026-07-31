# Scripting for the notes of the Unit 5 - Servlets in the subject of Web Technology

- Servlets are server-side programs that run on a web server and generate dynamic web pages in response to client requests .
- Servlets are written in Java and use the Servlet API (javax.servlet and javax.servlet.http packages) to interact with the web server and the client .
- Servlets have a life cycle that consists of three phases: initialization, service, and destruction .
- Initialization: The web server loads and instantiates the servlet class and invokes its init() method to initialize the servlet .
- Service: The web server invokes the servlet's service() method to handle each client request. The service() method can delegate the request to different methods depending on the HTTP method (GET, POST, etc.) such as doGet() or doPost() .
- Destruction: The web server invokes the servlet's destroy() method to terminate the servlet and release its resources .
- Servlets can read servlet parameters from the web.xml file or from the client request. Servlet parameters are key-value pairs that can be used to configure the servlet or pass information to the servlet .
- Servlets can handle HTTP requests and responses using the HttpServletRequest and HttpServletResponse interfaces. These interfaces provide methods to access the request and response headers, cookies, session attributes, query parameters, form data, etc. .
- Servlets can generate dynamic web pages using the PrintWriter object obtained from the response object. The PrintWriter object can write HTML tags, text, or other content to the output stream .
- Servlets can also use JavaServer Pages (JSP) to create dynamic web pages. JSP is a technology that allows developers to embed Java code in HTML pages using special JSP tags. JSP pages are compiled into servlets by the web server and executed as servlets.
- JSP provides several advantages over servlets, such as:
  - Separation of presentation and business logic
  - Ease of development and maintenance
  - Support for custom tags and expression language
  - Support for scripting elements and directives
  - Support for implicit objects and standard actions