# Inner Product Spaces

- An **inner product space** is a vector space with an additional operation called an **inner product** that allows us to measure the length and angle of vectors .
- An inner product is a function that takes two vectors and returns a scalar, often denoted with angle brackets such as $\langle a, b \rangle$ .
- An inner product must satisfy the following four properties for any vectors $u, v, w$ and scalar $c$:
  - **Linearity**: $\langle cu + v, w \rangle = c \langle u, w \rangle + \langle v, w \rangle$
  - **Symmetry**: $\langle u, v \rangle = \langle v, u \rangle$
  - **Positive-definiteness**: $\langle u, u \rangle \geq 0$ and $\langle u, u \rangle = 0$ if and only if $u = 0$
  - **Conjugate symmetry**: $\langle u, v \rangle = \overline{\langle v, u \rangle}$ (for complex vector spaces only)
- Examples of inner products are the **dot product** for real vector spaces and the **Hermitian product** for complex vector spaces.
- The inner product allows us to define the **norm** (or length) of a vector as $\|u\| = \sqrt{\langle u, u \rangle}$ and the **angle** between two vectors as $\cos \theta = \frac{\langle u, v \rangle}{\|u\| \|v\|}$.
- A vector space with an inner product is also called a **pre-Hilbert space**. If the vector space is also **complete** (meaning that every Cauchy sequence converges to a vector in the space), then it is called a **Hilbert space** .