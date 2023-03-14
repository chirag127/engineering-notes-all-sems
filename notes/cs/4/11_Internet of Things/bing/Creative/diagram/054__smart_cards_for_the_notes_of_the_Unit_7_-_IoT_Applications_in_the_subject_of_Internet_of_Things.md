### Smart cards for the notes of the Unit 7 - IoT Applications in the subject of Internet of Things

The following diagram illustrates the basic architecture of a smart card based IoT system:

```
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|     IoT device   |        |     IoT server   |        |     Smart card   |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Secure element  |        |  Authentication  |        |  Microprocessor  |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Device ID and   |        |  Session key     |        |  User ID and     |
|  encryption key  |        |  generation      |        |  encryption key  |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Device app      |        |  Device control  |        |  User app        |
|                  |        |  and data        |        |                  |
+------------------+        +------------------+        +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |------------------------|                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |------------------------|
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |

```

The diagram shows how a smart card can be used to login the user to the IoT server, which authenticates the user and generates a unique session key that enables the user to use the IoT device securely. The smart card also helps in encryption key management between the card, user and the device. The smart card has a microprocessor, some memory and some apps that can interact with the IoT device and the IoT server. The IoT device has a secure element, which is a chip that provides cryptographic functions and stores the device ID and encryption key. The IoT server has a device control and data module that can send commands and receive data from the IoT device. The device app and the user app are the software applications that run on the IoT device and the smart card respectively. They can communicate with each other and with the IoT server using the session key and the encryption key. The diagram shows the data flow between the components using arrows. The data is encrypted and decrypted using the encryption key and the session key. The smart card based IoT system provides a secure and convenient way to use IoT devices.