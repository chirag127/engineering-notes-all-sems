### Mobile IP for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

Mobile IP is a protocol that allows mobile devices to maintain connectivity to the Internet while moving across different networks. It enables seamless communication between mobile devices and the Internet, even when the devices change their locations.

#### How Mobile IP Works:

1. The mobile device sends a registration request to its home agent when it connects to a new network. The home agent is responsible for maintaining the permanent address of the mobile device.

2. The home agent forwards the registration request to a foreign agent on the new network.

3. The foreign agent assigns a temporary address to the mobile device and sends a registration reply to the home agent.

4. The home agent updates its database with the temporary address assigned to the mobile device.

5. When a correspondent node wants to communicate with the mobile device, it sends the packet to the home agent.

6. The home agent encapsulates the packet and sends it to the foreign agent.

7. The foreign agent decapsulates the packet and delivers it to the mobile device.

#### Advantages of Mobile IP:

- Enables seamless communication between mobile devices and the Internet while moving across different networks.
- Reduces the need for manual updates of IP addresses, which can be time-consuming and error-prone.
- Provides a solution for the limitations of traditional IP addressing, which is based on fixed network addresses.

#### Disadvantages of Mobile IP:

- Can cause additional network traffic due to the encapsulation and decapsulation of packets.
- Can result in longer packet delivery times due to the additional processing required by the home and foreign agents.
- Requires additional infrastructure to support the home and foreign agents.

#### Mnemonic:

- Remember the steps of Mobile IP registration as "Home, Forward, Assign, Update, Encapsulate, Decapsulate, Deliver" (HF AUEDD).

Mobile IP is an important protocol in the field of mobile computing and wireless networking, as it enables seamless communication between mobile devices and the Internet while moving across different networks. It is essential for maintaining connectivity and ensuring that mobile devices can access the Internet regardless of their location.