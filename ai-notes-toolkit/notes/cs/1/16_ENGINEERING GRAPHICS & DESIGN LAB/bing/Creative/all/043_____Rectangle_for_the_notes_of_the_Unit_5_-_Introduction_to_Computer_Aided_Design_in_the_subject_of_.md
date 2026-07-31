# Rectangle

A rectangle is a two-dimensional plane figure with four sides, four vertices, and four angles. It is one of the types of quadrilaterals in which the opposite sides are parallel and equal to each other and all four angles are right angles or equal to 90 degrees. The longer side of a rectangle is called its length and the shorter side is the width.

Some of the properties of a rectangle are :

- The opposite sides of a rectangle are congruent (equal in length).
- The opposite angles of a rectangle are congruent (equal in measure).
- The diagonals of a rectangle are congruent (equal in length).
- The diagonals of a rectangle bisect each other (divide each other into two equal parts).
- The diagonals of a rectangle are perpendicular to each other (form right angles).
- The perimeter of a rectangle is the sum of the lengths of all four sides. The formula is P = 2(l + w), where l is the length and w is the width.
- The area of a rectangle is the product of the length and the width. The formula is A = lw, where l is the length and w is the width.

To draw rectangles, you need a Graphics object and a Pen object. The Graphics object provides the DrawRectangle method, and the Pen object stores features of the line, such as color and width. The DrawRectangle method takes four parameters: the Pen object, the x-coordinate of the upper-left corner, the y-coordinate of the upper-left corner, and the width and height of the rectangle.

To dimension a rectangle, you need to specify the length and the width of the rectangle, as well as the location of the rectangle with respect to a reference point or a coordinate system. The dimension lines should be thin and have arrowheads at both ends. The dimension values should be placed above the dimension lines and aligned with them. The dimension lines should not cross each other or the object lines.

Here is an example of a rectangle drawn and dimensioned using the Graphics object and the Pen object in C#:

```csharp
using System.Drawing;

// Create a Graphics object
Graphics g = this.CreateGraphics();

// Create a Pen object
Pen p = new Pen(Color.Black, 2);

// Draw a rectangle with upper-left corner at (100, 100) and width 200 and height 150
g.DrawRectangle(p, 100, 100, 200, 150);

// Dimension the length and the width of the rectangle
g.DrawLine(p, 100, 90, 300, 90); // Draw a horizontal dimension line
g.DrawLine(p, 100, 90, 100, 85); // Draw a left arrowhead
g.DrawLine(p, 300, 90, 300, 85); // Draw a right arrowhead
g.DrawString("200", new Font("Arial", 12), new SolidBrush(Color.Black), 190, 70); // Draw the dimension value

g.DrawLine(p, 310, 100, 310, 250); // Draw a vertical dimension line
g.DrawLine(p, 310, 100, 315, 100); // Draw a top arrowhead
g.DrawLine(p, 310, 250, 315, 250); // Draw a bottom arrowhead
g.DrawString("150", new Font("Arial", 12), new SolidBrush(Color.Black), 320, 170); // Draw the dimension value
```

This is how the output looks like:

![Rectangle](https://i.imgur.com/9p6y1fA.png)