# 2D Transforms

2D transforms are operations that modify the position, size, shape, or orientation of an image on a 2D plane. They are useful for image processing and computer graphics applications, such as resizing, rotating, cropping, filtering, or enhancing images.

There are different types of 2D transforms, such as:

- **Translation**: This is the simplest 2D transform, which shifts an image by a certain amount of pixels in the horizontal and vertical directions. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
$$

where $t_x$ and $t_y$ are the translation parameters.

- **Scaling**: This is a 2D transform that changes the size of an image by a certain factor in the horizontal and vertical directions. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

where $s_x$ and $s_y$ are the scaling factors.

- **Rotation**: This is a 2D transform that rotates an image by a certain angle around a fixed point, usually the origin. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
\cos \theta & -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

where $\theta$ is the rotation angle.

- **Shearing**: This is a 2D transform that distorts an image by a certain amount in the horizontal or vertical direction, creating a slanted effect. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
1 & sh_x & 0 \\
sh_y & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

where $sh_x$ and $sh_y$ are the shearing parameters.

- **Affine**: This is a general 2D transform that combines any of the above transforms, or any other linear transformation, into a single matrix. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
0 & 0 & 1
\end{bmatrix}
$$

where $a, b, c, d, e, f$ are the affine parameters.

- **Fourier**: This is a special 2D transform that converts an image from the spatial domain to the frequency domain, or vice versa. It decomposes an image into a sum of sinusoidal components, each with a certain amplitude, frequency, and phase. It can be used for image filtering, compression, enhancement, or analysis. It can be represented by a complex-valued function of the form:

$$
F(u, v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) e^{-j 2 \pi (ux + vy)} dx dy
$$

where $f(x, y)$ is the spatial image, $F(u, v)$ is the frequency image, $u$ and $v$ are the frequency variables, and $j$ is the imaginary unit.

- **Wavelet**: This is another special 2D transform that converts an image from the spatial domain to the wavelet domain, or vice versa. It decomposes an image into a set of wavelet functions, each with a certain scale, location, and orientation. It can be used for image compression, denoising, segmentation, or analysis. It can be represented by a real-valued function of the form:

$$
W(a, b, \theta) = \frac{1}{\sqrt{a}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \psi \left( \frac{x - b_x}{a}, \frac{y - b_y}{a}, \theta \right) dx