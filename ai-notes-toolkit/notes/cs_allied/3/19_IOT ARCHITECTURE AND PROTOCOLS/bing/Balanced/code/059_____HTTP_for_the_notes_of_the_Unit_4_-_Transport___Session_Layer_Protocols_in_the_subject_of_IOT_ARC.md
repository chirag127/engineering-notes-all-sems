### HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application layer protocol in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It is used for transmitting hypermedia documents, such as HTML, between web browsers and web servers.

Some points to note about HTTP are:

- HTTP is a stateless protocol, which means that each request and response pair is independent and does not remember any previous interaction.
- HTTP uses TCP as the underlying and reliable transport layer protocol. TCP establishes a connection between the client and the server, and ensures that the data is delivered in order and without errors.
- HTTP follows a request-response model, where the client sends a request message to the server, and the server sends back a response message to the client. The request and response messages have a similar structure, consisting of a start-line, zero or more header fields, an empty line, and an optional message body.
- HTTP defines a set of methods, also known as verbs, that indicate the desired action to be performed on the resource identified by the request URI. Some common methods are GET, POST, PUT, DELETE, HEAD, and OPTIONS.
- HTTP defines a set of status codes, also known as response codes, that indicate the result of the request. Some common status codes are 200 (OK), 404 (Not Found), 301 (Moved Permanently), and 500 (Internal Server Error).
- HTTP can be extended by adding new header fields, methods, status codes, or media types. For example, HTTP/1.1 introduced persistent connections, chunked transfer encoding, and content negotiation.
- HTTP can also be modified or replaced by other protocols that offer different features or performance. For example, HTTPS is a secure version of HTTP that uses SSL/TLS encryption, HTTP/2 is a binary and multiplexed version of HTTP that reduces latency and overhead, and HTTP/3 is a version of HTTP that uses QUIC as the transport layer protocol.