### Cookies for the notes of the Unit 5 - Servlets in the subject of Web Technology

Cookies are small text files that are stored on the client's computer by the server. They are used to keep track of user preferences, login information, and other data that can be used to enhance the user experience. In the context of servlets, cookies are an important tool for maintaining state information across multiple requests. Here are some key points to remember about cookies in servlets:

- A servlet can create a cookie by calling the `Cookie` constructor and passing in a name-value pair.
- The `setMaxAge()` method can be used to set the cookie's expiration time, in seconds. A negative value means that the cookie will be deleted when the user closes the browser.
- The `addCookie()` method of the `HttpServletResponse` object can be used to send the cookie to the client.
- Cookies can be retrieved from the client's request by calling the `getCookies()` method of the `HttpServletRequest` object. This method returns an array of all cookies that were sent by the client.
- Once a cookie has been retrieved, its value can be accessed using the `getValue()` method.
- Cookies can be used to maintain user sessions. For example, a servlet could create a new session ID and store it in a cookie. Subsequent requests from the client would include the session ID cookie, allowing the server to retrieve the user's session information.
- Cookies can be used to implement shopping carts and other types of user preferences. For example, a user could select items to purchase and add them to a cart, which would be stored in a cookie. The user could then return to the site at a later time and have their cart restored from the cookie.

In summary, cookies are an important tool for maintaining state information in servlets. They can be used to store user preferences, login information, and other data that can enhance the user experience. By understanding how cookies work in servlets, developers can build more robust and user-friendly web applications.