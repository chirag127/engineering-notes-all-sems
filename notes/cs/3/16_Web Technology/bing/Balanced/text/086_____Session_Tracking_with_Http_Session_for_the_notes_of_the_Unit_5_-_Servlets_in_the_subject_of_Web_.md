### Session Tracking with Http Session

- Session tracking is a way to maintain state (data) of an user across multiple requests to the server .
- Http protocol is stateless, which means it does not remember the previous requests or responses .
- Session tracking allows the server to keep track of successive requests made by the same client and provide personalized services .
- The session is created between an HTTP client and an HTTP server by the servlet container using HttpSession .
- HttpSession is an interface that provides methods to store, retrieve, and remove attributes associated with a session .
- When the user makes a request, the server assigns it a session object and a unique session ID thereby helping in session tracking .
- The session ID can be passed between the client and the server using cookies, URL rewriting, or hidden form fields .
- The session object will be available to all of the servlets and JSPs that the user accesses until the session is closed due to timeout or error .
- The session object can be obtained by calling the getSession() method of the HttpServletRequest interface .
- The session object can be used to store and retrieve attributes using the setAttribute() and getAttribute() methods respectively .
- The session object can be invalidated by calling the invalidate() method, which removes all the attributes and terminates the session .
- The session object can be configured using the web.xml file, which specifies the session timeout, cookie name, and tracking mode .