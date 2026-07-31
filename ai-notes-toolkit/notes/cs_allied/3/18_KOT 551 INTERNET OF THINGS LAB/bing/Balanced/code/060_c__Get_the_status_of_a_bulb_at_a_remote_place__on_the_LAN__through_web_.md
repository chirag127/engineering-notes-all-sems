# Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, one needs to have a web server, a web client, and a smart bulb that can communicate with the web server.
- A web server is a software application that handles HTTP requests and responses over the network. It can serve static or dynamic web pages, as well as web services or APIs.
- A web client is a software application that sends HTTP requests and receives HTTP responses from the web server. It can be a web browser, a mobile app, or a command-line tool.
- A smart bulb is a device that can be controlled remotely through the internet or a local network. It can have different features, such as changing color, brightness, or schedule.
- To get the status of a smart bulb at a remote place, the following steps are required:

  - The web client sends an HTTP GET request to the web server, specifying the IP address or hostname of the smart bulb and the status parameter (such as on/off, color, brightness, etc.).
  - The web server receives the HTTP GET request and forwards it to the smart bulb using a protocol such as MQTT, CoAP, or HTTP.
  - The smart bulb receives the request and sends back the status information to the web server using the same protocol.
  - The web server receives the status information and sends back an HTTP response to the web client, containing the status information in a format such as JSON, XML, or plain text.
  - The web client receives the HTTP response and displays the status information to the user.

Some examples of HTTP GET requests and responses are:

- Request: `http://webserver.com/bulb1/status`
- Response: `{"on":true,"color":"red","brightness":80}`

- Request: `http://webserver.com/bulb2/status`
- Response: `{"on":false}`

- Request: `http://webserver.com/bulb3/status`
- Response: `{"on":true,"color":"blue","brightness":50,"schedule":"8:00-22:00"}`