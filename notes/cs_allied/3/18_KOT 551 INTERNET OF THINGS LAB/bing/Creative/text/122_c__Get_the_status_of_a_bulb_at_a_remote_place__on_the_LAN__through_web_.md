# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, we need to have the following components:
  - A bulb that can be controlled by a microcontroller such as Arduino or Raspberry Pi.
  - A microcontroller that can connect to the LAN and run a web server.
  - A device that can access the web server and send requests to the microcontroller.
- The steps to get the status of a bulb are as follows:
  - Connect the bulb to the microcontroller using a relay or a transistor circuit.
  - Connect the microcontroller to the LAN using an Ethernet shield or a Wi-Fi module.
  - Write a sketch or a program for the microcontroller that can read the state of the bulb (on or off) and send it as a response to a web request.
  - Upload the sketch or the program to the microcontroller and run it.
  - Find the IP address of the microcontroller on the LAN using a network scanner or a ping command.
  - On the device that can access the web server, open a web browser and enter the IP address of the microcontroller followed by a slash and a query parameter, such as `http://192.168.1.10/?status`.
  - The web browser will send a request to the microcontroller and receive a response that contains the status of the bulb, such as `ON` or `OFF`.
  - Display the status of the bulb on the web browser.