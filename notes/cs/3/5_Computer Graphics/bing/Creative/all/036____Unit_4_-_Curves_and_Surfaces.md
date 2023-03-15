# Unit 4 - Curves and Surfaces

- Curves and surfaces are the essential tools for computer-aided geometric design (CAGD) and are used extensively in design and manufacturing systems and computer graphics.
- Curves and surfaces can be represented in different ways, such as parametric, implicit, or explicit forms.
- Parametric curves and surfaces are defined by a set of control points and a function that maps a parameter domain to the curve or surface. For example, a parametric curve in 2D can be written as:

    $$\mathbf{p}(t) = (x(t), y(t))$$

    where $t$ is the parameter and $\mathbf{p}(t)$ is the point on the curve.

- Implicit curves and surfaces are defined by a function that states which points are on and off the curve or surface. For example, an implicit curve in 2D can be written as:

    $$f(x, y) = 0$$

    where $(x, y)$ is the point on the curve and $f(x, y)$ is the function.

- Explicit curves and surfaces are defined by a function that maps one or more variables to another variable. For example, an explicit curve in 2D can be written as:

    $$y = f(x)$$

    where $x$ is the independent variable and $y$ is the dependent variable.

- Curves and surfaces can be classified into different types based on their properties, such as degree, continuity, smoothness, rationality, and uniformity.
- Degree is the highest power of the parameter in the parametric form of the curve or surface. For example, a line has degree 1, a parabola has degree 2, and a cubic curve has degree 3.
- Continuity is the measure of how smoothly the curve or surface joins with itself or with another curve or surface. There are different levels of continuity, such as positional continuity ($C^0$), tangential continuity ($C^1$), curvature continuity ($C^2$), and so on.
- Smoothness is the measure of how free the curve or surface is from sharp corners or cusps. A curve or surface is smooth if it has at least $C^1$ continuity.
- Rationality is the property of the curve or surface that allows it to represent conic sections (such as circles, ellipses, parabolas, and hyperbolas) exactly. A curve or surface is rational if it can be written as a ratio of two polynomials in the parameter.
- Uniformity is the property of the curve or surface that determines how evenly the parameter values are distributed along the curve or surface. A curve or surface is uniform if the parameter values are equally spaced, and non-uniform otherwise.

- Curves and surfaces can be constructed using different methods, such as interpolation, approximation, subdivision, blending, and transformation .
- Interpolation is the method of finding a curve or surface that passes through a given set of data points. For example, a polynomial interpolation curve can be found using Lagrange or Newton methods.
- Approximation is the method of finding a curve or surface that is close to a given set of data points, but not necessarily passes through them. For example, a least-squares approximation curve can be found using linear algebra methods.
- Subdivision is the method of refining a coarse curve or surface into a finer one by adding more control points and subdividing the parameter domain. For example, a B-spline curve can be subdivided using the de Boor algorithm.
- Blending is the method of combining two or more curves or surfaces into a single one by using a weighting function. For example, a Bezier curve can be blended from two control points and two tangent vectors using the Bernstein polynomials.
- Transformation is the method of modifying a curve or surface by applying a geometric operation, such as translation, rotation, scaling, or shearing. For example, a circle can be transformed into an ellipse by scaling it along one axis.

- Curves and surfaces can be evaluated, rendered, and manipulated using different algorithms, such as de Casteljau, de Boor, Bresenham, Cohen-Sutherland, and Bezier clipping .
- de Casteljau is