### Definition of Eigenvalue and Eigenvector

- An **eigenvalue** of a square matrix A is a scalar λ that satisfies the equation Av = λv, where v is a non-zero vector in the same space as A.  
- An **eigenvector** of a square matrix A is a non-zero vector v that satisfies the equation Av = λv, where λ is a scalar called the eigenvalue of A corresponding to v.  
- The word eigen comes from the German word for "proper" or "characteristic". 
- Eigenvalues and eigenvectors are important concepts in linear algebra that help in analyzing the properties and behavior of linear transformations and matrices.  
- To find the eigenvalues and eigenvectors of a matrix A, one has to solve the characteristic equation det(A - λI) = 0, where I is the identity matrix of the same size as A. The roots of this equation are the eigenvalues of A, and the corresponding eigenvectors can be found by plugging in each eigenvalue into the equation (A - λI)v = 0 and solving for v.