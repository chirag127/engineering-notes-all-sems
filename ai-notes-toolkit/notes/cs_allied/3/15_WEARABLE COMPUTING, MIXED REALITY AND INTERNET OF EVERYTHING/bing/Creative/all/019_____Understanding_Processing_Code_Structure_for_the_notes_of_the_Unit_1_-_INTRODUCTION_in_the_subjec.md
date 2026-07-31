# Understanding Processing Code Structure

Processing is a programming language and environment for creating interactive graphics, animations, and games. It is based on Java, but has a simplified syntax and a built-in graphics library. Processing code consists of two main parts, setup and draw blocks .

- The setup block runs once when the code gets executed, and is used to initialize variables, load images, set the size of the window, and other configurations. The setup block is optional, but if it is present, it must have the keyword `void setup()` followed by curly braces `{}` that contain the code.
- The draw block runs continuously, and is used to update the display, handle user input, and perform calculations. The draw block is also optional, but if it is present, it must have the keyword `void draw()` followed by curly braces `{}` that contain the code. The main idea behind Processing is, what you write within the draw block will be executed 60 times per second from top to bottom, until your program terminates.

Here is an example of a simple Processing program that draws a circle that follows the mouse:

```java
// This is a comment. Comments are ignored by the computer, but help humans understand the code.

void setup() {
  // This code runs once at the beginning
  size(400, 400); // Set the size of the window to 400 by 400 pixels
  background(255); // Set the background color to white
}

void draw() {
  // This code runs repeatedly until the program stops
  ellipse(mouseX, mouseY, 50, 50); // Draw a circle with the center at the mouse position and a diameter of 50 pixels
}
```

Some important points to note about Processing code structure are:

- Processing code is case-sensitive, meaning that `size` and `Size` are different words. Keywords, such as `void`, `setup`, and `draw`, must be written in lowercase.
- Processing code must follow the rules of syntax, which are the grammar and punctuation of the language. For example, every statement must end with a semicolon `;`, and every block must be enclosed by curly braces `{}`.
- Processing code can be organized into functions, which are reusable blocks of code that perform a specific task. Functions can be defined by the user, or built-in to the language. For example, `size`, `background`, and `ellipse` are built-in functions that are part of the Processing graphics library. To use a function, you must write its name followed by parentheses `()` that contain the arguments, which are the values or variables that the function needs to work. For example, `size(400, 400)` uses the function `size` with the arguments `400` and `400`, which specify the width and height of the window in pixels.
- Processing code can also use variables, which are names that store values. Variables can be declared by using a data type, such as `int`, `float`, or `String`, followed by a name, such as `x`, `y`, or `name`. For example, `int x = 10;` declares a variable named `x` of type `int` (integer) and assigns it the value `10`. Variables can be used to store and manipulate data, such as the position, color, or speed of an object. Processing also has some built-in variables, such as `mouseX` and `mouseY`, which store the current position of the mouse in pixels.