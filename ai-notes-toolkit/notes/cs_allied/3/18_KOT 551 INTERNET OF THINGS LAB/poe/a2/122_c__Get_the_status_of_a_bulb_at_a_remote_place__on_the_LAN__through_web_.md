 Here is the content in markdown format without any emojis or external links:

# Get the status of a bulb at a remote place (on the LAN) through web

1. Install a web server on a computer connected to the same LAN as the bulb. This web server will display the status of the bulb.
2. Connect the bulb to an Arduino board. The Arduino board will detect the on/off status of the bulb and send this data to the web server.
3. Write a program for the Arduino board to sense the status of the bulb. If the bulb is on, the Arduino will send a signal to the web server that the bulb status is 'on'. If the bulb is off, the Arduino will send a signal to the web server that the bulb status is 'off'.
4. Write a web page on the web server to display the status of the bulb. The web page will receive data from the Arduino about the bulb status and display 'Bulb is on' or 'Bulb is off' depending on the received data.
5. Access the web page from any device on the same LAN to see the status of the bulb at the remote location.

The steps to achieve this are:
1. Setup the hardware - Connect the bulb and Arduino
2. Program the Arduino to sense bulb status and send to web server
3. Setup the web server and write web page to display bulb status
4. Access the web page from a remote device to get bulb status

This allows getting the status of a bulb at a remote location on the same local network through a web page. The status is sensed by the Arduino board and sent to the web server which displays it on a web page.