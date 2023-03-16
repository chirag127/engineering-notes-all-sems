## Unit 5 - Linear Transformations

1. **Definition:** A linear transformation is a function between two vector spaces that preserves the operations of vector addition and scalar multiplication.
2. **Properties:** Let T: V → W be a linear transformation. Then, for any vectors u, v ∈ V and any scalar c, the following properties hold:
    - T(u + v) = T(u) + T(v)
    - T(cu) = cT(u)
3. **Matrix representation:** Every linear transformation can be represented by a matrix. If T: V → W is a linear transformation, then there exists a unique matrix A such that T(v) = Av for all v ∈ V.
4. **Kernel and range:** The kernel of a linear transformation T: V → W is the set of all vectors v ∈ V such that T(v) = 0. The range of T is the set of all vectors w ∈ W such that w = T(v) for some v ∈ V.
5. **Injectivity and surjectivity:** A linear transformation is injective (one-to-one) if and only if its kernel is the zero vector. It is surjective (onto) if and only if its range is equal to the codomain W.
6. **Inverse:** If a linear transformation T: V → W is bijective (both injective and surjective), then it has an inverse transformation T⁻¹: W → V such that T⁻¹(T(v)) = v for all v ∈ V and T(T⁻¹(w)) = w for all w ∈ W.
7. **Composition:** The composition of two linear transformations is also a linear transformation. If T: U → V and S: V → W are linear transformations, then the composition S ∘ T: U → W is defined by (S ∘ T)(u) = S(T(u)) for all u ∈ U.
8. **Change of basis:** A change of basis is a linear transformation that converts the coordinates of a vector with respect to one basis to its coordinates with respect to another basis. It is represented by a matrix called the change of basis matrix.