### Hyper Text Transfer Protocol

Hyper Text Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access, for example by a mouse click or by tapping the screen in a web browser.

Here is an example of a simple HTTP request and response:

```
GET / HTTP/1.1
Host: www.example.com

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```

In this example, the client sends an HTTP GET request to the server, asking for the root document (`/`) of the website `www.example.com`. The server responds with an HTTP response, indicating that the request was successful (`200 OK`) and providing the requested document in the response body.
