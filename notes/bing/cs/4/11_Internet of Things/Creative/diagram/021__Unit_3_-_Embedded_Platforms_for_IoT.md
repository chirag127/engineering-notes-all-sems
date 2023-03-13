## Unit 3 - Embedded Platforms for IoT

Embedded platforms for IoT are hardware and software systems that enable IoT devices to communicate, process data, and perform specific functions. Embedded platforms for IoT can vary in complexity, size, power, and features, depending on the application and device requirements. Some examples of embedded platforms for IoT are Mbed OS, Amazon FreeRTOS, AMD Ryzen Embedded, and Azure IoT.

The following diagram illustrates the basic architecture of a typical embedded platform for IoT using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|     Sensors     |       |   Microcontroller   |       |    Actuators    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                         |                         |
                         |                         |
                         v                         v
+---------------------------------------------------------+
|                                                         |
|                   Embedded Software                     |
|                                                         |
+---------------------------------------------------------+
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                         |                         |
                         |                         |
                         v                         v
+---------------------------------------------------------+
|                                                         |
|                   Communication Module                   |
|                                                         |
+---------------------------------------------------------+
                         |
                         |
                         v
+---------------------------------------------------------+
|                                                         |
|                      IoT Network                        |
|                                                         |
+---------------------------------------------------------+
                         |
                         |
                         v
+---------------------------------------------------------+
|                                                         |
|                      IoT Platform                       |
|                                                         |
+---------------------------------------------------------+
```