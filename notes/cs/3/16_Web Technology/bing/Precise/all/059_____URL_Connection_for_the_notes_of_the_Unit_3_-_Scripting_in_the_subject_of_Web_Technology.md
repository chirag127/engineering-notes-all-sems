### URL Connection

URL Connection is a class in the `java.net` package that provides a way to communicate with a URL. It is used to establish a connection to a URL and perform operations such as reading from or writing to the resource the URL represents.

Here are some key points to remember about URL Connection:

1. URL Connection is an abstract class, which means it cannot be instantiated directly. Instead, an instance of a subclass of URL Connection is created by calling the `openConnection()` method on a URL object.

2. URL Connection provides methods for setting and getting various properties of the connection, such as the request method, request headers, and timeout values.

3. URL Connection provides methods for reading from and writing to the resource the URL represents. These methods include `getInputStream()`, `getOutputStream()`, and `getContent()`.

4. URL Connection provides support for both HTTP and HTTPS protocols. The `HttpsURLConnection` class is a subclass of URL Connection that provides additional methods for handling secure connections.

5. URL Connection can be used to perform various operations such as downloading a file, uploading a file, or sending a POST request to a server.

6. URL Connection provides support for handling cookies, which can be useful when working with websites that require authentication.

7. URL Connection provides support for handling redirects, which can be useful when working with websites that redirect the user to a different URL.

8. URL Connection provides support for handling caching, which can be useful when working with resources that do not change frequently.
