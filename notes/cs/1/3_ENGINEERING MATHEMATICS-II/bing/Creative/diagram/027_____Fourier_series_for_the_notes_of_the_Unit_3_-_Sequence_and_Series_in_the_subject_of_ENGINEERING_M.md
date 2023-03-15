### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions.
- The computation and study of Fourier series is known as harmonic analysis and is extremely useful as a way to break up an arbitrary periodic function into a set of simple terms that can be plugged in, solved individually, and then recombined to obtain the solution to the original problem or an approximation to it to whatever accuracy is desired or practical.
- Fourier series can be used to represent periodic functions of any period T, not just 2π.
- The general form of a Fourier series is:

![Fourier series formula](https://latex.codecogs.com/png.latex?f%28x%29%20%3D%20%5Cfrac%7Ba_%7B0%7D%7D%7B2%7D%20&plus;%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20%5Cleft%28a_%7Bn%7D%5Ccos%5Cfrac%7B2%5Cpi%20nx%7D%7BT%7D%20&plus;%20b_%7Bn%7D%5Csin%5Cfrac%7B2%5Cpi%20nx%7D%7BT%7D%5Cright%29)

where T is the period of the function, and the coefficients a<sub>n</sub> and b<sub>n</sub> are given by:

![Fourier coefficients formula](https://latex.codecogs.com/png.latex?a_%7Bn%7D%20%3D%20%5Cfrac%7B2%7D%7BT%7D%20%5Cint_%7B0%7D%5E%7BT%7D%20f%28x%29%5Ccos%5Cfrac%7B2%5Cpi%20nx%7D%7BT%7D%20dx%2C%20%5Cquad%20b_%7Bn%7D%20%3D%20%5Cfrac%7B2%7D%7BT%7D%20%5Cint_%7B0%7D%5E%7BT%7D%20f%28x%29%5Csin%5Cfrac%7B2%5Cpi%20nx%7D%7BT%7D%20dx)

- The Fourier series converges to the function f(x) if f(x) is continuous and has a finite number of discontinuities and maxima and minima in any given interval.
- Some applications of Fourier series are:
  - Signal processing and analysis
  - Image compression and reconstruction
  - Heat conduction and diffusion
  - Quantum mechanics and wave mechanics
  - Acoustics and vibration
  - Electrical engineering and circuit analysis
  - Cryptography and encryption