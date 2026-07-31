### Cookies in Servlets

Cookies are small text files that a web server sends to a client’s browser to store information that can be used to identify the user or track their activity on the website. In servlets, cookies can be used to store user-specific information and maintain session state.

Here are some important points to understand about cookies in servlets:

1. Cookies can be created and sent to the client using the `javax.servlet.http.Cookie` class, which provides methods for setting the cookie’s name, value, and other attributes.

2. Cookies can be added to the response using the `javax.servlet.http.HttpServletResponse.addCookie(Cookie cookie)` method.

3. Cookies can be retrieved from the request using the `javax.servlet.http.HttpServletRequest.getCookies()` method, which returns an array of `Cookie` objects.

4. Cookies can be used to store user-specific information such as login credentials, user preferences, and shopping cart contents.

5. Cookies can also be used to maintain session state, which is useful for tracking a user’s activity across multiple requests. To do this, a unique session ID can be stored in the cookie, which is used to retrieve the user’s session data from the server.

6. Cookies can have various attributes such as `max-age`, `secure`, and `httpOnly`, which control how the cookie is stored and transmitted. For example, the `httpOnly` attribute prevents the cookie from being accessed by client-side scripts, which can prevent cross-site scripting (XSS) attacks.

7. Cookies can be deleted by setting their `max-age` attribute to 0 and adding them to the response using the `addCookie()` method.

8. Cookies have a size limit of 4KB, so they should not be used to store large amounts of data.

In summary, cookies are an important tool for maintaining state and storing user-specific information in servlets. By understanding how to create, retrieve, and manipulate cookies, developers can build more robust and personalized web applications.