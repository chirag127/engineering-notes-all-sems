# Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or using a proximity-based technique, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 connections simultaneously, while classic Bluetooth devices are limited to 7.
  - More flexibility: BLE devices can use a variety of profiles and services to communicate, while classic Bluetooth devices are restricted to predefined profiles.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices. GAP also defines the roles and modes of devices, such as peripheral, central, broadcaster, and observer.
  - GATT defines how devices exchange data using services and characteristics. GATT also defines the procedures and formats for data transmission, such as read, write, notify, and indicate.
- BLE devices can operate in different modes depending on their roles and capabilities:
  - Peripheral mode: A device that advertises itself and provides data or services to other devices. For example, a heart rate monitor, a smartwatch, or a beacon.
  - Central mode: A device that scans for and connects to other devices that provide data or services. For example, a smartphone, a tablet, or a laptop.
  - Broadcaster mode: A device that advertises itself but does not allow connections from other devices. For example, a sensor, a key finder, or a tag.
  - Observer mode: A device that scans for other devices that advertise themselves but does not connect to them. For example, a scanner, a locator, or a tracker.