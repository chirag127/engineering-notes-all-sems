To program the Arduino for IoT, you need to use the Arduino IoT Cloud, which is an online platform that makes it easy for you to create, deploy and monitor IoT projects. You also need a cloud compatible board, such as the Arduino Nano 33 IoT, which has a Wi-Fi module and a crypto-chip for security. You can use the Arduino IDE or the Arduino Web Editor to write and upload code to your board. You can also use the Arduino IoT Cloud dashboard to monitor your sensor data and control your actuators.

The following diagram illustrates the basic architecture of a simple IoT device using Arduino:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Arduino Nano   |        |  Arduino IoT    |        |  Smartphone or  |
|  33 IoT Board   |  Wi-Fi |  Cloud Platform |  Wi-Fi |  PC Browser     |
|                 | <----> |                 | <----> |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Sensor         |        |  Dashboard      |        |  Dashboard      |
|  (e.g. button)  | -----> |  (e.g. chart)   | -----> |  (e.g. chart)   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Actuator       |        |  Variable       |        |  Variable       |
|  (e.g. LED)     | <----- |  (e.g. switch)  | <----- |  (e.g. switch)  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```