# Session Tracking with Http Session

- Session tracking is a technique to maintain the state of a client-server communication across multiple requests.
- The HTTP protocol is stateless, which means that each request is independent and does not carry any information from previous requests.
- Session tracking allows the server to keep track of successive requests made by the same client and associate them with a session object and a unique session ID.
- The session object can store information about the client's preferences, activities, or transactions.
- The session ID can be passed between the client and the server using different methods, such as cookies, URL rewriting, or SSL information.
- The servlet container provides an interface called HttpSession to create and manage session objects.
- The HttpSession interface has methods to set and get attributes, get the session ID, get the creation and last access time, invalidate the session, and check if the session is new.
- The session object can be obtained from the HttpServletRequest object using the getSession() method.
- The session object will be available to all of the servlets and JSPs that the user accesses until the session is closed due to timeout or error.
- Session tracking can be used for various purposes, such as tracking conversions in online shopping, mailing applications, and E-commerce.