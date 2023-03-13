The following diagram illustrates the basic architecture of a programming the arduino for IoT in ASCII art:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Arduino IDE   |        |  Arduino IoT   |        |  Arduino IoT   |
|                |        |  Cloud Agent   |        |  Cloud Platform|
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Arduino       |        |  WiFi Module   |        |  Cloud Server  |
|  Board         |        |  (e.g. ESP8266)|        |  (e.g. AWS)    |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
```

The diagram shows the following steps:

1. The Arduino IDE is used to write and upload the code to the Arduino board using C++ language.
2. The Arduino board is connected to a WiFi module (e.g. ESP8266) that enables the communication with the Arduino IoT Cloud Agent.
3. The Arduino IoT Cloud Agent is a plugin that runs on the user's computer and acts as a bridge between the Arduino board and the Arduino IoT Cloud Platform.
4. The Arduino IoT Cloud Platform is a web-based service that allows the user to create, manage and monitor their IoT devices from anywhere in the world.
5. The Arduino IoT Cloud Platform communicates with the cloud server (e.g. AWS) that hosts the data and the logic of the IoT application.