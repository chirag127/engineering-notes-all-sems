### Building peer to peer communication system using Bluetooth &WiFi

- Peer to peer (P2P) communication system is a network of devices that can communicate directly with each other without relying on any central server or infrastructure.
- P2P communication system can be useful for applications that require low latency, high reliability, or privacy, such as file sharing, gaming, or emergency response.
- Bluetooth and WiFi are two wireless technologies that can enable P2P communication system using the existing hardware in smartphones, laptops, or other devices.
- Bluetooth is a short-range wireless technology that can connect devices within 10 meters (33 feet) of each other. Bluetooth can support P2P streaming audio, data transfer, or device discovery applications.
- WiFi is a medium-range wireless technology that can connect devices within 100 meters (328 feet) of each other. WiFi can support P2P data transfer, video streaming, or device discovery applications.
- Bluetooth and WiFi have different advantages and disadvantages for P2P communication system, such as:

| Bluetooth | WiFi |
| --- | --- |
| + Low power consumption | + High data rate |
| + Easy pairing | + Wide coverage |
| - Low data rate | - High power consumption |
| - Limited range | - Complex security |

- To build a P2P communication system using Bluetooth and WiFi, the following steps are required:

  1. Enable the Bluetooth and WiFi antennas on the devices that want to communicate.
  2. Discover the nearby devices that support P2P communication using Bluetooth or WiFi Direct protocols.
  3. Establish a connection between the devices using Bluetooth or WiFi Direct protocols.
  4. Exchange data between the devices using Bluetooth or WiFi sockets or streams.
  5. Close the connection when the communication is finished.

- To implement a P2P communication system using Bluetooth and WiFi, the following tools and frameworks can be used:

  - For Android devices, the Android SDK provides the classes and methods for Bluetooth and WiFi Direct APIs, such as BluetoothAdapter, BluetoothDevice, BluetoothSocket, WifiP2pManager, WifiP2pDevice, WifiP2pConfig, and WifiP2pSocket.
  - For iOS devices, the iOS SDK provides the classes and methods for Bluetooth and WiFi Direct APIs, such as CBPeripheralManager, CBPeripheral, CBCharacteristic, CBService, MCSession, MCPeerID, MCBrowserViewController, and MCAdvertiserAssistant.
  - For cross-platform devices, there are some third-party libraries and frameworks that can support Bluetooth and WiFi Direct APIs, such as Bridgefy, FireChat, Nearby, or AllJoyn.