### Change of Order of Integration
In the study of multiple integrals, it is often necessary to change the order of integration. This is a powerful technique that allows us to evaluate integrals that would otherwise be very difficult or impossible to compute.

Here are some key points to keep in mind when changing the order of integration:

- The order of integration can be changed if the integrand is continuous on the region of integration.
- To change the order of integration, we need to express the region of integration as a projection onto one of the coordinate planes.
- Once we have expressed the region of integration as a projection onto one of the coordinate planes, we can integrate with respect to one variable at a time.

Let's take a closer look at each of these points.

### Condition for Changing the Order of Integration
The first condition for changing the order of integration is that the integrand must be continuous on the region of integration. If the integrand is not continuous, then we cannot guarantee that the integral will converge.

### Expressing the Region of Integration as a Projection
To change the order of integration, we need to express the region of integration as a projection onto one of the coordinate planes. To do this, we need to find the limits of integration for each variable.

For example, suppose we want to change the order of integration of the integral:

$$\int_{-1}^{1}\int_{0}^{\sqrt{1-x^2}} f(x,y) \,dy\,dx$$

To express the region of integration as a projection onto the y-axis, we need to find the limits of integration for y. We can do this by fixing x and looking at the curve that defines the upper and lower limits of integration for y:

$$0 \leq y \leq \sqrt{1-x^2}$$

This is the equation of a semicircle with center at the origin and radius 1. Hence, we can express the region of integration as:

$$\int_{0}^{1}\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} f(x,y) \,dx\,dy$$

### Integrating with Respect to One Variable at a Time
Once we have expressed the region of integration as a projection onto one of the coordinate planes, we can integrate with respect to one variable at a time. This means that we need to fix all other variables and integrate with respect to the variable of interest.

For example, if we want to integrate with respect to y in the integral:

$$\int_{0}^{1}\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} f(x,y) \,dx\,dy$$

we need to fix x and integrate with respect to y:

$$\int_{0}^{1} 2\sqrt{1-y^2} \cdot g(x) \,dy$$

where g(x) is the function obtained by fixing x in the original integrand f(x,y).

### Conclusion
Changing the order of integration is a powerful technique that allows us to evaluate difficult integrals. By following the conditions and steps outlined above, we can change the order of integration and simplify our computations.