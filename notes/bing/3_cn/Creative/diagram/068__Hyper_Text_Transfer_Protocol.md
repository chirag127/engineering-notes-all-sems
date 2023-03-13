Hyper Text Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML, between web browsers and web servers. HTTP defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands. HTTP is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access.

### Hyper Text Transfer Protocol

The following diagram illustrates the basic architecture of HTTP:

```
    +-----------------+                      +-----------------+
    |                 |                      |                 |
    |    Web Browser  |                      |    Web Server   |
    |                 |                      |                 |
    +-----------------+                      +-----------------+
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |<--------HTTP Request Message------|   |
          |   |                                    |   |
          |   |--------HTTP Response Message------>|   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |<--------HTTP Request Message------|   |
          |   |                                    |   |
          |   |--------HTTP Response Message------>|   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          V   V                                    V   V
```

An HTTP request message consists of a request line, header fields, and an optional message body. The request line contains the HTTP method, the request URI, and the HTTP version. For example:

```
GET /index.html HTTP/1.1
```

An HTTP response message consists of a status line, header fields, and an optional message body. The status line contains the HTTP version, the status code, and the reason phrase. For example:

```
HTTP/1.1 200 OK
```

HTTP supports different methods for different purposes. Some of the common methods are:

- GET: Requests a representation of the specified resource.
- POST: Submits data to be processed by the specified resource.
- PUT: Replaces the representation of the specified resource with the request payload.
- DELETE: Deletes the specified resource.
- HEAD: Requests only the header fields of the specified resource.
- OPTIONS: Requests the available methods and options for the specified resource.
- TRACE: Echoes back the received request for testing purposes.
- CONNECT: Establishes a tunnel to the specified server for proxying purposes.

HTTP also supports different status codes to indicate the outcome of a request. Some of the common status codes are:

- 200 OK: The request was successful and the response contains the requested resource.
- 301 Moved Permanently: The requested resource has been permanently moved to a new location, which is given by the Location header field.
- 400 Bad Request: The request was malformed or invalid and could not be processed by the server.
- 401 Unauthorized: The request requires authentication and the client did not provide valid credentials.
- 403 Forbidden: The server understood the request but refused to authorize it due to insufficient permissions.
- 404 Not Found: The requested resource was not found on the server.
- 500 Internal Server Error: The server encountered an unexpected error while processing the request and could not fulfill it.
- 503 Service Unavailable: The server is temporarily unable to handle the request due to overload or maintenance.