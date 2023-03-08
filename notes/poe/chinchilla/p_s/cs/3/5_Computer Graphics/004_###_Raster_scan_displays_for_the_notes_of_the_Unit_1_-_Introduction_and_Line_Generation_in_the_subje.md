### Raster scan displays

Raster scan displays, also known as raster displays or CRT displays, are a type of display device used in computer graphics. These displays are widely used in computer graphics applications, including gaming, animation, and scientific visualization.

#### Working Principle

The raster scan display works by sweeping an electron beam across the screen, illuminating phosphor dots that make up the image. The electron beam is controlled by a series of electromagnetic coils that deflect it in different directions. The beam moves across the screen from left to right, one line at a time, and then returns to the beginning of the next line.

#### Advantages

- Raster scan displays are relatively inexpensive compared to other types of displays.
- They have a high refresh rate, which makes them ideal for applications that require fast movement, such as gaming and animation.
- They can display a wide range of colors and shades, making them suitable for scientific visualization and other applications that require high color accuracy.

#### Disadvantages

- Raster scan displays are prone to flicker, which can cause eye strain and fatigue.
- They have a limited resolution, which can result in pixelation and jagged edges.
- They are bulky and heavy compared to other types of displays.

#### Applications

- Gaming: Raster scan displays are popular in gaming because of their high refresh rate and ability to display a wide range of colors and shades.
- Animation: Raster scan displays are used in animation because of their ability to display fast movement and high color accuracy.
- Scientific visualization: Raster scan displays are used in scientific visualization because of their ability to display a wide range of colors and shades, making them suitable for displaying complex data sets.

#### Example

Here is an example of how to draw a line using raster scan displays:

```python
def draw_line(x1, y1, x2, y2):
    # calculate slope
    m = (y2 - y1) / (x2 - x1)
    # calculate y-intercept
    b = y1 - m * x1
    # draw line
    for x in range(x1, x2):
        y = m * x + b
        set_pixel(x, round(y))
```

#### Conclusion

Raster scan displays are a popular type of display device used in computer graphics applications. They have advantages and disadvantages, and are used in a variety of applications, including gaming, animation, and scientific visualization.