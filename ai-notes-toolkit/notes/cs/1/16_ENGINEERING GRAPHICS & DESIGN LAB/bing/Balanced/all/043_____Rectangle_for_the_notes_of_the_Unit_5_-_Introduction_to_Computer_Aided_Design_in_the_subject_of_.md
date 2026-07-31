# Rectangle

- A rectangle is a two-dimensional plane figure with four sides, four vertices, and four angles .
- The opposite sides of a rectangle are equal in length and are parallel to each other .
- All four angles of a rectangle are right angles or equal to 90 degrees  .
- The longer side of a rectangle is called its length and the shorter side is the width.
- The diagonal of a rectangle is a line segment that joins two opposite vertices of the rectangle.
- The diagonals of a rectangle are equal in length and bisect each other at right angles.
- The area of a rectangle is the product of its length and width  .
- The perimeter of a rectangle is the sum of the lengths of all four sides  .
- The formula for the area of a rectangle is A = lw, where A is the area, l is the length, and w is the width  .
- The formula for the perimeter of a rectangle is P = 2(l + w), where P is the perimeter, l is the length, and w is the width  .

## Example of a Rectangle

![A rectangle with length l, width w, and diagonal d](https://www.cuemath.com/geometry/properties-of-rectangle/rectangle.png)

## How to Draw a Rectangle in Engineering Graphics

- To draw a rectangle, you need a Graphics object and a Pen object.
- The Graphics object provides the DrawRectangle method, and the Pen object stores features of the line, such as color and width.
- The DrawRectangle method takes four parameters: the Pen object, the x-coordinate of the upper-left corner of the rectangle, the y-coordinate of the upper-left corner of the rectangle, and the width and height of the rectangle.
- The following code snippet shows how to draw a rectangle in C# using the System.Drawing namespace:

```csharp
using System.Drawing;

// Create a Graphics object
Graphics g = Graphics.FromImage(image);

// Create a Pen object
Pen pen = new Pen(Color.Black, 2);

// Draw a rectangle with upper-left corner at (100, 100), width 200, and height 150
g.DrawRectangle(pen, 100, 100, 200, 150);

// Dispose the objects
pen.Dispose();
g.Dispose();
```

## How to Dimension a Rectangle in Engineering Graphics

- Dimensioning is the process of adding measurements and other information to a drawing to specify the size, shape, and location of the features of an object.
- The principles of dimensioning are based on clarity, accuracy, completeness, and consistency.
- To dimension a rectangle, you need to follow these steps:

  - Place the dimensions outside the outline of the object, leaving enough space between the object and the dimension lines.
  - Use horizontal and vertical dimension lines to indicate the length and width of the rectangle.
  - Use leader lines to indicate the diagonal of the rectangle.
  - Use arrowheads or dots to mark the ends of the dimension lines.
  - Use aligned or horizontal dimension text to indicate the values of the dimensions.
  - Use the same unit of measurement and the same number of decimal places for all dimensions.
  - Avoid unnecessary or redundant dimensions.

## Example of Dimensioning a Rectangle in Engineering Graphics

![A rectangle with dimensions in millimeters](https://www.mcgill.ca/engineeringdesign/files/engineeringdesign/fig_1_1.png)