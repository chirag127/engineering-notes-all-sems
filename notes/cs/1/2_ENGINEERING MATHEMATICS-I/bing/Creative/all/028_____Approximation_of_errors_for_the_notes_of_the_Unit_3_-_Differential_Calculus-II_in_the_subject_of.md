Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of approximation of errors for the notes of the Unit 3 - Differential Calculus-II in the subject of ENGINEERING MATHEMATICS-I.

# Approximation of errors

- In many practical situations, we need to estimate the error or uncertainty in a quantity that is calculated from other quantities with known errors.
- For example, if we measure the length and width of a rectangle with a ruler, we can calculate its area, but we also need to know how accurate our calculation is, given the possible errors in the measurements.
- One way to estimate the error in a function of several variables is to use the **differential approximation**. This method is based on the idea that if the variables change by small amounts, then the function changes by approximately the linear combination of the partial derivatives times the changes in the variables.
- Mathematically, we can write this as:

$$f(x+\Delta x, y+\Delta y) \approx f(x,y) + f_x(x,y)\Delta x + f_y(x,y)\Delta y$$

- where $\Delta x$ and $\Delta y$ are the errors or uncertainties in $x$ and $y$, respectively, and $f_x$ and $f_y$ are the partial derivatives of $f$ with respect to $x$ and $y$, respectively, evaluated at the point $(x,y)$.
- The difference between the left-hand side and the right-hand side of the equation is called the **error in the differential approximation**, and it represents the amount by which the linear approximation deviates from the actual value of the function.
- We can use the differential approximation to estimate the error in the function value as follows:

$$\text{Error in } f \approx f_x(x,y)\Delta x + f_y(x,y)\Delta y$$

- Note that this is only an approximation, and it becomes more accurate as the errors in the variables become smaller. Also, this method does not account for the possible correlations or dependencies between the variables, which may affect the error propagation.
- To find the **maximum possible error** in the function value, we need to use the **absolute values** of the partial derivatives and the errors, and add them up. This gives us the following formula:

$$\text{Maximum error in } f \leq |f_x(x,y)|\Delta x + |f_y(x,y)|\Delta y$$

- This is also known as the **first-order approximation** of the error, or the **total differential** of the function. It gives us an upper bound for the error, but it does not tell us the exact value or the direction of the error.
- To find the **relative error** or the **percentage error** in the function value, we need to divide the error by the function value and multiply by 100%. This gives us the following formulas:

$$\text{Relative error in } f \approx \frac{f_x(x,y)\Delta x + f_y(x,y)\Delta y}{f(x,y)}$$

$$\text{Percentage error in } f \approx \frac{f_x(x,y)\Delta x + f_y(x,y)\Delta y}{f(x,y)} \times 100\%$$

- These formulas give us an estimate of how large the error is compared to the function value, and they are useful for comparing the errors in different functions or situations.
- To illustrate the use of these formulas, let us consider an example.

## Example

- Suppose we want to calculate the volume of a cylindrical tank with radius $r$ and height $h$, given by the formula $V=\pi r^2 h$. We measure the radius and the height with a tape measure, and we find that $r=2.5 \pm 0.1$ m and $h=4 \pm 0.2$ m, where the $\pm$ signs indicate the possible errors in the measurements. How can we estimate the error in the volume?
- Solution:
  - To use the differential approximation, we need to find the partial derivatives of the volume function with respect to the radius and the height. We have:

  $$V_r = \frac{\partial V}{\partial r} = 2\pi r h$$

  $$V_h = \frac{\partial V}{\partial h} = \pi r^2$$

  - Evaluating these at the point $(r,h) = (2.5,4)$, we get:

  $$V_r(2.5,4) = 2\pi (2.5)(4) = 20\pi$$