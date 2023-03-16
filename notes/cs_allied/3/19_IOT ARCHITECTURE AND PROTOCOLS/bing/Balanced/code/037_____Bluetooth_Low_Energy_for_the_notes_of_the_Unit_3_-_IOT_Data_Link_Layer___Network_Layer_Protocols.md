### Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or proximity detection, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 connections simultaneously, while classic Bluetooth devices are limited to 7 connections.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices. GAP also defines the roles of devices, such as peripheral (device that advertises and provides data) and central (device that scans and consumes data).
  - GATT defines how devices exchange data using services, characteristics, and descriptors. GATT also defines the roles of devices, such as server (device that provides data) and client (device that requests data).
- BLE devices can operate in different modes, such as broadcast, connection, or mesh.
  - Broadcast mode: A device sends data to all nearby devices without establishing a connection. This mode is useful for applications such as beacons, which provide location or contextual information to nearby devices.
  - Connection mode: A device establishes a connection with another device and exchanges data using GATT. This mode is useful for applications such as fitness trackers, which provide biometric data to a smartphone or a smartwatch.
  - Mesh mode: A device connects with multiple devices and relays data between them. This mode is useful for applications such as smart home, which allow devices to communicate with each other and with a gateway device.