#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller should also have a web server that can handle HTTP requests and responses.
  - The microcontroller should be able to read the state of the bulb (on or off) using a digital input pin or a sensor, and store it in a variable or a memory location.
  - The microcontroller should be able to send the state of the bulb as a response to a HTTP GET request from a web client, such as a browser or an app. The response can be in plain text, JSON, XML, or any other format that the web client can parse.
  - The web client should be able to send a HTTP GET request to the microcontroller's IP address and port number, using the appropriate URL and query parameters. The web client should also be able to receive and display the response from the microcontroller, showing the status of the bulb.
  - The web client and the microcontroller should be on the same LAN, or connected through a router or a gateway that can forward the HTTP packets between them. The web client should also know the IP address and port number of the microcontroller, or use a service discovery protocol such as mDNS or UPnP to find them.