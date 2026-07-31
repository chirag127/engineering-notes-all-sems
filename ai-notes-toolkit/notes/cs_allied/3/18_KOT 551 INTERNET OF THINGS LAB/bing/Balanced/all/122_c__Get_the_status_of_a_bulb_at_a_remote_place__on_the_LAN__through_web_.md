# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, we need to use a web server, a web client, and a smart bulb that can communicate over the LAN.
- A web server is a software application that handles HTTP requests and responses. It can serve static or dynamic web pages, as well as web services or APIs.
- A web client is a software application that sends HTTP requests and receives HTTP responses from a web server. It can be a web browser, a mobile app, or a command-line tool.
- A smart bulb is a device that can be controlled remotely via a wireless network, such as Wi-Fi or Bluetooth. It can change its brightness, color, or other features according to the commands received from a web server or a web client.
- To get the status of a smart bulb at a remote place, we need to follow these steps:

  - Connect the smart bulb to the same LAN as the web server and the web client. This can be done by configuring the smart bulb's network settings, such as its IP address, subnet mask, gateway, and DNS server.
  - Install and run a web server on a device that is connected to the LAN, such as a computer or a router. The web server should have a web page or a web service that can communicate with the smart bulb and display its status, such as on or off, brightness, color, etc.
  - Access the web server's web page or web service from a web client that is connected to the LAN, such as a web browser or a mobile app. The web client should send an HTTP request to the web server, and the web server should send an HTTP response with the smart bulb's status.
  - Alternatively, the web client can also communicate directly with the smart bulb, if the smart bulb has a built-in web server or a web service that can handle HTTP requests and responses. In this case, the web client should send an HTTP request to the smart bulb's IP address, and the smart bulb should send an HTTP response with its status.