### Using libraries for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Libraries are collections of code that provide extra functionality for use in sketches, such as working with hardware or manipulating data.
- Libraries can be imported into sketches by selecting them from Sketch > Import Library menu in the Arduino IDE, or by using the #include directive at the top of the sketch.
- Libraries can be installed from the Library Manager, which is accessible from Tools > Manage Libraries menu in the Arduino IDE, or from the Libraries tab in the Arduino Web Editor.
- Libraries can be searched by name, category, or author in the Library Manager or the Web Editor. Some libraries are read-only, meaning they are authored and maintained by the Arduino team or its partners, while others are editable, meaning they are contributed by the community or the user.
- Libraries can be updated or removed from the Library Manager or the Web Editor. It is recommended to keep the libraries up to date to avoid compatibility issues or bugs.
- Libraries can be created by the user or modified from existing ones. To create a library, the user needs to follow some guidelines and conventions, such as using a header file (.h) and a source file (.cpp), and placing them in a folder with the same name as the library. To modify a library, the user can edit the files in the library folder, or make a copy of the library and rename it.
- Libraries can be shared with others by uploading them to the Arduino Library Manager, which requires a GitHub account and a repository for the library, or by publishing them on the Arduino Playground, which is a wiki for the Arduino community.

Some examples of libraries that are useful for the Internet of Things are:

- WiFiNINA: This library allows the user to connect to the internet using the Arduino Nano 33 IoT, Arduino MKR WiFi 1010, Arduino MKR VIDOR 4000, and Arduino UNO WiFi Rev.2 boards. It supports TCP and UDP protocols, as well as SSL/TLS encryption.
- PubSubClient: This library provides a client for the MQTT protocol, which is a lightweight messaging protocol for the Internet of Things. It allows the user to publish and subscribe to topics, and send and receive messages from a broker.
- ArduinoJson: This library allows the user to serialize and deserialize JSON data, which is a common format for exchanging data on the web. It supports both static and dynamic memory allocation, and can handle nested objects and arrays.
- ArduinoHttpClient: This library allows the user to make HTTP requests and parse HTTP responses from a server. It supports both GET and POST methods, as well as basic authentication and custom headers.

Some mnemonics and learning tricks for using libraries are:

- To remember the steps for installing a library, use the acronym LIM: Library Manager, Install, and Import.
- To remember the difference between read-only and editable libraries, use the rhyme: Read-only libraries are made by Arduino, editable libraries are made by you or someone you know.
- To remember the structure of a library, use the analogy: A library is like a book, with a header file as the cover and a source file as the content. The header file declares the functions and variables, and the source file defines them. The folder name is the same as the book title.