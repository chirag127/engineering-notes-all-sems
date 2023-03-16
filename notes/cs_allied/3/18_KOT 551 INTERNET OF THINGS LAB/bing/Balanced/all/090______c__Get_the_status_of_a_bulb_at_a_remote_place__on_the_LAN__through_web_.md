#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol.
  - The microcontroller should have a unique IP address on the LAN and a port number for the web server to access.
  - The web server should have a script that can handle the HTTP requests from the microcontroller and send back the appropriate responses.
  - The web browser on the user's device should send an HTTP GET request to the web server with the IP address and port number of the microcontroller as the URL.
  - The web server should forward the request to the microcontroller and wait for its response.
  - The microcontroller should read the status of the bulb (on or off) from its GPIO pin and send it back to the web server as an HTTP response.
  - The web server should relay the response to the web browser and display the status of the bulb on the user's device.

- The following diagram illustrates the process:

```
  +----------------+        +----------------+        +----------------+
  |                |        |                |        |                |
  |  Web Browser   |        |   Web Server   |        | Microcontroller|
  |                |        |                |        |                |
  +----------------+        +----------------+        +----------------+
       |   ^                      |    ^                    |    ^
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       v   |                      v    |                    v    |
  GET /192.168.1.100:8080  |  GET /192.168.1.100:8080  |  Read GPIO pin
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   |                      |    v                    |    v
       |   |                      |  HTTP response          |  HTTP response
       |   |                      |  (bulb status)          |  (bulb status)
       |   |                      |    |                    |    |
       |   |                      |    |                    |    |
       |   v                      |    v                    |    |
       |  HTTP response           |  HTTP response          |
       |  (bulb status)           |  (bulb status)          |
       |   |                      |    |                    |
       |   |                      |    |                    |
       |   v                      |    v                    |
       |  Display bulb status     |  Display bulb status    |
       |   |                      |    |                    |
       |   |                      |    |                    |
       |   v                      |    v                    |
  +----------------+        +----------------+        +----------------+
  |                |        |                |        |                |
  |  Web Browser   |        |   Web Server   |        | Microcontroller|
  |                |        |                |        |                |
  +----------------+        +----------------+        +----------------+
```