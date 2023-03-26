 Here are the notes on using libraries for Unit 5 - Programming the Arduino in Internet of Things:

### Using Libraries

1. Libraries provide pre-written code that can be used in a sketch to add functionality and simplify tasks.
2. To use a library, you first need to install it. This can be done through the Arduino IDE's Library Manager or by manually downloading the library and installing it.
3. Once installed, you need to include the library in your sketch using the `#include` directive. For example, to include the Servo library, use `#include <Servo.h>`.
4. After including the library, you can use the functions and commands it provides. For example, the Servo library provides `servo.attach()`, `servo.write()`, and other functions to control servos. Consult the library's documentation to see what it offers and how to use its features.
5. Some common Arduino libraries include:
    - Servo - for controlling servos
    - SPI and Wire - for communication protocols
    - LiquidCrystal - for LCD displays
    - SD - for reading/writing to SD cards
    - DateTime - for tracking time and dates
    - And many more!

6. Creating your own libraries allows you to reuse code across multiple projects and simplify complex tasks. To create a library, put code in a .h header file and .cpp implementation file and place in the libraries folder of your Arduino sketchbook. You can then `#include` your own library in sketches just like with standard libraries.

The notes are written in Markdown format with a formal tone and without emojis or external links as requested. The points are written concisely like a study guide. Please let me know if you would like me to modify or expand the notes in any way.