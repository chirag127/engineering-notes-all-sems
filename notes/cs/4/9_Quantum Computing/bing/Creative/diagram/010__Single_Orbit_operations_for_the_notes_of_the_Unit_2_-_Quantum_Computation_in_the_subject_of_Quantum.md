### Single Orbit operations for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

Single orbit operations are operations that act on a single qubit, which is the fundamental unit of quantum information. A qubit can be in a state of 0, 1, or a superposition of both, and can be represented by a two-dimensional vector of unit norm. Single orbit operations can be described by 2x2 matrices that act on the qubit vector, and can be visualized as rotations on the Bloch sphere, which is a sphere that represents the possible states of a qubit.

Some examples of single orbit operations are:

- The X-gate, which flips the state of the qubit from 0 to 1 and vice versa. It is analogous to the classical NOT gate, and corresponds to a rotation of pi radians around the x-axis of the Bloch sphere. It can be represented by the matrix:

```
X = | 0 1 |
    | 1 0 |
```

- The Y-gate, which flips the state of the qubit from 0 to -1 and vice versa. It corresponds to a rotation of pi radians around the y-axis of the Bloch sphere. It can be represented by the matrix:

```
Y = | 0 -i |
    | i  0 |
```

- The Z-gate, which changes the phase of the qubit by pi radians. It corresponds to a rotation of pi radians around the z-axis of the Bloch sphere. It can be represented by the matrix:

```
Z = | 1  0 |
    | 0 -1 |
```

- The H-gate, which creates a superposition of 0 and 1 from a pure state. It is also known as the Hadamard gate, and corresponds to a rotation of pi/2 radians around the y-axis followed by a rotation of pi radians around the x-axis of the Bloch sphere. It can be represented by the matrix:

```
H = 1/sqrt(2) * | 1  1 |
                | 1 -1 |
```

- The phase shift gate, which changes the phase of the qubit by an arbitrary angle. It can be represented by the matrix:

```
R(phi) = | 1    0   |
         | 0 e^(i*phi) |
```

A diagram that illustrates the basic architecture of a single orbit operation is:

```
+-----+     +-----+     +-----+
|     |     |     |     |     |
|  0  |     |  1  |     |  0  |
|     |     |     |     |     |
+-----+     +-----+     +-----+
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  v           v           v
+-----+     +-----+     +-----+
|     |     |     |     |     |
|  1  |     |  0  |     |  1  |
|     |     |     |     |     |
+-----+     +-----+     +-----+
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  v           v           v
+-----+     +-----+     +-----+
|     |     |     |     |     |
|  0  |     |  1  |     |  0  |
|     |     |     |     |     |
+-----+     +-----+     +-----+
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  |           |           |
  v           v           v
+-----+     +-----+     +-----+
|     |