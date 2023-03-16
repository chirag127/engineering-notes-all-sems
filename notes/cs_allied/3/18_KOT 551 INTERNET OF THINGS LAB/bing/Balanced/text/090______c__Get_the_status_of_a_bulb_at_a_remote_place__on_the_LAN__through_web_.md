#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol.
  - The microcontroller should have a unique IP address on the LAN and a port number for the web server to access.
  - The web server should have a script that can handle the HTTP requests from the microcontroller and send back the appropriate responses.
  - The web browser on the user's device should be able to send HTTP requests to the web server using the IP address and port number of the microcontroller.
  - The web browser should also be able to display the status of the bulb based on the HTTP responses from the web server.

- The following diagram illustrates the process of getting the status of a bulb at a remote place (on the LAN) through web:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Web Browser    |        |  Web Server     |        |  Microcontroller|
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                         |                         |
       |  HTTP request          |                         |
       |----------------------->|                         |
       |                         |                         |
       |                         |  HTTP request          |
       |                         |----------------------->|
       |                         |                         |
       |                         |  HTTP response         |
       |                         |<-----------------------|
       |                         |                         |
       |  HTTP response         |                         |
       |<-----------------------|                         |
       |                         |                         |
       |  Display status        |                         |
       |----------------------->|                         |
       |                         |                         |
```