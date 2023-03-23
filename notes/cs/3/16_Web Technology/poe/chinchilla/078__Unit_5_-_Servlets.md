## Unit 5 - Servlets

Servlets are Java-based components that are used to create web applications. They are server-side programs that run on the web server and generate dynamic content in response to user requests.

Servlets are widely used in web applications because of their ability to handle multiple requests simultaneously, their scalability, and their ability to process large amounts of data.

### 1. What are Servlets?

- Servlets are Java-based components that are used to create web applications.
- They are server-side programs that run on the web server and generate dynamic content in response to user requests.
- Servlets are used for handling HTTP requests and responses, and they can also interact with databases and other systems.

### 2. How Servlets work?

- Servlets work by receiving HTTP requests from clients and generating responses.
- When a client sends an HTTP request, the web server forwards the request to the servlet container.
- The servlet container then loads the appropriate servlet and passes the request to it.
- The servlet processes the request and generates a response, which is then sent back to the client.

### 3. Advantages of using Servlets

- Servlets can handle multiple requests simultaneously, making them highly scalable.
- They are platform-independent and can be run on any web server that supports Java.
- Servlets are efficient and can process large amounts of data quickly.
- They can be used to create dynamic web pages and web applications that can interact with databases and other systems.
- Servlets are easy to maintain and can be updated without affecting other parts of the application.

### 4. Servlet API

- The Servlet API is a set of Java classes and interfaces that provide the functionality required to create servlets.
- The Servlet API includes the javax.servlet and javax.servlet.http packages, which contain classes and interfaces for handling HTTP requests and responses.
- The Servlet API also includes the ServletContext and ServletConfig interfaces, which provide access to the web application's environment and configuration settings.

### 5. Servlet Lifecycle

- The lifecycle of a servlet consists of several stages, including initialization, service, and destruction.
- During initialization, the servlet container loads the servlet and calls its init() method.
- During service, the servlet processes HTTP requests and generates responses.
- During destruction, the servlet container calls the servlet's destroy() method, which allows the servlet to clean up any resources it has allocated.

### 6. Servlet Mapping

- Servlet mapping is the process of mapping a URL pattern to a servlet.
- The servlet container uses servlet mapping to determine which servlet should handle a particular request.
- Servlet mapping can be done using annotations or in the web.xml file.

### 7. Servlet Filters

- Servlet filters are Java classes that can be used to intercept requests and responses before they are processed by a servlet.
- Filters can be used to perform tasks such as authentication, data compression, and logging.
- Filters are configured in the web.xml file and can be mapped to one or more servlets.

### 8. Servlets vs JSP

- JSPs are Java-based pages that are used to create dynamic web pages.
- Servlets and JSPs are both server-side technologies that can be used to generate dynamic content.
- Servlets are more flexible and can be used to handle any type of request, while JSPs are typically used to generate HTML pages.
- Servlets are more efficient than JSPs because they do not require the overhead of compiling JSP pages.