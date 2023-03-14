Point-to-point networks in network layer are networks that use a data link layer protocol such as Point-to-Point Protocol (PPP) to communicate between two routers or hosts directly without any intermediate devices. Point-to-point networks can be used over various physical media such as serial cable, phone line, fiber optic, or wireless links. Point-to-point networks can support multiple network layer protocols such as IP, IPX, or AppleTalk. Point-to-point networks can also provide authentication, encryption, and compression features.

### Point-to-point networks in network layer

The following diagram illustrates the basic architecture of a point-to-point network in network layer using PPP as an example:

```
+--------+       +--------+
| Host A |-------| Host B |
+--------+       +--------+
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
+--------+       +--------+
| Router |-------| Router |
+--------+       +--------+
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
+--------+       +--------+
| Modem  |-------| Modem  |
+--------+       +--------+
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
  |                   |
+--------+       +--------+
| Phone  |-------| Phone  |
| Line   |       | Line   |
+--------+       +--------+
```

In this diagram, Host A and Host B are two computers that want to communicate over a point-to-point network. They are connected to routers that have modems attached to them. The modems use PPP to establish a data link layer connection over the phone line. The routers then use IP or another network layer protocol to route packets between Host A and Host B. The routers and the modems can also perform authentication, encryption, and compression functions to secure and optimize the data transmission.