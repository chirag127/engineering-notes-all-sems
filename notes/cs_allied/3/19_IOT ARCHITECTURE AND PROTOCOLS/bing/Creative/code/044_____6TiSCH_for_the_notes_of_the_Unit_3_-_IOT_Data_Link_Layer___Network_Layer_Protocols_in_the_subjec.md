# 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol stack that combines the industrial performance of TSCH with the seamless integration of IPv6 for the Industrial Internet of Things (IIoT).
- It enables reliable and delay-bounded communication in multi-hop and scalable wireless networks.
- It consists of the following components    :
  - The IEEE 802.15.4e TSCH link layer protocol, which provides time synchronization, channel hopping, and medium access control.
  - The 6TiSCH Operation Sublayer (6top), which manages the allocation and deallocation of TSCH timeslots and cells.
  - The 6top Protocol (6P), which defines the messages and rules for 6top transactions between neighboring nodes.
  - The 6LoWPAN adaptation layer, which compresses and fragments IPv6 packets to fit the IEEE 802.15.4 frame size.
  - The IP-in-IP encapsulation, which allows the transmission of IPv6 packets over non-IPv6 networks.
  - The Routing Protocol for Low-Power and Lossy Networks (RPL), which provides routing and topology management for 6TiSCH networks.
- Some of the benefits of 6TiSCH are    :
  - It supports a large number of devices with 128-bit IPv6 addresses.
  - It reduces interference and improves reliability by using channel hopping and frequency diversity.
  - It saves energy and bandwidth by using time synchronization and TDMA scheduling.
  - It enables interoperability and compatibility with existing IP networks and applications.
  - It provides flexibility and adaptability by allowing dynamic and distributed scheduling and routing.