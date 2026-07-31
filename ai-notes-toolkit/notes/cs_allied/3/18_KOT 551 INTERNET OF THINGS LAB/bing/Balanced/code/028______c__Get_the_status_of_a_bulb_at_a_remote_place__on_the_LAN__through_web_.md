#### c) Get the status of a bulb at a remote place (on the LAN) through web.

To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

- The bulb must be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller must also have a web server that can handle HTTP requests and responses.
- The microcontroller must be assigned an IP address on the LAN, either statically or dynamically, and must be reachable from the web browser of the user who wants to get the status of the bulb.
- The web server on the microcontroller must have a web page that can display the status of the bulb, either as text or as an image. The web page must also have a URL that can be accessed by the web browser of the user.
- The user must enter the URL of the web page on the web browser and send a HTTP GET request to the web server on the microcontroller. The web server must respond with a HTTP OK message and the web page that shows the status of the bulb.
- The user must view the web page on the web browser and see the status of the bulb. The user can also refresh the web page to get the updated status of the bulb.

Some of the advantages of this method are:

- It is simple and does not require any additional hardware or software apart from the microcontroller, the bulb, and the web browser.
- It is flexible and can be used for any device that can be controlled by a microcontroller and has a web server.
- It is scalable and can be used for multiple devices on the same LAN by assigning different IP addresses and URLs to each device.

Some of the disadvantages of this method are:

- It is dependent on the LAN and the web server on the microcontroller. If the LAN is down or the web server is not working, the user cannot get the status of the bulb.
- It is not secure and can be accessed by anyone who knows the IP address and the URL of the web server on the microcontroller. The user cannot authenticate or encrypt the communication between the web browser and the web server.
- It is not efficient and consumes more bandwidth and power than other methods that use protocols such as MQTT or CoAP. The user has to send a HTTP GET request and receive a HTTP OK message and a web page for every status update.