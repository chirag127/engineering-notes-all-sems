RARP stands for Reverse Address Resolution Protocol. It is a protocol that allows a device to obtain its IP address from a gateway server by sending its MAC address. The gateway server has a table that maps the MAC addresses to the IP addresses of the devices on the same network. The RARP server responds with the IP address of the device or an error message if the MAC address is not found in the table.

#### RARP

The following is a possible ASCII diagram for RARP:

```
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  RARP Client   |             |  RARP Server   |             |  Other Device  |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|  MAC: 00-11-22 |             |  MAC: 11-22-33 |             |  MAC: 22-33-44 |
|  IP:  ?        |             |  IP:  192.168.1.1|             |  IP:  192.168.1.2|
+----------------+             +----------------+             +----------------+
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |  RARP Request:             |                             |
       |  MAC: 00-11-22             |                             |
       |  IP:  ?                    |                             |
       |--------------------------->|                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |  RARP Reply:               |
       |                             |  MAC: 00-11-22             |
       |                             |  IP:  192.168.1.3          |
       |<---------------------------|                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
       |                             |                             |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  RARP Client   |             |  RARP Server   |             |  Other Device  |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|  MAC: 00-11-22 |             |  MAC: 11-22-33 |             |  MAC: 22-33-44 |
|  IP:  192.168.1.3|             |  IP:  192.168.1.1|             |  IP:  192.168.1.2|
+----------------+             +----------------+             +----------------+
```