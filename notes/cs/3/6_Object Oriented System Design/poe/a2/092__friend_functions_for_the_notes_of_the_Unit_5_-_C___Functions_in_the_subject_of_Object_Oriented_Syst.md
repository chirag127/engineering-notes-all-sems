 Here is the content in markdown format without any emojis or external links:

### Friend Functions

- Friend functions are the non-member functions which are given access to the private and protected members of a class.
- This access is done by declaring a function as a friend in the class.
- The prototype of a friend function is defined outside the class but it can access the private/protected members.
- This is done to allow the function to carry out some operations that require access that is otherwise not permitted.
- The purpose of friend functions is to allow classes to work together more efficiently or to simplify the interfaces.
- The key points to note about friend functions are:

1. Not in the scope of the class
2. Defined outside the class
3. Declared inside the class
4. Given privilege of accessing private/protected members
5. Friendship is not mutual/reciprocal

- The general form of declaring a friend function is:
`friend return-type function-name(parameter-list);`

- Example:
`class Rectangle;
class Square;

Rectangle::Rectangle(int a, int b) { ... }

Square::Square(int a) { ... }

void func(Rectangle& r, Square& s)
{
  // func() is a friend function
  // which can access private members of Rectangle and Square
}`

- This format maintains formality and sticks to points without any emojis or external links as instructed. Let me know if you would like me to modify or expand the content.