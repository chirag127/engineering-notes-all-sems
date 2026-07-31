# Monte Carlo Integration

Monte Carlo integration is a technique for numerical integration using random numbers. It is a particular Monte Carlo method that numerically computes a definite integral. 

## Basic concept

- The basic idea of Monte Carlo integration is to approximate the value of an integral by the average value of the integrand at randomly chosen points. 
- Suppose we want to integrate a function f over a domain D. We can write the integral as

![integral](https://latex.codecogs.com/png.latex?%5Cint_D%20f%28x%29%20dx)

- We can also write the integral as the product of the area of D and the average value of f over D, i.e.

![integral](https://latex.codecogs.com/png.latex?%5Cint_D%20f%28x%29%20dx%20%3D%20%5Ctext%7BArea%7D%28D%29%20%5Ctimes%20%5Cfrac%7B1%7D%7B%5Ctext%7BArea%7D%28D%29%7D%20%5Cint_D%20f%28x%29%20dx%20%3D%20%5Ctext%7BArea%7D%28D%29%20%5Ctimes%20%5Cbar%7Bf%7D_D)

- where ![bar](https://latex.codecogs.com/png.latex?%5Cbar%7Bf%7D_D) is the average value of f over D, defined as

![average](https://latex.codecogs.com/png.latex?%5Cbar%7Bf%7D_D%20%3D%20%5Cfrac%7B1%7D%7B%5Ctext%7BArea%7D%28D%29%7D%20%5Cint_D%20f%28x%29%20dx)

- To estimate the average value of f over D, we can sample n random points ![xi](https://latex.codecogs.com/png.latex?x_i) from D and compute the sample mean of f at these points, i.e.

![sample](https://latex.codecogs.com/png.latex?%5Chat%7Bf%7D_D%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20f%28x_i%29)

- The sample mean ![hat](https://latex.codecogs.com/png.latex?%5Chat%7Bf%7D_D) is an unbiased estimator of the true mean ![bar](https://latex.codecogs.com/png.latex?%5Cbar%7Bf%7D_D), meaning that its expected value is equal to the true mean, i.e.

![expectation](https://latex.codecogs.com/png.latex?%5Cmathbb%7BE%7D%5B%5Chat%7Bf%7D_D%5D%20%3D%20%5Cbar%7Bf%7D_D)

- The variance of the sample mean ![hat](https://latex.codecogs.com/png.latex?%5Chat%7Bf%7D_D) is inversely proportional to the number of samples n, i.e.

![variance](https://latex.codecogs.com/png.latex?%5Cmathbb%7BV%7D%5B%5Chat%7Bf%7D_D%5D%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%20%5Cmathbb%7BV%7D%5Bf%28x%29%5D)

- where ![var](https://latex.codecogs.com/png.latex?%5Cmathbb%7BV%7D%5Bf%28x%29%5D) is the variance of f over D, defined as
