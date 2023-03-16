### Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or proximity detection, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 connections simultaneously, while classic Bluetooth devices are limited to 7.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines the roles and modes of devices, such as peripheral, central, broadcaster, and observer, and how they advertise and scan for each other.
  - GATT defines the format and structure of data and services that devices can exchange, such as heart rate, battery level, or temperature.
- BLE devices communicate using radio frequency channels in the 2.4 GHz ISM band, which is divided into 40 channels, each 2 MHz wide.
  - Three of these channels (37, 38, and 39) are used for advertising, which is the process of broadcasting data packets to announce the presence and capabilities of a device.
  - The remaining 37 channels (0 to 36) are used for data transmission, which is the process of exchanging data packets between connected devices.
  - BLE devices use a technique called adaptive frequency hopping (AFH) to avoid interference and improve reliability, which means they switch channels randomly and frequently during data transmission.
- BLE devices use a modulation scheme called Gaussian frequency shift keying (GFSK) to encode data bits into radio signals.
  - GFSK is a type of frequency modulation (FM) that changes the frequency of the carrier signal according to the data bits, with a Gaussian filter applied to smooth the transitions.
  - GFSK has a modulation index of 0.5, which means the frequency deviation is half of the bit rate, and a symbol rate of 1 Msymbol/s, which means one data bit is transmitted per symbol.
  - GFSK can achieve a data rate of 1 Mbit/s, which is the maximum supported by BLE.