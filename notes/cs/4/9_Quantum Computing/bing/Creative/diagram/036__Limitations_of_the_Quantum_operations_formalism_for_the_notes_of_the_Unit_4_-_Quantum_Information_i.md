The quantum operations formalism is a general tool for describing the dynamics of quantum systems, either closed or open, in terms of linear maps on the density matrix. A quantum operation is a completely positive and trace-preserving map that represents the effect of a physical process on a quantum state. However, the quantum operations formalism has some limitations, such as:

- It does not account for the driving effect of the vacuum or zero-point radiation field (ZPF) on the quantum system, which may be responsible for the emergence of quantization and the operator formalism  .
- It does not capture the non-Markovian effects of the environment on the quantum system, which may lead to memory effects and nonlocal correlations .
- It does not address the computational complexity of quantum processes, which may be exponentially hard to simulate or verify using classical resources .

The following diagram illustrates the basic architecture of a quantum operation, where a quantum system S interacts with an environment E and undergoes a unitary evolution U, followed by a partial trace over E to obtain the final state of S:

```
+-----+     +-----+     +-----+
|  S  |-----|  U  |-----|  S  |
+-----+     +-----+     +-----+
  |           |           |
  |           |           |
+-----+     +-----+     +-----+
|  E  |-----|  U  |-----|  E  |
+-----+     +-----+     +-----+
  |           |           |
  |           |           |
  +-----------+-----------+
              |
              |
              v
           +-----+
           | TrE |
           +-----+
              |
              |
              v
           +-----+
           |  S  |
           +-----+
```