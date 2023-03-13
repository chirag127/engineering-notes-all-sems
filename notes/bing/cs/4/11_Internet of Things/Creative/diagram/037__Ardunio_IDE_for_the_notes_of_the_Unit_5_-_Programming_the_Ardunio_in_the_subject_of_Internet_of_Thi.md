The Arduino IDE is an open-source programming tool that allows users to write and upload code to Arduino boards. It consists of a text editor, a compiler, a serial monitor, and a board manager. The following diagram illustrates the basic architecture of the Arduino IDE:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Text Editor   |    |   Compiler      |    |   Serial Monitor|
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
       |                      |                       |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Sketch        |    |   Binary Code   |    |   Board Manager |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The text editor is where users write their code, also called sketches. The compiler converts the sketches into binary code that can be uploaded to the Arduino board. The serial monitor displays the output of the code and allows users to communicate with the board. The board manager lets users select and configure the type of Arduino board they are using.