# Double integral

- A double integral is a way to integrate over a two-dimensional area. It can be used to find the volume under a surface, the area of a region, the average value of a function, and other applications.
- A double integral of a function of two variables, say f(x,y), over a region R in the xy-plane, is denoted by ∬Rf(x,y)dA, where dA is a small element of area in R.
- A double integral can be evaluated by iterated integration, which means integrating first with respect to one variable and then with respect to the other variable. The order of integration can be changed if the region R is simple and the function f(x,y) is continuous.
- A double integral can also be evaluated by changing the variables to a different coordinate system, such as polar, cylindrical, or spherical coordinates. This can simplify the integration and the region of integration.
- A double integral can be interpreted geometrically as the volume of the solid bounded by the surface z=f(x,y) and the region R in the xy-plane. Alternatively, it can be interpreted as the sum of the values of f(x,y) over all the points in R, weighted by the area element dA.

## Examples

- Example 1: Find the double integral of f(x,y)=x+y over the region R=[0,1]×[0,2].

Solution: We can use iterated integration to evaluate the double integral. We have:

∬Rf(x,y)dA=∫0^1∫0^2(x+y)dydx

=∫0^1[xy+12y^2]0^2dx

=∫0^1(2x+2)dx

=[x^2+2x]0^1

=3

- Example 2: Find the double integral of f(x,y)=x^2+y^2 over the region R bounded by the circle x^2+y^2=4.

Solution: We can use polar coordinates to evaluate the double integral. We have:

x=rcosθ, y=rsinθ, dA=rdrdθ, 0≤r≤2, 0≤θ≤2π

∬Rf(x,y)dA=∫0^2π∫0^2(r^2cos^2θ+r^2sin^2θ)rdrdθ

=∫0^2π∫0^2r^3drdθ

=∫0^2π[14r^4]0^2dθ

=∫0^2π4dθ

=[4θ]0^2π

=8π