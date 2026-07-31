## Unit 5 - Linear Transformations

Linear transformations are mathematical functions that map one vector space to another. They are an essential concept in linear algebra and have many practical applications. In this unit, we will explore the definition of linear transformations, their properties, and various examples of linear transformations.

### Definition

A linear transformation is a function that maps one vector space to another, and preserves the structure of the vector space. In other words, it satisfies two conditions:

1. Linearity: For any vectors u and v in the domain, and any scalar c, the linear transformation T satisfies the following properties:

   - T(u + v) = T(u) + T(v)
   - T(cu) = cT(u)

2. Preservation of Structure: A linear transformation preserves the operations of vector addition and scalar multiplication. In other words, if u and v are vectors in the domain, and c is a scalar, then:

   - T(u + v) = T(u) + T(v)
   - T(cu) = cT(u)

### Properties of Linear Transformations

Linear transformations have several important properties that are useful in understanding their behavior:

- Linear transformations preserve the origin: T(0) = 0, where 0 is the zero vector in the domain and range.
- Linear transformations preserve linear combinations: T(c1u1 + c2u2 + ... + cnun) = c1T(u1) + c2T(u2) + ... + cnT(un), where c1, c2, ..., cn are scalars and u1, u2, ..., un are vectors in the domain.
- Linear transformations are uniquely determined by their action on a basis for the domain: If {v1, v2, ..., vn} is a basis for the domain, then any linear transformation T is uniquely determined by its action on the basis vectors T(v1), T(v2), ..., T(vn).

### Examples of Linear Transformations

Some common examples of linear transformations include:

- Rotation: A rotation of a vector space about a fixed point is a linear transformation.
- Scaling: A scaling of a vector space by a fixed factor is a linear transformation.
- Reflection: A reflection of a vector space about a fixed plane is a linear transformation.
- Projection: A projection of a vector space onto a subspace is a linear transformation.
- Shearing: A shearing of a vector space along a fixed axis is a linear transformation.

### Matrix Representations of Linear Transformations

Every linear transformation can be represented by a matrix, and every matrix defines a linear transformation. The matrix representation of a linear transformation depends on the choice of bases for the domain and range. If {v1, v2, ..., vn} is a basis for the domain, and {w1, w2, ..., wm} is a basis for the range, then the matrix representation of the linear transformation T is given by the mxn matrix [T] where the entry in the ith row and jth column is the scalar that multiplies wj in the expression T(vi) = a1i w1 + a2i w2 + ... + ami wm.

In conclusion, linear transformations are an important concept in linear algebra and have many practical applications in physics, engineering, and computer science. Understanding their properties and examples is crucial for mastering linear algebra.