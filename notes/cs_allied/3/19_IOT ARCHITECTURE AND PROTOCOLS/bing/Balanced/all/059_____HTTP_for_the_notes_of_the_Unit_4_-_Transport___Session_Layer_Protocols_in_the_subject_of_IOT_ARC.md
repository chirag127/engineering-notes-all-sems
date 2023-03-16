# HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

Some basic concepts of HTTP are:

- HTTP is a client-server protocol: requests are sent by one entity, the user-agent (or a proxy on behalf of it). Most of the time the user-agent is a web browser, but it can be anything, for example, a robot that crawls the web to populate and maintain a search engine index.
- HTTP is a stateless protocol: each request and response pair is independent of each other, and the server does not keep any information about the previous or future requests from the same client.
- HTTP is an extensible protocol: it relies on concepts like resources and Uniform Resource Identifiers (URIs), simple message structure, and client-server communication flow. On top of these basic concepts, numerous extensions have been developed over the years that add updated functionality and semantics with new HTTP methods or headers.

Some common features of HTTP are:

- HTTP methods: these are the verbs that indicate the action to be performed on a resource, such as GET, POST, PUT, DELETE, etc.
- HTTP headers: these are the key-value pairs that provide additional information about the request or the response, such as Content-Type, Content-Length, Accept, Cookie, etc.
- HTTP status codes: these are the numerical codes that indicate the outcome of the request, such as 200 OK, 404 Not Found, 500 Internal Server Error, etc.
- HTTP messages: these are the actual data that are exchanged between the client and the server, consisting of a start-line, zero or more headers, an empty line, and an optional message body.
- HTTP cookies: these are small pieces of data that are stored by the user-agent and sent back to the server with each request, to enable stateful sessions and personalization.
- HTTP authentication: this is the mechanism by which the user-agent can provide credentials to the server to access protected resources, using schemes such as Basic, Digest, or Bearer.
- HTTP proxy and tunneling: these are the techniques by which the user-agent can communicate with the server through an intermediary, to bypass network restrictions or enhance security.