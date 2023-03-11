### Mid-point Circle Generating Algorithm 

The mid-point circle generating algorithm is a popular algorithm used for drawing circles in computer graphics. It is a simple and efficient algorithm that is used to draw circles of different sizes and positions.

#### Algorithm Steps

The algorithm follows the following steps to draw a circle:

1. Input the center coordinates (x, y) and the radius (r) of the circle.
2. Set the initial point of the circle: (x+0, y+r)
3. Calculate the initial value of the decision parameter: 
```
d = 5/4 - r
```
4. At each step, choose one of the two possible points (x_k+1, y_k) or (x_k+1, y_k-1) based on the value of the decision parameter.
5. Calculate the next value of the decision parameter based on the chosen point:
```
if d < 0:
    d = d + 2*x_k + 3
else:
    d = d + 2*(x_k - y_k) + 5
    y_k = y_k - 1
```
6. Repeat steps 4 and 5 until x_k >= y_k

#### Advantages

1. The algorithm is simple and easy to understand.
2. It is efficient and fast, making it suitable for drawing circles of different sizes and positions.
3. It requires only integer arithmetic, making it suitable for implementation on systems with limited resources.
4. The algorithm can be easily modified to draw circles with different line styles.

#### Disadvantages

1. The algorithm may not produce circles that are perfectly round due to the use of integer arithmetic.
2. It may not work well for very large circles, as the number of iterations required may be too high.
3. The algorithm may not work well for circles with a radius of 1 or 2 due to the way the decision parameter is calculated.

#### Examples 

Here is an example implementation of the mid-point circle generating algorithm in Python:

```
def draw_circle(xc, yc, r):
    x = 0
    y = r
    d = 5/4 - r
    while x <= y:
        plot_points(xc, yc, x, y)
        if d < 0:
            d = d + 2*x + 3
        else:
            d = d + 2*(x - y) + 5
            y = y - 1
        x = x + 1
        
def plot_points(xc, yc, x, y):
    # plot the eight points of the circle
    plot(xc + x, yc + y)
    plot(xc - x, yc + y)
    plot(xc + x, yc - y)
    plot(xc - x, yc - y)
    plot(xc + y, yc + x)
    plot(xc - y, yc + x)
    plot(xc + y, yc - x)
    plot(xc - y, yc - x)
```

#### Applications 

The mid-point circle generating algorithm is used in a wide range of applications, including:

1. Computer graphics
2. Image processing
3. Medical imaging
4. Computer-aided design (CAD)
5. Video game development
6. Simulations and modeling. 

Overall, the mid-point circle generating algorithm is a useful and versatile algorithm that is widely used in computer graphics and related fields.