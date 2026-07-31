### Session Tracking with Http Session

- Session tracking is a technique to maintain the state of a client-server communication across multiple requests .
- The HTTP protocol is stateless, which means that each request is independent and does not carry any information about previous requests or responses.
- Session tracking allows the server to keep track of successive requests made by the same client and associate them with a session object and a unique session ID .
- The session object can store information about the client's preferences, actions, or transactions, and can be accessed by all the servlets and JSPs that the client visits until the session is closed due to timeout or error .
- Session tracking can be done by the server using the HttpSession interface, which provides methods to create, access, and manipulate session objects .
- The HttpSession interface also provides methods to get and set attributes, which are key-value pairs that can store any type of object in the session object .
- The session ID can be transmitted between the client and the server using cookies, URL rewriting, or SSL information.
- Cookies are small pieces of data that are stored by the browser and sent with each request to the server. The server can set a cookie with the session ID using the setCookie() method of the HttpServletResponse interface, and the client can send it back with the next request using the getCookies() method of the HttpServletRequest interface .
- URL rewriting is a technique to append the session ID as a query parameter to every URL that the client requests. The server can use the encodeURL() method of the HttpServletResponse interface to rewrite the URLs, and the client can send the session ID with the request using the getParameter() method of the HttpServletRequest interface .
- SSL information is a technique to use the secure sockets layer protocol to encrypt the communication between the client and the server. The server can use the getAttribute() method of the HttpServletRequest interface to get the SSL session ID, and the client can send it with the request using the setAttribute() method of the HttpServletRequest interface.