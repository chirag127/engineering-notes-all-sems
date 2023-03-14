### WAP: Architecture

- WAP stands for Wireless Application Protocol, which is a standard for accessing wireless data through various communication networks, such as cellular, satellite, and radio systems.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: Wireless Application Environment (WAE). This layer is of most interest to content developers because it contains among other things, device specifications, and the content development programming languages, WML, and WMLScript.
  - Session Layer: Wireless Session Protocol (WSP). Unlike HTTP, WSP has been designed by the WAP Forum to provide fast connection suspension and reconnection.
  - Transaction Layer: Wireless Transaction Protocol (WTP). The WTP runs on top of a datagram service, such as User Datagram Protocol (UDP) and is part of the standard suite of TCP/IP protocols used to provide a simplified protocol suitable for low bandwidth wireless stations.
  - Security Layer: Wireless Transport Layer Security (WTLS). WTLS incorporates security features that are based upon the established Transport Layer Security (TLS) protocol standard. It includes data integrity checks, privacy, service denial, and authentication services.
  - Transport Layer: Wireless Datagram Protocol (WDP). The WDP allows WAP to be bearer-independent by adapting the transport layer of the underlying bearer. The WDP presents a consistent data format to the higher layers of the WAP protocol stack, thereby offering the advantage of bearer independence to application developers.
- Each of these layers provides a well-defined interface to the layer above it. This means that the internal workings of any layer are transparent or invisible to the layers above it. The layered architecture allows other applications and services to utilize the features provided by the WAP-stack as well. This makes it possible to use the WAP-stack for services and applications that currently are not specified by WAP.
- The WAP architecture is composed of various protocols and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems.
- The WAP architecture is shown below alongside a typical Internet Protocol stack:

| WAP Protocol Stack | Internet Protocol Stack |
|--------------------|-------------------------|
| WAE                | HTML, XML, etc.        |
| WSP                | HTTP                    |
| WTP                | TCP                     |
| WTLS               | TLS                     |
| WDP                | UDP, IP, etc.           |
| Bearer Services    | Bearer Services         |

- WAP is known for cross-platform technology so that HTML and HTTP are combined in the protocol along with bandwidth devices and pagers in the network. In addition, wireless phones and digital devices are integrated into the system so that they can communicate well without any hindrance in the communication. Also, there are devices that view only those pages allowed in the protocol, maybe plain pages or black and white pages in the system.