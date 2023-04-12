# c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol.
  - The microcontroller should have a unique IP address on the LAN and a port number for the web server to access.
  - The web server should have a script that can send HTTP requests to the microcontroller and receive HTTP responses with the bulb status.
  - The web server should also have a web page that can display the bulb status to the user using HTML and JavaScript.
  - The user should have a web browser that can access the web page on the web server using the web server's IP address and port number.

- The following diagram illustrates the components and the data flow involved in getting the status of a bulb at a remote place (on the LAN) through web:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|     Bulb        |        |  Microcontroller|        |    Web Server   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                         |     |                      |     |
       |                         |     |                      |     |
       |                         |     |                      |     |
       |<------------------------|     |                      |     |
       |  Bulb status (0 or 1)   |     |                      |     |
       |                         |     |                      |     |
       |                         |     |----------------------|     |
       |                         |     |  HTTP request        |     |
       |                         |     |  (GET /bulb_status)  |     |
       |                         |     |                      |     |
       |                         |     |<---------------------|     |
       |                         |     |  HTTP response       |     |
       |                         |     |  (200 OK, 0 or 1)    |     |
       |                         |     |                      |     |
       |                         |     |                      |     |-----------------+
       |                         |     |                      |     |                 |
       |                         |     |                      |     |    Web Browser  |
       |                         |     |                      |     |                 |
       |                         |     |                      |     +-----------------+
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |<-------------|
       |                         |     |                      |  HTTP request
       |                         |     |                      |  (GET /index.html)
       |                         |     |                      |              |
       |                         |     |                      |------------->|
       |                         |     |                      |  HTTP response
       |                         |     |                      |  (200 OK, HTML and JS)
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |
       |                         |     |                      |              |<------------|
       |                         |     |                      |              |  Bulb status
       |                         |     |                      |              |  (0 or 1)
       |                         |     |                      |              |
```

- The following code snippets show examples of the script on the web server, the web page on the web server, and the code on the microcontroller:

  - Script on the web server (PHP):

  ```php
  <?php
  // Get the IP address and port number of the microcontroller
  $ip = "192.168.1.100";
  $port = 80;

  // Create a socket and connect to the microcontroller
  $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
  socket_connect($socket, $ip, $port);

  // Send a HTTP request to get the bulb status
  $request = "

```
