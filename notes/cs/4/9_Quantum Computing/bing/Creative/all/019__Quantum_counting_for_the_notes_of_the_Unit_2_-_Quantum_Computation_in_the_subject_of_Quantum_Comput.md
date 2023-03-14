### Quantum counting for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Quantum counting is a quantum algorithm for efficiently counting the number of solutions for a given search problem. 
- The algorithm is based on the quantum phase estimation algorithm and on Grover's search algorithm. 
- Counting problems are common in diverse fields such as statistical estimation, statistical physics, networking, etc. 
- The algorithm can also solve the quantum existence problem, which is to decide whether any solution exists, as a special case. 
- The algorithm was devised by Gilles Brassard, Peter Høyer and Alain Tapp in 1998. 

#### The problem

- Consider a finite set of size N and a set of "solutions" (that is a subset of S). Define f(x) as the indicator function of S, which returns 1 if x is a solution and 0 otherwise. 
- The problem is to calculate the number of solutions M. 
- Without any prior knowledge on the set of solutions (or the structure of the function f), a classical deterministic solution cannot perform better than O(N), because all the elements of S must be inspected. 

#### The algorithm

- The algorithm consists of the following steps:

  1. Prepare two registers: the first register has t qubits and the second register has n qubits, where N = 2^n.  
  2. Apply a Hadamard gate to each qubit in both registers to create a superposition state.  
  3. Apply a controlled-Grover operator to the second register, conditioned on the state of the first register. The Grover operator is a unitary matrix that rotates the state vector by an angle theta in the |w>, |s'> basis, where |w> is the state corresponding to the solutions and |s'> is the state orthogonal to |w>.  
  4. Apply an inverse quantum Fourier transform to the first register.  
  5. Measure the first register and obtain a t-bit approximation to the phase phi, where phi = theta/2pi.  
  6. Use the following formula to estimate the number of solutions M:  

     M = sin^2(pi * 2^t * phi) * N

- The algorithm has a success probability of at least 4/pi^2, which is about 40%.  
- The algorithm requires O(sqrt(N/M)) applications of the Grover operator, which is optimal.  

#### Example

- Suppose we want to count the number of solutions for a search problem with N = 16 and M = 5. We can use t = 4 and n = 4 qubits for the algorithm. 
- The Grover operator for this problem can be implemented as follows: 

```python
def example_grover_iteration():
    """Small circuit with 5/16 solutions"""
    # Do circuit
    qc = QuantumCircuit(4)
    # Oracle
    qc.h( [2,3])
    qc.ccx(0,1,2)
    qc.h(2)
    qc.x(2)
    qc.ccx(0,2,3)
    qc.x(2)
    qc.h(3)
    qc.x( [1,3])
    qc.h(2)
    qc.mct( [0,1,3],2)
    qc.x( [1,3])
    qc.h(2)
    # Diffuser
    qc.h(range(3))
    qc.x(range(3))
    qc.z(3)
    qc.mct( [0,1,2],3)
    qc.x(range(3))
    qc.h(range(3))
    qc.z(3)
    return qc
```

- The controlled-Grover operator can be obtained by adding a control qubit to the Grover operator. 

```python
def controlled_grover_iteration():
    """Controlled Grover iteration"""
    # Get the Grover circuit
    grover