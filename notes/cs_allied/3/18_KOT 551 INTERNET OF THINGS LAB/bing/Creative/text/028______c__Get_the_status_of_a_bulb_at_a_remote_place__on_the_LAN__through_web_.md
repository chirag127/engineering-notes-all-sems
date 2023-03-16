#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol. The microcontroller should also have a sensor to detect the bulb's state (on or off).
  - The web server should have a web page that can display the bulb's status and send requests to the microcontroller to change the bulb's state. The web page should also have a refresh button to update the bulb's status periodically.
  - The user should access the web page using a web browser on a device that is connected to the same LAN as the microcontroller and the bulb. The user should be able to see the bulb's status and toggle it on or off by clicking on the web page.

- The following diagram illustrates the components and the data flow involved in this process:

```
  +----------------+        +----------------+        +----------------+
  |                |        |                |        |                |
  |     Bulb       |<------>|  Microcontroller  |<----->|    Web Server  |
  |                |        |                |        |                |
  +----------------+        +----------------+        +----------------+
                                   ^                          ^
                                   |                          |
                                   |                          |
                                   |                          |
                                   v                          v
                              +----------------+        +----------------+
                              |                |        |                |
                              |    Sensor      |        |    Web Page    |
                              |                |        |                |
                              +----------------+        +----------------+
                                                         ^
                                                         |
                                                         |
                                                         |
                                                         v
                                                   +----------------+
                                                   |                |
                                                   |    Web Browser |
                                                   |                |
                                                   +----------------+
```

- The following code snippets show an example of how to implement this functionality using Arduino and Node.js:

  - Arduino code for the microcontroller:

```c
// Include the libraries for the Ethernet shield and the sensor
#include <SPI.h>
#include <Ethernet.h>
#include <DHT.h>

// Define the pin for the sensor and the bulb
#define DHTPIN 2
#define BULBPIN 3

// Initialize the sensor
DHT dht(DHTPIN, DHT11);

// Initialize the Ethernet client
EthernetClient client;

// Define the IP address and the MAC address of the microcontroller
byte ip[] = { 192, 168, 1, 177 };
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// Define the IP address and the port of the web server
byte server[] = { 192, 168, 1, 100 };
int port = 3000;

// Define a variable to store the bulb's state
int bulbState = 0;

void setup() {
  // Initialize the serial monitor
  Serial.begin(9600);

  // Initialize the Ethernet shield
  Ethernet.begin(mac, ip);

  // Initialize the sensor
  dht.begin();

  // Initialize the bulb pin as output
  pinMode(BULBPIN, OUTPUT);

  // Turn off the bulb initially
  digitalWrite(BULBPIN, LOW);
}

void loop() {
  // Check if the client is connected to the server
  if (client.connect(server, port)) {
    // Read the sensor data
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    // Send a GET request to the server with the sensor data and the bulb state
    client.print("GET /?humidity=");
    client.print(humidity);
    client.print("&temperature=");
    client.print(temperature);
    client.print("&bulbState=");
    client.print(bulbState);
    client.println(" HTTP/1.1");
    client.println("Host: 192.168.1.100");
    client.println("Connection: close");
    client.println();

    // Wait for the server's response
    while (client.connected()) {
      // Read a line from the server
      String line = client.readStringUntil('\n');

      // Check if the line contains the command to change the bulb state
      if (line.startsWith("BULB:")) {
        // Get the new bulb state from the line
        int newBulbState = line.substring(5).toInt();

        // Check if the new bulb state is different from the current one
        if (newBulbState != bulbState) {
          // Update the bulb state
          bulbState = newBulbState;

          // Turn on or