### Wireless applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless applications are the software programs that run on wireless devices, such as smartphones, tablets, laptops, etc. and use wireless networks, such as Wi-Fi, cellular, Bluetooth, etc. to communicate with other devices or servers.
- Wireless applications can benefit from user mobility, higher reliability, lower cost, and increased efficiency as compared to wired applications.
- Wireless applications can be classified into different categories, such as:
  - Wireless web applications: These are the applications that use web browsers to access web pages or web services over wireless networks. Examples are online banking, e-commerce, social media, etc.
  - Wireless native applications: These are the applications that are designed specifically for wireless devices and use the device's features, such as camera, GPS, accelerometer, etc. Examples are games, navigation, fitness, etc.
  - Wireless enterprise applications: These are the applications that are used by businesses or organizations to manage their operations, such as inventory, sales, customer service, etc. over wireless networks. Examples are email, CRM, ERP, etc.
  - Wireless multimedia applications: These are the applications that involve the transmission or streaming of audio, video, or images over wireless networks. Examples are video conferencing, online music, online video, etc.

- Wireless networking is the process of connecting wireless devices to each other or to a wired network using wireless technologies, such as radio waves, infrared, or microwave.
- Wireless networking can be classified into different types, such as:
  - Wireless personal area network (WPAN): This is a network that connects devices within a short range, such as a few meters. Examples are Bluetooth, NFC, etc.
  - Wireless local area network (WLAN): This is a network that connects devices within a limited area, such as a room, a building, or a campus. Examples are Wi-Fi, IEEE 802.11, etc.
  - Wireless metropolitan area network (WMAN): This is a network that connects devices within a large area, such as a city or a region. Examples are WiMAX, IEEE 802.16, etc.
  - Wireless wide area network (WWAN): This is a network that connects devices across a large geographic area, such as a country or a continent. Examples are cellular, GSM, CDMA, etc.

- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area using radio frequencies. WLANs are based on the IEEE 802.11 standard, which defines the physical layer (PHY) and the medium access control (MAC) layer protocols for wireless communication.
- WLANs use the Ethernet protocol and the CSMA/CA (carrier sense multiple access with collision avoidance) technique for sharing the wireless medium. CSMA/CA is a method that allows multiple devices to transmit data without interfering with each other. It works as follows:
  - A device that wants to transmit data first listens to the channel to check if it is idle or busy.
  - If the channel is idle, the device transmits a short frame called a request to send (RTS) to the intended receiver, indicating the duration of the data transmission.
  - The receiver replies with a short frame called a clear to send (CTS), which is heard by all the devices in the network. The CTS frame also indicates the duration of the data transmission.
  - The sender then transmits the data frame to the receiver, and the receiver sends an acknowledgment (ACK) frame to the sender, confirming the successful reception of the data.
  - If the channel is busy, the device waits for a random time interval before trying again. This is called the backoff time.
  - If a collision occurs, meaning that two or more devices transmit at the same time, the devices detect the collision and abort their transmission. They then wait for a longer backoff time before trying again. This is called the exponential backoff.

- The IEEE 802.11 standard has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of frequency band, data rate, modulation scheme, channel width, etc. The following table summarizes some of the main characteristics of these variants:

| Variant | Frequency band | Data rate | Modulation scheme | Channel width |
|---------|----------------|-----------|-------------------|---------------|
|