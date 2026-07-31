#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb must be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller must also have a web server that can handle HTTP requests and responses.
  - The microcontroller must be assigned an IP address on the LAN, either statically or dynamically, and must be reachable from the web browser on the user's device.
  - The web browser on the user's device must send an HTTP GET request to the microcontroller's IP address, specifying the path or resource that corresponds to the bulb's status. For example, http://192.168.1.10/bulb/status.
  - The microcontroller must receive the HTTP GET request and process it according to the logic programmed on it. It must read the current state of the bulb (on or off) from the GPIO pin connected to it and send an HTTP response back to the web browser with the status information. For example, {"status": "on"} or {"status": "off"}.
  - The web browser must receive the HTTP response and display the status information to the user. The user can also send another HTTP GET request to change the state of the bulb by specifying a different path or resource. For example, http://192.168.1.10/bulb/on or http://192.168.1.10/bulb/off.