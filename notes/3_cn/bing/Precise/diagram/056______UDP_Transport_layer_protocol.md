#### UDP Transport layer protocol

Here is an ASCII diagram of the UDP Transport layer protocol:

```
+---------------------+
|      IP Header      |
+---------------------+
|     UDP Header      |
+---------------------+
|                     |
|     Data Payload    |
|                     |
+---------------------+
```

The UDP Header consists of four fields: Source Port, Destination Port, Length, and Checksum. Each field is 16 bits in size.

```
+----------------+----------------+
|  Source Port   | Destination Port|
+----------------+----------------+
|     Length     |    Checksum     |
+----------------+----------------+
```
