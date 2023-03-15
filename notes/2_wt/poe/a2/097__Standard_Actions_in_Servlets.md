 Here is the content in markdown format with formal tone and without any emojis or external links:

#### Standard Actions in Servlets

1. doGet(): Called by the server (via the service() method) to allow a servlet to handle a GET request. This method is used when a browser issues an HTTP GET request to the servlet.
2. doPost(): Called by the server (via the service() method) to allow a servlet to handle a POST request. This method is used when a browser issues an HTTP POST request to the servlet.
3. init(): Called by the server (via the init() method) to initialize a servlet. This method is executed only once when a servlet is first loaded. It's used to perform any one-time initialization.
4. destroy(): Called by the server (via the destroy() method) to allow a servlet to perform any clean-up before it is unloaded. This method is executed only once when the servlet is about to be unloaded. It's used to release any resources that the servlet may have occupied.

The service() method of the HttpServlet class dispatches the HTTP requests to the appropriate doXXX() methods. A servlet container calls the service() method for every request and passes in an HttpServletRequest and an HttpServletResponse object.

The doGet() and doPost() methods handle GET and POST requests respectively. The programmer should override these methods to specify the request handling behavior of their servlet for these requests.

The init() and destroy() methods are called by the servlet container to manage the lifecycle of the servlet. The programmer can perform any initialization tasks or cleanup jobs in these methods respectively.