## Unit 4 - Curves and Surfaces

- Curves and surfaces are the essential tools for computer-aided geometric design (CAGD) and computer graphics.
- They are used to represent and manipulate complex shapes in design and manufacturing systems and computer animation.
- They provide a great level of control over the final shape through a small set of control points and constraints, while possessing attributes critical to these application areas, such as smoothness, continuity, and curvature.

### Types of curves and surfaces

- There are different types of curves and surfaces, depending on how they are defined and represented.
- Some common types are:

  - **Parametric curves and surfaces**: These are defined by a set of functions that map a parameter domain (such as a line segment or a rectangle) to a point in the Euclidean space (such as a curve in 2D or a surface in 3D). For example, a parametric curve in 2D can be defined by:

    ```
    x = f(t)
    y = g(t)
    ```

    where `t` is the parameter that varies along the curve, and `f` and `g` are the functions that determine the `x` and `y` coordinates of each point on the curve.

  - **Implicit curves and surfaces**: These are defined by a function that states which points are on and off the curves or surfaces. For example, an implicit curve in 2D can be defined by:

    ```
    f(x, y) = 0
    ```

    where `f` is the function that determines whether a point `(x, y)` is on the curve or not. For example, a line can be defined by `ax + by + c = 0`, and a circle can be defined by `x^2 + y^2 - r^2 = 0`.

  - **Non-uniform rational B-splines (NURBS)**: These are a special type of parametric curves and surfaces that use basis splines (B-splines) as the functions that map the parameter domain to the Euclidean space. They are commonly used in computer graphics for representing both analytic and modeled shapes, as they offer flexibility, precision, and efficiency. They are also able to represent conic sections (such as circles, ellipses, and parabolas) exactly, which is not possible with other types of curves and surfaces.

### Properties of curves and surfaces

- Some important properties of curves and surfaces that affect their appearance and behavior are:

  - **Smoothness**: This refers to how smoothly the curve or surface changes direction or orientation. Smoothness can be measured by the degree of continuity of the first and higher derivatives of the curve or surface functions. For example, a curve or surface is said to be `C^0` continuous if it has no gaps or breaks, `C^1` continuous if it has no sharp corners or cusps, and `C^2` continuous if it has no sudden changes in curvature.

  - **Continuity**: This refers to how well the curve or surface joins with other curves or surfaces. Continuity can be measured by the degree of compatibility of the first and higher derivatives of the curve or surface functions at the joining points. For example, a curve or surface is said to be `G^0` continuous if it meets another curve or surface at a point, `G^1` continuous if it meets another curve or surface with the same tangent direction, and `G^2` continuous if it meets another curve or surface with the same curvature.

  - **Curvature**: This refers to how much the curve or surface bends or curves. Curvature can be measured by the inverse of the radius of the circle that best approximates the curve or surface at a point. For example, a straight line has zero curvature, a circle has constant curvature, and a parabola has varying curvature.

### Applications of curves and surfaces

- Curves and surfaces have many applications in computer graphics, such as:

  - **Modeling and rendering**: Curves and surfaces can be used to create and display realistic and complex shapes, such as characters, objects, landscapes, and scenes. They can also be used to generate textures, lighting, shadows, and reflections on the