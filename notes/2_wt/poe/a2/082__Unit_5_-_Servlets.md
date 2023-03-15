 Here is the content in markdown format with formal tone and without emojis:

## Unit 5 - Servlets

1. Servlets are Java programs that run on a web server. They are used to handle requests and generate responses to the client.
2. The steps to create a servlet are:
- Extend the HttpServlet class
- Override the doGet/doPost methods to handle GET and POST requests respectively
- Configure servlet mapping in web.xml to map an URL to the servlet
3. The life cycle of a servlet involves the following stages:
- Loading: The servlet is loaded into memory when the web container starts up
- Initialization: The init() method is called to initialize the servlet
- Request handling: The service() method is called to handle client requests
- Destruction: The destroy() method is called when the servlet is unloaded from memory
4. Servlets can maintain state between client requests using techniques like session tracking and request dispatching. Sessions can be tracked using cookies, URL rewriting or the HttpSession object.
5. Advantages of servlets are:
- They are robust, fast and efficient
- They can access full Java APIs
- They are cost effective and platform independent
- They support multithreading and can handle large loads

The above content summarizes the key points about servlets in a formal tone with headings and points. External links are avoided and all content is written manually as instructed. Please let me know if you would like me to modify or add any other points.