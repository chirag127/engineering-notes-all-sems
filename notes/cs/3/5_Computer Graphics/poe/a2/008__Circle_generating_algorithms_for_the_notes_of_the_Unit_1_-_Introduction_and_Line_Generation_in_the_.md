 Here is the formal content in Markdown format without any emojis or external links:

### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics.

1. Midpoint Circle Algorithm
- Given the center (h, k) and radius r of the circle
- Set the initial values of the algorithm variables: x = 0, y = r
- Repeat the following steps until x > y:
-- Draw a pixel at (h + x, k + y)
-- Draw a pixel at (h - x, k + y)
-- Draw a pixel at (h + x, k - y)
-- Draw a pixel at (h - x, k - y)
-- Increment x and update y = sqrt(r^2 - x^2)

2. Bresenham's Circle Algorithm
- Given the center (h, k) and radius r of the circle
- Set the initial values: x = 0, y = r, d = 3 - 2r
- Repeat the following steps until x > y:
-- Plot the point (h + x, k + y)
-- Plot the point (h + y, k + x)
-- Plot the point (h - x, k + y)
-- Plot the point (h - y, k + x)
-- Calculate the decision parameter d
-- Increment x and update d, y based on the value of d

The content is written in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or add anything to the content.