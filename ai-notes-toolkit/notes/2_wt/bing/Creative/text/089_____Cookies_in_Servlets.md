### Cookies in Servlets

- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies are used to store information about the user's preferences, session state, authentication, etc.
- Cookies are sent by the server to the browser using the `Set-Cookie` header in the HTTP response.
- Cookies are sent back by the browser to the server using the `Cookie` header in the HTTP request.
- Cookies have a name, a value, and some optional attributes, such as `Domain`, `Path`, `Expires`, `Secure`, and `HttpOnly`.
- Cookies can be created, read, updated, and deleted by servlets using the `javax.servlet.http.Cookie` class and the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` interfaces.
- To create a cookie, a servlet can use the `Cookie` constructor with the name and value of the cookie as parameters, and then call the `addCookie` method of the `HttpServletResponse` object to send the cookie to the browser.
- To read a cookie, a servlet can use the `getCookies` method of the `HttpServletRequest` object to get an array of `Cookie` objects, and then loop through the array to find the cookie with the desired name.
- To update a cookie, a servlet can use the `setValue` method of the `Cookie` object to change the value of the cookie, and then call the `addCookie` method of the `HttpServletResponse` object to send the updated cookie to the browser.
- To delete a cookie, a servlet can use the `setMaxAge` method of the `Cookie` object to set the expiration time of the cookie to zero, and then call the `addCookie` method of the `HttpServletResponse` object to send the expired cookie to the browser.