
### Handling HTTP Get Requests for the Notes of the Unit 5 - Servlets in the Subject of Web Technology

1. HTTP (Hypertext Transfer Protocol) is a request-response protocol used to communicate between a client and a server. 
2. A GET request is used to retrieve data from a server. The request is sent to the server in the form of an HTTP request message, which consists of the request line (containing the request method, the resource requested, and the protocol used) and the request header. 
3. A servlet is a Java class that runs on a web server and processes requests from a client. Servlets are used to process HTTP GET requests and generate dynamic web content. 
4. The servlet container is responsible for managing the servlet's lifecycle, including loading and unloading the servlet, and handling requests. 
5. To handle a GET request, a servlet must implement the doGet() method. This method is called when a client sends a GET request to the server. The doGet() method takes two parameters: an HttpServletRequest object and an HttpServletResponse object. 
6. The HttpServletRequest object contains information about the request, such as the parameters and headers. The HttpServletResponse object is used to send a response back to the client. 
7. The doGet() method must return a response to the client. This response is typically an HTML page, an XML document, or a JSON object.