#### c) Get the status of a bulb at a remote place (on the LAN) through web.

To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

- The bulb must be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller must also have a web server that can handle HTTP requests and responses.
- The microcontroller must be assigned an IP address on the LAN, either statically or dynamically, and must be reachable from the web browser of the user who wants to get the status of the bulb.
- The web server on the microcontroller must have a web page that can display the status of the bulb, either as text or as an image. The web page must also have a URL that can be accessed by the web browser of the user.
- The user must enter the URL of the web page on the web browser and send a HTTP GET request to the web server on the microcontroller. The web server must respond with the web page that shows the status of the bulb.
- The user must view the web page on the web browser and see the status of the bulb.

The following diagram illustrates the process of getting the status of a bulb at a remote place (on the LAN) through web:

```
+----------------+        +-----------------+        +-----------------+
|                |        |                 |        |                 |
|  Web Browser   |        |      LAN        |        |  Microcontroller|
|                |        |                 |        |                 |
+----------------+        +-----------------+        +-----------------+
       |                          |                          |
       | HTTP GET request        |                          |
       |------------------------>|                          |
       |                          |                          |
       |                          | HTTP GET request         |
       |                          |------------------------->|
       |                          |                          |
       |                          | HTTP response            |
       |                          |<-------------------------|
       |                          |                          |
       | HTTP response           |                          |
       |<------------------------|                          |
       |                          |                          |
       |                          |                          |
       V                          V                          V
+----------------+        +-----------------+        +-----------------+
|                |        |                 |        |                 |
|  Web Page      |        |      LAN        |        |  Bulb           |
|  (Status of    |        |                 |        |                 |
|   Bulb)        |        +-----------------+        +-----------------+
|                |
+----------------+
```