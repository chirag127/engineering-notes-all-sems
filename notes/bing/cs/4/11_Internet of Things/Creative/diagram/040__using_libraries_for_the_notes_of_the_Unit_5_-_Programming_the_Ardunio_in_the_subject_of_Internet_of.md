The following diagram illustrates the basic architecture of using libraries for the notes of the Unit 5 - Programming the Ardunio in the subject of Internet of Things:

```
+-----------------+     +-----------------+     +-----------------+
| Arduino Board   |     | Arduino IDE     |     | Arduino Library |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Sketch      | |     | | Sketch      | |     | | Header file | |
| |             | |     | |             | |     | | (.h)        | |
| | #include    | |     | | #include    | |     | |             | |
| | <library.h> | |     | | <library.h> | |     | |             | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Hardware    | |     | | Compiler    | |     | | Source file | |
| |             | |     | |             | |     | | (.cpp)      | |
| |             | |<--->| |             | |<--->| |             | |
| |             | |     | |             | |     | |             | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows the following steps:

1. The sketch on the Arduino board includes the library header file (.h) using the #include directive.
2. The Arduino IDE compiles the sketch and links it with the library source file (.cpp) that contains the implementation of the library functions.
3. The Arduino IDE uploads the compiled sketch to the Arduino board, where it interacts with the hardware using the library functions.