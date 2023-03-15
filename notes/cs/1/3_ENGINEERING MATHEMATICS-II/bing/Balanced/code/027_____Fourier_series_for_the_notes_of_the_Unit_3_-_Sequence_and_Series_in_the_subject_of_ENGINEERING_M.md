### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines   .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions   .
- A Fourier series is analogous to a Taylor series, which represents functions as possibly infinite sums of monomial terms.
- The computation and study of Fourier series is known as harmonic analysis and is extremely useful as a way to break up an arbitrary periodic function into a set of simple terms that can be plugged in, solved individually, and then recombined to obtain the solution to the original problem or an approximation to it to whatever accuracy is desired or practical.
- The general form of a Fourier series is:

![Fourier series formula](https://latex.codecogs.com/png.latex?f%28x%29%20%3D%20%5Cfrac%7Ba_%7B0%7D%7D%7B2%7D%20&plus;%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20%5B%20a_%7Bn%7D%20%5Ccos%20%28n%5Comega%20x%29%20&plus;%20b_%7Bn%7D%20%5Csin%20%28n%5Comega%20x%29%20%5D)

where ![omega](https://latex.codecogs.com/png.latex?%5Comega) is the fundamental frequency of the function and ![a_n](https://latex.codecogs.com/png.latex?a_%7Bn%7D) and ![b_n](https://latex.codecogs.com/png.latex?b_%7Bn%7D) are the Fourier coefficients, which can be calculated by the following formulas:

![a_n formula](https://latex.codecogs.com/png.latex?a_%7Bn%7D%20%3D%20%5Cfrac%7B2%7D%7BL%7D%20%5Cint_%7B0%7D%5E%7BL%7D%20f%28x%29%20%5Ccos%20%28n%5Comega%20x%29%20dx)

![b_n formula](https://latex.codecogs.com/png.latex?b_%7Bn%7D%20%3D%20%5Cfrac%7B2%7D%7BL%7D%20%5Cint_%7B0%7D%5E%7BL%7D%20f%28x%29%20%5Csin%20%28n%5Comega%20x%29%20dx)

where L is the period of the function    .

- Some examples of Fourier series are:

  - The Fourier series of the function ![f(x) = x](https://latex.codecogs.com/png.latex?f%28x%29%20%3D%20x) with period ![2 pi](https://latex.codecogs.com/png.latex?2%5Cpi) is:

  ![Fourier series of x](https://latex.codecogs.com/png.latex?f%28x%29%20%3D%20%5Cfrac%7B%5Cpi%7D%7B2%7D%20&plus;%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20%5B%20%5Cfrac%7B%28-1%29%5E%7Bn&plus;1%7D%7D%7Bn%7D%20%5Csin%20%28nx%29%20%5D)
