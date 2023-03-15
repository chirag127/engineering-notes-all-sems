### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines  .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions  .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions  .
- Fourier series are analogous to Taylor series, which represent functions as possibly infinite sums of monomial terms.
- Fourier series are very powerful tools in connection with various problems involving partial differential equations .
- Fourier series have many applications in physics, engineering, signal processing, image processing, etc .

#### Formula of Fourier Series

- The general form of a Fourier series is:

![formula](https://latex.codecogs.com/png.latex?f%28x%29%20%3D%20%5Cfrac%7Ba_%7B0%7D%7D%7B2%7D%20&plus;%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20%5B%20a_%7Bn%7D%20%5Ccos%20%28n%5Comega%20x%29%20&plus;%20b_%7Bn%7D%20%5Csin%20%28n%5Comega%20x%29%20%5D)

where ![omega](https://latex.codecogs.com/png.latex?%5Comega) is the angular frequency, ![a0](https://latex.codecogs.com/png.latex?a_%7B0%7D) is the constant term, and ![an](https://latex.codecogs.com/png.latex?a_%7Bn%7D) and ![bn](https://latex.codecogs.com/png.latex?b_%7Bn%7D) are the coefficients of the cosine and sine terms, respectively    .

- The coefficients can be calculated using the following formulas:

![a0](https://latex.codecogs.com/png.latex?a_%7B0%7D%20%3D%20%5Cfrac%7B1%7D%7BT%7D%20%5Cint_%7B0%7D%5E%7BT%7D%20f%28x%29%20dx)

![an](https://latex.codecogs.com/png.latex?a_%7Bn%7D%20%3D%20%5Cfrac%7B2%7D%7BT%7D%20%5Cint_%7B0%7D%5E%7BT%7D%20f%28x%29%20%5Ccos%20%28n%5Comega%20x%29%20dx)

![bn](https://latex.codecogs.com/png.latex?b_%7Bn%7D%20%3D%20%5Cfrac%7B2%7D%7BT%7D%20%5Cint_%7B0%7D%5E%7BT%7D%20f%28x%29%20%5Csin%20%28n%5Comega%20x%29%20dx)

where T is the period of the function    .

#### Examples of Fourier Series

- Example 1: Find the Fourier series of the function f(x) = x, defined on the interval [-pi, pi] and extended periodically.

- Solution: The period of the function is 2pi, so ![omega](https://latex.codecogs.com/png.latex?%5Comega) = 1. The coefficients are:
