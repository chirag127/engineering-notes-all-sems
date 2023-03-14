## Unit 1 - Internet of Things (IoT)

The Internet of Things (IoT) is a network of physical devices (so-called “things”) that collect and exchange data with other devices and systems over the internet.   The architecture of an IoT system is a key consideration when designing and implementing IoT solutions. IoT architecture can be broken down into four layers: Device layer, Network layer, Data processing layer, and Application layer.    

The following diagram illustrates the basic architecture of an IoT system using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Application    |     |  Data processing|     |  Network        |     |  Device         |
|  Layer          |     |  Layer          |     |  Layer          |     |  Layer          |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  User interface |     |  Data analytics |     |  Internet       |     |  Sensors        |
|  and control    |     |  and machine    |     |  protocols      |     |  and actuators  |
|                 |     |  learning       |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Mobile apps    |     |  Data lake      |     |  WiFi           |     |  Embedded       |
|  Web portals    |     |  Data management|     |  Bluetooth      |     |  systems        |
|                 |     |  systems        |     |  Zigbee         |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  User           |     |  Data           |     |  Network        |     |  Device         |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
       ^                    ^                    ^                    ^
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       +--------------------+--------------------+--------------------+
                             IoT System
```