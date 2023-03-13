### Hyper Text Transfer Protocol

- Hyper Text Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML .
- HTTP is the underlying protocol used by the World Wide Web, developed by Tim Berners-Lee .
- HTTP defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands .
- HTTP is a stateless protocol, which means that each request is independent of the previous ones and the server does not keep track of the client's state .
- HTTP uses a client-server model, where the client initiates a request and the server responds with a response .
- HTTP requests and responses consist of a start-line, zero or more headers, an empty line, and an optional message body .
- The start-line of a request contains the method, the request-target, and the HTTP version . For example:

```
GET /index.html HTTP/1.1
```

- The start-line of a response contains the HTTP version, the status code, and the reason phrase . For example:

```
HTTP/1.1 200 OK
```

- The headers provide additional information about the request or the response, such as the content type, the content length, the date, the server name, etc . For example:

```
Content-Type: text/html
Content-Length: 1234
Date: Mon, 13 Mar 2023 12:48:03 GMT
Server: Apache
```

- The message body contains the actual data that is being transferred, such as the HTML document, the image, the JSON object, etc . For example:

```
<html>
<head>
<title>Example</title>
</head>
<body>
<h1>Hello, world!</h1>
</body>
</html>
```

- HTTP supports different methods for different purposes, such as GET, POST, PUT, DELETE, etc .
- GET is used to retrieve a resource from the server, such as a web page or an image .
- POST is used to send data to the server, such as a form submission or a file upload .
- PUT is used to update or create a resource on the server, such as a new document or a modified image .
- DELETE is used to delete a resource from the server, such as a document or an image .
- HTTP supports different status codes to indicate the outcome of a request, such as 200, 404, 500, etc .
- 200 means OK, which means that the request was successful and the response contains the requested resource .
- 404 means Not Found, which means that the request was unsuccessful and the server could not find the requested resource .
- 500 means Internal Server Error, which means that the request was unsuccessful and the server encountered an unexpected error .
- HTTP can be secured by using HTTPS, which is HTTP over TLS (Transport Layer Security) .
- HTTPS encrypts the communication between the client and the server, preventing eavesdropping, tampering, and impersonation .
- HTTPS uses certificates to verify the identity of the server and the client, ensuring that they are who they claim to be .
- HTTPS requires a valid certificate from a trusted authority, such as Let's Encrypt, VeriSign, or Comodo .

Some mnemonics and learning tricks for HTTP are:

- HTTP stands for Hyper Text Transfer Protocol, which can be remembered as **H**ow **T**o **T**ransfer **P**ages.
- HTTP methods can be remembered as **G**et **P**ost **P**ut **D**elete, which can be pronounced as **G**i**P****P**y **D**oo.
-