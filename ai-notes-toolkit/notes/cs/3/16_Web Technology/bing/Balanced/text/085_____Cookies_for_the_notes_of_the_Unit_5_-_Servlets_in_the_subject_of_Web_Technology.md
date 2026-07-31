### Cookies

- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies are used to store information about the user's preferences, session state, authentication, etc.
- Cookies are sent by the server to the browser in the response header, and the browser sends them back to the server in the request header.
- Cookies have a name, a value, an expiration date, a domain, and a path.
- Cookies can be created, read, updated, and deleted by using the javax.servlet.http.Cookie class in servlets.
- To create a cookie, use the Cookie constructor with the name and value as parameters, and then use the response.addCookie() method to send it to the browser.
- To read a cookie, use the request.getCookies() method to get an array of Cookie objects, and then loop through the array to find the cookie by its name.
- To update a cookie, create a new Cookie object with the same name and a different value, and then use the response.addCookie() method to overwrite the existing cookie.
- To delete a cookie, create a new Cookie object with the same name and a value of null, and then use the response.addCookie() method to send it to the browser. Alternatively, set the expiration date of the cookie to a past date.
- Cookies have some limitations, such as:
  - Cookies are not secure, as they can be intercepted, modified, or stolen by malicious users or programs.
  - Cookies are not reliable, as they can be disabled, deleted, or blocked by the browser or the user.
  - Cookies have a size limit of 4 KB, which limits the amount of data that can be stored in them.
  - Cookies are not shared across different domains or subdomains, which limits their scope and functionality.