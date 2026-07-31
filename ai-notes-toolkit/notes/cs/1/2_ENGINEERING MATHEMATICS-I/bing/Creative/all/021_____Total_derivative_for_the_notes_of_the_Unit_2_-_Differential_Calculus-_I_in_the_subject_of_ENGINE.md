# Total derivative

- The total derivative of a function of several variables means the total change in the dependent variable due to the changes in all the independent variables.
- The total derivative is the derivative with respect to a variable that depends on the function not only directly but also via the intermediate variables.
- The formula for a total derivative is a direct result of the chain rule.
- The total derivative can be used to approximate the change in a function given small changes in the variables, or to analyze the sensitivity or error propagation of a function.

## Definition and formula

- Suppose z = f(x, y) be a function of two variables, where z is the dependent variable and x and y are the independent variables.
- The total derivative of z with respect to t is denoted by dz/dt and is defined as the limit of the ratio of the change in z to the change in t as the change in t approaches zero:

![dz/dt = lim_(Delta t -> 0) (Delta z)/(Delta t)](https://latex.codecogs.com/png.latex?dz/dt%20%3D%20%5Clim_%7B%5CDelta%20t%20%5Cto%200%7D%20%5CDelta%20z/%5CDelta%20t)

- If x and y are also functions of t, then we can use the chain rule to express the total derivative as follows :

![dz/dt = (dz/dx)(dx/dt) + (dz/dy)(dy/dt)](https://latex.codecogs.com/png.latex?dz/dt%20%3D%20%28dz/dx%29%28dx/dt%29%20&plus;%20%28dz/dy%29%28dy/dt%29)

- The terms dz/dx and dz/dy are the partial derivatives of z with respect to x and y, respectively, and they measure the rate of change of z along the x and y directions.
- The terms dx/dt and dy/dt are the derivatives of x and y with respect to t, and they measure the rate of change of x and y along the t direction.

## Example

- Suppose z = x^2 + y^3, where x = t + 1 and y = 2t - 1 are functions of t. Find the total derivative of z with respect to t.
- Solution:

  - We first find the partial derivatives of z with respect to x and y:

    ![dz/dx = 2x](https://latex.codecogs.com/png.latex?dz/dx%20%3D%202x)

    ![dz/dy = 3y^2](https://latex.codecogs.com/png.latex?dz/dy%20%3D%203y%5E2)

  - We then find the derivatives of x and y with respect to t:

    ![dx/dt = 1](https://latex.codecogs.com/png.latex?dx/dt%20%3D%201)

    ![dy/dt = 2](https://latex.codecogs.com/png.latex?dy/dt%20%3D%202)

  - We then use the formula for the total derivative to get:

    ![dz/dt = (dz/dx)(dx/dt) + (dz/dy)(dy/dt)](https://latex.codecogs.com/png.latex?dz/dt%20%3D%20%28dz/dx%29%28dx/dt%29%20&plus;%20%28dz/dy%29%28dy/dt%29)

    ![= (2x)(1) + (3y^2)(2)](https://latex.codecogs.com/png.latex?%3D%20%282x%29%281%29%20&plus;%20%283y%5E2%29%282%29)

    ![= 2x + 6y^2](https://latex.codecogs.com/png.latex?%3D%202x%20&plus;%206y%5E2)

  - We can also substitute x = t + 1 and y = 2t - 1 to get:

    ![dz/dt = 2(t + 1) + 6(2t - 1)^2](https://latex.codecogs.com/png