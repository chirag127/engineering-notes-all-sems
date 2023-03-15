
### Cookies in Servlets

* Cookies are small pieces of data stored on the client-side that are used to remember states and information about a user. They are commonly used in web applications to store user-specific information such as preferences or login information. 
* Servlets are Java classes that act as a middle layer between a request coming from a web client and databases or applications on the HTTP server. They are used to process requests and generate dynamic web pages.
* Cookies can be used in servlets to track user information and store session-specific data. This allows the servlet to remember the user's state and personalize their experience.
* Cookies are stored on the client-side, so they must be sent with each request to the server. This is done by setting the `Cookie` header in the HTTP request. 
* Servlets can set cookies by adding the `Set-Cookie` header in the HTTP response. This header contains the cookie name, value, and other optional parameters such as expiration date and domain.
* When a servlet receives a request, it can access the cookies by using the `getCookies()` method of the `HttpServletRequest` class. This method returns an array of `Cookie` objects which can be used to access the cookie values.
* Cookies are not secure, so they should not be used to store sensitive information. Additionally, cookies can be modified or deleted by the user, so any data stored in them should not be trusted.

Mnemonic: 

*C*ookies *S*tore *U*ser *S*tate *I*n *S*ervlets