Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of IOT based Manhole Detection and Monitoring System for the Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB.

### IOT based Manhole Detection and Monitoring System

- A drainage monitoring system plays a significant role in keeping towns and cities healthy and clean  .
- Most of the manholes are open without any observations that cause accidents . In India, many cities adopted emptying underground system because it is vital.
- IOT based Manhole Detection and Monitoring System is a low-cost, low-maintenance, real-time system that alerts the managing station through messages when any manhole crosses its threshold values .
- This system reduces the death risk of manual scavengers who clean the underground drainage and also benefits the public .
- The system makes use of IOT to create a drainage monitoring system in an extremely high automotive by using sensors to detect and send alerts to authorities via GSM and GPS module .
- The system also monitors the water flow rate at node junctions to identify drainage water blockage.
- The system consists of Arduino, ultrasonic sensor, water flow sensor, GSM module, GPS module, buzzer, LCD display and power supply  .
- The ultrasonic sensor is used to measure the distance between the manhole cover and the water level  .
- The water flow sensor is used to measure the rate of water flow in the drainage pipes .
- The GSM module is used to send SMS alerts to the authorities with the location of the manhole  .
- The GPS module is used to get the coordinates of the manhole  .
- The buzzer is used to produce an audible alarm when the manhole is open or the water level is high  .
- The LCD display is used to show the status of the manhole and the water level  .
- The power supply is used to provide the required voltage to the system  .

The following diagram shows the block diagram of the system:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Ultrasonic    |       |  Water flow    |       |  GSM and GPS   |
|  sensor        +------>+  sensor        +------>+  module        +------> SMS alert
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
     |                                                    |
     |                                                    |
     v                                                    v
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Arduino       |       |  Buzzer        |       |  LCD display   |
|  controller    +------>+                +------>+                |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
     |
     |
     v
+----------------+
|                |
|  Power supply  |
|                |
+----------------+
```