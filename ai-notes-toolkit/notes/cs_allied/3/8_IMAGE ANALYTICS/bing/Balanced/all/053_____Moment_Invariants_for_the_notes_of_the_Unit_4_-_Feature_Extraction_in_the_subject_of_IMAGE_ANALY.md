# Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation .
- Moments are scalar quantities that describe the distribution of pixel values or intensities in an image. They can be computed for the whole image or for a region of interest.
- Moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc. Each type of moment has different properties and applications.
- Moment invariants are useful for image analysis and pattern recognition, as they can capture the shape and appearance of an object or a region in an image, regardless of its position, size and orientation .
- Moment invariants can be derived from different types of moments, but one of the most widely used and studied set of moment invariants is the one proposed by Hu in 1962 . Hu's moment invariants are based on normalized central moments and consist of seven values that are invariant to translation, scaling and rotation of an image .
- Hu's moment invariants are defined as follows :

  - Let $f(x,y)$ be a continuous image function, and let $m_{pq}$ be the geometric moments of $f(x,y)$, defined as:

    $$m_{pq} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x^p y^q f(x,y) dx dy$$

  - Let $\bar{x}$ and $\bar{y}$ be the centroid coordinates of $f(x,y)$, defined as:

    $$\bar{x} = \frac{m_{10}}{m_{00}}, \quad \bar{y} = \frac{m_{01}}{m_{00}}$$

  - Let $\mu_{pq}$ be the central moments of $f(x,y)$, defined as:

    $$\mu_{pq} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x - \bar{x})^p (y - \bar{y})^q f(x,y) dx dy$$

  - Let $\eta_{pq}$ be the normalized central moments of $f(x,y)$, defined as:

    $$\eta_{pq} = \frac{\mu_{pq}}{\mu_{00}^{(p+q)/2 + 1}}$$

  - Then, Hu's moment invariants are given by:

    $$\phi_1 = \eta_{20} + \eta_{02}$$

    $$\phi_2 = (\eta_{20} - \eta_{02})^2 + 4 \eta_{11}^2$$

    $$\phi_3 = (\eta_{30} - 3 \eta_{12})^2 + (3 \eta_{21} - \eta_{03})^2$$

    $$\phi_4 = (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2$$

    $$\phi_5 = (\eta_{30} - 3 \eta_{12})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] + (3 \eta_{21} - \eta_{03})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2]$$

    $$\phi_6 = (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4 \eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03})$$

    $$\phi_7 = (3 \eta_{21} - \eta_{03})(\eta_{30} + \