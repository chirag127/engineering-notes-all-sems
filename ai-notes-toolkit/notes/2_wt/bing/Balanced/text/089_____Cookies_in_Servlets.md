### Cookies in Servlets

- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies can be used to store information about the user, such as preferences, session state, or authentication details.
- Cookies are sent by the server to the browser using the `Set-Cookie` header in the response.
- Cookies are sent back by the browser to the server using the `Cookie` header in the request.
- Cookies have attributes such as name, value, domain, path, expiry date, secure flag, and http-only flag.
- Cookies can be created, read, updated, and deleted by servlets using the `javax.servlet.http.Cookie` class and the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` interfaces.
- Cookies can be created by calling the constructor of the `Cookie` class with the name and value of the cookie as parameters, such as `Cookie c = new Cookie("name", "value");`.
- Cookies can be read by calling the `getCookies()` method of the `HttpServletRequest` interface, which returns an array of `Cookie` objects, such as `Cookie[] cookies = request.getCookies();`.
- Cookies can be updated by changing the value or attributes of the `Cookie` object and sending it back to the browser using the `addCookie()` method of the `HttpServletResponse` interface, such as `c.setValue("new value"); response.addCookie(c);`.
- Cookies can be deleted by setting the expiry date of the `Cookie` object to a past date and sending it back to the browser using the `addCookie()` method of the `HttpServletResponse` interface, such as `c.setMaxAge(0); response.addCookie(c);`.
- Cookies can be used to implement various functionalities in web applications, such as user authentication, shopping cart, personalization, etc.