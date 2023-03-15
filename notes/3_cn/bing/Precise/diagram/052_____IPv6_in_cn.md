Here is a detailed ASCII diagram for IPv6 in computer networks:

### IPv6 in CN
```
  +----------------+
  |  Version (4)   |
  +----------------+
  | Traffic Class  |
  |     (8)        |
  +----------------+
  |  Flow Label    |
  |     (20)       |
  +----------------+
  |  Payload       |
  |  Length (16)   |
  +----------------+
  |  Next Header   |
  |     (8)        |
  +----------------+
  |  Hop Limit     |
  |     (8)        |
  +----------------+
  |  Source        |
  |  Address (128) |
  +----------------+
  |  Destination   |
  |  Address (128) |
  +----------------+
```

This diagram shows the structure of an IPv6 packet header. The numbers in parentheses indicate the number of bits used for each field. The Version field is 4 bits long and indicates the version of the Internet Protocol being used. The Traffic Class field is 8 bits long and is used to differentiate between different classes of traffic. The Flow Label field is 20 bits long and is used to identify a specific flow of data. The Payload Length field is 16 bits long and indicates the length of the payload in octets. The Next Header field is 8 bits long and indicates the type of header that follows the IPv6 header. The Hop Limit field is 8 bits long and is used to limit the number of hops a packet can make before being discarded. The Source Address and Destination Address fields are each 128 bits long and contain the IPv6 addresses of the source and destination of the packet, respectively.
