# c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller should also have a web server that can handle HTTP requests and responses.
  - The microcontroller should be able to read the state of the bulb (on or off) using a digital input pin or a sensor, and store it in a variable or a memory location.
  - The web server should be able to serve a web page that can display the status of the bulb using HTML and JavaScript. The web page should also have a refresh button that can send an HTTP GET request to the microcontroller to update the status of the bulb.
  - The user should be able to access the web page using a web browser on a device that is connected to the same LAN as the microcontroller. The user should enter the IP address or the hostname of the microcontroller in the web browser's address bar, and the web page should load and show the status of the bulb.
  - The user should be able to click the refresh button on the web page to send an HTTP GET request to the microcontroller, and the web page should update the status of the bulb accordingly.

- The following diagram illustrates the process of getting the status of a bulb at a remote place (on the LAN) through web:

```
  +-----------------+       +-----------------+       +-----------------+
  |                 |       |                 |       |                 |
  |     Bulb        |       |  Microcontroller|       |     User        |
  |                 |       |                 |       |                 |
  +-----------------+       +-----------------+       +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |<------------------------| HTTP GET request
        |                         |                         | (web page)
        |                         |------------------------>| HTTP response
        |                         |                         | (web page)
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |<------------------------| HTTP GET request
        |                         |                         | (refresh button)
        |                         |------------------------>| HTTP response
        |                         |                         | (bulb status)
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |<------------------------| Read bulb status        |
        |                         |                         |
        |------------------------>| Store bulb status       |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
```