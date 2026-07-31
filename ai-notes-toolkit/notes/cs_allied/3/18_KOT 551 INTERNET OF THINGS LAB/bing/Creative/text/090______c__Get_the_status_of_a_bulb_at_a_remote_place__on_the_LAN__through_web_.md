#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol. The microcontroller should also have a sensor to detect the bulb's state (on or off).
  - The web server should have a web page that can display the bulb's status and allow the user to control it. The web page should also have a script that can send and receive HTTP requests to the microcontroller.
  - The user should access the web page using a web browser on a device that is connected to the same LAN as the bulb and the web server. The user should also have the IP address or the hostname of the web server.
  - The web page should send a GET request to the microcontroller to get the bulb's status. The microcontroller should respond with a JSON object that contains the bulb's state and other information.
  - The web page should parse the JSON object and display the bulb's status on the web page. The web page should also update the bulb's status periodically by sending GET requests to the microcontroller at regular intervals.
  - The user should be able to toggle the bulb's state by clicking a button on the web page. The web page should send a POST request to the microcontroller with the desired state of the bulb. The microcontroller should change the bulb's state accordingly and send a confirmation message to the web page. The web page should update the bulb's status accordingly.