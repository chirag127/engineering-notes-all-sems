# Handling HTTP get Requests for the notes of the Unit 5 - Servlets in the subject of Web Technology

- HTTP get requests are used to retrieve data from a server based on the parameters specified in the URL.
- To handle HTTP get requests in a servlet, extend the HttpServlet class and override the doGet method.
- The doGet method takes two parameters: HttpServletRequest and HttpServletResponse, which represent the request and response objects respectively.
- The HttpServletRequest object provides methods to access the request information, such as the URL, the query string, the headers, the cookies, etc.
- The HttpServletResponse object provides methods to set the response information, such as the status code, the headers, the content type, the output stream, etc.
- The doGet method can use the request and response objects to process the HTTP get request and generate the appropriate response.
- The doGet method can also handle HTTP head requests, which are similar to get requests but only return the headers and not the body of the response.
- The doGet method is invoked by the server through the service method, which dispatches the request to the appropriate servlet method based on the HTTP method.
- The doGet method can throw ServletException or IOException, which indicate that the servlet encountered an error while processing the request or writing the response.
- The doGet method can also use the PrintWriter object obtained from the response object to write the response body as text.

: Servlet for handling HTTP GET request Example - Computer Notes
: Handling GET and POST Requests
: java - creating web server - handling incoming http requests
: Servlet - Client HTTP Request - GeeksforGeeks
: Handling HTTP get Requests | Servlets - flylib.com