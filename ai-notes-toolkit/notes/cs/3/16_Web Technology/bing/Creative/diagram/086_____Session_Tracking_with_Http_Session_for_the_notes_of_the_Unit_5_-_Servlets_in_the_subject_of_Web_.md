### Session Tracking with Http Session

- Session tracking is a technique to maintain the state of a client-server communication across multiple requests .
- The HTTP protocol is stateless, which means that each request is independent and does not carry any information about previous requests or responses.
- Session tracking allows the server to keep track of successive requests made by the same client and associate them with a session object and a unique session ID .
- The session object can store information about the client's preferences, activities, or transactions, and can be accessed by all the servlets and JSPs that the client visits .
- The session ID can be transmitted between the client and the server using different methods, such as cookies, URL rewriting, or SSL information.
- The HttpSession interface is a standard way to implement session tracking in servlets. It provides methods to create, access, modify, and invalidate session objects .
- The servlet container is responsible for creating and managing HttpSession objects and assigning them to the clients .
- The servlet can obtain the current session object by calling the request.getSession() method, which returns an existing session or creates a new one if none exists .
- The servlet can store and retrieve values in the session object by using the setAttribute() and getAttribute() methods, which take a name and an object as parameters .
- The servlet can remove a value from the session object by using the removeAttribute() method, which takes a name as a parameter .
- The servlet can invalidate the session object by using the invalidate() method, which terminates the session and releases the resources associated with it .
- The servlet can check if the session object is new or existing by using the isNew() method, which returns a boolean value .
- The servlet can get the session ID by using the getId() method, which returns a string value .
- The servlet can get or set the maximum inactive interval for the session object by using the getMaxInactiveInterval() and setMaxInactiveInterval() methods, which take or return an integer value in seconds .
- The servlet can add or remove listeners to the session object by using the addListener() and removeListener() methods, which take an HttpSessionListener object as a parameter .
- The HttpSessionListener interface defines two methods: sessionCreated() and sessionDestroyed(), which are invoked when a session is created or invalidated .