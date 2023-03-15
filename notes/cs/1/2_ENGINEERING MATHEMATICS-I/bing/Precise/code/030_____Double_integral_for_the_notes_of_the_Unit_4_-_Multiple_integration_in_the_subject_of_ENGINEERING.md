### Double integral

A double integral is a way to integrate over a two-dimensional area. It is used to calculate the volume under a surface or to find the mass of an object with varying density.

The basic idea of a double integral is to divide the region of integration into small rectangles, calculate the volume of each rectangular column, and then add up all the volumes to get the total volume.

The notation for a double integral is:

$$\iint_R f(x,y) dA$$

where $R$ is the region of integration and $f(x,y)$ is the function being integrated.

To evaluate a double integral, we first need to express the region of integration $R$ in terms of the limits of integration. This can be done in two ways: by expressing $R$ as a type I region or as a type II region.

A type I region is a region that can be expressed in the form:

$$a \leq x \leq b, g_1(x) \leq y \leq g_2(x)$$

where $a$ and $b$ are constants and $g_1(x)$ and $g_2(x)$ are continuous functions.

A type II region is a region that can be expressed in the form:

$$c \leq y \leq d, h_1(y) \leq x \leq h_2(y)$$

where $c$ and $d$ are constants and $h_1(y)$ and $h_2(y)$ are continuous functions.

Once the region of integration is expressed in terms of the limits of integration, the double integral can be evaluated as an iterated integral. That is, we first integrate with respect to one variable, treating the other variable as a constant, and then integrate the result with respect to the other variable.

For example, if $R$ is a type I region, then the double integral can be evaluated as:

$$\iint_R f(x,y) dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x,y) dy \right) dx$$

If $R$ is a type II region, then the double integral can be evaluated as:

$$\iint_R f(x,y) dA = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x,y) dx \right) dy$$

In some cases, it may be easier to evaluate the double integral by changing the order of integration. This can be done by expressing the region of integration as both a type I and a type II region and then choosing the order of integration that is easier to evaluate.

Double integrals can also be evaluated using polar coordinates. This is particularly useful when the region of integration is a disk or an annulus. In this case, the double integral can be expressed in the form:

$$\iint_R f(x,y) dA = \int_{\alpha}^{\beta} \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta) r dr d\theta$$

where $\alpha$ and $\beta$ are the limits of integration for the angle $\theta$ and $r_1(\theta)$ and $r_2(\theta)$ are the limits of integration for the radius $r$. The extra factor of $r$ in the integrand is due to the Jacobian of the transformation from Cartesian to polar coordinates.

Double integrals have many applications in physics and engineering, including calculating the center of mass, moments of inertia, and electric charge of an object. They are also used in probability theory to calculate joint probabilities and expectations. In general, double integrals provide a powerful tool for calculating quantities that depend on two variables.