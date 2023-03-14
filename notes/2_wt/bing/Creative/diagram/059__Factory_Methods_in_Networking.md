Factory Methods in Networking are a design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. This can be useful for creating different types of network devices, such as switches, routers, or wireless access points, depending on the requirements of the network environment.

The following diagram illustrates the basic architecture of a Factory Method in Networking using ASCII art:

```
+-----------------+    +-----------------+
|   NetworkDevice |    |   NetworkDevice |
|-----------------|    |-----------------|
| +createDevice() |    | +createDevice() |
+-----------------+    +-----------------+
          ^                      ^
          |                      |
          |                      |
+-----------------+    +-----------------+
| EthernetSwitch  |    |  WirelessRouter |
|-----------------|    |-----------------|
| +createDevice() |    | +createDevice() |
+-----------------+    +-----------------+
          ^                      ^
          |                      |
          |                      |
+-----------------+    +-----------------+
|   SwitchDevice  |    |  RouterDevice   |
|-----------------|    |-----------------|
| +connect()      |    | +connect()      |
| +send()         |    | +send()         |
| +receive()      |    | +receive()      |
+-----------------+    +-----------------+
```

In this diagram, NetworkDevice is an abstract class that defines the interface for creating network devices. EthernetSwitch and WirelessRouter are concrete subclasses that implement the createDevice() method to return different types of network devices, such as SwitchDevice or RouterDevice. These are the products of the factory method, and they have their own methods for connecting, sending, and receiving data over the network.