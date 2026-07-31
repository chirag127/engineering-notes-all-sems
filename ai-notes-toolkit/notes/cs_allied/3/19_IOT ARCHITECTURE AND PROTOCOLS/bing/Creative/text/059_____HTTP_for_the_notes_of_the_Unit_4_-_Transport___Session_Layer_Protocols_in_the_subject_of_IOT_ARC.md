### HTTP

HTTP stands for **Hypertext Transfer Protocol**. It is an **application layer protocol** in the Internet protocol suite model for **distributed, collaborative, hypermedia information systems**. It was designed for **communication between web browsers and web servers**, but it can also be used for other purposes.

Some of the main features of HTTP are:

- It is a **request-response protocol**, which means that a client sends a request to a server, and the server sends back a response to the client.
- It is a **stateless protocol**, which means that each request and response are independent and do not depend on the previous or future ones. However, stateful information can be maintained using cookies, sessions, or other mechanisms.
- It is a **text-based protocol**, which means that the messages are composed of human-readable characters. However, binary data can be transmitted using encoding schemes such as Base64 or multipart/form-data.
- It supports **multiple methods**, such as GET, POST, PUT, DELETE, etc., to perform different operations on the resources identified by Uniform Resource Identifiers (URIs).
- It supports **multiple media types**, such as HTML, XML, JSON, images, videos, etc., to represent the content of the resources. The media type is indicated by the Content-Type header in the message.
- It supports **multiple status codes**, such as 200 OK, 404 Not Found, 500 Internal Server Error, etc., to indicate the outcome of the request. The status code is indicated by the first line of the response message.
- It supports **multiple headers**, such as Host, User-Agent, Accept, Cookie, etc., to provide additional information about the request or the response. The headers are indicated by the lines following the first line of the message.
- It supports **multiple versions**, such as HTTP/1.0, HTTP/1.1, HTTP/2, etc., to introduce new features or improvements to the protocol. The version is indicated by the first line of the message.

Some of the main components of HTTP-based systems are:

- **Client**: the user-agent. The user-agent is any tool that acts on behalf of the user. This role is primarily performed by web browsers, but it can also be performed by other tools such as curl, wget, etc.
- **Server**: the web server. The web server is the software that serves the documents as requested by the clients. It can also execute scripts or programs to generate dynamic content. Some examples of web servers are Apache, Nginx, IIS, etc.
- **Proxies**: the intermediaries. The proxies are the entities that act as intermediaries between the clients and the servers. They can perform various functions such as caching, filtering, load balancing, authentication, etc. Some examples of proxies are Squid, HAProxy, Cloudflare, etc.