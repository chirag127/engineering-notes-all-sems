Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of cookies for the unit 5 - Servlets.

### Cookies
- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies are used to store information about the user's preferences, session state, authentication, etc.
- Cookies are sent by the server to the browser using the `Set-Cookie` header in the HTTP response.
- Cookies are sent back by the browser to the server using the `Cookie` header in the HTTP request.
- Cookies have a name, a value, and some optional attributes, such as `Expires`, `Domain`, `Path`, `Secure`, and `HttpOnly`.
- Cookies can be created, read, updated, and deleted by the servlets using the `javax.servlet.http.Cookie` class and the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` interfaces.
- To create a cookie, a servlet can use the `Cookie` constructor with the name and value as parameters, and then use the `addCookie` method of the `HttpServletResponse` object to send the cookie to the browser.
- To read a cookie, a servlet can use the `getCookies` method of the `HttpServletRequest` object to get an array of `Cookie` objects, and then use the `getName` and `getValue` methods of the `Cookie` class to access the cookie's name and value.
- To update a cookie, a servlet can use the `setValue` method of the `Cookie` class to change the cookie's value, and then use the `addCookie` method of the `HttpServletResponse` object to send the updated cookie to the browser.
- To delete a cookie, a servlet can use the `setMaxAge` method of the `Cookie` class to set the cookie's expiration time to zero, and then use the `addCookie` method of the `HttpServletResponse` object to send the expired cookie to the browser.
- Cookies have some limitations, such as:
  - Cookies are not secure, as they can be intercepted, modified, or stolen by malicious parties.
  - Cookies are not reliable, as they can be disabled, deleted, or blocked by the user or the browser.
  - Cookies have a size limit of 4 KB, which limits the amount of data that can be stored in a cookie.
  - Cookies are domain and path specific, which means they can only be accessed by the same domain and path that created them.