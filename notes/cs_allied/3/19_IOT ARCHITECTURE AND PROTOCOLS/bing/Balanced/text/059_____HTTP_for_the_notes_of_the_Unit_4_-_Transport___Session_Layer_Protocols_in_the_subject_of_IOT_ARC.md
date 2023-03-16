### HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

Some basic concepts of HTTP are:

- **Resources and URIs**: A resource is any piece of information that can be identified by a Uniform Resource Identifier (URI). A URI is a string that uniquely identifies a resource on the web. For example, `https://example.com/index.html` is a URI that identifies an HTML document on a web server.
- **Messages**: HTTP communication consists of messages that are exchanged between a client and a server. A message has a simple structure: a start-line, zero or more headers, an empty line, and an optional body. The start-line indicates the type of the message: a request or a response. The headers provide additional information about the message, such as the content type, the length, the encoding, etc. The body contains the actual data of the message, such as the HTML document, the image, the JSON data, etc.
- **Methods**: HTTP defines a set of methods that indicate the action to be performed on a resource. The most common methods are: GET, POST, PUT, DELETE, HEAD, OPTIONS, etc. For example, a GET request asks the server to send back the resource identified by the URI, while a POST request sends data to the server to create or update a resource.
- **Status codes**: HTTP defines a set of status codes that indicate the outcome of a request. The status codes are divided into five categories: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client error), and 5xx (server error). For example, a 200 status code means that the request was successful, while a 404 status code means that the resource was not found.
- **Client-server communication flow**: HTTP is a client-server protocol, which means that requests are sent by one entity, the user-agent (or a proxy on behalf of it), and responses are sent by another entity, the origin server (or a proxy on behalf of it). Most of the time, the user-agent is a web browser, but it can be anything, such as a robot that crawls the web to populate and maintain a search engine index. The communication flow is as follows:

  1. The user-agent initiates a connection to the server using the URI of the resource.
  2. The user-agent sends a request message to the server, specifying the method, the URI, the protocol version, the headers, and the body (if any).
  3. The server receives the request and processes it according to its logic and configuration.
  4. The server sends a response message to the user-agent, specifying the protocol version, the status code, the headers, and the body (if any).
  5. The user-agent receives the response and interprets it according to the status code, the headers, and the body. It may display the resource to the user, follow a redirection, handle an error, etc.
  6. The connection is closed, unless the user-agent or the server indicates that it wants to keep it alive for further requests.

- **Extensions**: HTTP is an extensible protocol that allows adding new functionality and semantics with new methods, headers, status codes, etc. For example, HTTP/1.1 introduced features such as persistent connections, chunked encoding, caching, etc. HTTP/2 introduced features such as multiplexing, compression, server push, etc. HTTP/3 introduced features such as using QUIC as the underlying transport layer, etc.