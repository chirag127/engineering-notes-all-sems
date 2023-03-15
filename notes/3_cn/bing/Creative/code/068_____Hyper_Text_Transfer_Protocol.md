### Hyper Text Transfer Protocol

Hyper Text Transfer Protocol (HTTP) is a protocol that defines how messages are formatted and transmitted over the World Wide Web. It also specifies what actions web servers and browsers should take in response to various commands.

HTTP is based on a request-response model, where a client (such as a web browser) sends a request to a server (such as a web server) and the server sends back a response. The request and response messages consist of a start-line, zero or more header fields, an empty line, and an optional message body.

The start-line of a request message has the following syntax:

```
method SP request-target SP HTTP-version CRLF
```

where `method` is the HTTP method (such as GET, POST, PUT, DELETE, etc.), `request-target` is the identifier of the resource being requested (such as a URL), `HTTP-version` is the version of the HTTP protocol (such as HTTP/1.1), `SP` is a space character, and `CRLF` is a carriage return and line feed character.

The start-line of a response message has the following syntax:

```
HTTP-version SP status-code SP reason-phrase CRLF
```

where `HTTP-version` is the version of the HTTP protocol, `status-code` is a three-digit number that indicates the outcome of the request (such as 200 for OK, 404 for Not Found, 500 for Internal Server Error, etc.), `reason-phrase` is a short textual description of the status code, and `CRLF` is a carriage return and line feed character.

The header fields of a message provide additional information about the request or response, such as the content type, the content length, the date, the server name, the cookies, etc. Each header field consists of a field name, a colon, and a field value, followed by a CRLF. For example:

```
Content-Type: text/html
Content-Length: 1024
Date: Wed, 15 Mar 2023 13:55:50 GMT
Server: Apache
```

The message body of a message contains the actual data being transferred, such as the HTML document, the image, the form data, etc. The message body is optional and may be absent in some cases, such as a HEAD request or a 204 No Content response. The message body is separated from the header fields by an empty line (CRLF).

Here is an example of a HTTP request message:

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: name=John

```

Here is an example of a HTTP response message:

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024
Date: Wed, 15 Mar 2023 13:55:50 GMT
Server: Apache

<html>
<head>
<title>Example Page</title>
</head>
<body>
<h1>Welcome to Example.com</h1>
<p>This is a sample web page.</p>
</body>
</html>
```