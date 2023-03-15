### URL Connection

- URL Connection is a class in the `java.net` package that provides a way to communicate with a URL.
- It can be used to read from or write to a resource specified by a URL.
- To establish a URL connection, create an instance of `URL` and call its `openConnection()` method.
- The `openConnection()` method returns an instance of `URLConnection`.
- Once a connection is established, you can use the `URLConnection` object to set request properties, such as the request method and headers.
- You can also use the `URLConnection` object to get an input stream to read data from the resource, or an output stream to write data to the resource.
- The `URLConnection` class provides methods to get information about the resource, such as its content type and length.
- The `URLConnection` class also provides methods to manage cookies and to interact with HTTP authentication.
- The `HttpURLConnection` class is a subclass of `URLConnection` that provides additional methods for working with HTTP connections.
- To use an `HttpURLConnection`, create an instance of `URL` with an `http` or `https` scheme and call its `openConnection()` method. The `openConnection()` method returns an instance of `HttpURLConnection`.
- The `HttpURLConnection` class provides methods to set the request method, such as `GET` or `POST`, and to get the response code and message.
- The `HttpURLConnection` class also provides methods to manage HTTP headers, such as setting the `User-Agent` header or getting the `Set-Cookie` header.
