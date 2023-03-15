## Unit 5 - Servlets

1. Servlets are Java programs that run on the server-side and handle client requests.
2. They are used to create dynamic web content and can interact with databases and other server-side resources.
3. Servlets are managed by a servlet container, which is part of a web server or application server.
4. The servlet container is responsible for managing the lifecycle of servlets, including initialization, request handling, and destruction.
5. Servlets can be configured using annotations or through a deployment descriptor (web.xml).
6. The `HttpServlet` class is a commonly used base class for creating servlets that handle HTTP requests.
7. Servlets can handle different types of requests, including GET, POST, PUT, DELETE, and others.
8. The `doGet` and `doPost` methods are used to handle GET and POST requests, respectively.
9. Servlets can generate responses in various formats, including HTML, JSON, XML, and others.
10. Servlets can also set response headers, cookies, and status codes.
11. The `RequestDispatcher` interface can be used to forward or include requests to other resources, such as other servlets or JSP pages.
12. Servlets can also use filters to intercept and modify requests and responses.
13. Servlets can be used in various applications, including e-commerce, social networking, and content management systems.

A mnemonic to remember the lifecycle of a servlet is "I am a servlet, I am alive, I serve, I die" which stands for Init, Service, and Destroy methods.