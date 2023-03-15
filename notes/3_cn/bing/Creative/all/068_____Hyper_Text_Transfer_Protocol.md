### Hyper Text Transfer Protocol

- Hyper Text Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML .
- HTTP is the underlying protocol used by the World Wide Web, developed by Tim Berners-Lee .
- HTTP defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands .
- HTTP is a stateless protocol, meaning that each request is independent of the previous one and the server does not keep track of the client's state .
- HTTP uses a client-server model, where the client initiates a request and the server responds with a response .
- HTTP requests and responses consist of a start-line, zero or more headers, an empty line, and an optional message body .
- The start-line of a request contains the method, the URI, and the HTTP version, such as `GET /index.html HTTP/1.1` .
- The start-line of a response contains the HTTP version, the status code, and the reason phrase, such as `HTTP/1.1 200 OK` .
- The headers provide additional information about the request or the response, such as the content type, the content length, the date, the server name, etc .
- The message body contains the actual data of the request or the response, such as the HTML document, the image, the JSON data, etc .
- HTTP supports different methods for different purposes, such as GET, POST, PUT, DELETE, HEAD, OPTIONS, etc .
- HTTP supports different status codes for different outcomes, such as 200 for success, 404 for not found, 500 for internal server error, etc .
- HTTP can be extended with new headers, methods, status codes, and media types, as long as they follow the syntax and semantics of the protocol .
- HTTP can be secured with HTTPS, which uses SSL/TLS to encrypt the communication between the client and the server .

#### Mnemonics and learning tricks

- To remember the structure of an HTTP request or response, you can use the acronym SLHM (Start-line, Headers, empty Line, Message body).
- To remember the common HTTP methods, you can use the acronym GPOD (GET, POST, PUT, DELETE).
- To remember the common HTTP status codes, you can use the following phrases:
  - 1xx: Informational (I need more information)
  - 2xx: Success (You did it!)
  - 3xx: Redirection (Go somewhere else)
  - 4xx: Client error (You messed up)
  - 5xx: Server error (I messed up)

#### Examples

- An example of an HTTP request:

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

- An example of an HTTP response:

```
HTTP/1.1 200 OK
Date: Wed, 15 Mar 2023 13:55:49 GMT
Server: Apache
Content-Type: text/html
Content-Length: 1234

<html>
<head>
<title>Example Page</title>
</head>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```

#### Advantages

- HTTP is simple and easy to implement .
- HTTP is flexible and extensible .
- HTTP is widely supported by browsers, servers, and proxies .
- HTTP is compatible with different media types and formats .

#### Disadvantages

- HTTP is stateless, meaning that it cannot maintain the context or the history of the communication .
- HTTP is insecure, meaning that it can be intercepted, modified, or spoofed by attackers .
- HTTP is inefficient, meaning that