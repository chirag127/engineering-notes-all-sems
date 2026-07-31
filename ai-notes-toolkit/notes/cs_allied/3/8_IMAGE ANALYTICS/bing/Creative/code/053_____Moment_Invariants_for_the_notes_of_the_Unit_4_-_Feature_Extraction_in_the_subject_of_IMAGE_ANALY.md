### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are computed from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation    .
- Moments are scalar quantities that describe the distribution of intensity values in an image. They can be computed for the whole image or for a region of interest. The moments of order (p+q) of a continuous image function f(x,y) are defined as:

$$
M_{pq} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x^p y^q f(x,y) dx dy
$$

- For a discrete image of size MxN, the moments are approximated by summations:

$$
M_{pq} = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} x^p y^q f(x,y)
$$

- The zeroth-order moment M00 is equal to the area of the image or the region, and the first-order moments M10 and M01 are related to the centroid (x̄,ȳ) of the image or the region by:

$$
x̄ = \frac{M_{10}}{M_{00}}, ȳ = \frac{M_{01}}{M_{00}}
$$

- The central moments of order (p+q) are defined as:

$$
\mu_{pq} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x-x̄)^p (y-ȳ)^q f(x,y) dx dy
$$

- For a discrete image, the central moments are approximated by:

$$
\mu_{pq} = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} (x-x̄)^p (y-ȳ)^q f(x,y)
$$

- The central moments are invariant to translation, but not to scaling and rotation. To achieve scale invariance, the normalized central moments (also called Hu moments) are defined as:

$$
\eta_{pq} = \frac{\mu_{pq}}{\mu_{00}^{(p+q)/2+1}}
$$

- To achieve rotation invariance, Hu proposed seven moment invariants that are derived from the normalized central moments up to the third order:

$$
\begin{aligned}
I_1 &= \eta_{20} + \eta_{02} \\
I_2 &= (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2 \\
I_3 &= (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2 \\
I_4 &= (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 \\
I_5 &= (\eta_{30} - 3\eta_{12})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] + (3\eta_{21} - \eta_{03})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] \\
I_6 &= (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4\eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03}) \\
I_7 &= (3\eta_{21} - \eta_{03})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03