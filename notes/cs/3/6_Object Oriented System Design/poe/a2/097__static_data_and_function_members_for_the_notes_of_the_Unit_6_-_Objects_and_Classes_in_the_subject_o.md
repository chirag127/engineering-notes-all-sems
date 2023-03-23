 Here are the notes on static data and function members for Unit 6 - Objects and Classes in Object Oriented System Design:

### Static Data Members

- Declared with the `static` keyword
- There is only one copy of a static data member shared by all objects of a class
- Memory is allocated for static data members only once, at the start of the program
- Can be accessed using the class name and the scope resolution operator (::) without creating an object
- Useful for constants (e.g. #pi in a Circle class) or shared values (e.g. count in a counter class)

### Static Function Members

- Declared with the `static` keyword
- There is only one copy of a static function shared by all objects of a class
- Memory is allocated for static functions only once, at the start of the program
- Can be accessed using the class name and the scope resolution operator (::) without creating an object
- Used for functions that only operate on static data (e.g. incrementing a shared counter) or do not require object data (e.g. library utility functions)
- Cannot access non-static data members or call non-static member functions directly

The above notes cover the key points about static data members and static function members in object-oriented programming. The content is written in a formal tone with points in a markdown format as requested, without any emojis or external links. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.