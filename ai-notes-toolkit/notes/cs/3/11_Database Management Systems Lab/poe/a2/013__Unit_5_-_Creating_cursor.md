 Here is the formal content written in Markdown format with points inside header ## Unit 5 - Creating cursor:

## Unit 5 - Creating cursor

1. What is a cursor?
- A cursor is a pointer that indicates the current position for user interaction on a computer or other device with a graphical user interface.
- The cursor allows the user to interact with the interface by selecting, dragging, or moving objects.

2. How to create a cursor?
- Cursors can be created in CSS using the cursor property.
- The cursor property accepts various system-defined or custom cursor values.
- Some common system cursor values are:
-- auto - Default cursor.
-- pointer - Arrow cursor.
-- move - Hand cursor.
-- text - I-beam cursor.

3. Creating custom cursors
- Custom cursors can be created by defining a cursor file with a .cur or .ico file extension.
- The file must contain an image depicting the custom cursor.
- The cursor file must then be specified in the cursor CSS property using the url() function.
- For example, to use a custom 'select' cursor, the CSS would be:
cursor: url('select.cur'), auto;

4. Advantages of custom cursors
- Custom cursors can enhance the user experience by using cursors that provide more meaning or context.
- Custom cursors allow for brand consistency by using branded cursor designs.
- Creative custom cursors can make an interface more fun and visually interesting.