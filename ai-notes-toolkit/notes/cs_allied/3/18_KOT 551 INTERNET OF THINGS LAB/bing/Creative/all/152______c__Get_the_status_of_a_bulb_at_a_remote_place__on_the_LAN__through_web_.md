# c) Get the status of a bulb at a remote place (on the LAN) through web.

To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

- The bulb should be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller should also have a web server that can handle HTTP requests and responses.
- The microcontroller should be able to read the state of the bulb (on or off) using a digital input pin or a sensor, and store it in a variable or a memory location.
- The web server should be able to serve a web page that displays the status of the bulb, and also allows the user to change the status of the bulb by sending an HTTP request to the microcontroller.
- The user should be able to access the web page using a web browser on a device that is connected to the same LAN as the microcontroller. The user should enter the IP address or the hostname of the microcontroller in the web browser's address bar, and then view the web page.
- The web page should show the current status of the bulb (on or off) using a text or an image, and also provide a button or a link that allows the user to toggle the status of the bulb. When the user clicks on the button or the link, the web browser should send an HTTP request to the microcontroller with a parameter that indicates the desired status of the bulb.
- The microcontroller should receive the HTTP request from the web browser, and parse the parameter to determine the desired status of the bulb. The microcontroller should then change the state of the bulb (on or off) using a digital output pin or a relay, and update the variable or the memory location that stores the status of the bulb.
- The microcontroller should also send an HTTP response to the web browser, confirming the change of the status of the bulb, and refreshing the web page to show the updated status of the bulb.