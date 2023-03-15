### URL Connection

- URL Connection is a class in the `java.net` package that provides a way to communicate with a URL.
- It can be used to read from or write to a resource specified by a URL.
- A URL Connection instance represents a connection to the resource referred to by the URL.
- To establish a connection to a URL, create a `URL` object and call its `openConnection` method.
- The `openConnection` method returns a `URLConnection` object, which can be used to interact with the resource.
- The `URLConnection` class provides methods to set request properties, such as the request method and headers.
- It also provides methods to get information about the response, such as the response code and headers.
- The `getInputStream` method can be used to read data from the resource, while the `getOutputStream` method can be used to write data to the resource.
- The `URLConnection` class is an abstract class, and its concrete subclasses provide protocol-specific behavior.
- For example, the `HttpURLConnection` class is a subclass of `URLConnection` that provides support for the HTTP protocol.
