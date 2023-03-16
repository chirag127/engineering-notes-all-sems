# ZWave

ZWave is a wireless communication protocol designed for smart home and IoT devices. It operates on the low-frequency 800 to 900 MHz band, which avoids interference with the 2.4 GHz band where Wi-Fi and Bluetooth operate. ZWave supports encryption, mesh networking, low power consumption, and interoperability among different vendors.

Some of the features and characteristics of ZWave are:

- It was developed by Zensys, a Danish company, in 1999.
- It is a proprietary protocol owned by Sigma Designs, Inc. An open source implementation of ZWave protocol stack, called open-zwave, is also available but it does not support security layer.
- It uses frequency shift keying (FSK) modulation and Gaussian frequency shift keying (GFSK) for data transmission.
- It supports up to 232 nodes per network and up to four hops between the source and the destination.
- It has a data rate of 9.6 kbps, 40 kbps, or 100 kbps depending on the region and the device class.
- It has a range of up to 100 meters in line of sight and up to 30 meters indoors.
- It supports three types of devices: controllers, slaves, and routing slaves. Controllers initiate and manage the communication, slaves respond to the commands from the controllers, and routing slaves act as repeaters and routers for the messages.
- It uses a source-routed protocol, which means that the controller specifies the route for each message. The route can be updated dynamically based on the network topology and the availability of the nodes.
- It supports two types of network topologies: star and mesh. In star topology, all the devices communicate directly with the controller. In mesh topology, the devices can communicate with each other and relay the messages for other devices.
- It supports encryption based on AES-128 algorithm. The encryption keys are exchanged during the network inclusion process, which is initiated by the controller.
- It supports interoperability among different vendors and devices through the ZWave Alliance, which is a consortium of companies that adhere to the ZWave certification program. The certification ensures that the devices comply with the ZWave protocol and can work together seamlessly  .