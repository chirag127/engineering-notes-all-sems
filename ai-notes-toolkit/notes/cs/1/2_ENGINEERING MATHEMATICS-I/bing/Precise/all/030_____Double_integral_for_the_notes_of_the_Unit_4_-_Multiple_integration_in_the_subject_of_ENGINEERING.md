# Double Integral

A double integral is a way to integrate over a two-dimensional area. It is used to calculate the volume under a surface in three-dimensional space or to calculate the area of a region in the plane.

The double integral of a function f(x,y) over a region R in the xy-plane is denoted by:

$$\iint_R f(x,y) dA$$

where dA represents an infinitesimal area element in the region R.

To evaluate a double integral, we first divide the region R into small subregions, and then approximate the volume under the surface over each subregion by the volume of a rectangular box with height f(x,y) at some point (x,y) in the subregion. The volume of the box is given by f(x,y)ΔA, where ΔA is the area of the subregion. The total volume under the surface over the region R is then approximated by the sum of the volumes of all the boxes:

$$\sum f(x,y) \Delta A$$

As the size of the subregions approaches zero, the sum approaches the exact value of the double integral.

To evaluate a double integral, we usually use iterated integrals. This involves integrating first with respect to one variable, and then with respect to the other variable. The order of integration can be interchanged, but the limits of integration must be adjusted accordingly.

For example, if we want to evaluate the double integral of f(x,y) over a rectangular region R defined by a ≤ x ≤ b and c ≤ y ≤ d, we can write the double integral as an iterated integral in either of the following ways:

$$\int_a^b \int_c^d f(x,y) dy dx$$

or

$$\int_c^d \int_a^b f(x,y) dx dy$$

The first integral is evaluated by first integrating with respect to y, treating x as a constant, and then integrating the result with respect to x. The second integral is evaluated by first integrating with respect to x, treating y as a constant, and then integrating the result with respect to y.

Double integrals can also be used to calculate the mass of a lamina with variable density, the average value of a function over a region, and the center of mass of a lamina, among other applications. In general, double integrals provide a powerful tool for solving problems in two-dimensional geometry and physics.