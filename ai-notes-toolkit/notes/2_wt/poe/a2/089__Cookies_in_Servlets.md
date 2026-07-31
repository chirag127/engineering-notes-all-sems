 Here is the content in markdown format with formal tone and without emojis:

### Cookies in Servlets

1. Cookies are small pieces of data sent from a web server to a web browser. The browser stores the cookies and sends them back to the server with every request.
2. This allows the server to keep track of the user over multiple pages or sessions. For example, a cookie can store a session ID to identify a user in a session management mechanism.
3. To set a cookie in a servlet, use the setHeader() method of the HttpServletResponse object. You need to specify a name and value for the cookie, as well as optionally an expiration date and path.
4. For example:
response.setHeader("Cookie", "name=value");

This will create a session cookie that expires when the browser is closed.

response.setHeader("Set-Cookie", "name=value; expires=Wed, 09 Jun 2021 10:18:14 GMT; path=/");

This will create a persistent cookie that expires on a specific date. The path indicates what path the cookie is valid for.

5. To retrieve cookies in a servlet, use the getHeaders() method of the HttpServletRequest object and look for "Cookie" headers. You'll need to parse the cookie header string to get the values of the individual cookies.

For example:
String cookie = request.getHeader("Cookie");
// Parse cookie...

This can be useful for session management, personalization, and tracking users on a website. However, cookies do have privacy implications that must be considered.