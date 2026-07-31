### Cookies in Servlets

Here is an ASCII diagram that shows how cookies work in servlets:

```
  +--------+       +------------+       +--------+
  | Client |       | Web Server |       | Servlet|
  +--------+       +------------+       +--------+
      |                   |                   |
      |--- Request -----> |                   |
      |                   |                   |
      |                   |--- Request -----> |
      |                   |                   |
      |                   |<-- Set-Cookie --- |
      |                   |                   |
      |<-- Set-Cookie --- |                   |
      |                   |                   |
      |--- Cookie ------> |                   |
      |                   |                   |
      |                   |--- Cookie ------> |
      |                   |                   |
      |                   |<-- Response ----- |
      |                   |                   |
      |<-- Response ----- |                   |
      |                   |                   |
```

In this diagram, the client sends a request to the web server. The web server forwards the request to the servlet. The servlet sends a `Set-Cookie` header back to the web server, which forwards it to the client. The client stores the cookie and sends it back to the web server with subsequent requests. The web server forwards the cookie to the servlet, which can use it to maintain state information about the client. Finally, the servlet sends a response back to the web server, which forwards it to the client.
