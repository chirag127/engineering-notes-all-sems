# 6LoWPAN

6LoWPAN is a protocol definition that enables IPv6 packets to be carried on top of low power wireless networks, specifically IEEE 802.15.4. The concept was born from the idea that the Internet Protocol could and should be applied to even the smallest of devices.

The 6LoWPAN protocol stack includes different networking topologies such as star and mesh, low bandwidth (250/40/20 kbps), low power consumption, typically battery-operated, relatively low cost, scalable networks, reliability, mobility, and long sleep times.

In the network layer, IPv6 is used. This makes it fit to support several devices, hence preferred in building IoT based systems. The channels have varying data rates and are allocated into different frequency bands with a total of twenty-seven channels being defined in the layer.

6LoWPAN only specifies the operation of IPv6 over the IEEE 802.15.4 standard, edge routers may also support IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as NAT64 defined in RFC 6146. These IPv6 transition mechanisms do not require the 6LoWPAN nodes to implement IPv4 in whole or in part.

The 6LoWPAN architecture is made up of low-power wireless area networks (LoWPANs), which are IPv6 stub networks. Three different kinds of LoWPANs have been defined: Simple LoWPANs, Extended LoWPANs, and Ad hoc LoWPANs.