 Here are the directives for the notes of Unit 5 - Servlets in the subject of Web Technology:

### Overview
- Servlets are server-side programs that can handle client requests and generate dynamic content.
- They extend the capabilities of servers that host applications accessed via a request-response programming model.

### Life cycle of a Servlet
- The life cycle of a servlet can be categorized into four phases:

1. Loading & Instantiation - When the servlet is first loaded, the servlet container creates an instance of the servlet and calls the init() method.
2. Request Handling - For each request, the servlet container calls the service() method of the servlet.
3. Removal from Service - The servlet container calls the destroy() method when it decides to remove the servlet instance from service. This happens when the servlet is being undeployed or the servlet container is being shut down.

### Parts of a Servlet
- The key parts of a servlet are:

1. Import statements - imports required Java packages and classes
2. Extends HttpServlet class - Servlets always extend either HttpServlet or GenericServlet class. HttpServlet is commonly extended to process HTTP requests.
3. Override doGet() and/or doPost() methods - These methods handle GET and POST requests respectively. We override them to specify the request handling logic.
4. Other life cycle methods - We can override init() and destroy() methods to perform initialization and cleanup actions respectively.

[Detailed explanations, examples, diagrams, codes, etc. can be added here for the sub-topics]