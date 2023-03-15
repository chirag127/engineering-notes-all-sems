### Multiplexing in transport layer
```
+---------------------+
|   Application       |
+---------------------+
|   Transport         |
+---------------------+
|   Network           |
+---------------------+
|   Data Link         |
+---------------------+
|   Physical          |
+---------------------+

```
In the transport layer, multiplexing is the process of combining multiple application-layer data streams into a single transport-layer data stream. This is done by assigning each application-layer data stream a unique identifier, called a port number. The transport layer then uses these port numbers to direct incoming data to the correct application.

Here is an example of how multiplexing works in the transport layer:

```
+---------------------+
|   Application       |
+----------+----------+
|   HTTP   |   FTP    |
+----------+----------+
|   Port 80|   Port 21|
+----------+----------+
|   Transport         |
+---------------------+
|   Network           |
+---------------------+
|   Data Link         |
+---------------------+
|   Physical          |
+---------------------+

```
In this example, the HTTP application is assigned port 80 and the FTP application is assigned port 21. When data is sent from the HTTP application, it is sent to the transport layer with the port number 80. The transport layer then uses this port number to direct the data to the correct application when it is received on the other end. Similarly, data sent from the FTP application is sent with the port number 21 and is directed to the correct application when it is received.
