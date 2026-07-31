 Here is the formal content in markdown format without emojis or external links:

# Get Status of Remote Bulb over LAN via Web

1. Requirements
- Remote bulb connected to a microcontroller
- Microcontroller connected to LAN
- Web server running on microcontroller

2. Steps
a. Microcontroller reads the status of the bulb (on/off)
b. Status is sent to the web server running on the microcontroller
c. The web server hosts a web page which displays the status of the bulb
d. We can access the web page over the LAN to see the status of the bulb

3. Implementation
- Microcontroller: Arduino/ESP8266/ESP32, etc.
- Programming: C/C++, Python, etc.
- Web server: Built-in (ESP8266/ESP32) or external (Arduino + Ethernet shield)
- Web page: HTML/JavaScript to display the status

The status of a bulb at a remote place on the LAN can be accessed through a web page by implementing the above steps. The microcontroller readings are sent to the web server which displays the status on a web page. The web page can be accessed over the local network to view the remote bulb status.