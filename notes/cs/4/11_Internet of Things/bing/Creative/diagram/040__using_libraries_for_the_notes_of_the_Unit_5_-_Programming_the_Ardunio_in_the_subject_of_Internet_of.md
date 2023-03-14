Using libraries for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

Libraries are a collection of code that makes it easy for you to connect to a sensor, display, module, etc. For example, the LiquidCrystal library makes it easy to talk to character LCD displays. There are thousands of libraries available for download directly through the Arduino IDE, and you can find all of them listed at the Arduino Library Reference.

To use a library in a sketch, select it from Sketch > Import Library. A number of libraries come installed with the IDE, but you can also download or create your own. Here are some instructions for setting up a library on the offline IDE:

1. Open the IDE and click "Sketch" on the menu tab and then Include Library > Manage Libraries. 
2. Search for the library that you need, click on it, then select the version of the library you want to install. 
3. Finally, click on install and wait for the IDE to install the new library. Once it has finished, an Installed tag should appear next to the library name. You can close the library manager. 

The following diagram illustrates the basic architecture of a sketch that uses a library:

```
+-----------------+     +-----------------+
|                 |     |                 |
|    Sketch.ino   |     |   Library.h     |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
| #include <...>  |     | #ifndef ...     |
|                 |     | #define ...     |
| setup()         |     | #endif          |
|                 |     |                 |
| loop()          |     |                 |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|                 |     |   Library.cpp   |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|                 |     | #include <...>  |
|                 |     |                 |
|                 |     | // Library code |
|                 |     |                 |
+-----------------+     +-----------------+
```

The sketch.ino file is the main program that runs on the Arduino board. It includes the library header file (library.h) that defines the interface of the library. The library.cpp file contains the implementation of the library code. The library.h file also has a preprocessor directive (#ifndef ... #define ... #endif) that prevents multiple inclusion of the same header file. 

To use the library functions in the sketch, you need to create an object of the library class and call its methods. For example, if you want to use the LiquidCrystal library to display some text on an LCD screen, you need to do something like this:

```
// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Hello, world!");
}

void loop() {
  // do nothing
}
```