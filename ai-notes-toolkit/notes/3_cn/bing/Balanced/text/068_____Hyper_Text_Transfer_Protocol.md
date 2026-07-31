### Hyper Text Transfer Protocol

- Hyper Text Transfer Protocol (HTTP) is a protocol that defines how web browsers and web servers communicate and exchange data over the internet.
- HTTP is based on a request-response model, where a client (such as a browser) sends a request to a server (such as a web server) and the server responds with a status code, headers, and optionally a body.
- HTTP requests and responses can contain different types of data, such as text, images, audio, video, etc. The data type is specified by the Content-Type header.
- HTTP uses Uniform Resource Locators (URLs) to identify the resources that the client wants to access. A URL consists of a scheme (such as http or https), a host name (such as www.example.com), a port number (optional), a path (such as /index.html), and a query string (optional).
- HTTP supports different methods (also called verbs) to perform different actions on the resources. The most common methods are GET, POST, PUT, DELETE, HEAD, and OPTIONS.
- GET method is used to retrieve a resource from the server. The request can include query parameters in the URL to specify the criteria for the resource.
- POST method is used to send data to the server, such as form data, files, etc. The request can include a body that contains the data to be sent.
- PUT method is used to update or create a resource on the server. The request can include a body that contains the data to be updated or created.
- DELETE method is used to delete a resource from the server. The request can include query parameters in the URL to specify the criteria for the resource.
- HEAD method is used to get the headers of a resource from the server, without the body. This can be useful to check the metadata of a resource, such as its size, type, modification date, etc.
- OPTIONS method is used to get the allowed methods for a resource from the server. This can be useful to check the capabilities of a resource, such as what methods it supports, what headers it accepts, etc.
- HTTP uses status codes to indicate the outcome of a request. The status codes are divided into five categories: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client error), and 5xx (server error).
- Some of the common status codes are:

  - 200 OK: The request was successful and the response contains the requested resource.
  - 301 Moved Permanently: The requested resource has been moved to a new URL and the client should use the new URL for future requests.
  - 302 Found: The requested resource has been found at a different URL and the client should use the new URL for this request only.
  - 304 Not Modified: The requested resource has not been modified since the last request and the client can use the cached version of the resource.
  - 400 Bad Request: The request was malformed or invalid and the server could not process it.
  - 401 Unauthorized: The request requires authentication and the client did not provide valid credentials.
  - 403 Forbidden: The request was valid but the server refused to fulfill it due to authorization or permission issues.
  - 404 Not Found: The requested resource was not found on the server and the server does not know where to find it.
  - 500 Internal Server Error: The server encountered an unexpected error while processing the request and could not complete it.
  - 503 Service Unavailable: The server is temporarily unable to handle the request due to overload or maintenance and the client should try again later.