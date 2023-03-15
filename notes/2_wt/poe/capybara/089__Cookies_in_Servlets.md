### Cookies in Servlets

Cookies are small text files that are sent from a web server to the client's computer. They are used to store information about the client's preferences and browsing history. In servlets, cookies can be created, read, and deleted using the javax.servlet.http.Cookie class. Here are some important points to remember about cookies in servlets:

- To create a cookie, use the Cookie constructor and set its name and value. For example, `Cookie cookie = new Cookie("username", "John");`
- To set the maximum age of a cookie in seconds, use the `setMaxAge(int maxAge)` method. For example, `cookie.setMaxAge(3600);` sets the cookie's maximum age to one hour.
- To add a cookie to the response, use the `addCookie(Cookie cookie)` method of the HttpServletResponse class. For example, `response.addCookie(cookie);` adds the cookie to the response.
- To read a cookie from the request, use the `getCookies()` method of the HttpServletRequest class. This method returns an array of Cookie objects. For example, `Cookie[] cookies = request.getCookies();`
- To delete a cookie, create a new cookie with the same name and set its maximum age to 0. Then add the cookie to the response using the `addCookie(Cookie cookie)` method. For example, `Cookie cookie = new Cookie("username", ""); cookie.setMaxAge(0); response.addCookie(cookie);`

Cookies are an important part of web development and servlets provide a convenient way to work with them. By understanding how cookies work in servlets, developers can create more personalized and efficient web applications.