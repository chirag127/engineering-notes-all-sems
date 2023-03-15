# Cookies

- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies are used to store information about the user's preferences, session state, authentication, etc.
- Cookies are sent by the server to the browser in the response header, and the browser sends them back to the server in the request header.
- Cookies have a name, a value, an expiration date, a domain, and a path.
- Cookies can be created, read, updated, and deleted by using the `javax.servlet.http.Cookie` class in servlets.
- To create a cookie, use the `Cookie` constructor with the name and value as parameters, and then use the `response.addCookie()` method to send it to the browser.
- To read a cookie, use the `request.getCookies()` method to get an array of cookies, and then loop through the array to find the cookie by its name.
- To update a cookie, create a new cookie with the same name and a different value, and then use the `response.addCookie()` method to overwrite the existing cookie.
- To delete a cookie, create a new cookie with the same name and a value of null, and then set its maximum age to zero using the `setMaxAge()` method, and then use the `response.addCookie()` method to send it to the browser.
- Cookies have some limitations, such as:
  - Cookies are not secure, as they can be intercepted, modified, or stolen by attackers.
  - Cookies are not reliable, as they can be disabled, deleted, or blocked by the user or the browser.
  - Cookies have a size limit of 4 KB, and a number limit of 20 per domain.
  - Cookies are not suitable for storing complex or sensitive data.