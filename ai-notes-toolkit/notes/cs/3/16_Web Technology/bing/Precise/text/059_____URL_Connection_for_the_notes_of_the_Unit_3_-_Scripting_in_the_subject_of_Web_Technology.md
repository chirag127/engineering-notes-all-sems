### URL Connection

- URL Connection is a class in the `java.net` package that represents a communication link between the application and a URL.
- It can be used to read from or write to a resource specified by a URL.
- To establish a URL connection, first create a `URL` object and then call its `openConnection()` method.
- The `openConnection()` method returns an instance of `URLConnection`.
- Once the connection is established, various methods can be used to interact with the resource.
- For example, the `getInputStream()` method can be used to read data from the resource, and the `getOutputStream()` method can be used to write data to the resource.
- The `setRequestProperty()` method can be used to set request headers, and the `getHeaderField()` method can be used to read response headers.
- URL Connection also provides support for common HTTP operations such as `GET` and `POST` through its subclasses `HttpURLConnection` and `HttpsURLConnection`.
- To perform an HTTP `GET` request, simply call the `connect()` method on an instance of `HttpURLConnection`.
- To perform an HTTP `POST` request, first call the `setDoOutput(true)` method to indicate that the connection will be used for output, then write the data to be posted to the connection's output stream using the `getOutputStream()` method, and finally call the `connect()` method to send the request.
- URL Connection provides a flexible and powerful way to interact with resources on the web, and is commonly used in web-based applications.